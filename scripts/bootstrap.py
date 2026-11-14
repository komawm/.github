#!/usr/bin/env python3
"""Install root routing templates without replacing existing local files."""

import argparse
from pathlib import Path
import sys


def install(source: Path, root: Path, check: bool, skip_agents: bool) -> int:
    errors = 0
    for item in sorted(source.rglob("*")):
        if not item.is_file():
            continue
        relative = item.relative_to(source)
        if skip_agents and relative.parts[0] == ".agents":
            continue
        destination = root / relative
        # Resolve neither destination nor its parents: an existing symlink must
        # never redirect installation outside the explicitly selected root.
        candidates = [destination, *destination.parents]
        if any(path.is_symlink() for path in candidates if path != root.parent):
            print(f"REFUSED symlink destination: {relative}", file=sys.stderr)
            errors += 1
            continue
        try:
            expected = item.read_bytes()
            if destination.exists():
                if destination.is_file() and destination.read_bytes() == expected:
                    print(f"OK {relative}")
                else:
                    print(f"CONFLICT {relative}: review local changes", file=sys.stderr)
                    errors += 1
            elif check:
                print(f"MISSING {relative}", file=sys.stderr)
                errors += 1
            else:
                destination.parent.mkdir(parents=True, exist_ok=True)
                # Exclusive creation also protects against another writer
                # creating this path after the existence check above.
                with destination.open("xb") as handle:
                    handle.write(expected)
                print(f"INSTALLED {relative}")
        except OSError as error:
            print(f"FAILED {relative}: {error}", file=sys.stderr)
            errors += 1
    if skip_agents:
        print("Agent resources intentionally skipped; agent installation is incomplete.")
    if errors:
        print(f"Workspace setup incomplete: {errors} file(s) require attention.", file=sys.stderr)
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="compare without writing")
    parser.add_argument("--skip-agents", action="store_true", help="install only routing files")
    args = parser.parse_args()
    root = args.root.absolute()
    if not root.is_dir() or root.is_symlink():
        parser.error("--root must be an existing real directory")
    source = Path(__file__).resolve().parents[1] / "workspace"
    return install(source, root, args.check, args.skip_agents)


if __name__ == "__main__":
    raise SystemExit(main())
