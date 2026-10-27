# OpenCode adapter

OpenCode discovers Agent Skills on demand. Keep the whole Cognition OS package together so relative references from `skills/*/SKILL.md` continue to resolve.

Project installation:

```powershell
New-Item -ItemType Directory -Force .opencode\vendor | Out-Null
Expand-Archive .\dist\cognition-os-0.5.0.zip .opencode\vendor\cognition-os -Force
@{ skills = @('.opencode/vendor/cognition-os/skills') } | ConvertTo-Json | Set-Content .\opencode.json
```

If `opencode.json` already exists, merge this path into its `skills` array instead of replacing the file. Relative skill paths resolve from the process working directory. Alternatively expose the package through `.opencode/skills`, `.agents/skills`, or a documented global skill directory.

Start a new session, inspect the skill list, and run `@cognition-orchestrator` for a deterministic activation smoke test. Natural-language matching may activate it automatically. Skill IDs come from directory paths; duplicate IDs can shadow one another. For an explicit negative control on OpenCode 1, deny the test skill through OpenCode's `skill` permission.

Evidence boundary: discovery is separate from model selection and task quality.
