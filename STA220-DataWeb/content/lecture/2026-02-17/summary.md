# STA220-DATA | W07-Tue | 2026-02-17

## Action Items

- Review the shared data sets (teacher salary, air quality, species lists, etc.) before next meeting
- Draft one or two research questions for the group to discuss by next Thursday
- Send any relevant code or documents to classmates for collaborative work
- Choose a primary project focus: web‑scraping, data visualization, or image processing
- Experiment with a small visualization (e.g., seaborn or ggplot) to test the chosen data source

## Presentation Schedule

- March 5: three presentations (first day)
- Remaining two days: five presentations each
- Aim for \~100 min total per day; allocate \~19 min per group (12‑15 min talk + 5 min discussion)
- Strict timing: move to next presenter after 20 min regardless of overruns

## Presentation Guidelines

- Start by convincing the audience why the research question matters
- Include brief data collection/description slide (sample size, feature count)
- Show a quick data‑processing overview (e.g., handling NAs, transformations)
- Highlight methods used between raw data and final results
- End with a clear visualization of findings and a 5‑minute Q&A

## Homework & Announcements

- Second homework due Friday
- Discussion session scheduled for Feb 26 (≈1 hour) to address project concerns
- Reminder: participation grade heavily weighted on discussion contributions

## Visualization Packages Overview

- **Low‑level**: Matplotlib (more code, high flexibility)
- **Mid‑level**: Seaborn (statistical plots, minimal code)
- **High‑level**: Plotly/ggplot‑style libraries (quick, polished visuals)
- Recommendation: start with Seaborn for professional looks; use ggplot‑style if familiar with R syntax

## Image Processing Basics

- Images loaded as NumPy arrays (shape: height × width × RGB)
- Simple operations: channel scaling, hue adjustments, region‑based color changes
- Example workflow: isolate a corner, compute mean/SD, recolor based on thresholds
- Packages mentioned: imread, numpy, basic filtering functions

## Mapping & Spatial Data

- Use Python mapping libraries to plot points (e.g., restaurants, climate stations) on interactive HTML maps
- Key steps: geocode addresses → latitude/longitude → add markers to map object
- Tile layers can show different data (satellite, terrain, custom overlays)
- Export map as HTML for easy sharing without needing a notebook server

## Project Ideas & Data Sources

- **Species / biodiversity**: scrape species lists, visualize endangered status by region
- **Teacher salary**: analyze county‑level salary data, combine with poverty metrics
- **Air quality**: pull PM2.5 data via API, merge with other environmental datasets
- **Winter & Summer Games**: map host cities, add temporal layers, explore event‑related metrics
- Potential to combine multiple sources (e.g., air quality + climate data) for richer analysis

## Next Steps for the Group

- Explore the listed datasets and decide which aligns best with interests and skill sets
- Prepare a short demo (code + visualization) for the next class to showcase feasibility
- Keep communication open on a shared document or repository for code and ideas.
