# ECS272-VIS | W02-Thu | 2026-01-15

## Visual Encoding Overview

- Lecture continuation from Tuesday on visual encoding
- Data types split into **categorical** and **quantitative**
- Marks (points, lines, areas) represent data attributes
- Visual channels convey information through position, size, color, texture, etc.

## Visual Channels

- **Position** = most powerful, works for both categorical and quantitative data
- **Size** (area, length) shows magnitude but not exact values
- **Color hue** encodes categories; saturation/value can add extra layers
- **Texture/Density** useful for ordering or grouping when color isn’t enough
- Avoid over‑loading channels; too many interacting channels hinder interpretation

## Marks and Their Uses

- **Point** marks for discrete items, often paired with size or color for extra meaning
- **Line** marks illustrate relationships or trends (quantitative)
- **Area** marks (bars, circles) indicate magnitude; beware of perceptual bias in area estimation
- Combine marks (e.g., shape + size) to differentiate qualitative vs. quantitative aspects

## Design Principles

- Choose the **highest‑ranked channel** (position) for the most important attribute
- Use **color hue** for categorical grouping, but keep palette limited for clarity
- Ensure legends match visual encoding; avoid decorative colors that add no meaning
- Consider presentation medium (screen, projector, paper) – colors may wash out on projectors
- Test readability: can viewers accurately compare sizes, distances, or colors?

## Common Pitfalls

- **Too many channels** → visual clutter, harder to decode
- Misusing **color saturation** for quantitative data can mislead
- Relying on **area** alone for precise comparisons (people underestimate differences)
- Ignoring **medium constraints** (e.g., washed‑out colors on projectors)
- Over‑decorating with colors that don’t convey information

## Example Insights

- Bar charts can imply quantity even when data are categorical → avoid misuse
- Bubble charts (size + color) are attractive but may hide precise values
- Tree maps provide hierarchical grouping; color often decorative, not informative
- Pie charts become unreadable with many slices; limit categories or use alternative visualizations

## Action Items

- Review upcoming assignment: select the most important data attribute and map it to **position**.
- Create a quick sketch using **point + size** for quantitative differences and **color hue** for categories.
- Test your visual on both a screen and a projector to ensure colors remain distinguishable.
