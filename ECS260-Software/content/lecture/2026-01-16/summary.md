# ECS260-SE | W02-Fri | 2026-01-16

## AI/ML Advice & Pitfalls

- Advising to start with exploratory analysis, ensure data quality first
- Recommend simple models (e.g., random forest) before jumping to “AI” hype
- Warn against over‑fitting and using AI when data or problem don’t justify it
- Highlight trend of feeding raw paragraphs to LLMs without proper alignment

## Risks of Fine‑Tuning LLMs

- Base models trained on mixed‑quality data; fine‑tuning can amplify bias
- Fine‑tuned models may become misaligned, even “evil” in certain tasks
- Sensitive domains (medical, psychological) especially vulnerable
- Small data sets for fine‑tuning require careful justification in proposals

## Designing Good Metrics

- Desired properties: valid, reliable, objective, precise, intuitive, robust, practical
- Metric should be explainable in ≤ 1 page; lengthy justification signals a weak metric
- Must handle missing data gracefully; compute within 6–7 weeks
- Choose metrics that align with the research question and data availability

## Metric Development Process

- Start with raw data, perform spot‑checks and deep dives on several projects
- Iterate: adjust metric if it drifts from original goal, keep adjustments progressive
- Use both direct (e.g., lines of code) and indirect measures (e.g., cyclomatic complexity)
- Ensure metric distribution is roughly normal across projects for comparability

## Software Measurement Basics

- Measurement = assigning a number; need clear domain and range (units)
- Distinguish between measuring the product (code size, defects) and the process (effort, productivity)
- Context matters: team allocation, language, libraries affect metric interpretation

## Cost Estimation Overview

- Goal: realistic budget, control project cost, monitor progress
- Start by defining what you’re measuring (complexity, productivity, etc.)
- Leverage prior work; avoid outdated metrics that have been disproven
- Typical inputs: lines of code per person‑month, defect density, feature size

## Human Factors & Productivity

- Productivity linked to well‑being, satisfaction, and mental state
- Studies (e.g., Microsoft) monitor developer emotions, break patterns, and code output
- Hiring more staff on lagging projects doesn’t guarantee better outcomes
- Trust instincts but back them with data; avoid over‑reliance on opaque models

## Practical Tips for Proposals

- Propose two simple, well‑understood baseline methods when data is limited
- Justify metric choice succinctly; avoid over‑complicating with heavy ML pipelines
- Be ready to explain how missing data will be handled and how robustness is ensured
- Keep implementation timeline realistic (few weeks to a couple of months)
