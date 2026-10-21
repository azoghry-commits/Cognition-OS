# Install on Hermes Agent

1. Extract the complete package to a stable profile directory.
2. Add the extracted `skills` directory through `skills.external_dirs`, or copy its skill folders into `~/.hermes/skills` on macOS/Linux and `%LOCALAPPDATA%\\hermes\\skills` on Windows.
3. Run `hermes skills list` and confirm all 12 entries are reported as local and enabled.
4. Start a new session; use the immediate refresh option only when needed because it invalidates prompt cache.
5. Invoke `/cognition-orchestrator` for a deterministic smoke test.
6. Run a representative task and verify that the quality gate escalates risky work.

Hermes loads compact skill descriptions first and full instructions only when selected. See the [official Hermes skills guide](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills/) and [skills system](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/).
