# Retired source audit

The original blueprint Markdown and strategic PDF were removed from the maintained repository in version 0.5.0 because the canonical 50-framework catalog, schemas, provenance fields, and audit findings are already generated and tested. The build now validates those retained canonical resources and no longer depends on the two source files. Historical references below describe the completed transformation and are retained as provenance, not as a runtime dependency.

**Delta audit completed during rebuild:** the entire Markdown source was read and all 15 PDF pages were freshly rendered and reinspected. See [SOURCE_TRANSFORMATION_V4_1.md](SOURCE_TRANSFORMATION_V4_1.md) and its related JSON evidence. The following note that reinspection had not occurred is historical context from the pre-rebuild concept review.

**V4.1 scope note:** this audit is baseline 3.1 evidence. The new concept prompt is preserved byte-for-byte at [evidence/master-implementation-prompt-v4.1.txt](evidence/master-implementation-prompt-v4.1.txt). The [V4.1 review](CONCEPT_V4_1.md) maps changes and all capability groups; the A/B document delta audit, including reinspection of all 15 PDF pages, was scheduled for Phase 0. The following inspection statements belong to the earlier audit and were not claims of reinspection during that concept review.

Both supplied source files remain byte-identical. See evidence/sources.json for SHA-256 and byte counts. All eight blueprint sections were read. All 15 image-only PDF pages were rendered and visually inspected; text extraction returns no text. See evidence/pdf/page-01.png through page-15.png and contact sheets. Small decorative diagram labels on page 1 are not treated as missing technical specifications.

| Blueprint section | Scope audited | Native transformation |
|---|---|---|
| 1 / PRD | Tripartite human/model/agent design, corrections, KPIs | Native host dialogue, canonical models, logical roles; KPI targets require measurement |
| 2 / architecture | Five layers and full SaaS stack | Intake, orchestration, model resources, validators and synthesis remain logical layers; no servers or UI stack |
| 3 / functional UX | Four modules, five phases, guardrails, memory and mastery | Focused skills, Markdown/Mermaid/JSON artifacts, explicit project storage and teaching |
| 4 / catalog | Every table row AG-01..50, AG-51/52, envelope and two detailed prompt examples | Canonical source extraction plus curated method instructions and versioned schemas |
| 5 / math | EV, Monte Carlo, Bayes, MECE formula and Python | Dependency-free validated helper; explicit distributions and reference tests |
| 6 / schemas | SQL user/problem/canvas/debate/simulation/alerts/cases tables; Cypher entities/activities/agents | Portable envelopes, evidence and provenance JSON, opt-in case files; no database server |
| 7 / execution | LangGraph sample, seven REST routes, SSE events and React component | Native skills/handoffs, deterministic helper and observable artifacts; sample responses are not real inference |
| 8 / deployment | Monorepo, compose with example passwords, roadmap and acceptance targets | Single plugin package, local marketplace catalogs, tests and release gates; no copied credentials |

| PDF page | Visual relationship and additional finding | Disposition |
|---|---|---|
| 1 | Radial graph around cognitive core; illustrative optimal/graph-density labels | Shared core concept; no live telemetry claim |
| 2 | Human intuition/context + model structure + AI computation Venn | Human final judgment and host-native assistance |
| 3 | Command Center, Thinking Canvas, Validation and Synthesis four modules | Conversational intake and artifacts; no replacement dashboard |
| 4 | Four-stage ingestion, western-store -25% sample | Conversational intake; sample not verified business evidence |
| 5 | SCQA -> MECE -> KT -> RICE data feed | Preset source workflow with explicit missing-input handoffs |
| 6 | Revenue/cost then volume/price tree; 340% stockout, 94% diagnosis | Preserve method, reject unsupported causal certainty |
| 7 | Optimistic Blue Ocean, critical Pre-Mortem and central Jury | Bounded evidence-driven debate; jury can reject |
| 8 | Probability/payoff/cost sliders, net EV +0.65M | Explicit conversational parameter changes; exact +0.655M |
| 9 | Overlap highlighting and bias spans; 99.2%, 78%, 92.5% | Observable checks; no copied integrity/bias probabilities; annotation references western-store narrative while example is Asia/Europe |
| 10 | Agent dot grid, four broad quadrants, MoSCoW shown near Strategic | Conceptual, not a complete 52-agent inventory; source A section 4 authoritative category places MoSCoW in Decision |
| 11 | Problem -> framework -> agent -> decision lineage | Observable artifact graph; no hidden thoughts |
| 12 | Netflix/Toyota/SpaceX cases and claimed common success pattern | No pre-seeded historical truth or aggregate success claim without sources/data |
| 13 | Answer-first pyramid, causal 94%, +1.2M EV and risk argument | Minto brief with audited claims and gross/net correction |
| 14 | Three mastery phases, badges, sample completed/50%/locked progress | Optional 90-day curriculum; no assumed learner progress |
| 15 | 50 models x 52 agents marketing equation | Catalog counts preserved; no unlimited-decision claim |

Source gaps: the 50 table rows are concise scopes, not 50 complete production prompts. Only AG-11 and AG-52 include detailed prompt examples. No training data proves specially trained models, no grounded confidence calibration exists, case studies lack citations, benchmarks lack measurement protocol, and native plugin schemas are absent. Curated method steps, FW numbering correspondence, formal contracts, routing heuristics, storage limits and test cases are ENGINEERING_ADAPTATION. They are never presented as verbatim source specifications.

## Mathematical and engineering inconsistency register

| ID | Original assertion / reference | Issue and implication | Recorded correction |
|---|---|---|---|
| C01 | A 1.2, 3.3, 6.2; B 8/13: +0.65M versus +1.2M | Same shown inputs produce gross 1.455 and net 0.655; conservative 1.2 lacks input derivation | Show exact gross/net separately; require adjusted assumptions for 1.2 |
| C02 | A 5.2 `likelihood_ ratios` | Invalid Python identifier prevents compilation | New validated Bayes implementation; reject invalid evidence rather than clamp |
| C03 | A 5.1 triangular upper 1.25C, A 5.2 1.20C; prose lognormal/triangular vs code clipped normal | Different stochastic models and expected costs | Require explicit distributions; no default variance or confidence-derived concentration |
| C04 | A 5.2 Beta parameters clamp to >=1, p=0/1 | Simulated success no longer matches boundary probability | Fixed boundary probabilities remain exact; positive Beta parameters explicit |
| C05 | A 1.2/4.3/5.2/6; B 6/9/13 confidence/integrity/margin | Uncalibrated constants and coverage masquerade as certainty | No default numeric confidence or hardcoded integrity; simulation numerical error labeled narrowly |
| C06 | A 7.1 hardcoded stockout, RICE and consensus | Sample ignores user input; graph appearance is not analysis | Host must execute methods against actual inputs; helpers return plans/checks only |
| C07 | A 5.2 automatic PROCEED and UI net>0 | Positive EV ignores user loss tolerance and constraints | Report metrics; user/host conditional decision required |
| C08 | A 5.2 lower 5% outcome called VaR95 | Signed outcome quantile is not a positive loss metric | Expose both net-outcome q05 and nonnegative loss VaR95 |
| C09 | A 5.1 MECE CE penalty can be negative; embeddings cannot prove completeness | Heuristic may mislead | Exact membership checks only for finite universe, qualitative semantic review otherwise |
| C10 | A 1.2/6.2; B 11 100% traceability | Links do not certify truth; absent evidence cannot be reconstructed | Defined coverage over material reported claims; null for empty denominator |
| C11 | A 1/2/8 performance and 52 parallel; B 10 specialized training | Targets and logical roles lack measured runtime/training proof | Distinguish logical/native/sequential execution; native performance benchmark gate remains unverified |
| C12 | A 8.2 example service passwords | Examples are unsafe production defaults | No servers or credential files in runtime package |
| C13 | A FW-11 example, table provides AG IDs | Complete FW enumeration not explicitly supplied | Stable corresponding FW-01..50 recorded as engineering mapping, original AG IDs retained |
| C14 | B 10 broad quadrant labels vs A 4 precise categories | Presentation is not category registry | Preserve all eight A categories; retain visual discrepancy in audit |

Risk register: native host behavior and cognition quality need independent live evaluations; source ownership/license needs owner decision before distribution; comparative latency/token gains remain unmeasured; local case JSON is not encrypted; project storage protection is not a replacement for the host sandbox.

