# Install on OpenCode

## 1. Prerequisites

Install the host and confirm its skills feature is available. Python 3.10+ is needed for local helpers. See [shared package preparation](INSTALLATION.md). Keep the complete package resource tree intact.

## 2. Install and discover

1. Build or download `cognition-os-0.5.0.zip`.
2. Extract it to a stable project or user directory.
3. Add the extracted `skills` directory to OpenCode's `skills` configuration, or expose each skill through `.opencode/skills`, `.agents/skills`, or their global equivalents.
4. Start a new session and inspect available skills.
5. Run `@cognition-orchestrator` with a bounded analysis request.
6. Confirm that only the matching skill and selected framework resources were loaded.

OpenCode loads skill names and descriptions for discovery, then loads the full `SKILL.md` through its skill tool only when selected. Supporting files are read on demand. See the [official OpenCode skills documentation](https://opencode.ai/docs/skills).

## 3. Verify behavior

Run the shared smoke test in the [installation index](INSTALLATION.md). Record host version, package version, loaded resource and actual helper output. Discovery is only the first check.

## 4. Update, rollback and remove

Retain the previous package, point the configured external directory at the reviewed replacement, and start a fresh session. Roll back by restoring that directory reference and verifying the installed version. Remove only the package registration/skill links when uninstalling. Preserve project `.cognition` data.

## 5. Troubleshoot

If a skill is missing, inspect its directory, frontmatter and host permissions. If a relative resource is missing, restore the complete package; copying isolated skill folders loses sibling resources. If a helper is unavailable, verify Python and the package-root path.
