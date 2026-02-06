# ECS260-SE | W05-Mon | 2026-02-02

## Action Items

- Use a power calculator to set α, desired power (e.g., 80 %), and estimate required sample size.
- Verify normality and appropriate scaling of variables before running any test.
- Apply multiple‑comparison corrections when testing many hypotheses (e.g., Bonferroni).
- Report correlation coefficients with their values and significance, not just “significant”.
- Choose the correct statistical test (t‑test, chi‑square, ANOVA, etc.) based on data type and design.

## Hypothesis‑Testing Basics

- Compare experimental group (e.g., Sacramento kids) vs. control (all US kids).
- Null hypothesis (H₀): no difference between groups.
- Alternative hypothesis (H₁): a statistically significant difference exists.
- Test statistic often the difference of means (e.g., 6.7 – 3.0 = 3.7).
- Normalize the difference (e.g., compute *d* or *t*).
- Use t‑test tables or software to obtain p‑value.

## Interpreting p‑Values & α

- p &lt; α → reject H₀; p &gt; α → fail to reject H₀.
- Typical α = 0.05 (two‑tailed → 2.5 % per tail).
- Example: p ≈ 0.002 → 98 % confidence result isn’t due to chance.

## Multiple Testing & False Positives

- Testing many hypotheses inflates false‑positive rate.
- 5 % false positives ≈ 5/100 tests, 50/1000 tests.
- Adjust α or use correction methods to control family‑wise error.

## Type II Error & Power

- β = probability of failing to reject false H₀ (type II error).
- Power = 1 – β; common target ≈ 0.80.
- Higher power → larger sample size or larger effect size.
- Power calculators help back‑solve required n given α, effect size, desired power.

## Common Statistical Tests

- **t‑test**: compare two means (independent or paired).
- **Chi‑square**: test association between categorical variables.
- **ANOVA**: compare &gt;2 group means; generalization of t‑test.
- Choose test matching data type (continuous vs. categorical) and design (paired vs. independent).

## Correlation Considerations

- Report correlation coefficient (r) and its significance.
- r ranges from –1 to +1; not a test of causation.
- Correlation values often non‑normal → avoid parametric follow‑up without transformation.
- Beware of spurious correlations in high‑dimensional data.

## Data Exploration & Assumptions

- Inspect distributions (histograms, Q‑Q plots) for normality.
- Check scale (interval, ratio) before applying parametric tests.
- Transform skewed data (log, sqrt) if needed.
- Mean is useful for symmetric distributions; median may be better for skewed data.
