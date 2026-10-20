"""Extract source identities and generate derived resources; never edits supplied sources."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.2.0"

def write(path, value):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n" if not isinstance(value, str) else value, encoding="utf-8")

# Curated engineering procedures augment the preserved source table. Semicolons delimit steps.
# id | required inputs | output fields | method
METHODS = '''
01|tasks|quadrants,tradeoffs|Separate deadline urgency from outcome importance;Assign Do First, Schedule, Delegate or Eliminate with reasons;Check delegated authority and revisit changing deadlines
02|initiatives,reach_unit,effort_unit,time_horizon|rankings,assumptions|Require reach, impact, confidence fraction and positive effort for every initiative;Use common reach period and effort units;Calculate RICE with the local helper and expose each factor;Sensitivity-test uncertain factors without interpreting confidence as truth probability
03|items,constraints|must,should,could,wont|Define the release or timebox and budget;Define Must as absence making the outcome unviable and distinguish Should from Could;Place explicitly excluded scope in Won't for this timebox;Check Must set feasibility against capacity
04|scenarios,unit|gross_ev,net_ev,assumptions|Require mutually exclusive outcomes with probabilities summing to one;Calculate probability-weighted signed payoffs and subtract explicitly supplied common costs;Display gross and net EV separately;Compare downside and constraints before any conditional recommendation
05|prior,likelihood_if_true,likelihood_if_false|posterior,bayes_factor,assumptions|Define hypothesis and observed evidence;Require justified prior and conditional likelihoods;Compute Bayes using the helper and reject impossible evidence;For multiple updates justify conditional independence or use conditional likelihoods
06|contributions,unit|ranked_contributions,cumulative_share,vital_few|Validate nonnegative comparable contributions and common period;Sort descending and calculate cumulative shares;Find the smallest group meeting the stated coverage target;Report the observed concentration rather than forcing an 80/20 split
07|costs,benefits,unit,time_period|bcr,npv,break_even,marginal_analysis|Align currencies, price basis, horizon and time periods;Require discount rate for discounted comparisons;Compute BCR and NPV using explicit period cash flows;Compare incremental benefits against incremental costs and state break-even conditions
08|options,horizon,values|regret_matrix,tradeoffs,recommendation|Define future viewpoints and user values;Compare action and inaction regret for each option;Separate reversible experiments from irreversible commitments;Make the recommendation conditional on values and unresolved uncertainty
09|question,scope,branches|issue_tree,exclusivity,coverage,gaps|Define universe, unit of analysis and decomposition rule;Test sibling overlap, duplicates and consistent abstraction levels;Test collective coverage including boundary and exceptional cases;If a finite universe exists use set validation;Treat semantic assessments as qualitative judgments
10|symptom,evidence|causal_chain,alternative_causes,diagnostic_tests|State the observed symptom and evidence;Ask successive why questions with supporting evidence per causal link;Branch when causes diverge and stop at an actionable supported cause or evidence gap;Do not force exactly five answers or confirm causality by repetition
11|deviation,is_is_not|is_vs_is_not_matrix,candidate_causes,diagnostic_tests,conclusion|Specify What, Where, When and Extent with IS, IS NOT, distinction and change;Generate causes from distinctions and relevant changes;Test each candidate against every IS and IS NOT condition;Separate plausible causes from verified causes and identify falsifying checks;Request missing contrasts before a confirmed diagnosis
12|effect,operational_context|fishbone,hypotheses,tests|Define a measurable effect and boundary;Explore Man, Machine, Material, Method, Measurement and Milieu;Attach evidence or hypothesis labels to each subcause;Test interactions and prioritize discriminating checks without declaring the diagram causal proof
13|problem,assumptions|assumption_ledger,fundamentals,reconstructed_options|Separate observations, constraints and conventional assumptions;Challenge each assumption using evidence and underlying physical or economic constraints;Reconstruct candidate solutions from supported fundamentals;Compare feasibility and identify tests for remaining assumptions
14|question,evidence,constraints|hypotheses,test_plan,decision_rules|State falsifiable competing hypotheses including a null when appropriate;Predict observations that distinguish alternatives;Specify metrics, sampling, thresholds and disconfirming evidence before inspecting outcomes;Update or reject hypotheses using actual results
15|context,causal_predictability|domain,response_protocol,reassessment|Assess whether cause and effect are obvious, expert-discoverable, emergent or unstable;Classify Clear, Complicated, Complex, Chaotic or Disorder with reasons;Choose Sense-Categorize-Respond, Sense-Analyze-Respond, Probe-Sense-Respond or Act-Sense-Respond accordingly;Reassess domain as evidence changes
16|goal,constraints|failure_conditions,preventive_actions|Invert the desired outcome into ways to guarantee failure;Identify necessary failure conditions and controllable precursors;Convert them into preventive checks and experiments;Do not assume avoiding failure alone guarantees success
17|process,capacities,demand|constraint,focusing_steps,throughput_tests|Measure end-to-end throughput, queues and effective capacities;Identify the current constraint and test it against demand and dependencies;Exploit the constraint then subordinate other work then elevate when justified;Repeat identification after improvement and guard against inertia
18|variables,relationships|causal_graph,loops,delays|Set system boundary and time horizon;Draw directed influences with positive or negative polarity and supporting mechanism;Mark delays and label reinforcing or balancing loops by sign product;Keep observed associations distinct from causal hypotheses
19|system,interventions|leverage_ranking,rationale,risks|Describe system goals, rules, flows and feedback;Compare interventions at parameters, buffers, structures, delays, balancing loops, reinforcing loops, information, rules, self-organization, goals, paradigms and transcending paradigms;Explain leverage and feasibility for each candidate;Treat ranking as a hypothesis requiring tests
20|action,actors,horizons|consequence_tree,uncertainties,indicators|State the immediate intended effect;Ask And then what for actor responses and feedback across second and third orders;Separate near, medium and long horizons;Identify countervailing effects, leading indicators and reversible probes
21|initial_stock,inflows,outflows,time_step,unit|stock_series,equations,assumptions|Define stock units and flow units per time;Apply stock_next equals stock plus inflows minus outflows times time_step;Represent delays and boundary constraints explicitly;Test conservation, nonnegative limits where applicable and sensitivity to step size
22|symptoms,history,relationships|archetype,loop_map,interventions|Compare evidence with Fixes that Fail, Shifting the Burden and Tragedy of the Commons;Map short-term relief, delays and long-term feedback;Test competing archetypes against history;Target structural loop changes rather than symptom suppression
23|network,interactions,metrics|effect_type,mechanisms,measurement_plan|Distinguish direct, indirect, two-sided and local effects;Define whose utility changes when which participants join;Separate network effects from scale economies and viral acquisition;Estimate elasticity or critical mass only from suitable data and assess congestion or moat decay
24|competitive_factors,noncustomers|errc,value_curve,tests|Identify industry value factors and noncustomer barriers;Build Eliminate, Reduce, Raise and Create choices with cost and buyer-value logic;Compare current and proposed value curves;Test demand, delivery and economic assumptions before asserting a blue ocean
25|user_need,components,dependencies,evolution_evidence|wardley_map,sourcing_options,uncertainties|Anchor the map on user need and visibility;Build dependency value chain;Position each component from Genesis through Custom Built and Product to Commodity using evidence;Use evolution and dependencies to evaluate build, buy or utility choices;Do not substitute a generic maturity quadrant
26|observations,context,options|ooda_cycle,decision,feedback|Observe current signals and uncertainty;Orient through context, assumptions, culture and competing interpretations;Decide a bounded hypothesis or action;Act with feedback and revisit orientation rather than optimizing speed alone
27|industry,market_evidence|forces,margin_implications,options|Define industry boundary and horizon;Assess rivalry, entry threat, substitutes, supplier power and buyer power separately;Ground intensity judgments in evidence and define any numeric rubric;Explain how structural forces affect margins and defensive choices
28|resources,evidence|vrio_matrix,advantage,actions|Assess Value, Rarity, Inimitability and Organization for each resource;Require evidence per dimension;Distinguish disadvantage, parity, temporary advantage, unused advantage and potential sustained advantage;Avoid asserting enduring advantage without evidence of durability
29|products,markets,risk_constraints|ansoff_quadrants,options,risks|Define existing versus new products and markets relative to the organization;Map penetration, market development, product development and diversification;Compare capability gaps and execution risks;Do not invent numerical risk weights
30|players,strategies,payoffs|payoff_matrix,best_responses,equilibria|Specify players, information, timing and utility units;Require complete payoff assumptions;Find best responses and test unilateral deviations before identifying Nash equilibria;Distinguish pure and mixed strategies and disclose when none is computed
31|business,customers,economics|business_model_canvas,coherence,gaps|Populate segments, value propositions, channels, relationships, revenues, resources, activities, partners and costs;Separate validated inputs from hypotheses in every block;Check revenue-cost and delivery-customer coherence;Design tests for the weakest links
32|customer_context,observations,alternatives|job_stories,forces,underserved_needs|Identify progress sought in a specific situation;Separate functional, emotional and social jobs;Write When, I want to, So I can job stories from observations;Analyze push, pull, habit and anxiety without inventing customer interviews
33|observations,user_problem,constraints|hmw,ideas,prototype,test_plan|Empathize using actual user evidence;Define a bounded How Might We question;Ideate multiple approaches and select a testable assumption;Prototype and test against explicit learning criteria;Iterate based on observations
34|customer_profile,value_map|fit_map,gaps,tests|Map customer jobs, pains and gains by importance with evidence;Map products, pain relievers and gain creators;Connect each offer element to an actual prioritized need;Identify unsupported fit claims and test them
35|attributes,survey_responses|kano_categories,uncertainty,priorities|Require paired functional and dysfunctional responses;Classify Must-be, One-dimensional, Attractive, Indifferent, Reverse or Questionable using a declared evaluation table;Report counts and sample limitations;Do not label delighters from intuition alone
36|existing_solution,constraints|scamper_concepts,selection,tests|Generate distinct Substitute, Combine, Adapt, Modify, Put to another use, Eliminate and Reverse or Rearrange variations;Explain the changed mechanism for each;Screen concepts against constraints;Prototype the highest learning-value options
37|improving_parameter,worsening_parameter,constraints|contradiction,principles,solutions,tests|State the technical or physical contradiction;Seek separation in space, time, condition or system level and applicable inventive principles;Distinguish a verified contradiction-matrix lookup from a proposed principle;Do not invent matrix cells or force a compromise disguised as contradiction resolution
38|workstreams,roles|raci_matrix,conflicts,actions|Map Responsible, Accountable, Consulted and Informed for every workstream;Require exactly one Accountable and at least one Responsible per row;Check role authority and capacity;Resolve gaps and conflicting accountability with stakeholders
39|objective,baseline,target,horizon|okrs,indicators,review_plan|Write a qualitative outcome objective;Define measurable key results with baseline, target, owner and deadline;Separate outcomes from activity lists and leading from lagging indicators;Schedule evidence-based reviews without inventing progress
40|problem,baseline,intervention,metrics|pdca_cycle,thresholds,decision|Plan a testable change and success criteria;Do a bounded intervention with observation;Check outcomes against baseline and thresholds;Act by adopting, adjusting or abandoning and start the next cycle
41|commitments,projects,constraints|next_actions,contexts,review|Capture commitments;Clarify actionable items and desired outcomes;Organize concrete next physical actions by context and project;Reflect through a review and engage according to constraints;Avoid treating a vague project title as a next action
42|tasks,durations,predecessors,time_unit|critical_path,schedule,slack|Validate dependency DAG and common duration units;Run a forward pass for earliest start and finish;Run a backward pass for latest start and finish;Compute slack and all critical activities;Disclose that resource constraints and uncertain duration need additional analysis
43|findings,recommendation,evidence|governing_thought,key_line,evidence_links,conditions|Lead with a supported answer or conditional conclusion;Group supporting reasons by a consistent MECE logic;Attach evidence and counterarguments to each key line;State uncertainty, decision conditions and concrete next actions
44|problem,context|situation,complication,question,answer|State supported Situation;Identify the Complication and its consequences;Formulate a decision-relevant Question;Give a provisional Answer with assumptions and evidence gaps;Do not smuggle a root-cause conclusion into framing
45|pyramid,audience,data|storyboard,action_titles,visual_specs|Define audience decision and governing narrative;Sequence declarative action titles that form a coherent argument;Choose a visual and cited data for each page;Check that evidence supports each title and flag missing data
46|stakeholders,interests,influence|stakeholder_grid,engagement_plan|Define power or influence and interest with evidence;Map manage closely, keep satisfied, keep informed and monitor;Identify conflicting interests and legitimate decision rights;Specify communication and feedback tactics without manipulative assumptions
47|situation,observations,desired_change|feedback_script,questions,followup|Describe observable behavior and impact;Combine Care Personally with Challenge Directly;Invite the other perspective and agree on concrete next behavior;Avoid personality diagnoses and invented motives
48|claim,grounds|claim,grounds,warrant,backing,qualifier,rebuttal,gaps|Separate claim from grounds;Make the connecting warrant explicit and identify backing;State the qualifier and strongest rebuttal conditions;Test unsupported warrants and alternate explanations before endorsement
49|proposal,assumptions,horizon|failure_scenarios,signals,mitigations,stop_conditions|Assume the proposal has failed at the stated horizon;Generate independent failure explanations and challenge optimistic assumptions;Tie each scenario to mechanism, early signal and mitigation;Specify stop or rollback conditions and retain unresolved objections
50|arguments,evidence,alternatives|bias_flags,alternative_interpretations,debiasing_tests|Inspect evidence selection, base rates, anchors, sunk costs, survival filtering, salience, group pressure, certainty, framing and outcome hindsight;Quote observable argument spans rather than diagnosing people;Offer competing interpretations and disconfirming checks;Do not invent bias probabilities
'''

def build():
    methods = {int(a): (b.split(','), c.split(','), d.split(';')) for a,b,c,d in (line.split('|') for line in METHODS.strip().splitlines())}
    source = (ROOT/'Cognition Os Master Blueprint.md').read_text(encoding='utf-8').splitlines()
    index, agents, category = [], [], ''
    for line_no, line in enumerate(source,1):
        if line.startswith('#### Kategori '):
            category = re.search(r'Kategori \d+: (.*?) \(',line).group(1)
        if not re.match(r'\| \*\*AG-\d\d\*\* \| \*\*', line) or not category:
            continue
        cells = [x.strip() for x in line.strip('|').split('|')]
        num=int(re.search(r'AG-(\d+)',cells[0]).group(1))
        if num>50: continue
        name=cells[1].strip('*'); aid=f'AG-{num:02}'; fid=f'FW-{num:02}'
        required, outputs, method=methods[num]
        ref={'document':'Cognition Os Master Blueprint.md','section':f'4.1 / {category}','line':line_no}
        f={'id':fid,'agent_id':aid,'name':name,'category':category,'version':VERSION,
           'provenance':'SOURCE_DERIVED','id_mapping':'ENGINEERING_ADAPTATION: FW numeric correspondence to AG; source explicitly illustrates FW-11',
           'source':ref,'source_original':{'purpose':cells[3],'inputs':cells[4],'outputs':cells[5]},
           'purpose':method[0],'applicability':required,'activation_conditions':[f'The host selects {name} to address an identified analytical gap, or the user explicitly requests it. Skip when prior host analysis is sufficient.'],
           'preconditions':[f'Supplied {field} or an explicit UNKNOWN gap before analysis.' for field in required],
           'input_schema':{'type':'object','required':required,'properties':{field:{} for field in required},'additionalProperties':True},
           'output_schema':f'schemas/framework-output/{fid}.schema.json',
           'required_inputs':required,'optional_inputs':['constraints','evidence','previous_findings','desired_deliverable'],
           'methodology':method,'methodology_provenance':'ENGINEERING_ADAPTATION grounded in source scope',
           'expected_outputs':outputs,'mathematical_requirements': ('Use deterministic helper or independently validated host calculation; disclose units and assumptions.' if num in [2,4,5,6,7,21,23,30,35,42] else 'No unsupported numerical scores.'),
           'tool_requirements':['Host reasoning and resource reading; calculation tool when required.'],
           'evidence_requirements':['Cite material claims; mark missing inputs UNKNOWN; do not reuse illustrative source conclusions.'],
           'limitations':['Host-authored analysis requires behavioral evaluation; schema validity does not prove truth.'],
           'failure_modes':['Invented inputs','Generic analysis replacing distinctive method','Unsupported certainty'],
           'relationships':[f'FW-{n:02}' for n in ({44:[9],9:[10,11],11:[10,2],2:[43],24:[49],49:[43],43:[48],17:[40],32:[34]}.get(num,[]))],
           'workflow_position':('framing' if num==44 else 'synthesis' if num==43 else 'review' if num in [48,49,50] else 'analysis'),
           'validation_criteria':[f'Provide {k} or declare it UNKNOWN with reason.' for k in outputs]+['Use all distinctive methodology steps and identify missing evidence.'],
           'reference_material':[ref]}
        write(f'cognitive-core/frameworks/definitions/{fid}.json',f)
        index.append({k:f[k] for k in ['id','agent_id','name','category'] }|{'path':f'definitions/{fid}.json'})
        agents.append({'id':aid,'name':cells[2].strip('`'),'framework_id':fid,'source':ref,'kind':'logical_specialist','execution':'host_role_or_native_subagent','contract':'schemas/agent-envelope.schema.json','responsibilities':method})
        write(f'schemas/framework-output/{fid}.schema.json',{'$schema':'https://json-schema.org/draft/2020-12/schema','title':f'{fid} analytical payload','type':'object','required':outputs,'properties':{k:{} for k in outputs},'additionalProperties':False})
    assert len(index)==50 and len(set(x['id'] for x in index))==50
    agents.extend([{'id':'AG-51','name':'Chief Orchestrator Agent','kind':'logical_orchestrator','framework_id':None,'source':{'document':'Cognition Os Master Blueprint.md','section':'4.2'},'responsibilities':['Classify problem and gaps','Select justified workflows','Bound execution and evidence retrieval','Check dependencies','Stop when sufficient or blocked']}, {'id':'AG-52','name':'Evaluator Jury & Critic Agent','kind':'logical_evaluator','framework_id':None,'source':{'document':'Cognition Os Master Blueprint.md','section':'4.2'},'responsibilities':['Review arguments and calculations','Retain contradictions','Reject unsupported conclusions','Return ACCEPT, CONDITIONAL, REJECT or INSUFFICIENT_EVIDENCE']}])
    write('cognitive-core/frameworks/registry.json',{'version':VERSION,'frameworks':index})
    write('cognitive-core/agents/registry.json',{'version':VERSION,'agents':agents})
    table='\n'.join(f"| {f['id']} | {f['agent_id']} | {f['name']} | {f['category']} | Source line {next(a for a in agents if a['id']==f['agent_id'])['source']['line']} |" for f in index)
    write('docs/MENTAL_MODEL_REGISTRY.md','# Mental model registry\n\nGenerated by scripts/build_catalog.py; canonical methodology lives in cognitive-core/frameworks/definitions. Source names and category membership are preserved. FW numbering beyond the illustrated FW-11 is an explicit engineering mapping to AG numbers.\n\n| Framework | Logical agent | Source name | Category | Provenance |\n|---|---|---|---|---|\n'+table+'\n')
    write('docs/AGENT_REGISTRY.md','# Logical specialists\n\nThese are 52 role definitions, not 52 running model instances. Source section 4.2 defines the orchestrator and jury. Claude exposes two reusable native agent wrappers; Codex uses available runtime delegation or sequential host roles.\n\n'+ '\n'.join(f"- {a['id']}: {a['name']} ({a.get('framework_id') or a['kind']})" for a in agents)+'\n')
    cases=[]
    for f in index:
        required, outputs, method=methods[int(f['id'][3:])]
        cases.append({'id':f['id'],'prompt':f"Use {f['name']} on a user-supplied case. The required {required[0]} is deliberately missing. Request or explicitly mark the gap before any conclusion.",'expected_method':method,'required_outputs':outputs,'reject':['invented evidence','unsupported numeric confidence','unqualified recommendation'],'status':'NOT_RUN_ON_HOST'})
    write('tests/cognitive-evals/cases.json',cases)
    print(f'Generated {len(index)} frameworks and {len(agents)} logical specialists.')

if __name__=='__main__': build()
