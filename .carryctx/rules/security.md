# Security and environment rules

Do not commit credentials, raw CarryCtx state, runtime sockets, host-specific
overrides, ISO images, VM disks, or private logs. Preserve unrelated files and
refuse installation through symlinks or over unreviewed conflicting files.
Keep Actions permissions minimal and dependencies pinned or update-managed.

Use the existing Hyprland session as protected host context. Test nested or in
isolated VMs before attempting hardware changes. Device access, GPU passthrough,
boot/service installation, and desktop replacement require an explicitly
authorized task. A read-only environment limitation is recorded, not bypassed.

Future publishing credentials are documented by name and purpose only. Prefer
GitHub's scoped token and OIDC where supported. No credentials are required or
created during local initialization.
