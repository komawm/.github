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
| `komawm/koma` | `release.yml` | Push of tag `vX.Y.Z` (or `workflow_dispatch` dry run) | `koma-<ver>-x86_64-unknown-linux-gnu.tar.gz` (binaries, resources, examples, `LICENSE`, `README.md`, `CHANGELOG.md`, `RELEASE-MANIFEST.toml`) and `SHA256SUMS` | Built-in `GITHUB_TOKEN`, `contents: write` only in the `publish` job |
| `komawm/jiku` | `release.yml` | Push of tag `vX.Y.Z` (or `workflow_dispatch` dry run) | `jiku-<ver>-src.tar.gz`, `RELEASE-MANIFEST.toml`, `SHA256SUMS` | Built-in `GITHUB_TOKEN`, `contents: write` only in the `publish` job |
| `komawm/koma-types` | `release.yml` | Push of tag `vX.Y.Z` (or `workflow_dispatch` dry run) | `koma-types-<ver>.tar.gz`, standalone `koma.lua`, `SHA256SUMS` | Built-in `GITHUB_TOKEN`, `contents: write` only in the `publish` job |
| `komawm/packaging` | `cd-archlinux.yml` | Manual `workflow_dispatch` (`publish` defaults to `false`; `true` runs `publish` job) | `koma-<pkgver>-<pkgrel>-x86_64.pkg.tar.zst`, `SHA256SUMS-archlinux`, `PACKAGE-MANIFEST-archlinux.toml` uploaded to the existing product release | `PRODUCT_RELEASE_TOKEN` |

Every publishing job runs in a protected `release` environment. Product
environments only accept deployments from tags matching `v*.*.*`, and
`workflow_dispatch` runs are dry runs that build artifacts without publishing.
The packaging `release` environment only accepts `main`, and all packaging CD
workflows must default `publish=false` so build-only verification never enters
the `release` environment or accesses publishing secrets. Each release workflow
re-runs the repository's `just check` gate (or verifies checksums/manifests in
packaging CD) on the target revision before any asset is uploaded. Consumers
verify downloads with `sha256sum -c SHA256SUMS`.

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

## Release Secrets Checklist

The product prerelease workflows need no user-supplied secret. Configure only
the credentials required by an authorized channel, strictly as environment
secrets of the owning repository's protected `release` environment (see
[github/repositories.toml](https://github.com/komawm/.github/blob/main/github/repositories.toml)).

### Active `v0.0.x` credentials

| Name | Repository / environment | Purpose | Handling |
| --- | --- | --- | --- |
| `GITHUB_TOKEN` | Product `release` (built-in) | Create the product's own GitHub prerelease and upload assets | Never stored; `contents: write` only in the `publish` job |
| `PRODUCT_RELEASE_TOKEN` | `komawm/packaging` → `release` | Upload packaging CD artifacts to `komawm/koma` (later `komawm/jiku`) Releases when `publish=true` | GitHub App installation token or fine-grained token limited to the target product repositories with `Contents: Read and write`; packaging's built-in token cannot write to other repositories |

### Planned multi-distro, BSD, and signing secrets (`v0.1.0+` / channel-authorized)

These secrets are **not active in `v0.0.x`**. Provision a channel's secrets
only when its workflow in `komawm/packaging` (or product repository) is
implemented, reviewed, and backed by isolated build/install/rollback evidence:

| Channel / Platform | Secret names | Repository / environment | Purpose & gating notes |
| --- | --- | --- | --- |
| GitHub Release signing (Cosign or PGP) | `COSIGN_PRIVATE_KEY`, `COSIGN_PASSWORD` (or `GPG_PRIVATE_KEY`, `GPG_PASSPHRASE` / `RELEASE_SIGNING_KEY`, `RELEASE_SIGNING_PASSPHRASE`) | Product or `komawm/packaging` → `release` | Sign release archives, `SHA256SUMS`, and manifests (`*.sig`/`.bundle`/`.asc`); prefer keyless Sigstore OIDC (`id-token: write`) if selected, and publish public verification keys first |
| Arch Linux (AUR) | `AUR_SSH_PRIVATE_KEY` | `komawm/packaging` → `release` | Dedicated SSH deploy key to push reviewed `PKGBUILD` / `.SRCINFO` updates to `aur.archlinux.org`; GitHub Release `.pkg.tar.zst` uploads continue using `PRODUCT_RELEASE_TOKEN` |
| Debian / Ubuntu (APT) | `APT_GPG_PRIVATE_KEY`, `APT_GPG_PASSPHRASE`, optional `APT_REPO_TOKEN` | `komawm/packaging` → `release` | Sign `.deb` repository `Release` / `InRelease` / `Release.gpg` metadata and authenticate pushes if hosting a dedicated APT repository |
| Fedora / RHEL (COPR & RPM) | `COPR_API_LOGIN`, `COPR_API_TOKEN`, optional `RPM_GPG_PRIVATE_KEY`, `RPM_GPG_PASSPHRASE` | `komawm/packaging` → `release` | Submit SRPM builds via Fedora Copr API (`~/.config/copr`) and sign standalone `.rpm` / `repomd.xml.asc` artifacts if self-hosted |
| Alpine Linux (`APKBUILD`) | `ABUILD_PRIVATE_KEY`, `ABUILD_PUBLIC_KEY` | `komawm/packaging` → `release` | `abuild-sign` RSA keypair for signing `.apk` packages and `APKINDEX.tar.gz`; document public key trust (`/etc/apk/keys/`) before enabling |
| Nix / Flakes & binary cache | `CACHIX_AUTH_TOKEN`, optional `CACHIX_SIGNING_KEY` | `komawm/packaging` or product → `release` | Push signed Nix closures to a binary cache; upstream `nixpkgs` updates use normal pull requests with no CI secret |
| Homebrew Tap (CLI tools) | `HOMEBREW_TAP_TOKEN` | `komawm/packaging` → `release` | Fine-grained PAT or GitHub App token scoped strictly to `komawm/homebrew-tap` (`Contents: Read and write`) for CLI formula updates (`komactl`, `jiku`) |
| Rust / crates.io | `CARGO_REGISTRY_TOKEN` | `komawm/koma`, `komawm/jiku` → `release` | Optional crates.io publishing of selected library crates (for example `koma-proto`); prefer crates.io Trusted Publishing / OIDC; never required for binary-only releases |
| FreeBSD / OpenBSD ports & packages | `FREEBSD_PKG_SIGNING_KEY` (plus `PRODUCT_RELEASE_TOKEN` / `COSIGN_PRIVATE_KEY` where applicable) | `komawm/packaging` → `release` | Blocked until BSD platform acceptance evidence exists; upstream FreeBSD/OpenBSD ports use reviewed PRs without CI secrets, while self-hosted `pkg repo` signing requires a dedicated RSA/ECDSA key |

### Secret hygiene and environment rules

- **Protected `release` environment**: Require tag `v*.*.*` on product repos and `branch:main` on `komawm/packaging`. Add required reviewers (with self-review disabled where policy allows) before authorizing external package publishing or `v0.1.0+` releases.
- **No secrets in build jobs**: Keep `build` jobs read-only (`permissions: contents: read`, zero `secrets.*`). Only the gated `publish` job (requiring `publish=true` in `komawm/packaging`, where `publish` defaults to `false`) may enter `environment: release`.
- **Least privilege and OIDC**: Prefer GitHub OIDC / Trusted Publishing where supported, pass secrets through job/step `env:` (never inline `${{ secrets.* }}` in `run:` shells), never print/commit/embed secret values in artifacts, rotate tokens before expiry, and revoke immediately if exposed.
- **Organization secrets**: Scope organization secrets to an explicit repository list only when multiple approved repositories share a single credential; otherwise keep credentials inside the owning repository's `release` environment.
