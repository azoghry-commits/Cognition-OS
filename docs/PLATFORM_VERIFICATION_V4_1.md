# V4.1 platform verification — 2026-10-20

Official documentation was reviewed again during the rebuild. Local observations: `codex-cli 0.153.0`, `Claude Code 2.1.201`. Local manifest validation is separate from inference and native-event tests. Account scope: [ACCOUNT_SCOPE.md](ACCOUNT_SCOPE.md).

| Aspect | Codex | Claude Code | Candidate runtime status |
|---|---|---|---|
| Model-selected skills | Name/description metadata and on-demand resources | Auto/model invocation by default; no disable-model-invocation setting | Package/metadata tested locally; actual selection not measured |
| Manifest | Portable root + extensions.com.openai; fallback is not merged | `.claude-plugin/plugin.json` with separate configuration | Local structural validation |
| PostToolUse | Tool input/output; apply_patch uses `tool_input.command` | Write/Edit uses `tool_input.file_path` | Fixtures for both payloads tested; host delivery untested |
| Feedback | `hookSpecificOutput.additionalContext` | `hookSpecificOutput.additionalContext` | Advisory only; no block/override |
| Script root | `PLUGIN_ROOT` | `CLAUDE_PLUGIN_ROOT` | Packaged path; optional Python must be available for the hook |
| Permission/trust | Non-managed plugin hooks require user review and trust; manual desktop install | Hooks and permissions follow Claude Code runtime | Does not change host trust/permissions |
| Native delegation | Use only tools actually available | Optional read-only agent wrappers | No automatic dispatch |

Official references and decisions:

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins): portable root and inline OpenAI settings, component paths, local/manual desktop hooks, and trust. A package containing hooks is not eligible for the public directory. This candidate is a local package and is not published there.
- [OpenAI skills](https://developers.openai.com/plugins/build/skills): metadata and resources for model workflows; [skill concepts](https://developers.openai.com/plugins/concepts/skills) describe task-fit selection. Installation is not used as proof of invocation.
- [Codex hooks](https://learn.chatgpt.com/docs/hooks): PostToolUse observes output; apply_patch supplies a command; `additionalContext` is feedback; a post-event hook cannot reverse an existing side effect. The candidate does not block or rewrite output.
- [Claude hooks](https://code.claude.com/docs/en/hooks): PostToolUse runs after successful tools, with absolute file paths in file-tool input and additional feedback. The candidate does not assume Bash edits are caught by the Write/Edit matcher.
- [Claude skills](https://code.claude.com/docs/en/skills): `user-invocable:false` is Claude-specific. Shared skills retain portable name/description frontmatter and manual diagnosis; they add no unverified cross-host fields and do not disable model invocation.

Claude Chat/Desktop Chat, Cowork, Codex CLI, and Codex desktop are assessed separately. Previously identified Claude Free limits and the prohibition on API-key use still apply. No new native Claude inference or installation occurred in this rebuild. This document verifies documentation contracts, not account entitlement or availability of every capability.
