# Governed self-improvement

Cognition OS can improve its project behavior through an inspectable engineering loop. It does not retrain a model or silently rewrite trusted instructions.

1. **Observe** a recurring failure or missed activation with evidence and scope.
2. **Propose** a bounded change with rationale, regression cases, and rollback plan.
3. **Evaluate** baseline and candidate behavior using the same cases and record the evidence.
4. **Approve** only a proposal whose evaluation outcome is `PASSED`; approval identifies the approver and reason.
5. **Version and deploy** the approved artifact, record verification, and retain a rollback reference.

The `improvement` helper stores this lifecycle under the authorized workspace at `.cognition/improvements/`. Every mutation requires explicit persistence authorization. State transitions are append-recorded, project-bound, size-limited, and reject linked storage paths. The ledger does not edit source, install a plugin, deploy a release, or grant permissions. The host performs those actions only within the user's existing authorization.

This supports evidence-based self-improvement across clients because the state contract is host-independent. Hosts without local file or Python access can still produce a reviewable proposal, but they cannot claim the persistent lifecycle completed.

Claims that a change significantly improves model or agent capability should attach the result of `capability-eval`. Its paired sample, effect-size, statistical, and critical-regression gates prevent approval from relying on a few favorable examples. See `CAPABILITY_AMPLIFICATION.md`.
