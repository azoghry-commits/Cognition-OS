# Install on Command Code

## 1. Prerequisites

Install the host and confirm its skills feature is available. Python 3.10+ is needed for local helpers. See [shared package preparation](INSTALLATION.md). Keep the complete package resource tree intact.

## 2. Install and discover

1. Extract the full package to a stable directory.
2. Add its `skills` directory to the `skills` array in user, project, or local `settings.json`.
3. Run `commandcode skills list --debug` on Windows, or `cmd skills list --debug` where the short CLI name is available, and resolve every skipped Cognition OS entry.
4. Start Command Code in the target project.
5. Invoke `/cognition-orchestrator`, or use `/skill:cognition-orchestrator` if a command name shadows it.
6. Run a semantic task and inspect evidence, limitations, and stopping behavior.

For a one-session test, use `commandcode --skill <package>/skills` on Windows or `cmd --skill <package>/skills` where available. Command Code also discovers `.agents/skills`. See the [official Command Code skills documentation](https://commandcode.ai/docs/skills).

## 3. Verify behavior

Run the shared smoke test in the [installation index](INSTALLATION.md). Record host version, package version, loaded resource and actual helper output. Discovery is only the first check.

## 4. Update, rollback and remove

Retain the previous package, point the configured external directory at the reviewed replacement, and start a fresh session. Roll back by restoring that directory reference and verifying the installed version. Remove only the package registration/skill links when uninstalling. Preserve project `.cognition` data.

## 5. Troubleshoot

If a skill is missing, inspect its directory, frontmatter and host permissions. If a relative resource is missing, restore the complete package; copying isolated skill folders loses sibling resources. If a helper is unavailable, verify Python and the package-root path.
