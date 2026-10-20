# V4.1 source audit and transformation

Audit on 2026-10-20: the complete Markdown source (1,362 lines / eight sections) was read and all 15 PDF pages inspected from a fresh 1,400 px rendering. Both source hashes match the original source manifest. Model-level locators, source inputs/outputs, and classifications are in the [evidence JSON](evidence/v4-1-source-audit.json).

New requirements come from the [V4.1 prompt](evidence/master-implementation-prompt-v4.1.txt). Model names, categories, AG-01..52, and source scope are retained. Implementation procedures, FW numbering, schemas, the governor, and hooks are engineering adaptations rather than quotes from a validated production specification. This audit does not establish improved host quality.

## Source-to-agent transformation matrix

| Source capability | Locator | V4.1 transformation | Form |
|---|---|---|---|
| Command Center / telemetry | A 3.1; B 1,3 | Host task context and observed status; illustrative health/density values are excluded | advisory resource |
| Problem Ingestion | A 3.2 phase 1; B 4 | Observable task-context envelope; ask only blocking questions | skill + schema |
| Framework Stack Builder / presets | A 3.2 phase 2; B 5 | Small complementary selection with explicit semantic handoffs | routing + skill |
| Thinking Canvas / drill-down / 5 Whys | A 3.2 phase 3; B 6 | Optional inspectable Markdown/Mermaid/JSON artifacts within host work | artifact resource |
| Adversarial Debate / rebuttals / jury | A 3.2 phase 4; B 7 | Conditional bounded advocate/challenger/jury analysis; no forced consensus | deep advisory |
| Scenario Simulator / sliders / distributions | A 3.2 phase 5; B 8 | Supplied numerical parameters, local calculation, explicit distributions and seed | deterministic tool |
| MECE / edge cases / contradiction review | A 3.3.1,5.1,5.2; B 9 | Exact finite-universe sets when possible, otherwise qualified semantic review | validation + advisory |
| Cognitive Bias Detector | A 3.3.1,4.1 AG-50; B 9 | Evidence-span review without fabricated probability | advisory |
| Executive Synthesis / Minto / storyboard | A 3.3.2,4.1 AG-43..45; B 13 | Optional synthesis appropriate to original requested format | skill |
| Export PDF/PPTX | A 2.2,7.2; B 13 | Use existing authorized host artifact tools only when requested; no export service | optional retained feature |
| Institutional Memory / case assistant | A 3.3.3,6.1; B 12 | Explicitly authorized project cases, provenance and review before reuse | optional local knowledge |
| Human Mastery Track / badges | A 3.3.4; B 14 | Separate opt-in human learning; no assumed progress or model training | optional skill |
| Agent orchestration / 52 roles | A 4.1,4.2,7.1; B 10,15 | 52 logical roles; host owns execution, no mandatory parallel processes | logical registry |
| Inter-agent envelope | A 4.3 | Versioned V4.1 request/result with explicit conversion from preserved 3.1 artifacts | schema |
| EV and Monte Carlo | A 5.1,5.2; B 8,13 | Retain formula; require input/model assumptions; no automatic PROCEED | calculation |
| Bayesian updates / log odds | A 5.1,5.2 | Use conditional likelihoods and justified independence; reject impossible evidence | calculation |
| MECE score formula | A 5.1,5.2 | Similarity cannot prove exclusivity/completeness; no invented integrity constants | qualified adaptation |
| SQL users/problems/canvas/debates/simulations/alerts/cases | A 6.1 | Host context, typed artifacts and opt-in local cases; no server database | schema + optional local files |
| Reasoning Knowledge Graph / decision lineage | A 6.2; B 11 | Observable artifact/evidence DAG; no hidden reasoning access | provenance validation |
| LangGraph fan-out/fan-in / hardcoded sample | A 7.1 | Host-native logical workflow; sample outputs are illustrative, never findings | skill + bounded plan |
| REST routes / SSE / agent_thought / WebSocket | A 7.2 | Native supported boundaries only; no mandatory server or reasoning interception | excluded infrastructure, retained capabilities |
| React Flow / real-time UI | A 7.3 | Host-owned output and optional diagrams; no standalone application | artifact resource |
| Monorepo / Docker / deployment defaults | A 8.1,8.2 | Single native plugin repository; no copied example passwords or infrastructure | native packaging |
| Roadmap / KPIs / acceptance | A 1.3,8.3; B 1,3,15 | V4.1 phase gates, actual host outcomes and A/B/C/D comparison | evaluation protocol |

## All 50 models

| Framework / logical role | Source name | Locator | Target role |
|---|---|---|---|
| FW-01 / AG-01 | Eisenhower Matrix | A line 276 | Canonical skill resource + logical specialization |
| FW-02 / AG-02 | RICE Scoring | A line 277 | Canonical skill resource + logical specialization |
| FW-03 / AG-03 | MoSCoW Method | A line 278 | Canonical skill resource + logical specialization |
| FW-04 / AG-04 | Expected Value (EV) Calculus | A line 279 | Canonical skill resource + logical specialization |
| FW-05 / AG-05 | Bayesian Updating | A line 280 | Canonical skill resource + logical specialization |
| FW-06 / AG-06 | Pareto Principle (80/20) | A line 281 | Canonical skill resource + logical specialization |
| FW-07 / AG-07 | Cost-Benefit & Marginal Utility | A line 282 | Canonical skill resource + logical specialization |
| FW-08 / AG-08 | Regret Minimization Framework | A line 283 | Canonical skill resource + logical specialization |
| FW-09 / AG-09 | MECE Issue Tree | A line 289 | Canonical skill resource + logical specialization |
| FW-10 / AG-10 | 5 Whys Analysis | A line 290 | Canonical skill resource + logical specialization |
| FW-11 / AG-11 | Kepner-Tregoe (KT) Matrix | A line 291 | Canonical skill resource + logical specialization |
| FW-12 / AG-12 | Fishbone (Ishikawa) Diagram | A line 292 | Canonical skill resource + logical specialization |
| FW-13 / AG-13 | First Principles Thinking | A line 293 | Canonical skill resource + logical specialization |
| FW-14 / AG-14 | Hypothesis-Driven Problem Solving | A line 294 | Canonical skill resource + logical specialization |
| FW-15 / AG-15 | Cynefin Framework | A line 295 | Canonical skill resource + logical specialization |
| FW-16 / AG-16 | Inversion Thinking | A line 296 | Canonical skill resource + logical specialization |
| FW-17 / AG-17 | Theory of Constraints (TOC) | A line 302 | Canonical skill resource + logical specialization |
| FW-18 / AG-18 | Causal Loop Diagrams (CLD) | A line 303 | Canonical skill resource + logical specialization |
| FW-19 / AG-19 | Meadows' 12 Leverage Points | A line 304 | Canonical skill resource + logical specialization |
| FW-20 / AG-20 | Second-Order Thinking | A line 305 | Canonical skill resource + logical specialization |
| FW-21 / AG-21 | Stock and Flow Modeling | A line 306 | Canonical skill resource + logical specialization |
| FW-22 / AG-22 | System Archetypes | A line 307 | Canonical skill resource + logical specialization |
| FW-23 / AG-23 | Network Effects & Feedback | A line 308 | Canonical skill resource + logical specialization |
| FW-24 / AG-24 | Blue Ocean Strategy (ERRC) | A line 314 | Canonical skill resource + logical specialization |
| FW-25 / AG-25 | Wardley Mapping | A line 315 | Canonical skill resource + logical specialization |
| FW-26 / AG-26 | OODA Loop | A line 316 | Canonical skill resource + logical specialization |
| FW-27 / AG-27 | Porter's Five Forces | A line 317 | Canonical skill resource + logical specialization |
| FW-28 / AG-28 | VRIO Framework | A line 318 | Canonical skill resource + logical specialization |
| FW-29 / AG-29 | Ansoff Matrix | A line 319 | Canonical skill resource + logical specialization |
| FW-30 / AG-30 | Game Theory (Nash Equilibrium) | A line 320 | Canonical skill resource + logical specialization |
| FW-31 / AG-31 | Business Model Canvas (BMC) | A line 321 | Canonical skill resource + logical specialization |
| FW-32 / AG-32 | Jobs-to-be-Done (JTBD) | A line 327 | Canonical skill resource + logical specialization |
| FW-33 / AG-33 | Design Thinking | A line 328 | Canonical skill resource + logical specialization |
| FW-34 / AG-34 | Value Proposition Canvas (VPC) | A line 329 | Canonical skill resource + logical specialization |
| FW-35 / AG-35 | Kano Model | A line 330 | Canonical skill resource + logical specialization |
| FW-36 / AG-36 | SCAMPER | A line 331 | Canonical skill resource + logical specialization |
| FW-37 / AG-37 | TRIZ (Inventive Problem Solving) | A line 332 | Canonical skill resource + logical specialization |
| FW-38 / AG-38 | RACI Governance Matrix | A line 338 | Canonical skill resource + logical specialization |
| FW-39 / AG-39 | OKRs (Objectives & Key Results) | A line 339 | Canonical skill resource + logical specialization |
| FW-40 / AG-40 | PDCA (Plan-Do-Check-Act) | A line 340 | Canonical skill resource + logical specialization |
| FW-41 / AG-41 | Getting Things Done (GTD) | A line 341 | Canonical skill resource + logical specialization |
| FW-42 / AG-42 | Critical Path Method (CPM) | A line 342 | Canonical skill resource + logical specialization |
| FW-43 / AG-43 | Minto Pyramid Principle | A line 348 | Canonical skill resource + logical specialization |
| FW-44 / AG-44 | SCQA Framework | A line 349 | Canonical skill resource + logical specialization |
| FW-45 / AG-45 | Storyboarding & Narrative | A line 350 | Canonical skill resource + logical specialization |
| FW-46 / AG-46 | Stakeholder Grid | A line 351 | Canonical skill resource + logical specialization |
| FW-47 / AG-47 | Radical Candor Feedback | A line 352 | Canonical skill resource + logical specialization |
| FW-48 / AG-48 | Toulmin Argumentation Model | A line 353 | Canonical skill resource + logical specialization |
| FW-49 / AG-49 | Pre-Mortem & Red Teaming | A line 359 | Canonical skill resource + logical specialization |
| FW-50 / AG-50 | Cognitive Bias Deconstruction | A line 360 | Canonical skill resource + logical specialization |

AG-51 coordinates selected analysis while the host retains task ownership. AG-52 examines support for recommendations and may reject them or mark evidence insufficient. AG-51/52 inputs, outputs, and responsibilities come from source A 4.2; they do not require two model processes.

## Visual inspection of the entire PDF

| Page in B | Finding / action |
|---|---|
| 1 | Radial core illustration; optimal/risk/density labels are illustrative. |
| 2 | Human/model/agent tripartite concept; absolute diagnosis/bias elimination lacks evidence. |
| 3 | Four modules and 50/52/100% telemetry; transform to host-native capabilities. |
| 4 | Four-stage intake and western stores -25%; do not force human wizard. |
| 5 | SCQA→MECE→KT→RICE; handoff compatibility and missing inputs need explicit mapping. |
| 6 | Revenue/cost tree, 340% stockout and 94% certainty are worked examples. |
| 7 | Optimist, jury, challenger; conditional review, no mandatory consensus or real parallelism claim. |
| 8 | 65%, 2.4M, 0.3M, 0.8M gives exact net 0.655M; positive EV is not execution authority. |
| 9 | 99.2/78/92.5 metrics uncalibrated; example Asia/Europe text mismatches western-store explanation. |
| 10 | 52 trained-agent claim unsupported; MoSCoW quadrant conflicts with precise A catalog category. |
| 11 | Lineage labels 5 Whys linked to KT Agent; preserve AG-10 versus AG-11 distinction. |
| 12 | Netflix/Toyota/SpaceX cases and success-pattern assertion require external evidence before reuse. |
| 13 | +1.2M EV and 94% unsupported under supplied inputs; export only when requested. |
| 14 | Three mastery phases and progress badges; progress is illustrative and learning is optional. |
| 15 | 50×52 count is conceptual; unlimited decision quality is not a measured outcome. |

## Gaps, conflicts, and security

The C01–C14 register in the [baseline audit](SOURCE_ANALYSIS.md) still applies. Additional C15: PDF B page 11 links a framework labeled 5 Whys to the KT Agent; source A distinguishes AG-10 and AG-11. Reconstructed lineage must use the correct role ID. Source A 4.3 provides two detailed prompt examples while its 50 table entries remain brief; complete methods/schemas are adaptations that need behavioral evaluation.

EV, Bayes/log-odds, RICE, Monte Carlo, and MECE heuristics in A 3.2/5 were audited against helpers and the correction register. Example EV is gross 1.455M and net 0.655M. The triangular cost range 1.20/1.25C, Beta clamping, uncalibrated confidence, VaR sign, and MECE similarity are not promoted to proof of correctness. Numeric helpers are tested separately.

The SCQA→MECE→KT/5 Whys→RICE dependency chain is a source example, not a universal pipeline. SaaS architecture, SQL, Cypher, REST/SSE endpoints, UI, and Docker are not mandatory infrastructure; their capabilities are mapped above. No intellectual feature is removed without disposition. Source passwords, example verdicts, and confidence labels are not copied into runtime configuration. Source and case content remain untrusted data; permissions and side effects follow the host.
