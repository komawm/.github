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

## Future artifact workflow

A later publishing task can prepare a Linux archive with the selected binaries,
configuration examples, session resources, license notices, a release manifest,
and checksums. Test installation and removal in an isolated VM before attaching
artifacts to a GitHub release. Add distribution packages only after their
build/install/upgrade/rollback process is accepted. Do not enable tag-triggered
release publication while the current product baseline is failing.

This local setup supplies quality and security workflows plus a release runbook.
It deliberately does not publish binaries, create tags or releases, or create
platform accounts. Existing CI must pass on the revision actually released.
Re-evaluate action/toolchain pins and platform packaging requirements in that
future task.

The dedicated [packaging repository](https://github.com/komawm/packaging) owns
distribution/CD implementation and its [channel acceptance runbook](https://github.com/komawm/packaging/blob/main/docs/release.md).
It uses local packaging checks without generic CI or an issue/PR requirement.
Publish accepted Koma artifacts to `komawm/koma` GitHub Releases and accepted
Jiku artifacts to `komawm/jiku` GitHub Releases. Docs needs no release pipeline.
Its MIT packaging infrastructure does not relicense GPL product binaries, the
separately licensed type definitions, canonical documentation, or upstream
Phodopus. Keep those notices and corresponding-source requirements in the
accepted distribution.

## Credential names for later work

No secret values are needed or stored now. Choose only the credentials required
by an explicitly selected publishing channel:

| Name | Future purpose | Handling |
| --- | --- | --- |
| `GITHUB_TOKEN` | Repository-scoped GitHub release uploads | Built-in Actions token; grant `contents: write` only in the publishing job |
| `PRODUCT_RELEASE_TOKEN` | Upload from packaging CD to a selected product repository | Use a narrowly scoped GitHub App installation or fine-grained token for that product; packaging's built-in token does not grant cross-repository write access |
| `CARGO_REGISTRY_TOKEN` | Optional crates.io publishing of selected library crates | Prefer trusted publishing/OIDC if available; never required for binary-only releases |
| `RELEASE_SIGNING_KEY` | Optional artifact signing after a signing scheme is selected | Protected environment secret; document rotation and verification separately |
| `RELEASE_SIGNING_PASSPHRASE` | Only if the selected signing key requires one | Protected environment secret; never print or include in artifacts |

Distribution-specific repository tokens or upload keys are chosen only when
that channel is authorized. Do not invent credentials or request broad personal
tokens during workspace initialization. Use protected release environments and
the minimum job permissions; document verification instructions for consumers.
Scope organization secrets to an explicit allowed repository list only when
multiple approved repositories share a need; otherwise use the owning product
or packaging repository's protected channel-specific environment. Bitty secrets
are neither universal defaults nor inputs to this setup.
