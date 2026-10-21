# Hermes Agent adapter

Hermes supports external skill directories and progressive disclosure. Extract the package to a stable location and point Hermes at its `skills` directory, or copy the complete package and expose those skill directories through the profile configuration.

```powershell
$target = Join-Path $env:LOCALAPPDATA 'hermes\cognition-os'
Expand-Archive .\dist\cognition-os-0.5.0.zip $target -Force
hermes skills list
hermes skills check
```

Add `$target\skills` as an external skills directory using the Hermes skills configuration UI. Start a new session, or invalidate the current prompt cache only when immediate refresh is required. Invoke `/cognition-orchestrator` for a direct smoke test; ordinary matching prompts can activate it automatically.

Do not place Cognition OS in Hermes Skill Workshop: Workshop is intended for agent-authored skills and versioned self-learning, while this package uses its own governed proposal/evaluation/approval ledger.
