# Account and validation scope

Updated 2026-10-20 after the user's clarification.

V4.1 update: the same authorized Codex-only installation has been updated through the native CLI to package 0.2.0 and reports installed/enabled. Its installed inventory and helper checks are recorded in [v4-1-codex-installation.json](evidence/v4-1-codex-installation.json). A rollback snapshot of 0.1.0 is retained locally. Desktop model selection, hook trust/event delivery and host outcome benchmarks remain unverified. The 0.1.0 records below describe the earlier baseline.

The user specifically identified **ChatGPT Desktop** as the intended host. See DESKTOP_QUICKSTART.md. CLI installation and helper checks are engineering evidence; they do not certify activation in that desktop surface.

- User-provided entitlement: ChatGPT Plus / Codex subscription; Claude Free. The subscription tier is user-reported, not inferred from a stored credential.
- Observed local authentication: `codex login status` reports `Logged in using ChatGPT`.
- This plugin calls no model API. Codex-native behavioral validation should use the existing ChatGPT login and its included usage allowance; no API key, credits purchase or API-billed inference is authorized.
- Claude API-key configuration detected earlier does not constitute authorization to use it. Do not run paid Claude inference or install the Claude adapter for this account. Keep its local package and validation evidence available for future authorized testing.
- The user explicitly approved: "Yes, install in Codex only." The personal local marketplace is registered and Cognition OS 0.1.0 is installed/enabled in Codex. See evidence/codex-installation.json and evidence/desktop-catalog.json. Its stable source is C:/Users/rizky/.codex/plugins/local-sources/cognition-os, excluding development dependencies, original source documents and repository internals. Desktop activation remains unverified.
- Claude native behavioral testing is deferred because current official plugin availability is documented for paid Claude plans; this does not mean the user must buy a Claude subscription to use the Codex package.

Official references checked: [Codex/ChatGPT pricing and plan access](https://learn.chatgpt.com/docs/pricing), [native local marketplace packaging](https://developers.openai.com/plugins/build/plugins), [Claude plugin plan requirements](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

Codex subscription usage is limited by the user's plan. A signed-in CLI alone proves neither a remaining usage allowance nor successful Cognition OS installation/activation. Verify those independently without silently switching to API credentials.

The first native CLI smoke attempt was rejected before analysis because the CLI-selected gpt-6.1-sol model was unsupported for ChatGPT authentication on that route. The CLI also reported an exceeded skills context budget. No model, authentication, unrelated plugin setting or billing mode was changed to work around this failure. The second native smoke was not attempted after the failed preflight. This leaves semantic activation and behavior unverified; installation and installed-helper execution are separately verified.
