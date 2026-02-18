# ECS260-SE | W06-Fri | 2026-02-13

## Action Items

- Ping the instructor on Slack/Discord if you have any lingering questions
- Post doubts on Piazza or attend office hours for deeper help
- Review the mixed‑effects model tutorial linked on the course webpage
- Use Claude 4.6 or similar coding agents only for assistance, not to generate the final analysis

## Progress Report Assignment

- Due Tuesday; max 6 pages, PDF only, no code included
- Include 1–2 tables and 1–2 plots plus \~4½–5 pages of text
- Show any preliminary data, EDA, and (if possible) CDA results – even if negative or from a sample
- If you have no data yet, pivot quickly to obtain a small dataset (replication allowed, but avoid plagiarism)
- Late‑submission penalty starts after 12 hours; use that window to finalize the pivot

## Regression Lecture Highlights

- **Collinearity**: high correlation among predictors inflates variance, makes coefficients unstable
- **VIF**: flag predictors with VIF &gt; 5–10; drop one of a highly correlated pair
- **Dummy variables**:
  - Binary categorical → single 0/1 indicator (e.g., male = 0, female = 1)
  - Multi‑level categorical → one‑hot encoding, omit one level as baseline
- **Interpretation**:
  - β₀ = mean outcome for baseline group
  - β₁ = difference between baseline and the compared group
- **Model fit metrics**: R², F‑statistic (&gt; 1 suggests significance), AIC & BIC (lower is better)
- **Residuals**: should be random, independent of predictors; patterns indicate missing variables or non‑linearity
- **Over‑fitting**: adding noisy predictors can artificially boost R²; use AIC/BIC to penalize excess variables

## Mixed‑Effects Modeling (Project Data)

- Fixed effects = standard predictors (e.g., gender diversity, tenure diversity)
- Random effects = grouping factors (project ID, quarter) that share a common slope/intercept
- Use lme (linear mixed‑effects) in R for analysis; tutorial available on course site
- Rule of thumb: need \~2–4× more observations than the number of predictors per random effect

## Diversity Study (GitHub Teams Paper)

- Investigated gender & seniority diversity impact on productivity & turnover in open‑source teams
- Data sources:
  - 2.6 M GitHub projects (filtered to \~23 k active projects, \~11 M commits, \~700 k developers)
  - Survey of \~2 k developers on diversity perceptions
- Key metrics:
  - Productivity = commits per quarter (not lines of code)
  - Turnover = fraction of new members each quarter
  - Diversity measured by Blau index (gender) and coefficient of variation (tenure)
- Findings:
  - Higher gender diversity → higher productivity, no effect on turnover
  - Higher tenure (10‑year) diversity → higher productivity **and** higher turnover
- Modeling approach: multivariate regression with controls (project age, activity, team size) plus mixed‑effects to account for repeated measurements per project/quarter
- Implications: diversity can boost output but may also increase churn; nuanced interpretation needed for team composition decisions
