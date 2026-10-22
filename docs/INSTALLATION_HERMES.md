# Install on Hermes Agent

## 1. Prerequisites

Install the host and confirm its skills feature is available. Python 3.10+ is needed for local helpers. See [shared package preparation](INSTALLATION.md). Keep the complete package resource tree intact.

## 2. Install and discover

1. Extract the complete package to a stable profile directory.
2. Add the extracted `skills` directory through `skills.external_dirs`, or copy its skill folders into `~/.hermes/skills` on macOS/Linux and `%LOCALAPPDATA%\\hermes\\skills` on Windows.
3. Run `hermes skills list` and confirm all 12 entries are reported as local and enabled.
4. Start a new session; use the immediate refresh option only when needed because it invalidates prompt cache.
5. Invoke `/cognition-orchestrator` for a deterministic smoke test.
6. Run a representative task and verify that the quality gate escalates risky work.

Hermes loads compact skill descriptions first and full instructions only when selected. See the [official Hermes skills guide](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills/) and [skills system](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/).

## 3. Verify behavior

Run the shared smoke test in the [installation index](INSTALLATION.md). Record host version, package version, loaded resource and actual helper output. Discovery is only the first check.

## 4. Update, rollback and remove

Retain the previous package, point the configured external directory at the reviewed replacement, and start a fresh session. Roll back by restoring that directory reference and verifying the installed version. Remove only the package registration/skill links when uninstalling. Preserve project `.cognition` data.

## 5. Troubleshoot

If a skill is missing, inspect its directory, frontmatter and host permissions. If a relative resource is missing, restore the complete package; copying isolated skill folders loses sibling resources. If a helper is unavailable, verify Python and the package-root path.
