# Claude installation and lifecycle

## V4.1 rebuild candidate / package 0.2.0

The runtime and marketplace ZIPs use version 0.2.0. Root `.claude-plugin/plugin.json` selects `hooks/claude/hooks.json`; all skills share the same core as Codex. Python is needed only for local helpers/hooks. The PostToolUse hook is advisory; it grants no permission and cannot reverse completed side effects.

The rebuild session tested only the local manifest and launcher; no Claude installation or inference was run on this account. Follow [ACCOUNT_SCOPE.md](ACCOUNT_SCOPE.md). The native steps below apply only in an available and authorized environment; they do not confirm Claude Free entitlement. Code, Chat/Desktop, and Cowork have distinct capabilities.

For update/rollback, use a reviewed package version and retain the previous source/ZIP and project cases outside the cache. Verify the installed manifest and test a natural task on the target surface before claiming invocation or event delivery. See [platform verification](PLATFORM_VERIFICATION_V4_1.md) and [rebuild status](REBUILD_STATUS_V4_1.md).

## Native mechanisms and baseline notes

Local runtime: baseline skill files; optional Python 3.10+ for calculations and project case helper. No API key, database, MCP server or privileged install is needed. Official format references are in PLATFORM_COMPATIBILITY.md.

Claude Code development: run `claude plugin validate .` from the plugin root, then start `claude --plugin-dir "D:/Bisnisan/CognitionOS-Plugin"`. Invoke `/cognition-os:setup` or select an installed skill. `--plugin-dir` loads this session without permanent personal installation. Confirm the skill list and read a selected canonical definition. On installed client 2.1.201, read-only inventory can be inspected using `claude --plugin-dir <root> plugin details cognition-os` when supported.

Marketplace installation: add the packaged local marketplace root using `/plugin marketplace add <absolute-marketplace-root>`, then `/plugin install cognition-os@cognition-os-local`. Native account-wide installation and organization provisioning may have different availability. Do not change organization settings or publish without authorization.

Claude Chat/Desktop/Cowork: official current help documents custom plugin upload through Customize > Plugins. Upload the plugin ZIP, then invoke its setup/skills in the native conversation. Paid plan and organization policies apply. Skills/commands span these surfaces; subagents/hooks and local MCP do not run in plain Chat. File execution/calculator availability must be checked in the actual surface. No automatic plugin equivalence is assumed. Installed Code 2.1.201 is below the documented 2.1.273 account-sync threshold; use local load rather than promising sync.

Update: preserve authorized cases outside plugin cache; replace/install reviewed version, reload/restart as required, run smoke and selected regression. Rollback: load prior versioned ZIP or local package; inspect schema versions before reusing data. Removal: use `/plugin uninstall cognition-os@cognition-os-local` or native Customize remove. Session-only loading ends when session ends. Do not delete project .cognition records unless explicitly requested.

