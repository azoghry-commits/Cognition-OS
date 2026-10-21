# Installation index

## 1. Choose your host

| Host | Guide |
| --- | --- |
| Codex desktop / CLI | [Codex](INSTALLATION_CODEX.md) |
| Claude Code / Desktop | [Claude](INSTALLATION_CLAUDE.md) |
| OpenCode | [OpenCode](INSTALLATION_OPENCODE.md) |
| Command Code | [Command Code](INSTALLATION_COMMANDCODE.md) |
| OpenClaw | [OpenClaw](INSTALLATION_OPENCLAW.md) |
| Hermes | [Hermes](INSTALLATION_HERMES.md) |
| Antigravity / Copilot / VS Code / generic | [Portable hosts](INSTALLATION_PORTABLE.md) |

## 2. Prepare the package

Current package version: 0.5.0. Feature branch changes remain Unreleased. Build from a reviewed checkout:

```text
python scripts/package_release.py
```

Use `dist/cognition-os-<version>.zip` for runtime or `dist/cognition-os-marketplace-<version>.zip` for marketplace installation. Compare the archive SHA-256 with `dist/SHA256SUMS.json`: PowerShell `Get-FileHash <archive> -Algorithm SHA256`, Linux `sha256sum <archive>`. Member checksums are in `PACKAGE_CONTENTS.json` inside the runtime ZIP.

Extract into a stable versioned directory. Preserve the complete package tree: skills reference sibling cognitive-core, references, schemas and scripts. Prefer an external skills directory pointing to `<runtime-root>/skills`. Copying isolated skill folders breaks these relationships; hosts requiring copies need a tested adapter.

## 3. Shared verification

1. Record host/surface version, package version and installed path; start a new session.
2. Confirm setup and cognition-orchestrator discovery.
3. Ask: "Use Cognition OS to diagnose a deployment taking 20 minutes instead of 5. Identify missing evidence and use a relevant framework."
4. Confirm actual selected skill/framework reads, explicit gaps and a useful deliverable.
5. From the runtime root run `python scripts/cognition.py compute --input references/examples/ev.json`; retain actual output and compare against the input assumptions.
6. Negative control: request a simple sentence rewrite; confirm no unnecessary framework workflow.

Discovery, deterministic helper success and semantic quality are separate checks. Record hook delivery and native delegation separately. No claim of native support follows from package checks alone.

## 4. Lifecycle and troubleshooting

Keep prior ZIP/checksums, switch the registered source to update, restart and repeat smoke checks. Roll back by restoring the prior source and reviewing schema compatibility. Uninstall removes registration while preserving project `.cognition` data. See [troubleshooting](TROUBLESHOOTING.md).
