# ECS272 VIS - Data Visualization Intro with TA Rin

## Course Overview

- Combine data + visual elements to discover or share insights
- Focus on design choices that make visualizations powerful
- Workflow: raw data → optional analysis → format (CSV/JSON) → visualization

## Contact & Logistics

- TA: Rin Shin – best reached by email (avoid Canvas messages)
- Office hours: one‑on‑one Zoom sessions
- Email is primary communication channel

## Tools & Setup

- Platforms: Observable notebooks **or** custom web apps (React, vanilla JS, Vue)
- Git & GitHub required for all assignments; use GitHub Classroom links
- IDE options: VS Code, PyCharm, or any editor you prefer
- GitHub Copilot education plan available for free with student verification

## HTML, CSS, & JavaScript Basics

- HTML defines page structure (elements, headings, paragraphs)
- CSS styles that structure (colors, opacity, layout) – mostly static
- JavaScript adds interactivity; needed for dynamic behavior beyond CSS
- Debugging: use browser dev tools (Console, Elements, Network, Performance) and console.log

## SVG vs. Canvas

- **SVG**: vector graphics, built from &lt;svg&gt; elements (circle, rect, path) – ideal for most class visualizations, fast for small‑to‑moderate data sizes
- **Canvas**: pixel‑based drawing via JavaScript – only needed for very large point clouds or custom rendering performance
- Typical SVG circle: cx, cy, r, fill attributes; rectangle uses x, y, width, height

## D3.js Overview

- D3 manipulates SVG elements based on data joins (enter, update, exit)
- Scales map data values to visual ranges (size, color, position)
- Supports basic animations and interactions (hover, click)
- Preferred for assignments that need many elements or smooth transitions

## Homework Assignments

- **Homework 1**: static dashboard (overview + two detail views) using provided templates (React, vanilla JS, Vue)
- **Homework 2**: static visualization (can use Observable or D3) – focus on clean data pipeline
- **Homework 3**: add interactivity & animation to previous visualizations
- Submission checklist:
  1. Live app/notebook link (Observable or hosted)
  2. GitHub repo link (with README: data sources, run instructions, known issues)
  3. No zip uploads; everything must be reproducible in Chrome

## Final Project

- Create a data‑driven story using one of three narrative structures (choose freely)
- Pick a unique dataset; avoid duplicating classmates’ choices
- Expected deliverable: interactive web app (React/JS) with clear storytelling flow
- Example topics: US insider‑trading disclosures, greenhouse‑gas emissions, medical visualization

## Visualization Examples Discussed

- Academic performance dashboard (overview left, detailed right)
- Data‑science salary comparison across countries
- Pesticide sales by crop (size = sales, color = toxicity)
- Insider‑trading network (circle size = investment, x‑axis = return)
- Tree map of stock market sectors (area = market cap)
- COVID‑19 case trends with hover details

## Debugging & Development Tips

- Verify data format before building visualizations (CSV → JSON)
- Use console logs and dev‑tool panels to inspect element attributes and network requests
- Build incrementally: start with static HTML/CSS, then add JS interactivity step‑by‑step
- Log and version control frequently; push commits to GitHub often

## Additional Resources

- Observable notebook docs & example notebooks (linked in slides)
- D3.js official website (scales, selections, transitions)
- GitHub Classroom guides for cloning, committing, and pulling assignments
- Browser developer tools cheat sheet (shortcuts for Console, Elements, Network)
