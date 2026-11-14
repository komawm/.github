# Delivery rules

1. Work belongs to one owning repository and a scoped CarryCtx task. Record
   dependencies, named identity/session, decisions, progress, blockers, and
   checkpoints. Inspect existing work before starting.
2. The current initialization is local-only. Do not create or modify GitHub
   repositories, issues, labels, milestones, releases, settings, or secrets.
   Track future configuration in the organization repository instead.
3. After publication is explicitly authorized, link the GitHub issue and CarryCtx
   task. Use branches/worktrees, coherent commits, a linked pull request, review,
   and passing required checks before merge for repositories using that workflow.
   Docs requires only local Markdown checks, with no CI/CD or issue/PR/review
   requirement. Packaging uses local packaging checks and CD without a generic
   CI or issue/PR requirement. Shared templates do not override those scopes.
   Before an initial commit, shared
   checkout work requires disjoint scopes.
4. Labels describe type, area, platform, priority, and a meaningful blocking
   condition. Milestones group an actual acceptance target, not merely a date.
   Apply the locally declared labels consistently when remote work is authorized.
5. For local initialization, an independent review plus local gate evidence is
   sufficient to accept infrastructure. Report preexisting product gate failures
   and keep product acceptance as separate work.
6. CodeRabbit review is additional evidence when the user installs the bot.
   Resolve actionable blocking findings and rerun relevant checks. Do not make
   unavailable remote review or a missing bot a prerequisite for local setup.
7. Update affected canonical documentation and release state. Checkpoint tested
   results and remaining work before ending sessions. Complete only the outcome
   actually accepted; do not mark product readiness through governance changes.
8. Owned repositories are Koma, Jiku, koma-types, koma-docs, packaging, and this
   organization repository. The external Phodopus reference may be a symlink;
   do not write through it or initialize another project there. Packaging owns
   distribution/CD delivery and its MIT infrastructure remains separate from
   product-source licensing. Each owned repository uses one root `LICENSE`:
   GPL-3.0-or-later for Koma/Jiku, Apache-2.0 for koma-types, and MIT for
   docs/packaging/organization infrastructure.
