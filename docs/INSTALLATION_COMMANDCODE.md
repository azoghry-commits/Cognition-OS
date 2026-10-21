# Install on Command Code

1. Extract the full package to a stable directory.
2. Add its `skills` directory to the `skills` array in user, project, or local `settings.json`.
3. Run `commandcode skills list --debug` on Windows, or `cmd skills list --debug` where the short CLI name is available, and resolve every skipped Cognition OS entry.
4. Start Command Code in the target project.
5. Invoke `/cognition-orchestrator`, or use `/skill:cognition-orchestrator` if a command name shadows it.
6. Run a semantic task and inspect evidence, limitations, and stopping behavior.

For a one-session test, use `commandcode --skill <package>/skills` on Windows or `cmd --skill <package>/skills` where available. Command Code also discovers `.agents/skills`. See the [official Command Code skills documentation](https://commandcode.ai/docs/skills).
