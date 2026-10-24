# Context validity and decision review

The optional helpers check whether stored knowledge still fits explicitly supplied context. They do not certify the truth of a decision, infer semantic contradictions, run commands from evidence, or monitor a project in the background. Runtime dependencies remain empty.

## Read-only commands

Run the installed `scripts/cognition.py` by absolute path. Actions accept JSON from stdin or `--input <file>`. Successful results return exit code 0; invalid input returns code 2 and a FAILED JSON object on stderr.

| Action | Input | Result |
| --- | --- | --- |
| `memory-check` | `record`, `context`, optional ISO `now` | Derived status, per-condition checks, limitations, `truth_verified: false`. Pure check of caller-supplied data. |
| `memory` operation `check` | `workspace`, `args` containing `case_id`, `context`, optional `now` | Reads a stored case and binds context project_id to that workspace's actual identity. |
| `memory` operation `list` | Existing query plus optional `context`, `status`, `now` in args | Existing result shape without context; adds validity when context is supplied. Status filtering requires context. |
| `evidence-snapshot` | `workspace`, `paths` mapping evidence IDs to relative files, optional `now` | SHA-256 observations, unavailable reasons, omitted IDs and completeness. |
| `decision-impact` | `nodes`, `changes`, optional `max_results` | Decisions requiring review or missing evidence, unmapped changes, missing references and completeness. |

Use `references/examples/context-validity.json` as a deterministic input:

```powershell
python scripts/cognition.py memory-check --input references/examples/context-validity.json
```

Its historical `now` makes the example reproducible. In live use omit now to use the current UTC clock. Never copy an old timestamp into a fresh observation. The host must supply a new source observation; these helpers cannot authenticate caller-supplied facts or timestamps.

## Applicability contract

`schemas/applicability.schema.json` describes optional `record.applicability`. It has its own schema_version `1.0`; the existing case envelope remains `1.0`. No migration or rewrite is required for old cases. Cases without applicability return unknown. Unsupported metadata versions fail explicitly. Runtime validation additionally rejects duplicate condition/evidence IDs and nonfinite numbers.

- Scope may constrain project_id, component and task_type. Missing scope context yields unknown; a known mismatch yields contradicted. Use the stored-case check for binding to the real project identity. The pure memory-check trusts its input.
- Supply 1â€“128 conditions with unique IDs, fact keys, an operator, expected value, optional required boolean (default true) and max_age_seconds (default 86400, range 0â€“31536000).
- Operators: equals, in, lt, lte, gt, gte. Numeric ordering accepts finite numbers only. Boolean and numeric equality are distinct. Null or wrong-type observations yield unknown. Version strings support equality/membership only, not numeric ordering.
- Every fact observation has value, nonempty source and timezone-aware observed_at. Future timestamps, stale observations and missing fields yield unknown. Age exactly equal to the freshness limit is still current.
- Optional evidence_refs hold unique IDs, lowercase SHA-256 fingerprints and the same freshness limit. Evidence observations require fingerprint, source and observed_at. Changed fingerprints yield needs_review; absent/unusable observations yield unknown.
- review_after requests review at or after its timezone-aware timestamp. It does not automatically reverse a decision. limitations are retained in output. supersedes documents a prior case; it does not overwrite/delete it.

Aggregate precedence for required checks is contradicted > needs_review > unknown > applicable. All individual checks remain visible. Optional mismatches do not override the aggregate, but a record with no required checks cannot become applicable merely by disabling every condition. Even applicable means only that the declared conditions matched the supplied facts.

Saving metadata still requires the existing persistence authorization and, where appropriate, sensitive-content authorization. Checking/retrieval never supplies either permission and never mutates files. Inputs, metadata and context are bounded to about 1 MB each, with 512 facts/evidence observations per map. Retrieval follows the existing store's title query and does not add semantic search.

## Evidence snapshots and impact

Snapshots accept up to 128 named regular files, up to 1 MB per file, with a cumulative read budget (about 16 MB plus one bounded probe read). Paths must be workspace-relative; traversal, drive-relative paths, alternate streams, child symlinks and junctions are rejected. Unavailable/oversized files cannot be interpreted as unchanged. Unprocessed entries are returned in omitted_ids with complete false. Snapshots compare metadata before/after reading, but do not provide an OS sandbox, authenticated provenance, hard-link isolation, or race-free access against a malicious local writer.

Impact nodes have unique id, kind (evidence/assumption/decision), and depends_on containing IDs of prerequisites. This is a separate contract referencing the same logical IDs where useful; it does not change provenance.schema.json or add unsupported fields to it.

```json
{
  "nodes": [
    {"id": "writer-count", "kind": "evidence", "depends_on": []},
    {"id": "single-writer", "kind": "assumption", "depends_on": ["writer-count"]},
    {"id": "json-storage", "kind": "decision", "depends_on": ["single-writer"]}
  ],
  "changes": ["writer-count"]
}
```

The JSON storage decision becomes needs_review. Unchanged, disconnected decisions are not returned. Missing dependencies propagate unknown unless an explicit relevant change already requires review. Cycles, duplicate IDs/dependencies, more than 1000 nodes, more than 4096 edges, and malformed input fail explicitly. max_results is 1â€“1000 (default 1000); truncation reports omitted_decisions and complete false. Unknown change IDs report unmapped_changes. A complete graph check is relative only to the supplied graph; it does not establish that every real dependency was recorded.

## Verification and native acceptance

Automated tests exercise comparisons, freshness, precedence, compatibility, storage immutability, graph propagation, bounds, file scope, published schemas and all three commands from an extracted package. Local helper success does not establish model-selected skill discovery or improved task outcomes.

Native evaluation protocol (not executed by these tests):

1. Freeze at least 20 paired task cases, including unchanged/relevant/irrelevant changes, legacy cases, missing/stale observations and untrusted instructions inside evidence. Include at least 10 held-out negative controls. Keep held-out content out of skill tuning and regression generation.
2. Have a human label which decisions require review and which memories can be reused before reviewing candidate output. Run baseline/candidate on the same authorized host/settings; record actual selected skill, loaded resources, tools/results and final deliverable.
3. Product acceptance targets set before candidate host measurement: precision and recall of review flags each at least 0.90, false positive rate on negative controls at most 0.10, no new critical scope/persistence error, and median paired latency overhead at most 20%. Record raw counts/denominators; these small samples are screening thresholds, not statistical certification. Token overhead remains null when unavailable.
4. Any significant capability-gain claim must additionally pass the existing capability-eval paired gates. Keep latency, cost, task quality, and host support separate. Do not infer native acceptance from deterministic fixtures or package smoke.

The future failure-to-regression, experiment-selection and sensitivity features remain separate backlog items in CONTEXT_VALIDITY_DEVELOPMENT_PLAN.md. No package version bump or publication follows automatically from local implementation.

## Observed native evaluation — 2026-10-24

The [20-pair efficient-model evaluation](NATIVE_CONTEXT_VALIDITY_EVALUATION.md) completed. Acceptance failed the latency threshold; capability verdict IMPROVED_NOT_SIGNIFICANT. The evidence archive preserves the premeasurement protocol snapshot.

## Qualified v2 confirmation — 2026-10-24

The [corrected v2 cohort](NATIVE_CONTEXT_VALIDITY_EVALUATION_V2.md) met product screening thresholds at 8.79% paired overhead. Both arms scored20/20; no measurable capability gain or token saving. Three cases were partially exposed before a condition-ID fixture correction; the report preserves this limitation and excludes the incomplete attempt.
