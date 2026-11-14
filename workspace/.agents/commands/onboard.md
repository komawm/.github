# Onboard to Koma

1. Read workspace.toml, root AGENTS.md, and the owning repository's README, AGENTS.md, repo.toml, and relevant design documents.
2. Run the organization environment doctor and workspace verifier. Check actual access to GPU/KVM and ISO_PATH; record missing capabilities rather than assuming host access.
3. Enter the owning organization Git repository. Inspect status and existing CarryCtx tasks before initializing anything. In a fresh owned clone, initialize CarryCtx using that repository's task prefix, register a named identity, and start a session. The external Phodopus reference is read-only: do not initialize or mutate state through its link.
4. Record a scoped task and checkpoint before multi-step edits. Preserve existing changes. Keep Phodopus an independent upstream checkout and Koma's Cargo dependency resolution explicit.
5. Use /tmp/koma/ for disposable work and ignored recording/ for persistent local evidence. Do not treat specification text or green metadata checks as runtime acceptance.
