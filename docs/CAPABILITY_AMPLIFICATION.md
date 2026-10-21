# Capability amplification

Cognition OS improves task execution without changing or retraining model weights. It supplies an adaptive task contract, relevant methods, bounded context packets, dependency-aware execution, deterministic tools, evidence links, adversarial checks, and a governed learning loop. The gain belongs to the combined host-plus-plugin system and must be measured on representative tasks.

## Tier adaptation

`python scripts/cognition.py capability-plan` accepts an observed profile rather than a model brand. `constrained` uses small sequential steps, one method per step, worked patterns, and explicit checklists. `balanced` allows bounded decomposition and parallel evidence/method work when delegation exists. `advanced` uses sparse scaffolding, independent challenge, and parallel analysis only when it adds value. `unknown` starts conservatively and can be promoted only from repeated task evidence.

The profile records context allowance, verified tools, and native parallel capacity. A plan never proves that a model is capable, never dispatches work by itself, and never expands host permissions.

## Significant improvement gate

`python scripts/cognition.py capability-eval` compares baseline and candidate results on exactly matched case IDs. Each case has a normalized score and a critical-error flag. The default verdict is `SIGNIFICANT_IMPROVEMENT` only when all gates pass:

1. at least 20 paired cases;
2. mean score gain of at least 0.10;
3. two-sided paired sign-test p-value no greater than 0.05;
4. no new critical error.

These defaults are experiment settings, not universal scientific constants. The case set must represent the target workload, scoring must be blinded or independently reviewable, and latency, token use, cost, tool failures, and judge reliability must be reported separately. A small positive sample is `IMPROVED_NOT_SIGNIFICANT`; a new critical error is `REGRESSION` even when the average score rises.

## Improvement lifecycle

A successful capability evaluation can become evidence for the governed improvement ledger. The workflow remains Observe, Propose, Evaluate, Approve, Version, Deploy. Deployment requires explicit approval and rollback information. The plugin does not silently rewrite its trusted instructions, alter host settings, fine-tune a model, or promote a capability tier from branding.

## Offline strategy selection (Unreleased)

`python scripts/cognition.py scaffolding-select --input <comparison.json>` accepts `baseline`, `candidate`, `strategy` (`bounded` or `sparse`) and `evidence_id`. Both lists contain exactly matched `case_id`, normalized `score`, and mandatory boolean `critical_error`. Baseline means conservative scaffolding. Missing critical results are rejected. Any candidate critical error retains conservative scaffolding even when it also occurred in baseline. The helper does not invoke providers, verify provenance, or change host configuration.

Use development cases to select one challenger, then freeze it before held-out confirmation. Do not repeatedly compare candidates on the same held-out set. See [analysis and remaining gates](MEASURED_SCAFFOLDING_ANALYSIS.md).
