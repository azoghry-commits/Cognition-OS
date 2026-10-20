# Codex installation and lifecycle

## V4.1 rebuild candidate / package 0.2.0

Build locally with `python scripts/rebuild_plugin.py --package`. The runtime package is `dist/cognition-os-0.2.0.zip`, the local marketplace is `dist/cognition-os-marketplace-0.2.0.zip`, and checksums are in `dist/SHA256SUMS.json`. Verify checksums and inventory before using a package. Building does not alter personal source/cache or installed/enabled state.

For updates, retain the previous ZIP and marketplace configuration, keep user cases outside the cache, point the reviewed marketplace source at the candidate runtime, and refresh/install through the UI or available native command. Verify version 0.2.0 in the installed manifest; discovery alone does not establish installation. The host may need a restart or new chat to load updated skills.

The root manifest selects `hooks/codex/hooks.json`. Hook availability depends on the supported surface/installation and requires host-side user review/trust; building or enabling the plugin does not grant it. Ensure Python is available. Supported skills and helpers remain usable without the hook. Run setup diagnostics, then a natural task and negative control; retain evidence of the selected skill/resource, tool result, event feedback, and deliverable.

Rollback: select the retained 0.1.0 source/ZIP, reinstall through the native mechanism, and inspect the installed version and artifact compatibility. Framework envelope 3.1 remains available; advisory request/result 4.1 is a new contract. Do not automatically delete or convert `.cognition/cases`. The rebuild session updated the Codex-only installation to 0.2.0; the native CLI reported installed/enabled, and installed inventory hashes and helpers were verified. A backup is at `dist/cognition-os-rollback-0.1.0.zip`; restore has not been tested. See [installation evidence](evidence/v4-1-codex-installation.json) and [acceptance status](REBUILD_STATUS_V4_1.md).

## Baseline installation history and local mechanism

For this user's account, use the existing ChatGPT login and ChatGPT Plus/Codex allowance. `codex login status` was verified to report ChatGPT authentication. No API key or Claude subscription is required by this package. Do not switch to API billing or buy credits. See ACCOUNT_SCOPE.md for the current authorization and deferred Claude tests.

Portable root plugin.json is canonical. Root extensions.com.openai replaces the optional .codex-plugin/plugin.json OpenAI settings wholesale; it does not merge. Both discover the same skills and canonical resources. No MCP/hook is required. No API credentials are needed. Python 3.10+ is optional when native validated calculation is unavailable.

The repo includes .agents/plugins/marketplace.json pointing to ./local-marketplace/plugins/cognition-os relative to the marketplace root. First run the packaging script, then scripts/prepare_local_marketplace.py once to stage the allowlisted runtime. Registering this repository then installs that clean snapshot rather than copying source documents, development dependencies and Git internals. Local installs use a cache copy; verify its content/version after changes. Review an existing staging directory before replacing it.

Observed on this account: cognition-os@cognition-os-local version 0.1.0 is installed and enabled. Open a fresh Codex desktop chat, select the Cognition OS setup skill and check activation. The earlier native CLI smoke failed before analysis on its model availability/context-budget settings; installation success does not certify that behavioral gate.

For a packaged marketplace, extract dist/cognition-os-marketplace-0.1.0.zip. It contains plugins/cognition-os and both marketplace catalogs. Add its root with `codex plugin marketplace add <absolute-marketplace-root>`. Current installed CLI 0.153.0 also exposes `codex plugin add cognition-os@cognition-os-local --json`; this command's availability was verified by local help, and must be distinguished from the official desktop installation walkthrough. Do not infer a successful desktop install from CLI help.

In a fresh native chat run the installed setup skill through the skill picker, then request Kepner-Tregoe for a deviation with missing IS NOT evidence. Confirm correct skill activation, referenced core file access, missing-data behavior and helper execution. Use references/examples/ev.json as the calculation smoke; require exact gross/net values within floating tolerance. Record actual tool and response evidence.

Personal marketplace instructions: maintain ~/.agents/plugins/marketplace.json, point its source at a plugin location relative to that marketplace root, restart the desktop host and install from the local source. This project does not modify personal files automatically. Repo settings .codex/config.toml can enable a trusted local-marketplace entry with [plugins."cognition-os@cognition-os-local"] enabled=true, but discovery alone is not installation proof.

Update: regenerate/validate, increment version, install/refresh the reviewed source and confirm cache content. Rollback: retain previous ZIP/version, restore its marketplace entry and reinstall after reviewing data schema compatibility. Removal: native plugin remove or verified CLI `codex plugin remove` usage. Preserve user .cognition/cases data; uninstall never deletes it. Claude agent files are not advertised as Codex-native registered agents.

