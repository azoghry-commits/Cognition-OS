# V4.1 rebuild architecture

The plugin's direct consumers are Claude and Codex models/agents. The host selects capabilities, receives advisory findings, and completes the original deliverable. Package candidate 0.2.0 implements V4.1 contracts; framework artifacts using the 3.1 format remain readable through a compatibility path. The package version is separate from the specification version.

## Three paths and the governor

`cognition/augmentation.py:assess` accepts host-normalized task context: objective, task type, risk, complexity, evidence, artifact, capabilities, prior analysis, and remaining budget. `cognitive-core/augmentation/policy.json` stores seven reviewable policies and routing rules. This is rule-based advice, not a trained classifier or runtime interceptor. The helper performs no model reasoning, native dispatch, or file mutation.

Path A uses model-selected skills with lazy-loaded references. Path B applies deterministic scripts to relevant PostToolUse events. Path C provides bounded deep planning with logical advocate/challenger/jury roles. Native delegation defaults to zero; the host may delegate when authorized and actually supported. Answer length does not trigger deep advisory. Simple tasks and tasks with sufficient prior analysis use `PASS_THROUGH`. An unavailable required check produces `BLOCKED`, rather than being hidden by advisory degradation.

The budget covers framework invocations, subagent calls, debates, tools, compute time, and context. Default numbers are initial engineering allowances, adjustable by host context and not yet calibrated through benchmarks. The helper does not measure host tokens. Exhausting the budget produces a gap or incomplete outcome; it does not imply safety, correctness, or completion.

## Contracts and core

The request contract is `schemas/cognitive-request.schema.json`; the result contract is `schemas/advisory-result.schema.json`; task context is `schemas/task-context.schema.json`. `review-advisory` checks structure, identity, evidence scope, links, and calculation records; the host remains responsible for meaning and truth. There is no fabricated confidence score. `INFERENCE` claims need support; explicit `HYPOTHESIS`, `ASSUMPTION`, and `UNKNOWN` claims may lack evidence.

`normalize-legacy` creates a new object from a 3.1 envelope, preserving its origin classification, AG ID, and trace ID. It does not rewrite user cases or invent missing evidence. `CALCULATED_RESULT` and `SIMULATED_RESULT` are not automatically validated merely because JSON output exists.

All 50 definitions in `cognitive-core/frameworks/definitions` include preconditions, input schema, output schema path, triggers, methods, evidence requirements, limitations, relationships, validation criteria, and source references. One AG-01..52 registry points to the same core. An empty framework relationship list means no pairing has been explicitly recommended; it does not forbid compatibility.

## Deterministic hook

The separate configurations are `hooks/codex/hooks.json` and `hooks/claude/hooks.json`. Both use PostToolUse with a Write/Edit/apply_patch matcher, a three-second timeout, and the `scripts/check_artifact.py` entrypoint. Host configuration uses the plugin-root variable documented for that host. Python must be available in the execution environment. Installation alone does not grant trust or execution permission.

The validator reads only paths named by the edit tool under `cwd/.cognition/artifacts` with a `.json` extension. It rejects links/junctions, traversal, out-of-scope paths, invalid JSON, and oversized artifacts. Limits are eight paths and one MiB per file; failed or bounded output is advisory. It does not execute commands from payloads, call a model or network, or write artifacts. File contents and paths are not promoted into host instructions.

A content hash deduplicates identical results within one event; this candidate has no cross-process disk cache. The check remains idempotent and bounded. Cross-event overhead reduction still requires native measurement before introducing persistent caching. The hook cannot block or reverse an edit that has already happened. Required security enforcement belongs to a verified host mechanism separate from this advisory hook.

## Support and limits

The baseline works without MCP, a database server, Docker, model credentials, or a standalone application. When hooks or scripts are unavailable, use supported skills and disclose material limitations. Do not invent results when evidence or a calculator is missing. Local cases and the Human Mastery Track remain opt-in; they do not automatically train the model.

Local structural and CLI checks are separate from model skill selection and native event delivery. Rebuild status and evidence are recorded in [REBUILD_STATUS_V4_1.md](REBUILD_STATUS_V4_1.md). Generator sources are aligned in this order: build_catalog → build_plugin (including build_hybrid) → build_docs. For 0.2.x, build_docs updates hybrid assets without overwriting historical 3.1 audits and status records.
