# ECS260-SE | W05-Fri | 2026-02-06

## Action Items

- Download **diversity_data.csv** from the classroom link
- Open the Jupyter notebook provided by the professor
- Run the initial data import and inspect the DataFrame shape (≈ 9,299 rows)
- Perform basic EDA: summary statistics, data types, missing values
- Apply log‑transform to skewed numeric columns (e.g., total_per_meter)
- Conduct normality tests (p‑value &lt; 0.05 → non‑normal) and, if needed, re‑test after transformation
- Prepare visualizations (histograms, box plots, scatter plots, QQ‑plots) for the report

## Overview

- Lecture focused on a **diversity dataset** from GitHub projects
- Goal: practice EDA, hypothesis testing, and visual reporting
- Emphasis on both **positive** and **negative** results in the progress report
- Professor encouraged questions and discussion throughout

## Data Description

- Each record represents a GitHub repository
- Key fields: owner, project name, language, creation date, domain, watchers, stars, forks, project age, issue count, commit count, contributors’ gender, country, and “limit” parameter
- CSV uses semicolons; professor converted it to commas for easier handling
- Numeric columns include counts (watchers, forks, commits, etc.)
- Categorical columns include language, domain, gender

## Exploratory Data Analysis (EDA)

- Load CSV into a pandas DataFrame; verify column data types
- Use df.describe() for numeric summaries (mean, std, quartiles)
- Identify string/object columns that need encoding or exclusion (e.g., row_id, project_id)
- Filter columns relevant to the analysis (e.g., total_per_meter, num_commits)
- Check for outliers and extreme values in count columns

## Statistical Testing & Normality

- Null hypothesis: data follows a normal distribution
- Perform Gaussian normality test (p‑value &lt; 0.05 → reject normality)
- Log‑transform skewed variables (total_per_meter) to improve normality
- Re‑run normality test after transformation; note p‑value changes
- If still non‑normal, consider square‑root transform or non‑parametric tests

## Visualization Techniques

- **Histogram** of total_per_meter (raw vs. log‑transformed) to show skewness
- **Box plot** to highlight outliers across projects
- **QQ‑plot** to assess normality visually
- **Scatter plot** (e.g., number of comments vs. total_per_meter) to explore relationships
- Use log‑scaled axes when appropriate to reveal patterns

## Correlation & Further Analysis

- Compute Pearson correlation matrix for numeric variables (r and p values)
- Observe low/insignificant correlations between gender presence and permits
- Conduct two‑sample t‑tests to compare groups (e.g., projects with vs. without women contributors)
- Interpret results: significant p‑value &lt; 0.05 indicates a likely effect, otherwise chance
- Consider multivariate analysis if comparing more than two variables simultaneously
