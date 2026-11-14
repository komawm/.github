# Workspace agent resources

The [organization repository](https://github.com/komawm/.github) maintains these portable agent files. The root directory is not a CarryCtx project. Start from the [workspace guidance](https://github.com/komawm/.github/blob/main/workspace/AGENTS.md) and run lifecycle commands in the owning Git repository.

Available resources include the [CarryCtx skill](https://github.com/komawm/.github/blob/main/workspace/.agents/skills/use-carryctx/SKILL.md), [onboarding command](https://github.com/komawm/.github/blob/main/workspace/.agents/commands/onboard.md), and [validation command](https://github.com/komawm/.github/blob/main/workspace/.agents/commands/validate.md). The CarryCtx skill and references are vendored from the locally installed skill, version 1.3.0; command flags must still be checked against the installed CLI.

Install with the organization bootstrap script. If the execution environment makes the root agent directory read-only, the bootstrap reports the missing files and leaves these tracked sources available for a later install from a writable session.
