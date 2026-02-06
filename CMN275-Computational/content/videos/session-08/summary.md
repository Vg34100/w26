# CMN SESSION 8 - Computer Simulation

## Action Items

- None identified for Pablo.

## Quiz Review – Key Concepts

- Replication Crisis: many social‑science findings fail to replicate.
- People take more risks on small, low‑stakes choices (e.g., picking lunch for many friends).
- Choosing a college minor is a lower‑stakes decision than picking a first internship.
- Weekend trips with a fun but conflict‑prone friend are riskier than a safe date.
- Risk‑taking is higher when impact is low; safety is preferred for high‑impact outcomes.
- “Risky” jar (1‑10) offers more variety → possible low or high payoff; “safe” jar (7‑9) limits outcomes.
- random 5 in NetLogo returns 0‑4; adding 5 yields 5‑7.

## Risk Modeling – Safe vs. Risky Decisions

- Safe bet: draw from numbers 7, 8, 9 (limited, consistently high).
- Risky bet: draw from numbers 1‑10 (wide range, includes low values).
- Mean of safe bet &gt; mean of risky bet (≈ 8 vs 5.5).
- When averaging many draws, safe bets give higher expected payoff.

## Mean vs. Max Strategies

- **Playing for the mean**: aim for a good average (e.g., many dates, gig work).
- **Playing for the max**: chase the best single outcome (e.g., career, long‑term partner).
- With few attempts, safe bet still wins; with many attempts, risky bet can outperform.
- “Sweet spot” for risky vs. safe crossover is around 6–9 attempts.

## NetLogo Code Basics

- random 10 → 0‑9; add 1 to get 1‑10.
- random 3 + 7 → 7‑9 (safe bet).
- n-values 100 \[random 10 + 1\] creates 100 random draws; mean computes average.
- Switching mean to max changes focus from average to best outcome.

## Epidemiology Overview

- Studies distribution & determinants of health across populations.
- Focuses on disease frequency, risk factors, and how social/behavioral contexts shape health.
- Social epidemiology examines how education, income, race, policies, etc., affect health outcomes.

## Education & Dementia Findings

- More education → lower risk of Alzheimer’s and other dementias.
- Correlation ≠ causation: higher education is associated with lower risk, but not proven to cause it.

## Natural Experiments in Education

- Compulsory schooling laws serve as interventions (experimental group) vs. states without them (control).
- Difference‑in‑differences: compare before/after within a state **and** across states to isolate causal effect.
- Results: longer mandatory schooling modestly improves later‑life cognition.

## Stroke Disparities & Simulations

- Young Black adults have \~2× higher stroke risk than whites; disparity narrows with age and reverses after \~80 y.
- Selective survival & Medicare access explain older‑age patterns.
- Researchers used computer simulations (Monte Carlo style) to model how differential mortality biases observed stroke rates.
- Simulations showed that bias grows as more of the cohort dies from other causes.

## Agent‑Based Modeling Fundamentals

- **Agents** = individual entities (people, governments, NGOs).
- **Attributes** = traits of agents (political orientation, income).
- Models are **modular** (code can be reused) and **probabilistic** (outcomes are distributions).
- Emergence: macro‑level patterns arise from micro‑level interactions.

## Granovetter Threshold Model

- Threshold = number of others acting before you join (e.g., panic in a crowd).
- With diverse thresholds (1, 2, 3,…), a single starter can trigger a cascade where everyone eventually runs.
- If thresholds are higher (e.g., 8, 10), the cascade stops early (only low‑threshold individuals act).

## Traffic Jam Emergence

- Small variations in acceleration/deceleration among drivers create “waves” that cause jams even without obstacles.
- The “interesting in‑between” of driver behavior (neither fully uniform nor completely random) drives emergent stop‑and‑go traffic.

## Wolf‑Sheep Predation Dynamics

- Sheep reproduce; wolves do **not** reproduce in the standard NetLogo model.
- Wolves lose energy each step, gain it by eating sheep, and die when energy hits zero.
- Feedback loops (grass → sheep → wolves) generate oscillatory population cycles.
- When many sheep over‑graze, grass declines, leading to sheep decline, then wolf decline, and the cycle repeats.

## Phase Transitions & Social Emergence

- Quantitative changes can trigger qualitative shifts (e.g., water → vapor).
- In societies, small policy tweaks can tip a system from segregation to integration, or from stability to crisis.
- Inter‑dependency among diverse agents is the engine of phase transitions.

## Computational Modeling Principles

- **Occam’s Razor**: prefer the simpler model when predictive power is equal.
- **Probabilistic Humility**: models give distributions of outcomes, not precise predictions for single events.
- All models are “wrong” but can be useful; the goal is to capture enough of reality to be informative.
- More computing power & richer data enable finer‑grained, more realistic simulations, but a perfect one‑to‑one replica of reality remains impossible.

## Applications & Policy Advice

- Simulations provide an intuitive way to explore “what‑if” scenarios for policymakers, CEOs, or NGOs.
- Modular code lets you adapt a base model (e.g., traffic flow) to new contexts without rebuilding from scratch.
- Combining empirical data, analytical theory, and simulation offers a powerful, interdisciplinary research toolkit.
