---
name: adversarial-review
description: "Challenge an existing recommendation with optimistic and critical cases, logic guardrails, evidence audit and an independent jury verdict."
---

# Adversarial Review

Required: proposal, supporting artifacts and evidence. Optional: risk limits, counterarguments and desired depth.
Read `../../references/REVIEW.md`. Use FW-24 for an ERRC-based optimistic value case when strategically relevant, FW-49 for failure scenarios and FW-50/FW-48 for bias and argument checks. Otherwise use clearly labeled optimistic and critical perspectives without misrepresenting them as completed ERRC analysis. AG-52 evaluates both sides and may ACCEPT, CONDITIONAL, REJECT or INSUFFICIENT_EVIDENCE. Agreement is not mandatory. Bound rebuttals using the mode policy; never repeat debate without new decision value.
Inspect contradictory evidence, invalid calculations, circular warrants, missing critical facts, MECE overlap and all nine requested bias families. Quote the observable spans and offer alternative interpretations. Use `audit`, `mece`, `provenance` and `jury` helpers where useful; their structural verdicts do not replace analytical judgment. Preserve unresolved objections in the final recommendation.
Output: optimistic case, critical case, rebuttal evidence, gap list, jury verdict, conditions and next checks.

Nonactivation: do not apply this skill to unrelated tasks merely because a framework term appears incidentally.

You provide internal analytical assistance to the host model/agent. The host owns the task, tools, permissions and original deliverable. Use only what resolves a material analytical gap; simple tasks and sufficient prior analysis pass through. Do not ask the human to select a mode or operate Cognition OS. Do not replace requested code, documents or answers with a plugin report.

Load [shared execution rules](../../references/EXECUTION.md) only when needed, then the selected canonical `../../cognitive-core/frameworks/definitions/FW-XX.json`. Resolve paths from this installed skill. Preserve the distinctive methodology. Never load all definitions or launch specialists automatically. Report inaccessible resources; do not invent their contents.

Return concise findings, evidence, issues, actual computations, limitations and unresolved checks to the host. The analytical output fields below describe internal artifacts only when needed; they do not mandate a separate user-facing report. Full structured handoffs use `../../schemas/cognitive-request.schema.json` and `../../schemas/advisory-result.schema.json`. Individual framework artifacts retain the compatible 3.1 envelope. Missing evidence remains UNKNOWN; no invented confidence or hidden chain-of-thought.

Use only available, authorized native tools. Optional `../../scripts/cognition.py` supports assess, deep-plan, review-advisory and local calculation actions. Run Python helpers by installed absolute path; no API key or MCP server is needed. Write scratch inputs only in authorized scope. Without a permitted calculator, disclose unverified arithmetic. Optional hooks are advisory and do not prove semantic correctness or grant permissions.

Budget framework calls, tools, iterations and context against the host's actual remaining allowance; defaults are engineering estimates. Use `token-plan` when context cost is material: load discovery metadata first, then one matching skill, then only selected framework definitions and evidence. Never force a profile below its quality floor. Escalate on evidence conflict, a missing decision-critical input, failed validation, a critical objection, or an unsupported deliverable. Stop when sufficient, blocked on evidence/tools, out of allowance, or further analysis adds no value. Preserve partial findings and critical gaps; never turn an incomplete check into endorsement. Delegate only with existing authorization and useful independent work; record actual dispatch IDs. No default persistence, background monitoring or trusted-instruction rewrites.
