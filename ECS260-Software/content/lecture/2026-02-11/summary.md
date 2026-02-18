# ECS260-SE | W06-Wed | 2026-02-11

## Action Items

- Note quiz rescheduled to **Wednesday** (originally Friday, then Monday, now Wednesday).
- Run a **t‑test** on the log‑transformed commit data to verify significance.
- Create two subsets: projects **with a woman** and projects **without a woman**.
- Build a **multivariate regression** including: number of commits, presence of a woman, project age, team size, number of committers.
- Check **VIF** values for all predictors; keep each below \~5.
- Plot residuals and verify normality and homoscedasticity assumptions.
- Prepare to explore **random‑effects / clustering** for next lecture (model 3).

## Quiz Update

- Quiz moved from Friday → Monday → Wednesday.
- Monday is a holiday, so Wednesday is the new date.

## Lecture Overview

- Demonstration of data analysis in **R** (RStudio shown).
- Emphasis that same steps apply in other languages (e.g., Python).
- Goal: illustrate proper EDA, transformation, and regression workflow.

## Data Set Overview

- CSV file with \~10 000 rows (capped from &gt;30 000).
- 46 variables: project ID, language, domain, forks, watchers, commits, project age, team size, gender info, etc.
- Data collected at six‑month intervals; includes pull‑request counts, team member IDs.

## Initial EDA

- Viewed data frame structure, row/column counts.
- Box plot of **commits** split by **has_woman** (true/false).
- Noted heavy right‑skew, many outliers, non‑normal distribution.

## Transformations

- Tried **square‑root** and **log** transforms on commit counts.
- Log transform removed outliers, produced near‑normal shape.
- Discussed why scaling axes isn’t enough; data itself must be transformed for normality.

## Statistical Tests

- Conducted **t‑test** on log‑transformed commits between groups.
  - Difference ≈ ‑0.85, p &lt; 0.0001 → highly significant.
  - Means (log scale): 3.5 (women) vs 2.6 (no women).
- Highlighted that significance alone doesn’t imply causation; other variables may confound.

## Modeling Approach

- Proposed **multivariate regression**:
  - Dependent variable = number of commits (log‑transformed).
  - Predictors: has_woman, project_age, team_size, num_committers, etc.
- Demonstrated creating model object, extracting coefficients (betas) and summary.

## Model Diagnostics

- **R‑squared** ≈ 0.40 → model explains \~40 % of variance.
- **VIF** checked; all below threshold, indicating acceptable multicollinearity.
- Residual plots show non‑normality and outliers; assumptions violated.
- Suggested re‑transforming response or using robust methods.

## Interpretation of Results

- In full model, **has_woman** loses significance (p ≈ 0.84).
- Team size shows **negative** effect on commits; more people ≠ higher productivity.
- Number of committers shows **positive** effect.
- Concluded that simple box‑plot differences disappear after controlling for covariates.

## Discussion on Diversity

- Initial EDA suggested teams with women have more commits, but multivariate analysis tempers that claim.
- Referenced published paper: after proper controls, gender diversity modestly boosts productivity; similar effects for age/experience diversity.

## Tools Comparison

- R praised for rapid interactive analysis (interpreter).
- Python’s **scikit‑learn** mentioned for similar modeling pipelines, though less immediate than R’s REPL.

## Closing Remarks

- Emphasized need for **controlled analysis** before drawing conclusions.
- Next session will cover **random‑effects models** and clustering of projects (model 3).
- Open floor for questions; otherwise students may leave.
