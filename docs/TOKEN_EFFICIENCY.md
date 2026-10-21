# Token efficiency with a quality floor

Cognition OS uses progressive disclosure and chooses the smallest safe context profile:

| Profile | Typical use | Framework cap | Reference cap | Review rounds |
| --- | --- | ---: | ---: | ---: |
| LEAN | simple, grounded, low-risk task | 1 | 1 | 0 |
| BALANCED | incomplete evidence or moderate complexity | 4 | 3 | 1 |
| DEEP | high complexity, risk, or uncertainty | 8 | 6 | 2 |

`python scripts/cognition.py token-plan` returns the selected profile, bounded context allowance, retained quality checks, and escalation triggers. A caller cannot force LEAN below the deterministic quality floor.

The system expands context when evidence conflicts, a decision-critical input is missing, a deterministic check fails, a critical objection appears, or the deliverable remains unsupported. It preserves claim-to-evidence links, UNKNOWN gaps, completion checks, and high-risk review.

`token-eval` accepts paired measured token usage and rubric scores. It permits `TOKEN_EFFICIENT_QUALITY_RETAINED` only when both the token-reduction threshold and maximum quality-loss threshold pass. This verdict applies only to the supplied paired evaluation; context budgets are not provider billing measurements.
