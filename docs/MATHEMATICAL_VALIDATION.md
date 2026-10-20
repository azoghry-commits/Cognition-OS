# Mathematical validation

See references/CALCULATIONS.md for exact interfaces. Implementation: cognition/mathematics.py. Independent reference tests: tests/test_mathematics.py. Source contradictions: SOURCE_ANALYSIS C01-C09.

Reference EV: 0.65*2.4 - 0.35*0.3 = 1.455 gross; subtract 0.8 -> 0.655 USD million net. Source +1.2M requires changed assumptions that are not supplied. No forecast confidence or PROCEED label is inferred.

Bayes preserves endpoints and rejects impossible evidence. Sequence calculation uses log likelihoods to avoid underflow and requires explicit independence acknowledgement. RICE validates common reach/effort/period and confidence as a fraction. Weighted matrices normalize declared benefit/cost scales; outputs express preference, never certainty. Cash flows begin at t=0 and require common periods and explicit discount rate.

Simulation uses explicit fixed, triangular, lognormal or beta distributions, bounded iterations and integer seed. It separates stochastic samples from empirical observations and measures numerical standard error only. Fixed p=0/1 remains exact. Loss VaR is distinguished from signed net-outcome quantiles. The caller must justify parameterization and independence; these are not facts verified by the helper.

CPM validates a DAG and returns early/late dates, slack and critical activities; stock-flow checks time-step units and conservation with nonnegative stock. Sensitivity varies only a declared EV input. Boundary/invalid/overflow cases are rejected with exit code 2, not silently corrected.

