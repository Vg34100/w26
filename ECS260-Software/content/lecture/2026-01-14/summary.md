# ECS260-SE | W02-Wed | 2026-01-14

## Action Items

- Draft research proposal: include research questions (4‑5), motivation, data source, and methods
- Choose 20–30 GitHub repositories to pilot data collection
- Install **PyDriller** (or Percival) and run a test extraction on a sample repo
- Monitor GitHub API usage (≈5 k requests/hr); consider multiple accounts for higher throughput
- Create a reproducibility checklist: data inclusion/exclusion, handling missing values, versioning of scripts

## Lecture Overview

- Upcoming flux of activities starts Tuesday, lasting a few days
- Small incremental changes tied to a specific timeline
- Each student to prepare a short paper/presentation on their topic
- Team must agree on research focus and formulate 4‑5 questions

## Digital Archaeology & Repository Mining

- Treat code history as a “digital archaeological” record
- Analyze past commits to forecast future trends
- Recognize distinct roles: **authors**, **completers**, **acknowledgers**
- Multiple titles may appear for the same contributor

## GitHub Structure & Pitfalls

- Main repo usually read‑only; contributions go through forks & pull requests
- Two repo types: **base** (original) and **fork** (contributor copy)
- Activity hidden in forks/merges; not all changes visible in base repo
- Most projects inactive: \~90 % &lt; 50 commits, only \~30 % active in last month

## Selecting Projects for Analysis

- Use heuristics to filter: activity level, number of commits, project age
- Expect only a small fraction of commits to be directly analyzable
- Prioritize projects with clear commit history and accessible metadata

## Data Gathering Workflow

- Pull data via GitHub API (rate‑limited to \~5 k requests/hr)
- Parallelize with multiple accounts or async scripts for larger batches
- Start with a shallow crawl of 20–30 repos, verify data quality, then scale up

## Tools & Resources

- **PyDriller** – primary Python library for mining Git repositories
- **Percival** – extended metrics calculation
- **Chaos** – collection of software‑engineering metrics (complexity, churn, etc.)
- Additional code search platforms (e.g., Sourcegraph) for broader coverage

## Metrics & Measurement Considerations

- Decide **what** to measure (e.g., churn, author diversity, issue response time)
- Ensure metrics align with research questions and are **rational**
- Normalize by **lines of code (SLOC)** to control for project size
- Be aware of SLOC counting nuances: executable vs. non‑executable, pre‑ vs. post‑release

## Ensuring Reproducibility

- Document data collection steps, scripts, and version numbers
- Record missing or anomalous values and how they are handled
- Share a checklist covering: data source, extraction method, cleaning procedures, and storage location

## Practical Next Steps

- Upcoming class will include a hands‑on example of repository mining (not today)
- Prepare to discuss your proposal and preliminary data set in the next session
- Keep an eye on the weekend schedule for any planned work or rest periods.
