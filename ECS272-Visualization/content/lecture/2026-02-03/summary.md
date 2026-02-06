# ECS272-VIS | W05-TUE | 2026-02-03

## Action Items

- Review the lecture slides on logarithmic space and distortion techniques.
- Experiment with allocating visual space to emphasize dense data regions in your own project.
- Try building a small‑multiple view for a time‑series dataset you have.
- Sketch a storyline‑style visualization for a simple narrative (e.g., a short story or movie plot).

## Visualization Space & Distortion

- Choose the right visual space for the data you want to show.
- Logarithmic space works well for large dynamic ranges (e.g., radar‑change data).
- Use distortion to highlight important aspects or give more room to dense data.
- Allocate display space to emphasize selected data features.

## Time Dimension in Visualizations

- Time is a common extra dimension; often visualized separately from spatial axes.
- Preserve space for conveying temporal evolution (e.g., disease progression).
- Align subjects by a common event (e.g., disease onset) to compare trajectories.

## Chronic Kidney Disease Cohort Example

- 18‑year patient cohort, chronic kidney disease progression.
- Align patients by the time they first receive a diagnosis (time = 0).
- Visualize disease onset and evolution across the cohort.
- Allow physicians to select subsets (e.g., by gender, event type).

## Train Schedule Example (Encoding Time & Space)

- Hand‑drawn schedule shows stations along a spatial axis and time on the horizontal axis.
- Lines indicate train departures, arrivals, and stops.
- Demonstrates how a single view can encode both location and temporal information.

## Bomb‑Building Movement Scenario

- Visualization of a building floor plan with a bomb location and exits.
- Track individual movements; use color to indicate status (inside, outside, deceased).
- Highlight pre‑explosion movements to identify suspects.
- Show how direct physical‑space mapping can become cluttered; consider alternative encodings.

## Storyline Visualization & Movie Examples

- Storyline visualizations map characters/events over time (e.g., *Star Wars*, *Jurassic Park*, *12 Angry Men*).
- Use lines, colors, and labels to indicate interactions, proximity, and key moments.
- Emphasize critical time points (e.g., time‑travel scenes).
- Storyline approach works for narrative data but can overload with many entities.

## Animation in Data Visualization

- Animation useful for time‑dependent data (e.g., butterfly fluid‑flow simulation).
- Design choices: what to animate, visual encodings (color, transparency), transition smoothness.
- Animated transitions help compare statistical graphics (bar → donut, sorting, log transforms).
- Limitations: long videos are hard to recall; interactive control (play/pause, scrub) mitigates this.

## Open‑Source Repository Visualization

- Visualize commit history, file check‑outs, and developer interactions.
- Use particles/dots for developers, color for activity type (code vs. docs).
- No fixed axes; layout reflects relational proximity of files and contributors.
- Histogram overlay shows activity cycles (weekly, holidays).

## Small Multiples & Comparative Views

- Place multiple snapshots side‑by‑side for easy comparison (e.g., air‑pollution hourly frames).
- Works well for limited time points; avoids overloading a single animation.
- Good for scientific data (earthquake simulations, pollution maps).

## Design Considerations & User Interaction

- Allow users to filter/select subsets (by attribute, gender, event type).
- Provide both static (storyline) and interactive (animation) options.
- Use transitions to preserve mental map when switching layouts.
- Keep visual encoding consistent to aid interpretation.
