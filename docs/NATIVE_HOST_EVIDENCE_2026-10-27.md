# Native host evidence — 2026-10-27

This record covers one Windows machine, one installed Cognition OS 0.5.0 snapshot, and the host/model versions named below. It is evidence for these runs only, not a general host certification.

## Codex Desktop

Each case ran in a new Codex Desktop task.

| Case | Observable result | Verdict |
| --- | --- | --- |
| Explicit invocation | Codex read the installed `skills/cognition-orchestrator/SKILL.md`, then read `cognitive-core/augmentation/policy.json`, and returned `SKILL_USED=cognition-orchestrator`. | PASS |
| Implicit invocation | Codex completed the bounded release analysis without reading a Cognition OS skill and returned `SKILL_USED=none`. | NOT ACTIVATED |
| Negative control | The arithmetic prompt returned `17 + 25 = 42` and `SKILL_USED=none`. | PASS |

The explicit case proves installed-skill discovery and execution for that prompt. The implicit case does not support a claim that Codex Desktop automatically selects Cognition OS from the skill description.

## OpenCode

OpenCode 1.18.27 ran from a clean project fixture containing one project-local skill (`native-proof`) and one supporting file (`reference.txt`). Both successful runs used `--pure` and the available `opencode/big-pickle` model.

| Case | Observable result | Verdict |
| --- | --- | --- |
| Positive prompt | OpenCode displayed `Skill "native-proof"`, read `.opencode/skills/native-proof/reference.txt`, returned `REFERENCE_TOKEN: COGNITION_NATIVE_20261027`, and ended with `SKILL_USED=native-proof`. | PASS |
| Negative prompt | OpenCode returned `17 + 25 equals 42` and `SKILL_USED=none`; it did not display a skill or reference read. | PASS |

The installed OpenCode launcher initially contained its postinstall error stub. Running the package's bundled `postinstall.mjs` restored the Windows executable. The configured default Cloudflare model and one RAP fallback were unavailable during this check, so the successful evidence uses the explicit model above.

## Claim boundary

These observations establish explicit Cognition OS use in Codex Desktop and positive/negative project-skill behavior in OpenCode. They do not establish automatic Cognition OS activation in Codex Desktop, optional hook delivery, behavior on other accounts or machines, or semantic quality improvements.
