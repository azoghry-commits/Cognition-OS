# Cross-host compatibility

Package 0.4.0 keeps one cognitive core and uses thin host adapters. The canonical `plugin.json` follows Agent Plugins 1.0 for Codex, GitHub Copilot, and VS Code-compatible harnesses. Claude uses `.claude-plugin/plugin.json`. Antigravity receives a dedicated archive with its minimal root manifest while reusing the same skills and resources. Generic Agent Skills hosts may consume selected `skills/<name>/` bundles directly.

| Surface | Packaging path | Portable baseline | Host-dependent capability |
|---|---|---|---|
| Codex CLI/Desktop | Agent Plugins 1.0 plus OpenAI extension | Skills, schemas, helpers | hooks, delegation, local tools |
| Claude Desktop Chat | Claude custom plugin | Skills and commands | no local hooks or subagents in Chat |
| Claude Code/CLI | Claude plugin | Skills, agents, hooks, helpers | account sync, permissions, concurrency |
| Antigravity App/CLI/IDE | Antigravity archive or local plugin | Skills, helpers, DAG plans | subagents, background work, hooks |
| GitHub Copilot | Agent Plugins 1.0 or repository skills | Skills and portable resources | cloud-agent settings, code review, agents |
| VS Code | Agent Plugins 1.0 | Skills and portable resources | selected harness, hooks, agents, MCP |
| Other Agent Skills hosts | selected skill folders | instructions and referenced resources | scripts, tools, persistence, delegation |

Compatibility means the host can discover the package format. It does not prove model selection, account eligibility, permissions, event delivery, semantic quality, or parallel capacity. Validate each target surface with its customization diagnostics or plugin inventory and a natural activation task plus a negative control.

## Analysis execution

`analysis-plan` accepts a list of steps with `step_id` and `depends_on`, then produces dependency-safe waves. `SEQUENTIAL` emits one step per wave. `PARALLEL` and `HYBRID` group independent steps only when the host reports parallel support and the concurrency allowance is greater than one. The next wave begins after all prerequisite outputs have been returned and validated. Planning never fabricates a native dispatch.
