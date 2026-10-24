# Native context validity evaluation — 2026-10-24

Correctness screening improved, but overall acceptance failed because latency exceeded the predeclared limit. The paired capability verdict is `IMPROVED_NOT_SIGNIFICANT`; this evidence does not support a significant-improvement claim or release promotion.

## Protocol and result

The user approved labels before held-out candidate execution. Both arms used authenticated Codex CLI 0.153.0 with `gpt-5.6-luna`, low reasoning, sequential shuffled execution (seed 20261023): 20 synthetic pairs, including 10 negative controls. Candidate runtime was frozen at `1eda4349fab4d71162e0ff207b89c1e8f5858e60`. Candidate explicitly read the project-local skill and executed the memory-check helper in all 20 runs. All 40 runs completed with verified workspace reads.

| Measure | Baseline | Candidate |
| --- | ---: | ---: |
| Exact structured decisions | 18/20 | 20/20 |
| Mean three-field rubric | 0.9333 | 1.0000 |
| Review precision | 90.9% | 100% |
| Review recall | 100% | 100% |
| Negative-control false-positive rate | 10% | 0% |
| Median whole-CLI latency | 14.892 s | 24.840 s |
| Host-reported input tokens | 4,840,909 | 6,650,413 |
| Cached input tokens (subset of input) | 3,043,200 | 4,253,184 |
| Output tokens | 4,632 | 8,428 |

Median paired latency overhead was **59.1%**, exceeding the maximum **20%**. This is the median of per-pair ratios, not the ratio of group medians. Other product screening gates passed; `acceptance_passed=false`.

The capability comparison produced 2 wins, 0 losses and 18 ties, mean score delta 0.0667 (minimum 0.1), sign-test p=0.5 (maximum 0.05). Baseline errors involved boolean/numeric typing (CV-08) and an inclusive freshness boundary (CV-12). The rubric equally weights status, reuse_allowed and review_required; it does not semantically grade the reason text.

## Interpretation and limits

No fixture modifications or prohibited deletion attempts were observed by the runner's tripwires. This is bounded evidence, not a security certification. Explicit invocation does not establish automatic skill activation, installed-plugin discovery, hooks, cross-host behavior or production readiness.

Token usage increased. Global user instructions were observed at 479,812 bytes; a separate context-limit probe did not remove that context and was excluded from the cohort. Local helper timing across 10 runs had a median of 0.225 s including Python startup/imports/JSON. Extra host interactions and global context are plausible contributors to overhead, but these measurements do not establish a causal breakdown. No monetary cost or token-saving claim is made. No additional solver inference was used for the final audit.

Earlier unsupported-model, blocked-read and quota preflights, plus an incomplete default-frontier cohort, were excluded from this efficient-model comparison. Automatic approval remained host-managed; the runner did not bypass approval review.

A fresh lightweight review found that loose command/output matching could mistake echoed text for actual reads or helper execution. Post-collection harness fixes now bind input hashes (LF/CRLF), allowed command shapes and complete helper JSON to the expected fixture. Regression tests cover those false-positive paths. The same raw logs were audited again with unchanged labels, rubric and candidate runtime; all 20 helper executions remain verified. The archive preserves the original runner and original records alongside the audited records and hardened auditor source.

## Reproducible evidence and next step

- [Audited summary](evidence/context-validity-native-2026-10-24.json)
- [Raw logs, frozen inputs, approval and auditor](evidence/context-validity-native-2026-10-24.zip)
- [Collection protocol](CONTEXT_VALIDITY.md) and [runner instructions](../tests/native-evals/context-validity/README.md)

The archive contains the original frozen protocol snapshot. Its SHA-256 is recorded in the audited summary. Original collected records remain intact; audited-runs.json adds fixture-bound evidence, and audited-summary.json is the authoritative regrade.

Keep this as an engineering candidate on feat/context-validity. Next investigate fewer host/tool round trips and bounded context on development cases, then confirm any revised candidate against a new independently reviewed held-out set. This set is consumed; reruns are diagnostic only. No release, merge or installation is justified by these results alone.
