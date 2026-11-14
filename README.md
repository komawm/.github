# Koma organization and workspace

This repository belongs to [komawm](https://github.com/komawm) and contains the organization profile, shared contribution templates, and the portable Koma workspace setup. The owner has created the remote repositories. Current workspace changes remain local; this setup does not update GitHub settings, issues, labels, milestones, secrets, or releases.

The workspace has six organization repositories: [Koma](https://github.com/komawm/koma) for the compositor and its tools, [Jiku](https://github.com/komawm/jiku) for the orchestration agent and bundled skills, [koma-types](https://github.com/komawm/koma-types) for Lua types, [koma-docs](https://github.com/komawm/docs) for canonical specifications, [packaging](https://github.com/komawm/packaging) for distribution packaging and CD, and this repository for organization governance. [Phodopus](https://github.com/Xuepoo/phodopus) is an external shared runtime reference, optionally linked from another workspace. There are no Git submodules or umbrella Git repository. Jiku's repository boundary is established; its daemon remains an implementation task, separate from existing specifications and examples.

To create or update the routing files in an existing workspace, run this from its root:

```bash
python3 .github/scripts/bootstrap.py --root .
python3 .github/scripts/verify.py --workspace .
python3 .github/scripts/doctor.py --root .
```

An optional Bash setup command is `source .github/scripts/env.sh`. It sets
`KOMA_WORKSPACE` for that shell and selects the local ignored Rustup directory
only when the product-pinned Rust toolchain is actually installed there. It
selects an existing local Cargo cache as well, without copying global credentials
or configuration. Standalone clones without these caches retain normal settings.

Bootstrap creates missing files, accepts identical files, and refuses conflicting files or symlink destinations. It never clones, commits, pushes, overwrites existing work, or changes system configuration. If an environment protects the root agent directory, it reports that installation is incomplete; the source remains available in this repository. Use `--skip-agents` only when deliberately installing the other routing files without agent files. `--check` compares without writing.

See [workspace guidance](https://github.com/komawm/.github/blob/main/workspace/AGENTS.md), [setup and conventions](https://github.com/komawm/.github/blob/main/docs/workspace.md), and [repository agent guidance](https://github.com/komawm/.github/blob/main/AGENTS.md). Run `just check` in this checkout to validate the kit and workflows.

The [GitHub configuration plan](https://github.com/komawm/.github/blob/main/github/README.md) records future repository descriptions/topics, labels, milestones, branch review rules, and CodeRabbit conventions. The [release plan](https://github.com/komawm/.github/blob/main/docs/releases.md) keeps Koma in `v0.0.x` development until `v0.1.0` product acceptance and documents future publishing credential names without values. Run `just hooks-install` in this checkout to compose lefthook's local quality gate with CarryCtx's managed hooks.

This repository's new infrastructure is [MIT licensed](https://github.com/komawm/.github/blob/main/LICENSE). Vendored skills retain their own notices; product and documentation licenses are listed in the [workspace guide](https://github.com/komawm/.github/blob/main/workspace/README.md).
