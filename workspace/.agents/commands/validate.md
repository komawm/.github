# Validate a workspace change

1. Run `just check` in the repository changed. Run the workspace verifier when descriptors, root templates, repository layout, or agent resources change.
2. Keep formatting/compilation failures from inherited source visible. Do not disable a gate to turn a preexisting failure green.
3. Validate pure Rust behavior before nested Wayland tests. Only proceed to isolated VM/hardware tests when the task and device access allow it. Preserve current Hyprland and user data.
4. Retain exact commands, tool versions, exit statuses, and relevant logs in ignored recording/. Capture screenshots only when they verify an observable behavior.
5. Read CarryCtx task state and inspect the diff before completion. Checkpoint any unresolved blockers and end the named session. Publishing repositories, raw task state, or releases is not part of local validation.
