# Calculation interface

Invoke the installed absolute path to scripts/cognition.py: `python <helper> compute --input <workspace-input.json>`. The input is {"operation":"ev","inputs":{...}}. No shell expressions or dynamic code are accepted. Helpers support Python 3.10+. Inputs must be finite JSON numbers; booleans are rejected as numbers. Results do not issue automatic financial decisions.

| Operation | Required input keys | Method / limitations |
|---|---|---|
| ev | probability, upside, downside, costs, unit | gross=pU-(1-p)D; net=gross-C; losses and common costs nonnegative |
| expected_value | outcomes, costs, unit | outcomes each probability, signed payoff; probabilities sum to one; mutually exclusive/exhaustive is caller assumption |
| scenario_compare | scenarios, unit | each name, probability, upside, downside, costs; common unit; rank by net EV only |
| bayes | prior, likelihood_if_true, likelihood_if_false | exact Bayes; zero-probability evidence rejected; infinite Bayes factor reported as null with note |
| bayes_sequence | prior, likelihood_pairs, conditional_independence | pairs of conditional likelihoods; explicit independence acknowledgement; stable log calculations |
| rice | initiatives, reach_unit, effort_unit, time_horizon | each name, reach, impact, confidence 0..1, effort>0; never invent factors |
| decision_matrix | criteria, alternatives | criterion name/weight/minimum/maximum/direction benefit or cost; weights sum to one; each alternative name and scores map |
| break_even | fixed_cost, price, variable_cost, unit | fixed/(price-variable); no finite answer for nonpositive contribution margin |
| cost_benefit | costs, benefits, discount_rate, unit, period | matching nonnegative series starting t=0; discounted PV, NPV and BCR; no assumed rate |
| sensitivity | base, parameter, values | base contains all ev arguments; vary one parameter; up to 1,000 points |
| simulate | probability, upside, downside, costs, iterations, seed, unit | independent draws, explicit distributions; 2..100,000 iterations; numerical interval does not measure forecast reliability |
| pareto | contributions, unit; optional target | observed cumulative shares; default target 0.8 is a configurable coverage target, not a claim about actual 80/20 concentration |
| critical_path | tasks, time_unit | each id, duration, predecessors; forward/backward DAG passes; all zero-slack activities; excludes resource leveling |
| stock_flow | initial_stock, inflows, outflows, time_step, stock_unit, time_unit | discrete conservation; rates per time; rejects stock underflow |

Distribution shapes: fixed {type,value}; triangular {type,low,mode,high}; lognormal {type,mu_log,sigma_log}; beta {type,alpha,beta}. Probability accepts fixed in [0,1] or positive-parameter beta. Monetary quantities use nonnegative fixed, triangular or lognormal. State unit, price basis, horizon and independence assumption. No distribution widths are inferred from an uncalibrated confidence score. Record helper version, Python version, seed and full inputs.

Risk outputs include probability of positive net outcome, fifth-percentile net outcome and nonnegative loss VaR95. A user must supply risk tolerance before interpreting those metrics. Sample-mean intervals describe sampling error conditional on the supplied model, never certainty about a real forecast.
