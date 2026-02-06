# ECS260-SE | W04-Fri | 2026-01-30

## Action Items

- Read the newly posted Science paper (added to reading list next week)
- Review the series of Mining Software Repository conference papers on AI code
- Download the R script and accompanying data from the lecture page
- Practice basic EDA in R: load data, compute mean/median/SD, create histograms & boxplots
- Run normality tests (e.g., Shapiro‑Wilk, Q‑Q plot) on each variable
- Identify and handle outliers (remove or cap at 1.5–2× IQR)
- Check pairwise correlations; drop one of any variables with ≥ 0.9 correlation

## Lecture Overview

- Focus on presenting & visualizing research results
- Emphasis on EDA before formal modeling
- Importance of clear, reproducible data pipelines

## Data Organization & Reshaping

- Store raw data in CSV or spreadsheet format
- Two common structures: “stacked” (one row per subject/condition) vs. “unstacked” (wide format)
- Unstacked saves space but can hide condition ordering
- Keep condition labels (e.g., before/after) to preserve context

## Summary Statistics & Variability

- Compute mean, median, mode for central tendency
- Use variance, standard deviation, and standard error to describe spread
- Recognize bimodal or skewed distributions that simple averages can mask

## Distribution Visualization

- Histograms: choose appropriate bin count (avoid too few or too many)
- Boxplots: show median, IQR, whiskers, and outliers (1.5× IQR rule)
- Scatter plots for continuous‑continuous relationships
- Q‑Q plots to assess normality visually

## Normality & Z‑Scores

- Normal (Gaussian) shape arises from independent trials
- Z‑score = (value – mean) / SD; 95 % of data ≈ within ±2 SD
- Verify normality before applying parametric tests (use Shapiro‑Wilk, KS, etc.)

## Outlier Handling

- Detect outliers via boxplot rule or &gt; 2–3 SD from mean
- Options: delete, cap, or add noise to reduce impact
- Prefer exclusion for initial analysis unless outlier has substantive meaning

## Correlation & Variable Selection

- Compute correlation matrix; drop one of any pair with very high correlation (≈ 1.0)
- Reduces multicollinearity and simplifies models

## Using R for EDA

- R script provided links to data, functions for summary stats & plots
- Install tidyverse for data wrangling, ggplot2 for visualizations
- Encourage self‑guided tutorials (Google, GPT) for quick function lookup

## Recommended Reading

- Science paper on mixed empirical/inferential AI code detection
- Papers discussing AI‑generated code classifiers
- Mining Software Repository conference papers on AI‑related mining techniques
