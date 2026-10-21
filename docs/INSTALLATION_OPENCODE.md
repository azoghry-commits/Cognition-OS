# Install on OpenCode

1. Build or download `cognition-os-0.5.0.zip`.
2. Extract it to a stable project or user directory.
3. Add the extracted `skills` directory to OpenCode's `skills` configuration, or expose each skill through `.opencode/skills`, `.agents/skills`, or their global equivalents.
4. Start a new session and inspect available skills.
5. Run `@cognition-orchestrator` with a bounded analysis request.
6. Confirm that only the matching skill and selected framework resources were loaded.

OpenCode loads skill names and descriptions for discovery, then loads the full `SKILL.md` through its skill tool only when selected. Supporting files are read on demand. See the [official OpenCode skills documentation](https://opencode.ai/docs/skills).
