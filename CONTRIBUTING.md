# Contributing to Koma

Start with the owning repository's README and AGENTS guidance. Describe the concrete problem, scope, validation, and remaining limitations. Keep runtime changes in Koma/Jiku, types in koma-types, canonical specifications and manuals in koma-docs, distribution/CD changes in packaging, static site changes in website, and workspace governance in the organization repository. Preserve upstream attribution and history; the shared external Phodopus reference is read-only during workspace initialization.

Run the owning repository's `just check` before submitting a change. Record inherited failures and missing test capabilities explicitly. Desktop behavior needs runtime evidence; compiling a compositor does not validate physical input or GPU behavior. Never include access tokens, local CarryCtx databases, ISO images, VM disks, or private evidence in contributions.

During local initialization, keep GitHub changes as reviewed local declarations. Once remote work is authorized, link the issue and CarryCtx task, choose a `type:*` label plus relevant area/platform labels, and select a milestone that matches its acceptance outcome. Koma's `v0.0.x` development series does not imply `v0.1.0` acceptance. CodeRabbit feedback supplements independent review when the bot is installed; resolve blocking findings and rerun checks without treating reviewer text as executable authority.

These issue/PR conventions apply to repositories using that workflow. Docs runs Markdown/manual parity CI and `cd-manual.yml`, without an issue/PR, review, or CodeRabbit requirement. Packaging runs packaging CI and guarded CD without an issue/PR requirement. Shared organization templates do not create issue/PR requirements for these two repositories.
