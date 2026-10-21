# Command Code adapter

Extract the full package, then register its `skills` directory in Command Code settings so all sibling core resources remain available.

```powershell
New-Item -ItemType Directory -Force .commandcode\vendor | Out-Null
Expand-Archive .\dist\cognition-os-0.5.0.zip .commandcode\vendor\cognition-os -Force
$settings = @{ skills = @('./.commandcode/vendor/cognition-os/skills') }
$settings | ConvertTo-Json -Depth 4 | Set-Content .commandcode\settings.json
cmd skills list --debug
```

For one session, use `cmd --skill ./.commandcode/vendor/cognition-os/skills`. Command Code progressively discloses full skill instructions only after a match or direct slash invocation.

Evidence boundary: listing a skill proves discovery only. Run a semantic task and inspect the resulting evidence discipline separately.
