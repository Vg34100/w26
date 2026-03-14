# STA220-DATA | W10-Thu | 2026-03-10

## Action Items

- Use the generic question list after each group presentation to earn participation points.
- For the data‑lab project, ask the integration, dynamic‑site, tool‑choice, user‑friendliness, and data‑accuracy questions.
- After the graph‑visualization segment, pose the seed‑page, cycle‑handling, PageRank runtime, parameter‑adjustment, and application‑impact questions.
- Review the lecture’s key findings on hospital rating divergence, bike‑scooter traffic, and NBA clutch performance; note any unclear points for follow‑up.
- Prepare at least one clarifying question for the professor on CMS data sources or methodology.

## Generic Participation Questions

- Main challenge your group faced?
- How did you decide on your approach or topic?
- What would you add or improve with more time?
- Most surprising thing you learned?
- How did you divide the work?
- Biggest takeaway from the presentation?
- How does your topic connect to class material?

## CMS Definition

- Centers for Medicare & Medicaid Services – U.S. agency managing national healthcare programs.
- Publishes hospital quality ratings and performance data.

## Third Presentation – Data Lab Project (Full‑Stack Web App)

- Goal: simplify data scraping and analysis in one interactive platform.
- Motivation: online data is abundant but hard to collect without coding.
- Tool lets users point to a website and extract structured data with little or no code.
- Use cases: students learning selectors, researchers gathering data, developers testing selectors.
- Tech stack: BeautifulSoup for static scraping, Selenium for dynamic pages, React front‑end, decoupled back‑end API, PostgreSQL storage.

## Tailored Questions for Data Lab Project

- Biggest challenges integrating front‑end and back‑end?
- How does the tool handle dynamic sites that change frequently?
- Why choose BeautifulSoup and Selenium over other scraping libraries?
- Can the app be adapted for non‑technical users (e.g., researchers)?
- How do you ensure scraped data stays accurate and up‑to‑date?

## Dynamic Website Examples

- Twitter – constantly updating tweets and trends.
- Amazon product pages – price, stock, and recommendation changes.
- News sites (CNN) – live updates and script‑loaded content.
- YouTube – videos, comments, view counts, and recommendations refresh in real time.

## Additional Tailored Questions (Graph Visualization & PageRank)

- How do you decide the seed page for building the graph?
- Does the crawler handle cycles or repeated links?
- Typical runtime to compute PageRank for a large site?
- Can users adjust the damping factor or node limit?
- How could PageRank results improve data collection or analysis?

## Lecture – Hospital Ratings Divergence (CMS vs. Online)

- Public CMS ratings based on clinical outcomes, readmissions, patient experience.
- Online platforms (Google Maps, Yelp) provide crowd‑sourced reputations.
- Research questions:
  - Do online reputations reflect objective clinical safety?
  - What drives the perceptual gap (social‑economic, digital traffic)?
  - How do hospital structures affect ranking differences?
- Data sources: Google API (county‑level in California) + CMS data, fuzzy‑matched on hospital names (75 % cutoff).
- Sample: \~250 California hospitals after cleaning; 65 unmatched initially, later re‑matched.
- Methods: percentile gap analysis, Wilcoxon tests (non‑normal data), regression models for gap explanation.
- Findings: moderate correlation between Google and CMS overall; clinical outcomes show no correlation.
- Digital “traffic” (review count) inflates Google scores; institutional bias observed (e.g., Kaiser hospitals).
- Limitations: California‑only data, self‑selected online reviews, missing data for large institutions, API rate limits.

## Lecture – Data Lab Full‑Stack Application (Demo)

- Crawl starts from a seed URL, bounded hop depth, domain restriction, link‑extraction cap.
- Graph nodes = pages; edges = hyperlinks.
- PageRank computed iteratively with damping factor to avoid cycles.
- Visual cues: node size = hop distance, color = domain, edge thickness = PageRank weight.
- Interactive features: hover for node details, adjustable parameters, export of graph data.
- Current constraints: limited UI polish, scaling issues, incomplete data visualizations.
- Future plans: improve performance, add video‑based analysis, enhance UI/UX, support more data sources.

## Lecture – Bike & Scooter Traffic Study (Davis, CA)

- Data: bicycle/scooter counter at 3rd St & University (May 2023).
- Objectives: assess impact of weather, holidays, daylight, temperature on traffic volume.
- Predictors: temperature, precipitation, holidays, weekends, daylight hours (via “astro” package).
- Modeling: negative binomial regression; key results:
  - Holidays, weekends, rainfall significantly reduce counts.
  - Daylight and temperature have minimal effect (Davis weather is generally mild).
  - Scooters less sensitive to holidays than bikes (possible electric‑scooter factor).
- Clustering: PCA → 3 components (≥90 % variance), then Gaussian Mixture Model to identify weekly patterns (summer low traffic, academic term high traffic, holiday/long‑weekend anomalies).
- Limitations: single counter location, occasional under‑counting (multiple riders), lack of hourly data for full period.

## Lecture – NBA Clutch Performance Analysis

- Research questions:
  1. Do top regular‑season teams also excel in clutch situations?
  2. Which team‑level factors best explain clutch success?
  3. How does clutch performance change across seasons?
- Data: regular‑season metrics (offensive/defensive), clutch metrics (last 5 min of close games), four “clutch factors” (effective field goal %, turnover %, free‑throw %, etc.).
- Methods: correlation heatmap, regression, quadrant plots (EFG vs. turnover).
- Key findings:
  - Effective field goal % is the strongest positive driver of clutch wins.
  - High turnover % strongly negative.
  - Rebounding shows minimal impact.
  - Teams with high EFG & low turnovers dominate clutch quadrant (e.g., Thunder, Celtics, Pacers).
- Limitations: only one season, no player‑level data, clutch definition thresholds affect results, small sample (\~240 games).
- Suggested extensions: incorporate player‑level stats, opponent strength adjustments, multi‑season analysis.
