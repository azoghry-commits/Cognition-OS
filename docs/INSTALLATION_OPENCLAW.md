# Install on OpenClaw

## 1. Prerequisites

Install the host and confirm its skills feature is available. Python 3.10+ is needed for local helpers. See [shared package preparation](INSTALLATION.md). Keep the complete package resource tree intact.

## 2. Install and discover

1. Review the extracted package and its `skills` directory.
2. Install every skill with `openclaw skills install --global --force --acknowledge-install-policy-warning <package-directory>/skills/<skill-name>`.
3. Inspect the entry point with `openclaw skills info cognition-orchestrator --json`.
4. Confirm `eligible`, `modelVisible`, and `userInvocable` are true.
5. Restart or refresh the serving Gateway/session.
6. Run a semantic task; skill discovery alone is not behavioral acceptance.

The package retains `openclaw.plugin.json` for compatible bundle tooling, while the skill installer is the verified path for this skills-only distribution. See the [official OpenClaw skills guide](https://docs.openclaw.ai/skills) and [plugin manifest reference](https://docs.openclaw.ai/plugins/manifest).

## 3. Verify behavior

Run the shared smoke test in the [installation index](INSTALLATION.md). Record host version, package version, loaded resource and actual helper output. Discovery is only the first check.

## 4. Update, rollback and remove

Retain the previous package, point the configured external directory at the reviewed replacement, and start a fresh session. Roll back by restoring that directory reference and verifying the installed version. Remove only the package registration/skill links when uninstalling. Preserve project `.cognition` data.

## 5. Troubleshoot

If a skill is missing, inspect its directory, frontmatter and host permissions. If a relative resource is missing, restore the complete package; copying isolated skill folders loses sibling resources. If a helper is unavailable, verify Python and the package-root path.
