# Claude adapter — V4.1

Identity: .claude-plugin/plugin.json; hooks/claude/hooks.json is selected separately from Codex. Shared skills and canonical 50/52 resources remain at the plugin root. Two optional read-only agent wrappers support explicitly delegated analysis.

Model invocation remains enabled. Shared skill frontmatter uses portable name/description; user-invocable:false was evaluated as a Claude-specific option and is not imposed on shared files. The hook launcher reads CLAUDE_PLUGIN_ROOT in Python. PostToolUse Write/Edit payloads use tool_input.file_path; no assumption is made that Bash edits or other Claude surfaces behave identically.

Local manifest/launcher checks are separate from native Claude inference and account eligibility. This account's Claude installation/inference is deferred; see ../../docs/ACCOUNT_SCOPE.md. Do not assume Code, Chat, Desktop and Cowork support the same hooks, agents or execution. See ../../docs/PLATFORM_VERIFICATION_V4_1.md and ../../docs/INSTALLATION_CLAUDE.md.
