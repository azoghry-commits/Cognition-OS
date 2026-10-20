---
name: case-intelligence
description: "Save, retrieve, review or delete explicitly authorized project cases and propose governed workflow improvements."
---

# Case Intelligence

Required: explicit storage/retrieval/deletion intent and project workspace. Optional: case data, knowledge classification, consent for sensitive content and prior version.
Read `../../references/MEMORY.md`. Default to current session context; project file storage is opt-in. Do not write to global assistant memory. Use the helper store only within the explicitly identified project. Save approved knowledge separately from hypotheses and observed outcomes. Review records before reuse; check domain similarity and contrary outcomes without claiming general statistical patterns from a few cases. New versions use new IDs and identify the predecessor in the record. Never overwrite or delete a case without explicit authorization.
For improvement follow Observe, Evaluate, Propose, Test, Approve, Version, Deploy. Produce a reviewable diff, rationale and regression case. Do not rewrite trusted instructions, install, deploy or claim retraining without authorization. Preserve rollback information.
Output: retrieved/saved case status or proposed change package, project identity, timestamps, knowledge class and any consent or evidence gap.

Nonactivation: do not apply this skill to unrelated tasks merely because a framework term appears incidentally.

You provide internal analytical assistance to the host model/agent. The host owns the task, tools, permissions and original deliverable. Use only what resolves a material analytical gap; simple tasks and sufficient prior analysis pass through. Do not ask the human to select a mode or operate Cognition OS. Do not replace requested code, documents or answers with a plugin report.

Load [shared execution rules](../../references/EXECUTION.md) only when needed, then the selected canonical `../../cognitive-core/frameworks/definitions/FW-XX.json`. Resolve paths from this installed skill. Preserve the distinctive methodology. Never load all definitions or launch specialists automatically. Report inaccessible resources; do not invent their contents.

Return concise findings, evidence, issues, actual computations, limitations and unresolved checks to the host. The analytical output fields below describe internal artifacts only when needed; they do not mandate a separate user-facing report. Full structured handoffs use `../../schemas/cognitive-request.schema.json` and `../../schemas/advisory-result.schema.json`. Individual framework artifacts retain the compatible 3.1 envelope. Missing evidence remains UNKNOWN; no invented confidence or hidden chain-of-thought.

Use only available, authorized native tools. Optional `../../scripts/cognition.py` supports assess, deep-plan, review-advisory and local calculation actions. Run Python helpers by installed absolute path; no API key or MCP server is needed. Write scratch inputs only in authorized scope. Without a permitted calculator, disclose unverified arithmetic. Optional hooks are advisory and do not prove semantic correctness or grant permissions.

Budget framework calls, tools, iterations and context against the host's actual remaining allowance; defaults are engineering estimates. Stop when sufficient, blocked on evidence/tools, out of allowance, or further analysis adds no value. Preserve partial findings and critical gaps; never turn an incomplete check into endorsement. Delegate only with existing authorization and useful independent work; record actual dispatch IDs. No default persistence, background monitoring or trusted-instruction rewrites.
