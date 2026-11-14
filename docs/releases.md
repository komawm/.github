# Development versions and release acceptance

Koma begins with development versions in the `0.0.x` series. `v0.0.1` identifies
the initial development baseline; subsequent patch iterations can record
accepted increments. A version or tag does not imply a working desktop, a
security guarantee, or support for every architectural target. The organization
repository is governance material and does not need to mirror product tags.

## Acceptance before v0.1.0

The first product release is `v0.1.0` only after independent acceptance of a
clearly selected platform and backend matrix. At minimum, select a Linux target,
run reproducible builds and all applicable checks, exercise nested Wayland,
verify the intended DRM/KMS and input behavior in an isolated suitable setup,
and document installation, rollback, configuration, IPC, and failure handling.
Retain security-boundary review and runtime observations. Architecture-only
targets such as BSD or additional CPU architectures remain planned until
separate evidence establishes their status.

Publish a support matrix naming each accepted distribution/architecture/backend,
test revision, toolchain, driver/device or VM configuration, and known limits.
Software rendering or nested tests alone do not establish hardware support.
KVM availability does not establish GPU passthrough. Preserve the current
Hyprland session during all validation.

## Development prerelease channel (`v0.0.x`)

`v0.0.1` is published as a GitHub **prerelease** marked as a development
build. It records a reviewed, CI-green source revision and convenience
artifacts; it is not the accepted `v0.1.0` product release and makes no
hardware, DRM/KMS, or security claim.

| Repository | Workflow | Trigger | Assets | Credential |
| --- | --- | --- | --- | --- |
| `komawm/koma` | `release.yml` | Push of tag `vX.Y.Z` (or `workflow_dispatch` dry run) | `koma-<ver>-x86_64-unknown-linux-gnu.tar.gz` (binaries, resources, examples, `LICENSE`, `RELEASE-MANIFEST.toml`) and `SHA256SUMS` | Built-in `GITHUB_TOKEN`, `contents: write` only in the `publish` job |
| `komawm/jiku` | `release.yml` | Push of tag `vX.Y.Z` | `jiku-<ver>-src.tar.gz` (library scaffold source), manifest, `SHA256SUMS` | Built-in `GITHUB_TOKEN` |
| `komawm/koma-types` | `release.yml` | Push of tag `vX.Y.Z` | `koma-types-<ver>.tar.gz`, standalone `koma.lua`, `SHA256SUMS` | Built-in `GITHUB_TOKEN` |
| `komawm/packaging` | `cd-archlinux.yml` | Manual `workflow_dispatch` with `publish=true` | Arch Linux package, `SHA256SUMS-archlinux`, `PACKAGE-MANIFEST.toml` uploaded to the existing product release | `PRODUCT_RELEASE_TOKEN` |

Every publishing job runs in a protected `release` environment. Product
environments only accept deployments from tags matching `v*.*.*`; the packaging
environment only accepts `main`. Each release workflow re-runs the repository's
`just check` gate on the tagged revision and verifies that the tag equals the
manifest version before any asset is uploaded. Consumers verify downloads with
`sha256sum -c SHA256SUMS`.

Distribution packages produced by packaging CD are development review
candidates until their install, upgrade, and rollback process is accepted.
Re-evaluate action/toolchain pins before each release.

The dedicated [packaging repository](https://github.com/komawm/packaging) owns
distribution/CD implementation and its [channel acceptance runbook](https://github.com/komawm/packaging/blob/main/docs/release.md).
It uses local packaging checks without generic CI or an issue/PR requirement.
Publish accepted Koma artifacts to `komawm/koma` GitHub Releases and accepted
Jiku artifacts to `komawm/jiku` GitHub Releases. Docs needs no release pipeline.
Its MIT packaging infrastructure does not relicense GPL product binaries, the
separately licensed type definitions, canonical documentation, or upstream
Phodopus. Keep those notices and corresponding-source requirements in the
accepted distribution.

## Credentials

The product prerelease workflows need no user-supplied secret. Configure only
the credentials required by a selected channel, as environment secrets of the
owning repository's `release` environment:

| Name | Repository / environment | Purpose | Handling |
| --- | --- | --- | --- |
| `GITHUB_TOKEN` | Product `release` (built-in) | Create the product's own GitHub prerelease and upload assets | Never stored; `contents: write` only in the `publish` job |
| `PRODUCT_RELEASE_TOKEN` | `komawm/packaging` → `release` | Upload packaging CD artifacts to `komawm/koma` (later `komawm/jiku`) Releases | GitHub App installation token or fine-grained token limited to the target product repositories with `Contents: write`; packaging's built-in token cannot write to other repositories |
| `CARGO_REGISTRY_TOKEN` | Product `release` | Optional crates.io publishing of selected library crates | Not used by `v0.0.x`; prefer trusted publishing/OIDC |
| `RELEASE_SIGNING_KEY` / `RELEASE_SIGNING_PASSPHRASE` | Product or packaging `release` | Optional artifact signing after a scheme is selected | Not used by `v0.0.x`; document rotation and verification first |

Add required reviewers to a `release` environment when publication should need
an explicit approval. Never print, commit, or embed secret values in artifacts,
and scope organization secrets to an explicit repository list only when several
repositories share a need.
