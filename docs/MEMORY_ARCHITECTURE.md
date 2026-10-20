# Memory and state

Use current session context first, then authorized existing host project resources, then optional project JSON. SQLite and external stores are deferred because there is no demonstrated scale need. Default runtime never writes memory. See references/MEMORY.md for the concrete consent and review/delete interface.

Case files contain schema version, version, project fingerprint, UTC timestamp, sensitivity flag and classified record. Existing IDs cannot be overwritten. New versions receive new IDs with predecessor in record. Project fingerprint prevents accidental copied-case reuse across project roots. It does not anonymize content or provide access control against another local process.

Current cases, decisions, preferences, hypotheses, outcomes and lessons can be recorded explicitly. Store no credentials. User must identify sensitive content and approve its persistence; detection is a host responsibility. Cases are plain JSON, bounded to 1 MB each. Deletion requires explicit intent. Installation/removal never silently erases user records. No cross-session or host-cloud memory is assumed beyond the verified file mechanism.

Improvement remains a proposal until tested and approved. No model retraining or self-modification occurs. Moving a workspace changes its identity; export and review migration rather than silently bypassing identity checks.

