# Security Policy

This is the organization-wide security policy for [komawm](https://github.com/komawm). It applies across organization repositories that do not define a separate policy.

## Supported Versions

All `komawm` repositories are currently on the `0.0.x` incubation line (`v0.0.1` development prereleases exist for `komawm/koma`, `komawm/jiku`, and `komawm/koma-types`). Per the [release plan](https://github.com/komawm/.github/blob/main/docs/releases.md), development prereleases record reviewed source baselines only and make no hardware, DRM/KMS, or security support claims.

| Version | Supported |
| --- | --- |
| `0.0.x` (development prerelease) | No (incubation only) |
| `< 0.1.0` | No |

Supported release lines and backport windows will be listed here only after `v0.1.0` meets independent release acceptance.

## Repository Scope

Report vulnerabilities against the owning repository where the issue originates:

| Repository | Scope |
| --- | --- |
| [komawm/koma](https://github.com/komawm/koma) | Wayland compositor (`koma`), IPC contracts (`koma-proto`), Lua host (`koma-lua`), controller (`komactl`), MCP adapter (`koma-mcp`), and overview (`koma-overview`) |
| [komawm/jiku](https://github.com/komawm/jiku) | Desktop orchestration daemon (`jikud`), CLI/MCP (`jiku`), episodic memory (`jiku-memory`), TTS/notifications (`jiku-tts`), and bundled `skills` |
| [komawm/koma-types](https://github.com/komawm/koma-types) | Versioned LuaLS configuration type definitions |
| [komawm/packaging](https://github.com/komawm/packaging) | Distribution packaging templates, release manifests, and CD workflows |
| [komawm/docs](https://github.com/komawm/docs) | Canonical architecture, IPC, and configuration specifications |
| [komawm/website](https://github.com/komawm/website) | Public Astro static site (`https://komawm.org`, `https://komawm.org/jiku/`) and Edge Worker (`komawm-website`) |
| [komawm/.github](https://github.com/komawm/.github) | Organization templates, governance workflows, and workspace setup kit |

Issues originating in the external Lua runtime [Xuepoo/phodopus](https://github.com/Xuepoo/phodopus) that affect Koma or Jiku sandbox boundaries may be reported privately to `komawm` first for coordinated triage.

## Reporting a Vulnerability

Do **not** report security vulnerabilities through public GitHub issues, pull requests, discussions, or public chat channels.

Use one of the following private channels:

1. **GitHub Security Advisories** (preferred when Private Vulnerability Reporting is enabled on the target repository):
   - [Report in komawm/koma](https://github.com/komawm/koma/security/advisories/new)
   - [Report in komawm/jiku](https://github.com/komawm/jiku/security/advisories/new)
   - [Report in komawm/koma-types](https://github.com/komawm/koma-types/security/advisories/new)
   - [Report in komawm/packaging](https://github.com/komawm/packaging/security/advisories/new)
   - [Report in komawm/docs](https://github.com/komawm/docs/security/advisories/new)
   - [Report in komawm/website](https://github.com/komawm/website/security/advisories/new)
   - [Report in komawm/.github](https://github.com/komawm/.github/security/advisories/new)
2. **Direct maintainer email** (use this directly if Private Vulnerability Reporting is not enabled on a repository or if you require an email channel):
   - Send details to [`xuepoofoter@gmail.com`](mailto:xuepoofoter@gmail.com) (the organization contact listed on [github.com/komawm](https://github.com/komawm)) with `[komawm security] <repository>` in the subject line.

When reporting, include as much of the following as possible:

- Affected repository, crate or binary, tag or commit SHA, and distribution/architecture/backend (`--winit`, `--tty`/DRM, or VM)
- Clear reproduction steps or a minimal proof of concept
- Expected versus actual behavior (for example capability-token or `Epoch` fencing bypass, protected-surface blackout leaks, `koma-admin.sock` / `security-context-v1` privilege escalation, Phodopus Lua sandbox escapes, or CI/CD credential/supply-chain flaws)
- Assessment of impact and any known mitigations or workarounds

Never include real API keys (`GEMINI_API_KEY`, `OPENCODE_GO_API_KEY`), capability tokens, personal credentials, or private CarryCtx state in reports.

## Disclosure Policy and Response Expectations

- Reports are handled privately from intake through triage, fix development, and coordinated disclosure. Details are withheld from public issues and commits while a fix or mitigation is prepared.
- Maintainers target an initial acknowledgment within **5 business days** and an initial severity and scope assessment within **10 business days** of acknowledgment.
- Coordinated disclosure is the default: public advisories or release notes follow availability of a fix or mitigation. Reporters receive credit by default unless anonymity is requested.

This policy describes the organization's vulnerability intake and disclosure process only. It does not claim that `0.0.x` development baselines or unaccepted packages have completed security verification or hardening; pre-`0.1.0` security-boundary and acceptance gates remain governed by the [release plan](https://github.com/komawm/.github/blob/main/docs/releases.md).
