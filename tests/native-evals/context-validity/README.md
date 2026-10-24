# Context validity native host evaluation

This set contains 20 synthetic held-out tasks, including 10 negative controls. The user approved the provisional labels before any held-out candidate execution; human-review.json preserves that approval. These are screening tasks for validity decisions, not production incident outcomes.

Run explicitly (uses authenticated ChatGPT Codex CLI quota):

```powershell
uv run --locked --extra dev python scripts/evaluate_context_host.py --run --pilot --output tmp/native-pilot
uv run --locked --extra dev python scripts/evaluate_context_host.py --run --output tmp/native-heldout
```

Output directories must not already exist. Without --run, only a frozen manifest is prepared. No API key, account reset, credits purchase, frontier fallback or paid API fallback is used. Both arms explicitly use gpt-5.6-luna with low reasoning effort, as requested by the user. --ignore-user-config and temporary feature overrides leave the user configuration intact. apps, plugins, memories and multi_agent are disabled to avoid installed-plugin contamination; candidate gets a project-local copy of the skill and supporting resources. Invocation is explicit, so these runs do not test automatic skill activation or marketplace installation.

Each task runs in its own temporary workspace. The CLI uses its supported --approve-for-me mode; its automatic review and user rules still apply. Prompts authorize only workspace reads and helper execution; injection strings inside input data cannot grant permissions. The runner records actual tool commands, input hash changes and suspicious deletion attempts. These checks are evidence, not a general sandbox proof. Failed approval, model or quota preflights are kept separately; refusal or a plausible answer without actual tool execution is not a native candidate pass.

The runner freezes case/label/protocol/runtime hashes before execution, shuffles 40 individual runs with seed 20261023, executes sequentially, and stops on execution failure or missing helper evidence. Responses contain case_id, status, reuse_allowed, review_required and reason. The first three decision fields receive equal score weight. Reason text remains inspectable but is not semantically graded by the script. Structured review flags produce precision, recall and negative-control false-positive rate. Default runtime capability-eval gates remain unchanged. Whole-CLI paired latency includes startup, review and tool overhead. Token totals use host-reported input/cached-input/output counts; no cost estimate is fabricated.

Any native acceptance result is limited to this host, protocol, task set, skill invocation and source snapshot. It does not establish global activation, cross-host behavior, hooks, or production readiness. A candidate can pass correctness but fail the predeclared latency threshold; report that result without retuning on this held-out set.

## Consumed evaluation set

This set was consumed on 2026-10-24. See [results](../../../docs/NATIVE_CONTEXT_VALIDITY_EVALUATION.md). Re-execution is diagnostic, not fresh held-out confirmation. Use a new independently reviewed set for a revised candidate. Raw original and hardened audited records are preserved in the report archive.
