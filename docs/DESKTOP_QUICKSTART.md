# ChatGPT Desktop quick start

The user's target is ChatGPT Desktop on Windows, using the existing ChatGPT Plus/Codex login. CLI commands used during engineering are not the ordinary operating interface.

1. Save any ongoing work and restart ChatGPT Desktop to refresh local plugin discovery.
2. Open a new Codex or supported local Work chat, then open Plugins Directory.
3. Select the local source named **Cognition OS local** or **Cognition OS local development** and locate **Cognition OS**. Confirm it is installed/enabled; if the directory offers Install, use that native action.
4. Select the packaged **setup** skill through the native skill picker, or ask: "Use Cognition OS setup and check which capabilities are available in this chat."
5. Try: "Use Cognition OS and Kepner-Tregoe to analyze recurring MariaDB failures. No logs have been supplied yet." The expected behavior is to identify missing evidence and safe checks, not claim a verified cause.

Installation/cache integrity is verified. Activation and behavioral output in this ChatGPT Desktop surface remain unverified until those native interactions are observed. The earlier CLI model/context-budget rejection is a separate result and does not prove desktop failure. No Claude or API-billed inference is authorized.

Personal marketplace discovery uses ~/.agents/plugins/marketplace.json. Its source points to a stable clean plugin snapshot under ~/.codex/plugins/local-sources/cognition-os, with the native installed cache kept separately. Official reference: [OpenAI local marketplace instructions](https://developers.openai.com/plugins/build/plugins).
