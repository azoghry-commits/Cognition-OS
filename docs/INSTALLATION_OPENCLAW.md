# Install on OpenClaw

1. Review the extracted package and its `skills` directory.
2. Install every skill with `openclaw skills install --global --force --acknowledge-install-policy-warning <package-directory>/skills/<skill-name>`.
3. Inspect the entry point with `openclaw skills info cognition-orchestrator --json`.
4. Confirm `eligible`, `modelVisible`, and `userInvocable` are true.
5. Restart or refresh the serving Gateway/session.
6. Run a semantic task; skill discovery alone is not behavioral acceptance.

The package retains `openclaw.plugin.json` for compatible bundle tooling, while the skill installer is the verified path for this skills-only distribution. See the [official OpenClaw skills guide](https://docs.openclaw.ai/skills) and [plugin manifest reference](https://docs.openclaw.ai/plugins/manifest).
