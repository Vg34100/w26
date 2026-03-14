# ECS260-SE | W07-Wed | 2026-02-18

## Announcements

- Upcoming treat: Arne & Helen’s new paper presentation, first time in class, scheduled for Wednesday
- Guest lectures & LLM session planned for next week
- AI‑related Q&A session will follow the lecture
- Progress reports to be discussed today

## Progress Report Discussion

- Review what went well vs. what didn’t
- Identify patterns & anti‑patterns in work flow
- Gauge team satisfaction (happy vs. unsatisfied)
- Check if teams are the right size (too big / too small)
- Discuss fairness, metric clarity, and achievable goals

## Team Process & Load Sharing

- Ensure process is clear to avoid difficulties
- Iterate and adjust process as needed
- Decide between self‑selecting work vs. assigning tasks
- Emphasize communication for any changes
- Voting required for major pipeline modifications

## Data Sampling & Bias

- Current sample: first 10 k rows of a larger dataset
- Risk of bias if data is sorted (e.g., early categories dominate)
- Need to shuffle or use a more representative sampling method

## Mixed Effects Modeling

- Fixed effects + random effect of project ID added
- Log‑transform commits to handle outlier skew
- Model 1: \~40 % variance explained, poor residuals
- Model 2: improved fit after adjustments
- Model 3: mixed‑effects, separates project‑level slopes

## Model Evaluation & Variance Explained

- Use AIC/BIC for model comparison (BIC preferred)
- Conditional R² (including random effects) vs. marginal R² (fixed effects only)
- Variance explained rose from \~40 % → 43 % with mixed model, 67 % in final paper after adding diversity factor

## Diversity Metrics

- Compute Blau index for each project (0 = no diversity, 1 = maximal diversity)
- Example: 2 men + 2 women → index = 1; all same gender → index = 0
- Diversity linked to higher explained variance in models

## AI & LLM Topics

- Need for explainability when using AI/LLMs
- Distinguish discriminative vs. generative learning
- Supervised learning: labeled data → predict labels
- Unsupervised/contrastive learning: find similarity structure without labels
- Brief review options: theory (GANs, attention, contrastive learning) vs. jump straight to applications

## Student Questions & Next Steps

- Ask whether to review theory first or move to paper applications
- Offer slides on contrastive learning, GANs, attention mechanisms
- Encourage questions on fixed vs. random effects, model interpretation, and AI concepts
