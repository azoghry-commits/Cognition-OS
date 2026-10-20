---
name: root-cause-analysis
description: "Diagnose recurring incidents or operational deviations with MECE, Kepner-Tregoe and evidence-based causal tests."
---

# Root Cause Analysis

Required: deviation and available incident evidence. Optional: expected versus actual behavior, locations, times, affected scope, changes and constraints.
Use FW-44 for framing, FW-09 for decomposition, FW-11 for IS/IS NOT analysis and FW-10 for causal depth as justified. For Kepner-Tregoe require What, Where, When and Extent with distinctions and changes. Test candidates against both affected and unaffected conditions. An empty IS NOT field is a gap, not evidence that the cause is confirmed. Define diagnostic tests that could disprove each candidate. Use FW-17 for a measured throughput constraint and FW-02 only when prioritization inputs exist.
For service incidents, gather read-only evidence first: timestamps, logs, process identity, resource pressure and change history. Recovery proposals must include backup/rollback checks and authorized scope. Do not run destructive recovery operations from a diagnosis request alone.
Output: observed deviation, contrasted facts, candidate cause matrix, verified versus hypothetical links, safe diagnostic plan, conditional mitigations and rollback criteria.

Nonactivation: do not apply this skill to unrelated tasks merely because a framework term appears incidentally.

You provide internal analytical assistance to the host model/agent. The host owns the task, tools, permissions and original deliverable. Use only what resolves a material analytical gap; simple tasks and sufficient prior analysis pass through. Do not ask the human to select a mode or operate Cognition OS. Do not replace requested code, documents or answers with a plugin report.

Load [shared execution rules](../../references/EXECUTION.md) only when needed, then the selected canonical `../../cognitive-core/frameworks/definitions/FW-XX.json`. Resolve paths from this installed skill. Preserve the distinctive methodology. Never load all definitions or launch specialists automatically. Report inaccessible resources; do not invent their contents.

Return concise findings, evidence, issues, actual computations, limitations and unresolved checks to the host. The analytical output fields below describe internal artifacts only when needed; they do not mandate a separate user-facing report. Full structured handoffs use `../../schemas/cognitive-request.schema.json` and `../../schemas/advisory-result.schema.json`. Individual framework artifacts retain the compatible 3.1 envelope. Missing evidence remains UNKNOWN; no invented confidence or hidden chain-of-thought.

Use only available, authorized native tools. Optional `../../scripts/cognition.py` supports assess, deep-plan, review-advisory and local calculation actions. Run Python helpers by installed absolute path; no API key or MCP server is needed. Write scratch inputs only in authorized scope. Without a permitted calculator, disclose unverified arithmetic. Optional hooks are advisory and do not prove semantic correctness or grant permissions.

Budget framework calls, tools, iterations and context against the host's actual remaining allowance; defaults are engineering estimates. Stop when sufficient, blocked on evidence/tools, out of allowance, or further analysis adds no value. Preserve partial findings and critical gaps; never turn an incomplete check into endorsement. Delegate only with existing authorization and useful independent work; record actual dispatch IDs. No default persistence, background monitoring or trusted-instruction rewrites.
