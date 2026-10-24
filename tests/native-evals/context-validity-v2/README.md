# Context validity confirmation v2

20 newly authored synthetic confirmation cases, including 10 negative controls. Labels were authored from the documented contract; labels were not adjusted from candidate outputs. Human review and subsequent execution are recorded below. This set covers composed conditions/scopes, optional facts, timezone observations, provenance, evidence changes and untrusted evidence content. It is a small screening set and not production-representative.

The previous CV-01..20 suite is consumed and excluded. Use the same efficient model, host settings and scoring/latency gates for both arms. No full cohort execution until human approval.

## Executed and consumed

User approval is recorded in human-review.json. The initial attempt exposed three cases before duplicate condition IDs were repaired; predicates, observations and labels were unchanged. The corrected40-run cohort is qualified confirmation evidence, and all attempts are archived separately. See [report](../../../docs/NATIVE_CONTEXT_VALIDITY_EVALUATION_V2.md). Do not reuse this set as fresh held-out evidence.

Offline reproduction (no inference):

```powershell
uv run --locked --extra dev python scripts/audit_context_host.py audit --summary docs/evidence/context-validity-native-v2-2026-10-24.json --cohort heldout-batched-v2-corrected-20261024 --output tmp/offline-v2.json
```

The historical human-review.json is preserved unbound. The current collector blocks new nonpilot execution with this certificate; it requires content-bound approval of the specific suite. See [approval and audit instructions](../../../docs/OFFLINE_EVALUATION_AUDIT.md). Do not manufacture a new approval by adding hashes to the historical certificate. This consumed set cannot become fresh held-out evidence.
