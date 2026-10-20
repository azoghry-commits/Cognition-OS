# Data contracts

All contracts use JSON Schema 2020-12. schemas/framework.schema.json describes canonical method resources; agent.schema.json describes logical roles; agent-envelope.schema.json version 3.1 records observable inputs, payload, claims, gaps and real execution IDs. Legacy 2.0 sample metrics are intentionally excluded because no calibration exists.

schemas/framework-output/FW-XX.schema.json supplies a distinct required-output contract per model. Kepner-Tregoe additionally requires all four contrast dimensions, distinctions/changes, candidate tests and a nonempty diagnostic-test list. Most qualitative payload contracts admit structured objects/arrays so that host outputs can reflect actual domain context. Structural schemas cannot prove methodological fidelity.

evidence.schema.json separates source/assumption/calculation/simulation/observation, requires identity/locator/content, and permits actual method/inputs/result/verification records. decision.schema.json carries recommendation, verdict, alternatives, risks, conditions and human disposition. provenance.schema.json represents typed entities, activities, agents and permitted PROV-inspired relationships.

The dependency-free runtime validator implements type, required, properties, additionalProperties, enum, const, array bounds/uniqueness, string minimum/pattern and numeric bounds. It deliberately rejects $ref rather than pretend to resolve it. Full JSON Schema verification can use the optional development jsonschema package; it is not a runtime requirement. Runtime functions also enforce cross-field and graph constraints.

No schema grants execution permission or certifies a claim. For structured output: validate envelope, then validate payload against its framework ID, then review methodology/evidence. A missing required input blocks completion even if payload structure passes.

