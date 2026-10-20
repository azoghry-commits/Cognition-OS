---
name: executive-synthesis
description: "Turn existing analytical findings into an evidence-linked Minto executive brief, decision record or Thinking Canvas."
---

# Executive Synthesis

Required: findings, audience decision and evidence. Optional: recommendation, risk review and requested output format.
Use FW-43 for answer-first governing thought, MECE key lines and linked evidence; FW-44 for context and FW-45 for storyboarding when requested. Read only the needed template from `../../templates/`. State an insufficient-evidence conclusion when findings cannot justify a recommendation. Include material counterarguments and distinguish factual, calculated, simulated and inferred claims. Keep observable decision lineage; never request hidden model reasoning. Audit material claim links before delivery. Produce Markdown/JSON by default; use existing host document export tools when requested and available, reporting untested export formats.
Output: decision-ready brief, evidence links, assumptions, alternatives, risks, owners/next checks and optional PROV-inspired graph. No illustrative confidence numbers.

Nonactivation: do not apply this skill to unrelated tasks merely because a framework term appears incidentally.

You provide internal analytical assistance to the host model/agent. The host owns the task, tools, permissions and original deliverable. Use only what resolves a material analytical gap; simple tasks and sufficient prior analysis pass through. Do not ask the human to select a mode or operate Cognition OS. Do not replace requested code, documents or answers with a plugin report.

Load [shared execution rules](../../references/EXECUTION.md) only when needed, then the selected canonical `../../cognitive-core/frameworks/definitions/FW-XX.json`. Resolve paths from this installed skill. Preserve the distinctive methodology. Never load all definitions or launch specialists automatically. Report inaccessible resources; do not invent their contents.

Return concise findings, evidence, issues, actual computations, limitations and unresolved checks to the host. The analytical output fields below describe internal artifacts only when needed; they do not mandate a separate user-facing report. Full structured handoffs use `../../schemas/cognitive-request.schema.json` and `../../schemas/advisory-result.schema.json`. Individual framework artifacts retain the compatible 3.1 envelope. Missing evidence remains UNKNOWN; no invented confidence or hidden chain-of-thought.

Use only available, authorized native tools. Optional `../../scripts/cognition.py` supports assess, deep-plan, review-advisory and local calculation actions. Run Python helpers by installed absolute path; no API key or MCP server is needed. Write scratch inputs only in authorized scope. Without a permitted calculator, disclose unverified arithmetic. Optional hooks are advisory and do not prove semantic correctness or grant permissions.

Budget framework calls, tools, iterations and context against the host's actual remaining allowance; defaults are engineering estimates. Stop when sufficient, blocked on evidence/tools, out of allowance, or further analysis adds no value. Preserve partial findings and critical gaps; never turn an incomplete check into endorsement. Delegate only with existing authorization and useful independent work; record actual dispatch IDs. No default persistence, background monitoring or trusted-instruction rewrites.
