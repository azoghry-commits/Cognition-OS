# Model compatibility

Cognition OS is model-agnostic. It works best when the host model can follow system instructions, select a skill, read local files, preserve structured fields, and use tools. The plugin can improve task execution through scaffolding, evidence discipline, deterministic checks, and bounded review; it does not change model weights, context limits, provider policy, or underlying intelligence.

Use the latest generally available instruct, reasoning, or coding model exposed by the host. Confirm the exact model ID in the provider or host picker because catalogs and aliases change.

| Provider or route | Suitable model families | Recommended profile | Notes |
| --- | --- | --- | --- |
| OpenAI / Codex | current GPT reasoning, GPT coding/Codex, GPT mini; `gpt-oss` for capable local serving | BALANCED or DEEP; LEAN for well-defined edits | Prefer tool-capable models with configurable reasoning for complex workflows. |
| Anthropic / Claude | current Claude Opus and Sonnet; Haiku for bounded low-risk tasks | DEEP for Opus/Sonnet; LEAN or BALANCED for Haiku | Claude plugin components differ between chat, Desktop, and Code; verify the active surface. |
| Google / Antigravity / Gemini | current Gemini Pro and Flash; Flash-Lite for routine work; Gemma instruct models when locally hosted | DEEP for Pro, BALANCED for Flash, LEAN with escalation for Flash-Lite/Gemma | Stable model IDs are preferred over preview aliases for reproducible acceptance. |
| GitHub Copilot | any current Copilot model with Agent Skills/plugin discovery and tool use | AUTO | The selectable provider model varies by account, policy, and client. |
| xAI | current Grok reasoning or coding-capable models | BALANCED or DEEP | Require tool use and structured-output acceptance in the chosen host. |
| DeepSeek | current DeepSeek general/reasoning models with function calling | BALANCED or DEEP | Thinking mode may increase tokens; combine it with the plugin quality floor. |
| Mistral | current Large, Medium, Small, or Codestral instruct models | BALANCED for Large/Medium; LEAN with escalation for Small/Codestral | Validate tool calls and long-context behavior on the selected endpoint. |
| Alibaba Qwen | current Qwen Coder, Plus/Max, or capable Qwen instruct models | BALANCED or DEEP; constrained profile for smaller local variants | Qwen Code and OpenAI-compatible hosts can expose several providers. |
| Meta Llama | current Llama Instruct models served through a compatible host | capability-dependent | Larger instruct variants generally need less scaffolding; local quantization can affect reliability. |
| MiniMax, Kimi, Z.AI and other OpenAI/Anthropic-compatible providers | current instruct/reasoning/coding model offered by the host | start BALANCED, then evaluate | Compatibility depends on the host's skill discovery and tool protocol, not the provider name alone. |
| Ollama, vLLM, llama.cpp, LM Studio and other local routes | any instruct model that reliably follows the host's skill and tool protocol | constrained or BALANCED | Use small evidence packets, sequential steps, and deterministic checks. Context size alone does not establish quality. |

Provider references: [OpenAI models](https://platform.openai.com/docs/models), [Anthropic models](https://docs.anthropic.com/en/docs/about-claude/models), [Gemini models](https://ai.google.dev/gemini-api/docs/models), [xAI models](https://docs.x.ai/docs/models), [DeepSeek model API](https://api-docs.deepseek.com/api/list-models/), [Mistral models](https://docs.mistral.ai/getting-started/models/models_overview/), [Qwen model providers](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers/), and [Meta Llama](https://ai.meta.com/llama/get-started/).

## Tier guidance

- **Constrained models:** explicit contracts, one method per step, small evidence packets, sequential execution, and mandatory checks.
- **Balanced models:** bounded decomposition, claim-to-evidence links, selective deterministic checks, and one adversarial pass when useful.
- **Advanced models:** sparse scaffolding, parallel independent challenge where supported, and stopping when marginal value is exhausted.

Promotion between profiles uses observed paired task results, not marketing tiers or price. Use `capability-eval` for capability claims and `token-eval` for token-efficiency claims.
