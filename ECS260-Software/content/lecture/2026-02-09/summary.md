# ECS260-SE | W06-Mon | 2026-02-09

## Action Items

- Review progress report assignment details & rubric (due in \~8‑10 days, set for the 17th)
- Include methodology, data pipeline, preliminary results, and plans for remaining work
- Prepare specific progress, accomplishments, and any obstacles for the report
- Raise questions via hand‑raise reaction or chat during upcoming lectures
- Study the regression slides shared by the professor
- Run linear regression on the provided marketing‑budget dataset
- Report intercept and slope coefficients with confidence intervals and significance tests
- Explore multiple linear regression with all three predictors (TV, radio, newspaper) and compare to single‑predictor models

## Progress Report Overview

- Due \~8‑10 days from now, scheduled for the 17th (day after holiday)
- Expect “meat”: real results, not just proposal
- Need methodology, data‑gathering pipeline, and preliminary findings
- Specific plans for remaining project time required
- Use the rubric to guide content and grading criteria
- Questions can be asked via hand‑raise or chat; professor will pause periodically

## Lecture Interaction Guidelines

- Online lectures: three more sessions planned
- Ask questions by raising hand (reaction button) or posting in chat
- Professor will monitor both and address periodically
- If professor seems distracted, feel free to interject politely

## Methodology & Baseline Comparison

- Focus on creating new methods and comparing them to simple baselines
- Linear regression presented as the baseline model
- Emphasize explainability of simple models vs. fancy methods
- Comparison needed for both performance and interpretability
- Use baseline to justify any claimed improvements

## Regression Modeling Basics

- Goal: predict outcome (sales) from predictors (TV, radio, newspaper budgets)
- Define X = predictors (features), Y = response (sales)
- Assume underlying functional relationship f(x) plus random error ε
- Linear model: Ŷ = β₀ + β₁X (single predictor) or Ŷ = β₀ + β₁X₁ + β₂X₂ + β₃X₃ (multiple)
- Errors are inevitable; model estimates f̂ (beta coefficients)

## Linear Regression Concepts

- Fit line by minimizing sum of squared residuals (MSE)
- β₀ = intercept (sales with zero budget), β₁ = slope (sales change per $1k budget)
- Example: β₀ ≈ 7.5, β₁ ≈ 0.04 → each extra $1k TV budget adds \~0.04 M sales
- Assumptions: linearity, independent errors, homoscedasticity, normality of residuals
- Violations affect model reliability; check during EDA

## Coefficient Interpretation

- Intercept: predicted sales when predictor = 0
- Slope: change in sales per unit increase in predictor
- Sign and magnitude guide decision‑making (e.g., increase TV spend if β₁ &gt; 0)
- Confidence intervals needed to assess reliability of β estimates

## Confidence Intervals & Hypothesis Testing

- Estimate standard errors for β₀, β₁ via analytical formulas or bootstrapping
- Use t‑test: t = (β̂ – 0) / SE(β̂) to test if coefficient differs from zero
- p‑value &lt; 0.05 (or 0.1 for small samples) → coefficient considered significant
- Confidence intervals provide range of plausible β values
- Significance informs which predictors truly affect outcome

## Multiple Linear Regression Findings

- Ran separate models for TV, radio, newspaper and a combined model
- Individual models: coefficients similar to combined model but with larger standard errors
- In combined model, newspaper predictor became non‑significant
- Standard errors tighter in combined model despite loss of significance for one predictor
- Highlights trade‑off: adding variables can improve fit but may dilute individual predictor impact
- Discuss interpretation of non‑significant coefficients and tighter confidence bounds.
