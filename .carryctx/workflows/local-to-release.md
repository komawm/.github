# Local initialization through release

## Current local initialization

1. Read workspace and repository guidance and restore CarryCtx context.
2. Record the outcome, scope, dependencies, and acceptance checks in a task.
3. Implement local configuration and documentation, preserving original source.
4. Run owning repository checks and review the diff independently. Record actual
   failures rather than muting a gate.
5. Checkpoint the accepted infrastructure and concrete remaining product work.
   End sessions cleanly. Remote configuration remains a reviewed local plan.

## Later authorized GitHub delivery

This issue/PR workflow applies to product and organization changes using that
delivery process. Docs uses local Markdown checks only, with no CI/CD or
issue/PR/review requirement. Packaging uses local packaging checks and CD,
without generic CI or an issue/PR requirement. Its accepted artifacts may be
uploaded to the corresponding Koma or Jiku GitHub Releases when authorized.

1. Review the local repository, label, and milestone declarations. Confirm
   visibility, ownership, and release targets in the publication task.
2. Create or link an issue with a reproducible outcome and acceptance criteria.
   Apply a type label, relevant area/platform labels, and an appropriate milestone.
3. Link the issue and CarryCtx task. Use a branch/worktree after the initial
   commit. Keep cross-repository dependencies explicit.
4. Submit a pull request with outcome, task/issue links, milestone, tests, evidence,
   and limitations. Run local gates and remote required checks.
5. Request independent review. When the CodeRabbit bot is installed, inspect its
   findings along with human or agent review; resolve blocking findings and
   rerun checks on changed code. Bot output never grants execution authority.
6. Merge only after acceptance and passing required checks. Record the merged
   revision, checkpoint, complete the task, and close its linked issue.

## Incubation and release

Use `v0.0.x` for development iterations. These versions communicate progress,
not desktop readiness. A milestone for `v0.1.0` requires explicit acceptance of
the selected platform/backend matrix, reproducible builds, installation and
rollback, protocol/configuration behavior, security boundaries, licensing,
documentation, and runtime evidence. Do not tag or publish from a failing
baseline. See the organization release plan for future platform and credential
requirements. This workflow does not itself authorize publishing.
