# Koma workspace

This directory groups independent repositories for [komawm](https://github.com/komawm) and one external shared runtime reference. It is a navigation and local-work area, not a Git repository or a Cargo workspace. There are no Git submodules.

| Checkout | Purpose | Upstream |
| --- | --- | --- |
| `koma` | Rust compositor workspace and companion tools | [komawm/koma](https://github.com/komawm/koma) |
| `jiku` | Desktop orchestration agent and bundled `skills` | [komawm/jiku](https://github.com/komawm/jiku) |
| `koma-types` | Versioned Lua configuration type definitions | [komawm/koma-types](https://github.com/komawm/koma-types) |
| `koma-docs` | Canonical Koma/Jiku specs, development docs, and tri-lingual `manual/` sources | [komawm/docs](https://github.com/komawm/docs) |
| `packaging` | Multi-distro packaging (`nFPM`/APT/RPM/Alpine/Arch/BSD/Homebrew) and guarded R2/release CD | [komawm/packaging](https://github.com/komawm/packaging) |
| `website` | Public tri-lingual Astro static site (`https://komawm.org` and `https://komawm.org/jiku/`) | [komawm/website](https://github.com/komawm/website) |
| `.github` | Organization profile, workspace templates, and shared guidance | [komawm/.github](https://github.com/komawm/.github) |
| `phodopus` | Shared external Lua runtime, directory or symlink | [Xuepoo/phodopus](https://github.com/Xuepoo/phodopus) |

`workspace.toml` distinguishes organization repositories from external references. Its keys name local checkouts; `koma-docs` points to the remote `komawm/docs` repository. Each organization repository has a `repo.toml` descriptor and owns its Git history, CarryCtx state, and local checks. Koma, Jiku, koma-types, website, and the organization repository use CI. Docs runs Markdown/manual parity CI and `cd-manual.yml`, which uploads tri-lingual manual bundles to Cloudflare R2 (`https://cdn.komawm.org/manual/`) and dispatches `repository_dispatch: manual-published` to `komawm/website` for commitless static rebuilds. Packaging runs packaging CI and guarded CD targeting `https://cdn.komawm.org` (`releases/`, `apt/`, `install/`), GitHub Releases on `komawm/koma` / `komawm/jiku`, AUR, Copr, and optional Nix Cachix pushes (delegating `flake.nix` ownership to `komawm/koma`). Koma's nine crates remain together. Jiku includes its skills in the same repository; avatar work is deferred. Jiku's current library scaffolds and specifications must not be described as an accepted implementation. Preserve the external Phodopus checkout, origin, history, and state; no bootstrap or verification command writes through its link.

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

The seven `komawm` repositories are published on GitHub (`remote_changes_enabled = true`) and configured from the [declarative GitHub configuration](https://github.com/komawm/.github/tree/main/github) for labels, milestones, repository settings, and review conventions. Koma remains in `v0.0.x` incubation development until the [v0.1.0 acceptance requirements](https://github.com/komawm/.github/blob/main/docs/releases.md) are met. CodeRabbit bot integration is planned for installation; local independent review and checks remain usable alongside remote workflows.

Repository licenses are explicit boundaries:

| Repository | License |
| --- | --- |
| `koma` | GPL-3.0-or-later |
| `jiku` | GPL-3.0-or-later |
| `koma-types` | Apache-2.0 |
| `koma-docs` (remote `docs`) | MIT |
| `packaging`, `website`, `.github` | MIT infrastructure; vendored resources retain their notices |
| External `phodopus` | Upstream licensing and attribution, independent of komawm |

Each owned repository uses one root `LICENSE` file. Preserve third-party notices in vendored resources.
