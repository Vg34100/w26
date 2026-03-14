# ECS272-VIS | W08-Thu| 2026-02-26

## Action Items

- Notify professor if you develop a novel interaction technique (credit possible)
- Choose and apply at least one interaction method that fits your final‑project data
- Design your visualization with both author‑driven defaults and user‑driven controls
- Implement selection, linking, and focus‑plus‑context to keep users oriented
- Provide clear color legends, labels, and optional label‑dragging for readability

## Core Ideas

- Interactivity is the heart of effective visualizations
- Interaction design applies to any digital device (phones, websites, apps)
- Good UI comes from costly user studies and iterative design
- Users need to learn from data, not be overwhelmed by clutter

## Interaction Techniques Overview

- **Selection & Highlighting** – brush, click to isolate items, dim others
- **Linking / Brushing Across Views** – coordinated updates when one view changes
- **Small Multiples** – repeat same axis across multiple panels for comparison
- **Focus + Context** – overview pane + zoomed detail, keep orientation
- **Filtering by Time/Category** – sliders, dropdowns for range or categorical filters
- **Drag‑and‑Drop Encoding** – Tableau‑style attribute mapping for quick re‑encoding

## Design Guidance for Final Project

- Define the purpose: what story or insight should the visualization reveal?
- Decide author‑driven defaults (what users see first) vs. user‑driven exploration
- Prioritize interactions that match the data (categorical vs. quantitative axes)
- Limit number of simultaneous views; hide unrelated panels to save screen space
- Use consistent color scales (e.g., orange‑green gradient) and size encoding for importance
- Offer a “reset” button to return to the original overview

## Example Applications Mentioned

- Scientific data validation and discovery (model verification, hypothesis testing)
- Geographic maps with zoomable regions and time‑based heatmaps
- Travel‑time graphs (hour‑of‑day, day‑of‑week) with degree‑based node size
- Housing rent vs. buy decision tool with linked charts and thresholds
- Tableau drag‑and‑drop UI for quick chart creation
- Social‑network analysis of school bullying (color‑coded roles, animated edges, size by report count)

## User‑Centric Principles

- Keep users oriented: history navigation, breadcrumb trail, focus‑plus‑context
- Provide clear legends and annotations for colors, sizes, and axes
- Allow label repositioning when overlap occurs
- Support multiple devices (mouse, touch, keyboard) but prioritize mouse for most demos
- Enable easy filtering and searching of key attributes (e.g., gender, grade level)

## Practical Tips

- Use threshold selection to “blow up” a subset for detailed view
- Combine small multiples with linked brushing for side‑by‑side comparison
- When many variables exist, let users pick a subset via dropdown or slider
- Test your interface with peers to catch disorientation issues early
- Document both the final visualization and the interaction steps that led to it
