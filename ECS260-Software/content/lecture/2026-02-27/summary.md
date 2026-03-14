# ECS260-SE | W08-Fri | 2026-02-27

## Action Items

- Finish the paper (due Sunday) – incorporate professor’s feedback, aim for 19.5 % grade
- Prepare surveys and interview guides for next class (Monday)
- Review modified PPT template before submission
- Check team progress – ensure everyone starts the assignment
- Allocate time Friday – Saturday / Sunday to work on paper
- Explore Nvidia recruiter outreach if interested in job opportunities

## AI & MLOps Overview

- AI now integral to ML pipelines – “you cannot not use AI”
- Operations focus on software tools, not just hardware
- AI apps map architecture → implementation → dependency control instantly
- Continuous alerts needed for changing components

## Common ML Project Pain Points

- Reproducibility failures: random seeds, data splits, environment drift
- Model results vary across runs – randomness, data changes, code tweaks
- Pipeline breaks when dependencies or data versions shift
- Incompatible library updates cause hidden bugs

## Learning Curve & Tooling

- Steep learning curve – need quick up‑skill on templates & configs
- Use separate Git branch for tests → CI/CD integration
- Deployment = compile, package, run on multiple systems (web, cloud)
- DevOps philosophy: frequent commits, immediate fixes, automated pipelines

## Data Pipelines & Production Flow

- Ingest → store (data lake/SQL) → process → control via software/hardware
- Daily or hourly data refreshes for up‑to‑date models
- Model management: pre‑production (CI tests, validation) vs production (live serving)
- Continuous input stream feeds training → evaluation → deployment

## Case Study: COVID‑19 Bed‑Demand Prediction

- Data sourced from Washington & UC Davis servers, hourly updates
- Simple model predicts next‑day bed needs, improves staffing by \~30 %
- HIPAA‑compliant handling: separate identified & de‑identified data stores
- Model iterates each pandemic wave – requires flexible pipeline

## DevOps vs DataOps Roles

- DevOps: keep production stable, manage releases, guard against breakage
- DataOps: acquire maximal data, ensure data quality, feed models
- Tension: stability vs data volume/variety
- Data scientists need upstream design skills to bridge both sides

## Production Considerations

- Production model must be validated, cost‑estimated, energy‑aware
- Avoid “run a million models” without proper validation – leads to poor results
- Wrappers & automation now handle many steps that were manual before

## Upcoming Class Activities

- Monday: practice surveys & interview techniques
- Continue discussion on ML pipeline best practices
- Open Q&A – no further questions, enjoy the week
