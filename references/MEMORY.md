# Optional case memory

No storage occurs during ordinary analysis. Prefer existing authorized host project context; do not assume cross-session persistence. When explicitly requested, the helper stores project files under <workspace>/.cognition/cases/<id>.json. Only the identified workspace is used; IDs contain lowercase letters, digits and hyphens. Links/junctions and path escape are rejected. Store is local plain JSON, not encrypted or a secure secrets vault. Never store credentials.

Save input: {"workspace":"absolute project folder","operation":"save","args":{"case_id":"case-name","record":{"title":"...","classification":"approved_knowledge","summary":"..."},"authorized":true}}. The host sets authorized=true only from explicit user intent. For sensitive content, set sensitive=true and require separately explicit sensitive_authorized=true. Supported classes: approved_knowledge, hypothesis, observed_outcome, user_preference. Classification is a user/host assertion, not proof of correctness.

Read via operation get with case_id; retrieve a title list via list with optional query. The project fingerprint must match. A save uses exclusive creation; new versions use new IDs and retain a predecessor reference in the record. Review and prune with the user; one case is limited to 1 MB. Delete uses operation delete and an explicit authorized=true from deletion intent. Uninstall preserves cases. Back up/export authorized case JSON before moving the project; project relocation changes the fingerprint and requires a reviewed migration.

No self-rewriting. Improvement proposals need an observed failure, before/after change, regression evidence, approval, version and rollback. A proposal can be saved as a case only when requested. Neither a stored case nor a generated lesson retrains the underlying model.

Security boundary: validation prevents accidental path escape but is not an OS sandbox. A malicious local process able to race filesystem links remains outside this threat model; use host sandbox controls. Concurrent overwrite is rejected, and writes are not a transactional multi-process database.
