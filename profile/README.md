# Koma

[Koma](https://github.com/komawm/koma) is a Wayland tiling compositor designed to support both a keyboard-driven desktop and explicit, isolated desktop automation interfaces.

The Rust compositor workspace contains protocol and layout models (`Dwindle` default, `Scrolling`, `Deck`, and `BSP`), sandboxed Phodopus Lua configuration with Hyprland-compatible default keybinds and typed appearance/shader/animation overrides, controller CLI (`komactl`), MCP adapter (`koma-mcp`), and overview companion (`koma-overview`). [Jiku](https://github.com/komawm/jiku) owns the companion desktop orchestration contracts and bundled skills, [koma-types](https://github.com/komawm/koma-types) owns LuaLS type definitions, [koma-docs](https://github.com/komawm/docs) owns canonical specifications, and [packaging](https://github.com/komawm/packaging) owns distribution delivery. Existing code and specifications are under active `v0.0.x` incubation development; hardware behavior and security properties require independent validation.

[Start with Koma](https://github.com/komawm/koma) · [Architecture](https://github.com/komawm/docs/blob/main/docs/ARCHITECTURE.md) · [Workspace setup](https://github.com/komawm/.github)
