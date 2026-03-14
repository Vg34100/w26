# ECS260-SE | W08-Wed| 2026-02-25

## Action Items

- Read the **Meter white‑paper** on the controlled experiment with Cursor.
- Review the recent **Poseidon study** estimating long‑term Cursor impact.
- Check the three recommended books on causal inference (Scott Colin Palm, basic stats text, formal causal inference book).
- Explore **large language models** for causal‑inference help and parameter tuning.
- Apply a **difference‑in‑differences** or **quasi‑experimental** design to any upcoming project data.

## Lecture Overview

- Professor Vasilescu introduced the student group’s work in empirical software engineering.
- Shift from regression‑focused AI models to causal reasoning.
- Emphasis on moving beyond high predictive accuracy to understanding mechanisms.

## Predictive vs. Causal Models

- Predictive models excel at accuracy (e.g., 98 % performance) but don’t reveal “why”.
- Causal models aim to identify true cause‑effect links, not just correlations.
- Many AI tools provide explanatory power only when paired with solid theory.

## Confounders & Selection Bias

- Project age, team skill, domain, code complexity act as confounders.
- Self‑selection: developers eager to try new tools may already be more productive.
- Unobservable factors (e.g., developer enthusiasm) can bias simple regressions.

## Causal Inference Frameworks

- **Directed Acyclic Graphs (DAGs)**: map assumed relationships, identify confounders, mediators, colliders.
- **Potential Outcomes**: think of each unit’s outcome with and without treatment; impossible to observe both, so estimate via models.

## Common Methods

- **Linear / multivariate regression**: good for correlation, limited causal claim without full covariate set.
- **Fixed‑effects / panel regression**: controls for time‑invariant unobserved heterogeneity.
- **Difference‑in‑Differences**: compares trends of treated vs. untreated groups over time.
- **Natural / quasi‑experiments**: exploit external shocks or policy changes to approximate randomization.
- **Regression discontinuity**: leverages a cutoff to isolate treatment effect.

## Cursor Example (AI coding assistant)

- Simple comparison of GitHub projects with vs. without Cursor shows higher commit counts, but confounded by skill, project size, enthusiasm.
- Need to include relevant covariates (domain, team skill, project complexity) or use quasi‑experimental design.
- Long‑term benefits appear only in early‑stage or highly motivated projects; productivity fades as projects mature.

## Recommendations & Resources

- Build a **causal theory graph** before data collection.
- Choose a method that matches the data and the assumed causal structure.
- Avoid “kitchen‑sink” regressions; too many irrelevant controls dilute the true effect.
- Use **books** and **LLM assistants** to verify assumptions and model specifications.

## Q&A Highlights

- Project duration matters: early‑stage AI assistance boosts speed, later stages see diminishing returns.
- Selection‑into‑treatment can be mitigated with quasi‑experimental setups (e.g., diff‑in‑diff).
- Distinguishing rigorous causal work from “big‑regression” hype requires careful variable selection and theory‑driven modeling.
