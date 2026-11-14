#!/usr/bin/env python3
"""Report local tooling, virtual-machine inputs, and actual device visibility."""

import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    tools = {}
    names = ("git", "gh", "cargo", "rustc", "bun", "just", "lefthook", "carryctx", "podman", "docker", "qemu-system-x86_64", "actionlint")
    for name in names:
        executable = shutil.which(name)
        entry = {"path": executable, "version": None}
        if executable:
            try:
                result = subprocess.run(
                    [executable, "--version"], capture_output=True, text=True,
                    timeout=5, cwd=args.root,
                )
                lines = (result.stdout or result.stderr).splitlines()
                entry["version"] = lines[0] if lines else None
                entry["version_exit_code"] = result.returncode
            except (OSError, subprocess.TimeoutExpired) as error:
                entry["error"] = str(error)
        tools[name] = entry
    devices = {}
    for name in ("/dev/kvm", "/dev/dri"):
        path = Path(name)
        devices[name] = {
            "exists": path.exists(),
            "readable": os.access(path, os.R_OK),
            "writable": os.access(path, os.W_OK),
        }
    iso_value = os.environ.get("ISO_PATH")
    iso = {"path": iso_value, "images": []}
    if iso_value:
        try:
            iso["images"] = [{"name": path.name, "bytes": path.stat().st_size} for path in sorted(Path(iso_value).glob("*.iso")) if path.is_file()]
        except OSError as error:
            iso["error"] = str(error)
    print(json.dumps({
        "platform": platform.platform(),
        "workspace": str(args.root.resolve()),
        "session": {key: os.environ.get(key) for key in ("XDG_CURRENT_DESKTOP", "XDG_SESSION_TYPE", "WAYLAND_DISPLAY", "DISPLAY")},
        "tools": tools,
        "devices": devices,
        "iso": iso,
        "scope": "Availability report only; no compositor, KVM, GPU, or VM acceptance test was performed.",
    }, indent=2))


if __name__ == "__main__":
    main()
