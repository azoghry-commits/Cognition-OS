---
name: quantitative-decision
description: "Calculate or simulate Cognition OS decision scenarios, Bayesian updates, RICE, sensitivity and weighted alternatives from explicit inputs."
---

# Quantitative Decision

Required: calculation operation and its numerical inputs, units and assumptions. Optional: distributions, seed, horizon and risk policy.
Read `../../references/CALCULATIONS.md` for operation contracts and examples. Prefer a verified native calculator; otherwise run the helper. Never guess probabilities, discount rates, scores, costs, units or distribution widths. Validate all inputs and reject invalid values. Use explicit distributions for simulations; fixed distributions are valid when uncertainty parameters are absent. State independence and label simulated results distinctly from observed data. Describe Monte Carlo standard error as numerical simulation uncertainty only. Report gross and net EV together. A positive EV cannot override loss tolerance, feasibility or user approval.
Output: supplied inputs and units, formula/method, actual tool result, reproducibility details, sensitivity, limitations and decision conditions. If no permitted calculator is available return BLOCKED for arithmetic verification.

Nonactivation: do not apply this skill to unrelated tasks merely because a framework term appears incidentally.

You provide internal analytical assistance to the host model/agent. The host owns the task, tools, permissions and original deliverable. Use only what resolves a material analytical gap; simple tasks and sufficient prior analysis pass through. Do not ask the human to select a mode or operate Cognition OS. Do not replace requested code, documents or answers with a plugin report.

Load [shared execution rules](../../references/EXECUTION.md) only when needed, then the selected canonical `../../cognitive-core/frameworks/definitions/FW-XX.json`. Resolve paths from this installed skill. Preserve the distinctive methodology. Never load all definitions or launch specialists automatically. Report inaccessible resources; do not invent their contents.

Return concise findings, evidence, issues, actual computations, limitations and unresolved checks to the host. The analytical output fields below describe internal artifacts only when needed; they do not mandate a separate user-facing report. Full structured handoffs use `../../schemas/cognitive-request.schema.json` and `../../schemas/advisory-result.schema.json`. Individual framework artifacts retain the compatible 3.1 envelope. Missing evidence remains UNKNOWN; no invented confidence or hidden chain-of-thought.

Use only available, authorized native tools. Optional `../../scripts/cognition.py` supports assess, deep-plan, review-advisory and local calculation actions. Run Python helpers by installed absolute path; no API key or MCP server is needed. Write scratch inputs only in authorized scope. Without a permitted calculator, disclose unverified arithmetic. Optional hooks are advisory and do not prove semantic correctness or grant permissions.

Budget framework calls, tools, iterations and context against the host's actual remaining allowance; defaults are engineering estimates. Use `token-plan` when context cost is material: load discovery metadata first, then one matching skill, then only selected framework definitions and evidence. Never force a profile below its quality floor. Escalate on evidence conflict, a missing decision-critical input, failed validation, a critical objection, or an unsupported deliverable. Stop when sufficient, blocked on evidence/tools, out of allowance, or further analysis adds no value. Preserve partial findings and critical gaps; never turn an incomplete check into endorsement. Delegate only with existing authorization and useful independent work; record actual dispatch IDs. No default persistence, background monitoring or trusted-instruction rewrites.
