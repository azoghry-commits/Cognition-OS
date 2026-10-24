# Native context validity v2 — 2026-10-24

The corrected v2 cohort passed the predeclared product screening thresholds. It did not show a capability gain or token saving. Because three cases were exposed in an incomplete attempt before an administrative fixture correction, this is qualified confirmation evidence rather than a completely untouched held-out result.

## Measured results

20 pairs and 10 negative controls ran sequentially with gpt-5.6-luna, low reasoning, identical host settings and unchanged scoring/latency gates. Human approval of v2 labels was recorded before candidate execution. The revised invocation reads the skill and executes the helper in one tool call. Both arms used exactly one observed command call per task.

| Measure | Baseline | Candidate |
| --- | ---: | ---: |
| Exact structured decisions | 20/20 | 20/20 |
| Mean three-field rubric | 1.0000 | 1.0000 |
| Review precision / recall | 100% / 100% | 100% / 100% |
| Negative-control false-positive rate | 0/10 | 0/10 |
| Median whole-CLI latency | 14.736 s | 16.813 s |
| Input tokens | 4,841,796 | 4,908,710 |
| Cached input tokens (subset) | 3,198,976 | 2,580,480 |
| Output tokens | 5,037 | 5,506 |

Median paired latency overhead was **8.79%**, below the **20%** limit. This is the median of individual paired ratios, not the ratio of group medians. All product screening gates passed, including actual helper execution in all 20 candidate tasks, workspace reads, complete execution and no observed critical tripwire errors. No input mutation or prohibited deletion attempt was observed; this is not a general security certification.

Capability verdict: **NO_MEASURABLE_GAIN** (0 wins, 0 losses, 20 ties; mean delta 0; sign-test p=1). Input tokens increased **1.38%**; output tokens increased **9.31%**. Noncached input was 1,642,820 baseline versus 2,328,230 candidate, so caching differences also matter. No cost estimate or efficiency-savings claim is made. The host still loaded 479,812 bytes of global user instructions; these were not modified.

The earlier cohort measured 59.1% paired overhead. It used a different task set and invocation, so comparing that number with 8.79% does not isolate the causal effect of batching. This v2 run supports the bounded overhead screening result on these tasks only. It does not establish better task outcomes, automatic activation, cross-host behavior or production readiness.

## Fixture correction and scope

The first v2 attempt stopped after three candidate runs (CV2-11, CV2-03 and CV2-10) because duplicate condition IDs made two fixtures invalid. The fixture authoring error was corrected by assigning unique IDs. An automated comparison verified that predicates, observations and reviewed labels were unchanged. No runtime or skill tuning followed those outputs. A new manifest was frozen and the full 40-run corrected cohort was collected from scratch. The incomplete attempt is archived and excluded from the reported metrics, not pooled or treated as success.

Added preflight validation now rejects malformed applicability metadata before host invocation. A separate execution guard requires human label approval before a nonpilot cohort can launch. Both guards have RED/GREEN regression evidence. The labels remain named provisional and retain their original author metadata; human-review.json is the authoritative user approval record.

The separate development pilot ran one pair: baseline 16.634 s and candidate 14.593 s, with one actual command each. That pilot and the incomplete attempt add 5 solver executions beyond the 40-run main cohort. Their host-reported usage is preserved in the summary. No frontier solver or paid API fallback was used.

## Reproduction and provenance

- [Audited summary and attempt accounting](evidence/context-validity-native-v2-2026-10-24.json)
- [Raw evidence archive](evidence/context-validity-native-v2-2026-10-24.zip)
- [Reviewed cases and runner instructions](../tests/native-evals/context-validity-v2/README.md)

Archive SHA-256: `07af034c215dfcd7257d4c7cd4be83c48614a0bcadbe9ed74da6814bad941eea`.

The source base is c8ead90. Frozen hashes, exact runner, source diff, suite, runtime files and skill are in the archive; do not attribute this measurement solely to the base commit. All frozen inputs were verified at completion. Replaying raw events with the frozen auditor reproduced the original complete summary. Original logs remain intact alongside audited copies. The original invalid suite is preserved under the excluded attempt.

Local validation: 154 tests run, 1 Windows symlink skip, runtime coverage 85%; Ruff, mypy, structural validation and four package builds passed. No live Linux CI was run. No release, installation or merge was performed.

This suite is consumed. Keep the feature opt-in. A significant capability claim needs harder, representative tasks that distinguish baseline from candidate and a new independently reviewed evaluation. A clean unseen confirmation also remains needed if promotion requires that stricter evidence standard. Further context optimization should be tested on development tasks, without changing global user instructions or using these outcomes to relabel confirmation cases.
