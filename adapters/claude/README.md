# Claude adapter

Identity: ../../.claude-plugin/plugin.json. Discovery: shared ../../skills and two read-only ../../agents wrappers. No hooks/MCP. Framework and specialist definitions are canonical shared assets, not copied into the adapter.

Code development uses --plugin-dir; native Chat/Cowork uses supported custom upload subject to plan/policy. Plain Chat does not run native agents or local MCP. See ../../docs/INSTALLATION_CLAUDE.md and ../../docs/PLATFORM_COMPATIBILITY.md. Resource paths resolve from installed skill locations; if a native wrapper cannot locate the core, return BLOCKED and ask the main host for the appropriate installed-resource location.
