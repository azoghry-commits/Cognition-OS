# Install on Codex

## 1. Prerequisites

Use a supported Codex desktop/CLI and your existing host account. No provider API key is required. Python 3.10+ is needed for helpers and optional hooks. Historical account results are in [installation evidence](evidence/v4-1-codex-installation.json).

## 2. Prepare and register

Follow [package preparation](INSTALLATION.md). Extract the marketplace ZIP. Its root contains `.agents`, `.claude-plugin` and `plugins`.

```text
codex plugin marketplace add <absolute-marketplace-root>
codex plugin marketplace list
```

Source development: package first, then run `python scripts/prepare_local_marketplace.py` after reviewing the existing staged directory. The repository marketplace points at `local-marketplace/plugins/cognition-os`, so stage before registering the repository root.

## 3. Install

Open the desktop Plugins Directory, choose Cognition OS local and install the plugin. Restart if the local source is absent. Start a new chat and select setup. Marketplace discovery and enabled settings alone do not prove installation behavior. The host uses an installed cache copy; maintain source in the repository.

## 4. Verify

Check the installed manifest version and run the [shared verification](INSTALLATION.md). Review optional hook trust separately; hooks grant no additional permission and skills remain usable without them.

## 5. Update, rollback and remove

Retain the prior package and project cases. Refresh the configured source, reinstall/update through the host and open a fresh chat. Roll back using the retained package. Remove through native plugin controls; preserve `.cognition` records.

## 6. Troubleshoot

Check marketplace selection, installed cache version, Python and complete resource layout. Unsupported hooks require an explicit unavailable status.

Reference: [official packaging and local marketplaces](https://developers.openai.com/plugins/build/plugins).
