# Codex adapter — V4.1

Root plugin.json is canonical; extensions.com.openai selects hooks/codex/hooks.json. The optional .codex-plugin compatibility manifest points to the same resources and is not merged into the inline extension. All skills share one cognitive core.

The host owns task execution. Model-selected assistance is primary; no unsupported Codex agent manifest is registered. Native delegation uses only observed tools and existing authorization. Hook scripts require local Python and reviewed host trust. The static launcher reads PLUGIN_ROOT in Python so shell interpolation of plugin paths is unnecessary.

PostToolUse checks are read-only structural advisory for explicitly edited cwd/.cognition/artifacts JSON. They never grant permission, block or undo a tool. Local fixture/launcher success does not establish native event delivery. No MCP, credential, separate app, database server or daemon is required. See ../../docs/HYBRID_ARCHITECTURE.md and ../../docs/INSTALLATION_CODEX.md.
