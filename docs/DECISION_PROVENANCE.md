# Observable decision lineage

Source: blueprint 6.2 and PDF 11. Nodes: Entity (source, assumption, finding, recommendation), Activity (framework or tool operation), Agent (logical specialist or actual host actor). Relationships: used(Activity,Entity), wasGeneratedBy(Entity,Activity), wasDerivedFrom(Entity,Entity), wasAssociatedWith(Activity,Agent), wasAttributedTo(Entity,Agent).

The validator enforces unique IDs, valid endpoints/kinds and acyclic data derivation. It is PROV-inspired JSON; no RDF/OWL equivalence or W3C conformance certification is claimed. Keep concise rationale, actual calculation records and evidence links. Never request hidden chain-of-thought or store private internal reasoning.

Traceability coverage = material externally reported claims with existing usable evidence/calculation links / all material externally reported claims. Empty denominator -> null. audit_evidence reports dangling links, missing method/inputs/results and unrecorded verification. Link completeness is not truth or calibrated confidence. Verify that a citation actually entails its claim and preserve contradictory evidence; the script cannot perform that semantic check.

Human decision remains PENDING, APPROVED, REJECTED or NOT_REQUESTED. A plugin verdict never silently supplies human approval. Persist/export a lineage only in authorized scope.

