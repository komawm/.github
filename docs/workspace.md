# Workspace setup and conventions

The umbrella follows the useful part of Bitty's workspace pattern: a machine-readable roster and repository identity descriptors, with one Git history, CarryCtx database, quality entry point, and agent guide per owned checkout. Koma does not inherit Bitty's extension fleet or Git submodules. The user-selected product matrix is Koma, Jiku, koma-types, koma-docs, and packaging, plus the organization repository. The nine compositor Cargo crates stay together; Jiku's skills stay inside Jiku and avatar work is deferred.

## Ownership

The organization repository owns root navigation and agent templates. Koma owns the compositor and tools; Jiku owns the desktop agent and bundled skills; koma-types owns Lua type snapshots; koma-docs owns canonical specifications and development docs; packaging owns distribution packaging and CD. Product licenses and packaging's MIT infrastructure license are distinct repository boundaries. A repository skeleton does not establish implementation acceptance.

Map keys and descriptor names identify local checkout directories. The local `koma-docs` checkout uses the existing remote `komawm/docs`. Docs runs local Markdown checks only and requires no CI/CD, issue, PR, or CodeRabbit review. Packaging runs local packaging checks and owns CD without generic CI or an issue/PR requirement. Accepted build artifacts can be uploaded to the corresponding Koma or Jiku GitHub Releases after publication is authorized.

Each owned repository uses a single root `LICENSE`: Koma and Jiku use GPL-3.0-or-later, koma-types uses Apache-2.0, and docs, packaging, and organization infrastructure use MIT. Preserve third-party notices.

Phodopus is outside the Koma organization. The external roster points to the existing Xuepoo upstream and may resolve a user-managed symlink to another workspace. Verification reads the target's Git identity and remote without demanding a Koma-owned descriptor, reinitializing CarryCtx, or changing its source files, history, config, or origin. Bootstrap never clones or updates this dependency. The consuming Cargo Git URL/revision contract is managed explicitly in Koma rather than silently patched to a local path.

## Installation

Use Python 3.11 or later. From the umbrella directory, run `python3 .github/scripts/bootstrap.py --root .`. The script installs only tracked workspace templates, rejects paths through symlinks, and refuses to replace differing files. It does not create repositories or install dependencies. Run with `--check` to compare without writing. Conflicts require reviewing the local diff; the script has no force-overwrite mode.

An optional Bash helper, `source .github/scripts/env.sh`, sets `KOMA_WORKSPACE`
and uses the local ignored Rustup cache only if the product-pinned toolchain
is installed there. It also opts into an existing local Cargo cache. It changes
only the current shell, leaves global dotfiles untouched, and copies no global
credentials/configuration. Without local caches, normal per-clone settings apply.

An environment may protect root control directories such as `.agents`. A denied installation returns a nonzero status with explicit diagnostics, while other independent root files may already be installed. The complete source remains tracked under `workspace/.agents`. `--skip-agents` intentionally limits installation and checking to the other root files; it must not be reported as a complete agent installation.

## Local state

Disposable data belongs in `/tmp/koma/`. Durable local evidence, image captures, VM disks, machine capability reports, experiment notes, and read-only external reference clones under `recording/references/` (such as `Hyprland` and `niri`) belong in ignored `recording/`. The six `komawm` repositories are published on GitHub (`remote_changes_enabled = true`, `v0.0.x` incubation line before `v0.1.0` release acceptance) and configured from the declarative GitHub plan in `github/`. The root ignore file is a routing convention; each real repository also ignores its own recording directory. Root ignore rules do not turn the umbrella into a Git repository. Never commit raw CarryCtx state, runtime sockets, access tokens, local environment overrides, ISO images, or disk images.

CarryCtx is initialized inside each Git checkout. Its database lives under the Git common directory; configuration is versioned in the owning repository. New clones initialize fresh local state. Vendored agent skills provide operating instructions, not state synchronization. Never push private snapshots; any public state transport needs an explicitly redacted publication artifact and separate authorization.

## Validation and evidence

`just check` in this repository validates the kit without requiring sibling repositories. `just workspace-check` validates installed descriptors and independent Git roots in the umbrella. The environment doctor reads tool versions, device access, and the ISO inventory, then prints JSON. An available QEMU executable is distinct from usable KVM, and visible rendering libraries are distinct from access to DRM devices.

The host context is Arch Linux, Hyprland, and a dedicated GPU. Preserve the running desktop. Start with pure Rust tests, then nested compositor tests, then isolated VM testing. Record exact observations rather than claiming bare-metal, passthrough, performance, security, or BSD acceptance from a source build. Session installation and device rebinding require an explicitly authorized task.
