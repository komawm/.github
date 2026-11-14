#!/usr/bin/env python3
"""Validate the portable workspace kit and optionally installed sibling repos."""

import argparse
import ast
from pathlib import Path
import re
import subprocess
import sys
import tomllib


def load(path: Path) -> dict:
    return tomllib.loads(path.read_text())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path)
    args = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    errors = []
    for path in repository.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix == ".toml":
            try:
                load(path)
            except (OSError, tomllib.TOMLDecodeError) as error:
                errors.append(f"{path.relative_to(repository)}: {error}")
        elif path.suffix == ".py":
            try:
                ast.parse(path.read_text(), filename=str(path))
            except SyntaxError as error:
                errors.append(str(error))
        if path.name in {"README.md", "AGENTS.md"}:
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if not target.startswith(("https://", "mailto:", "#")):
                    errors.append(f"{path.relative_to(repository)}: noncanonical link {target}")
    source_map = load(repository / "workspace/workspace.toml")
    if source_map["workspace"]["model"] != "independent-repositories":
        errors.append("Workspace must use independent repositories")
    for name, entry in source_map["repo"].items():
        # A local checkout name need not equal its remote name (koma-docs -> docs).
        if not re.fullmatch(r"https://github\.com/komawm/[A-Za-z0-9_.-]+", entry.get("repository", "")):
            errors.append(f"{name}: owned repositories must use their canonical organization URL")
    if "phodopus" in source_map["repo"]:
        errors.append("Phodopus belongs in the external roster, not the organization roster")
    descriptor = load(repository / "repo.toml")["repo"]
    for key, value in source_map["repo"][".github"].items():
        if descriptor.get(key) != value:
            errors.append(f"Organization identity mismatch: {key}")
    skill = repository / "workspace/.agents/skills/use-carryctx/SKILL.md"
    if not skill.is_file():
        errors.append("Missing vendored CarryCtx skill")
    carryctx = load(repository / ".carryctx/config.toml")
    if carryctx["project"]["task_prefix"] != "KWS":
        errors.append("Organization CarryCtx must use its own KWS task prefix")
    if carryctx["verification"]["commands"] != ["just check"]:
        errors.append("CarryCtx verification must run just check")
    if carryctx["worktree"]["cleanup"]["delete_branch"] != "when_removed":
        errors.append("Task branches must only be deleted after worktree removal")
    labels = load(repository / "github/labels.toml")["labels"]
    names = [label["name"] for label in labels]
    if len(names) != len(set(names)):
        errors.append("Duplicate planned GitHub labels")
    for label in labels:
        if not re.fullmatch(r"[0-9a-fA-F]{6}", label.get("color", "")):
            errors.append(f"Invalid label color: {label.get('name')}")
    milestones = load(repository / "github/milestones.toml")["milestones"]
    if {item["title"] for item in milestones} != {"v0.0.1", "v0.1.0"}:
        errors.append("Planned milestones must distinguish incubation and acceptance")
    for milestone in milestones:
        if not milestone.get("acceptance"):
            errors.append(f"Missing milestone acceptance criteria: {milestone['title']}")
    settings = load(repository / "github/repositories.toml")
    if not isinstance(settings.get("remote_changes_enabled"), bool):
        errors.append("github/repositories.toml must declare boolean remote_changes_enabled")
    if source_map["workspace"].get("remote_changes_enabled") != settings.get("remote_changes_enabled"):
        errors.append("workspace.toml and github/repositories.toml must agree on remote_changes_enabled")
    if settings.get("remote_changes_enabled") is True:
        for repo_key, entry in settings["repositories"].items():
            if entry.get("visibility") not in {"public", "private"}:
                errors.append(f"{repo_key}: active remote_changes_enabled requires explicit public or private visibility")
    if {entry["url"] for entry in settings["repositories"].values()} != {
        entry["repository"] for entry in source_map["repo"].values()
    }:
        errors.append("Future repository settings must cover exactly the owned roster")
    if args.workspace:
        root = args.workspace.resolve()
        probe = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
            capture_output=True, text=True,
        )
        if probe.returncode == 0:
            errors.append("Umbrella root must not be a Git repository")
        deployed_map = root / "workspace.toml"
        if not deployed_map.is_file() or load(deployed_map) != source_map:
            errors.append("Installed workspace.toml differs from tracked template")
        project_ids = set()
        task_prefixes = set()
        for name, expected in source_map["repo"].items():
            checkout = root / name
            probe = subprocess.run(
                ["git", "-C", str(checkout), "rev-parse", "--show-toplevel"],
                capture_output=True, text=True,
            )
            if probe.returncode or Path(probe.stdout.strip()).resolve() != checkout.resolve():
                errors.append(f"{name}: not an independent Git checkout")
            if (checkout / ".gitmodules").exists():
                errors.append(f"{name}: submodules are not part of this workspace")
            identity_file = checkout / "repo.toml"
            if not identity_file.is_file():
                errors.append(f"{name}: missing repo.toml")
                continue
            identity = load(identity_file)["repo"]
            if identity.get("name") != name:
                errors.append(f"{name}: descriptor name mismatch")
            for field in ("kind", "lang", "role", "owner", "docs"):
                if identity.get(field) != expected.get(field):
                    errors.append(f"{name}: descriptor {field} mismatch")
            if identity.get("repository") != expected["repository"]:
                errors.append(f"{name}: descriptor repository URL mismatch")
            config_file = checkout / ".carryctx/config.toml"
            if not config_file.is_file():
                errors.append(f"{name}: missing CarryCtx configuration")
                continue
            config = load(config_file)
            project = config["project"]
            if project["id"] in project_ids or project["task_prefix"] in task_prefixes:
                errors.append(f"{name}: owned repositories must have unique CarryCtx identities")
            project_ids.add(project["id"])
            task_prefixes.add(project["task_prefix"])
            if config["verification"]["commands"] != ["just check"]:
                errors.append(f"{name}: CarryCtx verification must run just check")
        for name, expected in source_map.get("external", {}).items():
            relative = Path(expected["path"])
            if relative.is_absolute() or ".." in relative.parts:
                errors.append(f"{name}: external path must be a named workspace reference")
                continue
            checkout = root / relative
            probe = subprocess.run(
                ["git", "-C", str(checkout), "rev-parse", "--show-toplevel"],
                capture_output=True, text=True,
            )
            if probe.returncode or Path(probe.stdout.strip()).resolve() != checkout.resolve():
                errors.append(f"{name}: external reference does not resolve to a Git checkout")
                continue
            origin = subprocess.run(
                ["git", "-C", str(checkout), "remote", "get-url", "origin"],
                capture_output=True, text=True,
            )
            remote = origin.stdout.strip().removesuffix(".git")
            if remote.startswith("git@github.com:"):
                remote = "https://github.com/" + remote.removeprefix("git@github.com:")
            if origin.returncode or remote != expected["repository"]:
                errors.append(f"{name}: external origin does not match its canonical repository")
        ignore = root / ".gitignore"
        if not ignore.is_file() or "/recording/" not in ignore.read_text().splitlines():
            errors.append("Root ignore convention must include /recording/")
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    if errors:
        return 1
    print("Workspace kit validation passed" + ("; installed repositories verified" if args.workspace else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
