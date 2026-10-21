# OpenCode adapter

OpenCode discovers Agent Skills on demand. Keep the whole Cognition OS package together so relative references from `skills/*/SKILL.md` continue to resolve.

Project installation:

```powershell
New-Item -ItemType Directory -Force .opencode\vendor | Out-Null
Expand-Archive .\dist\cognition-os-0.5.0.zip .opencode\vendor\cognition-os -Force
@{ skills = @('.opencode/vendor/cognition-os/skills') } | ConvertTo-Json | Set-Content .opencode\opencode.json
```

Alternatively add the extracted `skills` directory to the existing OpenCode `skills` configuration. Start a new session, inspect the skill list, and run `@cognition-orchestrator` for a deterministic activation smoke test. Natural-language matching may activate it automatically.

Evidence boundary: discovery is separate from model selection and task quality.
