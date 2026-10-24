# Context validity confirmation v2

20 newly authored synthetic confirmation cases, including 10 negative controls. Labels were authored from the documented contract; candidate outputs have not been collected or used to set labels. Human review is pending. This set covers composed conditions/scopes, optional facts, timezone observations, provenance, evidence changes and untrusted evidence content. It is a small screening set and not production-representative.

The previous CV-01..20 suite is consumed and excluded. Use the same efficient model, host settings and scoring/latency gates for both arms. No full cohort execution until human approval.

## Executed and consumed

User approval is recorded in human-review.json. The initial attempt exposed three cases before duplicate condition IDs were repaired; predicates, observations and labels were unchanged. The corrected40-run cohort is qualified confirmation evidence, and all attempts are archived separately. See [report](../../../docs/NATIVE_CONTEXT_VALIDITY_EVALUATION_V2.md). Do not reuse this set as fresh held-out evidence.

Reproduction for diagnostics only (consumes subscription quota):

```powershell
uv run --locked --extra dev python scripts/evaluate_context_host.py --run --fixtures tests/native-evals/context-validity-v2 --output tmp/v2-diagnostic
```

Without --run, the runner validates and freezes inputs only. A nonpilot run rejects absent human approval before launching the host. Schema preflight rejects duplicate condition IDs before inference. The frozen historical runner is included in the archive.
