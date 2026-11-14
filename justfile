default: check

# Validate metadata, Python syntax, documentation links, and tracked templates.
kit-check:
    python3 scripts/verify.py

# Actions must be validated with the locally installed tool.
actionlint:
    actionlint

shellcheck:
    shellcheck scripts/env.sh

check: kit-check actionlint shellcheck

# These require sibling checkouts and are intentionally separate from CI.
workspace-check:
    python3 scripts/verify.py --workspace ..

bootstrap-check:
    python3 scripts/bootstrap.py --root .. --check

doctor:
    python3 scripts/doctor.py --root ..

# Compose the local quality gate with CarryCtx's checkpoint/commit hooks.
hooks-install:
    lefthook install
    carryctx hooks install --compose
