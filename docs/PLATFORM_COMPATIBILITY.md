# Platform compatibility, checked 2026-10-21

Package 0.3.0 extends the portable baseline to Antigravity, GitHub Copilot, VS Code, and generic Agent Skills hosts. The detailed packaging routes and current verification boundary are in [CROSS_HOST_COMPATIBILITY.md](CROSS_HOST_COMPATIBILITY.md). Claude Desktop Chat can use uploaded plugins for skills and commands; hooks and subagents remain limited to Claude Code and Cowork. GitHub Copilot and VS Code can consume Agent Plugins 1.0, while Antigravity uses the dedicated minimal-manifest archive.

**V4.1 rebuild:** the latest official documentation review and candidate adapter limits are recorded in [PLATFORM_VERIFICATION_V4_1.md](PLATFORM_VERIFICATION_V4_1.md). Package 0.2.0 includes optional advisory hooks; the baseline statement that the package has no hooks applies only to 0.1.0.

Documentation establishes the advertised integration path; local observation establishes only what was tested. Installed clients observed: Claude Code 2.1.201 and codex-cli 0.153.0. Desktop product branding is not proof that every documented feature is active on this account.

Status vocabulary: SUPPORTED, SUPPORTED_WITH_LIMITATIONS, UNSUPPORTED, NOT_VERIFIED, REQUIRES_OPTIONAL_DEPENDENCY. None of the documented support labels means this package passed all native behavior tests.

## Official evidence index

- O1: [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins): portable manifest, fixed component paths, inline precedence, native local marketplace workflows and hooks limitations.
- O2: [OpenAI skills](https://developers.openai.com/plugins/build/skills): frontmatter, bundled resources and workflow instructions.
- O3: [Desktop-only OpenAI plugins](https://developers.openai.com/plugins/deploy/desktop-only): local execution and stdio differences; no service configured here.
- O4: [OpenAI plugin security](https://developers.openai.com/plugins/guides/security-privacy): runtime permissions and trust boundaries; retrieved in this audit.
- C1: [Claude Code plugin creation](https://code.claude.com/docs/en/plugins/create): .claude-plugin manifest, fixed skill/agent locations and session-only --plugin-dir.
- C2: [Claude plugin components](https://code.claude.com/docs/en/plugins/components): native agents, hooks and supported component discovery.
- C3: [Claude marketplaces](https://code.claude.com/docs/en/plugin-marketplaces): source formats and validation.
- C4: [Claude skills](https://code.claude.com/docs/en/skills): skill structure, invocation and supporting resources.
- C5: [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude): paid plans, Chat/Desktop/Cowork distinctions, local MCP, organization controls and Code account sync >=2.1.273.
- C6: [Claude subagents](https://code.claude.com/docs/en/sub-agents): separate contexts and supported native definitions.
- C7: [Claude Enterprise Plugins API](https://platform.claude.com/docs/en/manage-claude/plugins-api): scoped admin access; not a baseline personal-runtime requirement.
- P1: [Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json): fetched verbatim at schemas/vendor/plugin.schema.json and checked with a full JSON Schema validator.

## Capability matrix

| Feature | Codex CLI | Codex/Work in desktop | Claude Code | Claude Chat/Desktop Chat | Claude Cowork | Evidence and scope |
|---|---|---|---|---|---|---|
| Installation | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | O1, C1, C5; local CLI help additionally confirms plugin add; live desktop install unverified |
| Discovery | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | O1 local/repo sources; C3/C5; account/admin policies apply |
| Skills | SUPPORTED | SUPPORTED | SUPPORTED | SUPPORTED | SUPPORTED | O2, C4/C5; actual Code inventory found eleven skills |
| Specialized agents | NOT_VERIFIED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | UNSUPPORTED | SUPPORTED_WITH_LIMITATIONS | C2/C5/C6; Code inventory found two; Codex uses only tools actually present in the runtime, no agent manifest extension invented |
| Parallel execution | NOT_VERIFIED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | UNSUPPORTED | SUPPORTED_WITH_LIMITATIONS | C6; desktop runtime can expose delegation but per-account capacity/authorization must be observed; no guaranteed 52 concurrency |
| MCP | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | O1/O3, C2/C5; local stdio unavailable in Chat; Cowork cloud connector reachability differs |
| Hooks | NOT_VERIFIED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | UNSUPPORTED | SUPPORTED_WITH_LIMITATIONS | O1 manually installed desktop plugins only; C2/C5; package intentionally has none |
| Script execution | REQUIRES_OPTIONAL_DEPENDENCY | REQUIRES_OPTIONAL_DEPENDENCY | REQUIRES_OPTIONAL_DEPENDENCY | NOT_VERIFIED | SUPPORTED_WITH_LIMITATIONS | Optional Python or permitted native calculator; shell/code permission and actual runtime govern availability |
| Local files | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | NOT_VERIFIED | SUPPORTED_WITH_LIMITATIONS | Host-selected workspace/tools/permissions; no unrestricted filesystem promise |
| Memory | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | NOT_VERIFIED | SUPPORTED_WITH_LIMITATIONS | Plugin's explicit case files only when file tools exist; no host memory promise |
| Persistent state | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | NOT_VERIFIED | SUPPORTED_WITH_LIMITATIONS | Project JSON helper tested; host cache/state availability is separate |
| Network | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | Host policies/connectors govern; no runtime helper network code |
| Permissions | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | Existing host controls remain authoritative; manifest grants no permission |
| Onboarding | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | O1 onboardingSkill; Claude setup is an ordinary packaged skill; actual auto-onboarding unverified |
| Updates | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | O1, C3/C5; local cache refresh versus account-managed version differs |
| Removal | SUPPORTED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | SUPPORTED | SUPPORTED | Local CLI help and C5; removal must preserve separately stored user cases |
| Native commands | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | SUPPORTED | SUPPORTED_WITH_LIMITATIONS | SUPPORTED_WITH_LIMITATIONS | Host picker/mentions or namespaced skill invocation; do not assume identical slash syntax across brands |
| Background execution | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | UNSUPPORTED | SUPPORTED_WITH_LIMITATIONS | C5 surface distinctions; background feature availability is not activated by this plugin |

## Packaging and distribution decisions

Portable root plugin.json declares Agent Plugins 1.0.0. No unsupported portable fields are used. OpenAI-specific interface/onboarding fields live under extensions.com.openai. The fallback .codex-plugin manifest is optional and uses documented skills/interface metadata. When inline com.openai exists, it wholly replaces fallback OpenAI settings. Claude uses its own manifest and scans the same skills; no duplicate intellectual catalog is maintained.

Repo .agents/plugins/marketplace.json and separate .claude-plugin/marketplace.json support private local development. A generated marketplace archive places the same runtime under plugins/cognition-os and points each platform's catalog at it. No public or organization publication is attempted. Personal marketplace modification and host installations outside this workspace are left to explicit user-authorized installation. No license, owner email, repository URL or privacy policy is fabricated.

Code 2.1.201's local manifest validation and eleven-skill/two-agent inventory were observed. The newer official account-sync minimum is not satisfied by that local version; this does not invalidate its tested --plugin-dir path. Claude Chat/Cowork upload and Codex desktop discovery/activation need independent live confirmation. Any failed native behavioral test remains a release blocker regardless of schema validity.
