# Organization CarryCtx

<!-- carryctx:v1 -->

This directory stores versioned CarryCtx configuration, local operating rules,
personas, and delivery workflows for the [Koma organization
repository](https://github.com/komawm/.github). Product, type, documentation, and
packaging tasks belong to their respective owned repositories and separate
task databases; the external Phodopus reference is never initialized here.

Runtime state (tasks, agents, events, sessions) lives in
`<git-common-dir>/carryctx/state.sqlite`, not in `.carryctx`.
Do not edit `state.sqlite` by hand; use `carryctx` commands.

Read the [commander persona](https://github.com/komawm/.github/blob/main/.carryctx/personas/commander.md),
[delivery rules](https://github.com/komawm/.github/blob/main/.carryctx/rules/delivery.md),
and [local-to-release workflow](https://github.com/komawm/.github/blob/main/.carryctx/workflows/local-to-release.md)
when coordinating this repository. Markdown files provide agent guidance;
they are not automatically installed preset packs.

The current task is local-only initialization. Record GitHub-related plans in
tracked declarative files and CarryCtx, without creating issues, labels,
milestones, repositories, releases, or secrets remotely. A later authorized
publication task can apply the reviewed plan.

Configuration uses the repository's existing project ID, `KWS` task prefix,
`just check` verification, named sessions, checkpoints before session end,
and idle-only worktree cleanup. Delete a task branch only after its clean,
inactive worktree was actually removed. Keep cancelled worktrees. Managed Git
hooks and lefthook must coexist; never bypass hooks to make a commit pass.

- Repository: https://github.com/Xuepoo/carryctx
- Documentation: https://carryctx.xuepoo.xyz
  (see `carryctx-docs/configuration.md` for storage and XDG layout)
