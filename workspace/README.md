# Koma workspace

This directory groups independent repositories for [komawm](https://github.com/komawm) and one external shared runtime reference. It is a navigation and local-work area, not a Git repository or a Cargo workspace. There are no Git submodules.

| Checkout | Purpose | Upstream |
| --- | --- | --- |
| `koma` | Rust compositor workspace and companion tools | [komawm/koma](https://github.com/komawm/koma) |
| `jiku` | Desktop orchestration agent and bundled `skills` | [komawm/jiku](https://github.com/komawm/jiku) |
| `koma-types` | Versioned Lua configuration type definitions | [komawm/koma-types](https://github.com/komawm/koma-types) |
| `koma-docs` | Canonical Koma/Jiku specifications and development docs | [komawm/docs](https://github.com/komawm/docs) |
| `packaging` | Distribution packaging and guarded release/CD delivery | [komawm/packaging](https://github.com/komawm/packaging) |
| `.github` | Organization profile, workspace templates, and shared guidance | [komawm/.github](https://github.com/komawm/.github) |
| `phodopus` | Shared external Lua runtime, directory or symlink | [Xuepoo/phodopus](https://github.com/Xuepoo/phodopus) |

`workspace.toml` distinguishes organization repositories from external references. Its keys name local checkouts; `koma-docs` points to the remote `komawm/docs` repository. Each organization repository has a `repo.toml` descriptor and owns its Git history, CarryCtx state, and local checks. Koma, Jiku, koma-types, and the organization repository use CI. Docs uses local Markdown checks, with no CI/CD or PR requirement. Packaging uses local checks and owns CD; its build artifacts can be attached to the corresponding Koma or Jiku GitHub Releases. Koma's nine crates remain together. Jiku includes its skills in the same repository; avatar work is deferred. Jiku's current library scaffolds and specifications must not be described as an accepted implementation. Preserve the external Phodopus checkout, origin, history, and state; no bootstrap or verification command writes through its link.

Use `/tmp/koma/` for disposable data and the ignored `recording/` directory for durable local evidence, screenshots, logs, VM data, and read-only external reference clones under `recording/references/` (such as `Hyprland` and `niri`). Neither location is a repository or a CarryCtx project. Do not store secrets in tracked files.

From this directory, run:

```bash
python3 .github/scripts/bootstrap.py --root . --check
python3 .github/scripts/verify.py --workspace .
python3 .github/scripts/doctor.py --root .
```

In Bash, `source .github/scripts/env.sh` optionally sets `KOMA_WORKSPACE` and
selects an existing product-pinned Rust installation and Cargo cache from the
ignored build-cache directory. It changes `RUSTUP_HOME` and `CARGO_HOME` only in
the current shell when the respective local caches exist; normal settings remain
in use when they are absent.

Run build and CarryCtx commands from the relevant owned checkout. See [workspace agent guidance](https://github.com/komawm/.github/blob/main/workspace/AGENTS.md), [setup details](https://github.com/komawm/.github/blob/main/docs/workspace.md), and [Koma onboarding](https://github.com/komawm/docs/tree/main/docs/development).

The six `komawm` repositories are published on GitHub (`remote_changes_enabled = true`) and configured from the [declarative GitHub configuration](https://github.com/komawm/.github/tree/main/github) for labels, milestones, repository settings, and review conventions. Koma remains in `v0.0.x` incubation development until the [v0.1.0 acceptance requirements](https://github.com/komawm/.github/blob/main/docs/releases.md) are met. CodeRabbit bot integration is planned for installation; local independent review and checks remain usable alongside remote workflows.

Repository licenses are explicit boundaries:

| Repository | License |
| --- | --- |
| `koma` | GPL-3.0-or-later |
| `jiku` | GPL-3.0-or-later |
| `koma-types` | Apache-2.0 |
| `koma-docs` (remote `docs`) | MIT |
| `packaging`, `.github` | MIT infrastructure; vendored resources retain their notices |
| External `phodopus` | Upstream licensing and attribution, independent of komawm |

Each owned repository uses one root `LICENSE` file. Preserve third-party notices in vendored resources.
