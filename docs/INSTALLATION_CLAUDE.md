# Install on Claude

## 1. Prerequisites

Use an available, authorized Claude surface. Code, Desktop/Chat and Cowork have different capabilities. Python 3.10+ is needed for local helpers/hooks. See [account scope](ACCOUNT_SCOPE.md); installation does not authorize paid inference.

## 2. Prepare

Follow [package preparation](INSTALLATION.md) and retain the complete runtime tree.

## 3. Install

Session-only Claude Code, from the extracted runtime root:

```text
claude plugin validate .
claude --plugin-dir <absolute-runtime-root>
```

Packaged local marketplace, inside Claude Code:

```text
/plugin marketplace add <absolute-marketplace-root>
/plugin install cognition-os@cognition-os-local
```

For Desktop/Chat/Cowork, use the supported Customize/Plugins upload flow when available to your account. Do not assume Code hooks, agents or local execution exist in plain Chat.

## 4. Verify

Start a new session. Invoke `/cognition-os:setup` on Code or select setup on the active surface, then run [shared verification](INSTALLATION.md). Native Claude inference remains unverified in this checkout; manifest validation does not close that gate.

## 5. Update, rollback and remove

Replace the reviewed package source, reinstall and start a new session. Roll back to the retained prior package. Use `/plugin uninstall cognition-os@cognition-os-local` on Code or native remove controls elsewhere. Preserve project cases.

## 6. Troubleshoot

Check discovery, resource paths, Python, account availability and optional hook trust/delivery. See [platform compatibility and official references](PLATFORM_COMPATIBILITY.md) and [observed verification](PLATFORM_VERIFICATION_V4_1.md).
