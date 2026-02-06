# ECS272 Vis - 01/13

## Visualization Process

- Start by identifying data type (spreadsheet, graph, image, etc.)
- Define purpose: personal insight vs. client presentation
- Explore data to extract key insights; large sets may need filtering
- Use search/filter tools: attributes, ranges, categories
- Iterate: refine visual encoding (color, size) based on feedback

## Data Types & Sources

- Structured data: rows & columns (typical spreadsheets)
- Unstructured/irregular data: network graphs, social media, audio, simulation outputs
- Spatial/field data: sensor or satellite grids, 3‑D computational grids
- Mixed datasets possible (e.g., spreadsheet + network + spatial)
- Choose dataset early; allow time for preprocessing

## Marks and Channels

- Marks: basic graphical elements (point, line, bar, area, shape)
- Channels: visual properties used to encode data (position, color, size, shape, angle)
- Match mark type to data: categorical → shape/color; quantitative → position/size
- Order matters for size encoding: render larger marks first, then smaller

## Visual Encoding Principles

- Categorical data: no inherent order; use shape or distinct colors
- Ordinal data: implied ranking; can use hue gradient or size progression
- Quantitative data: precise values; encode with position, length, or area
- Avoid overloading a single channel; combine channels for richer stories
- Include legends/color keys; place them thoughtfully for readability

## Design & User Considerations

- Clear layout and legend placement improve comprehension
- Conduct user studies: peers review visualizations, note confusion points
- Provide overview visualizations before detailed drill‑downs
- Allow users to customize filters, groupings, or clustering for comparison
- Ensure accessibility: distinguishable colors, adequate contrast

## Case Studies & Examples

- Car dataset: encode make, model, year, performance using color, shape, size
- eBay user behavior: visualize clickstreams, segment customers, detect outliers
- Simulation of room temperature: map 3‑D grid values to color gradients
- Research projects: visualize domain‑specific data (bio‑networks, spatial fields)

## Practical Tips

- Start with simple plots; add encoding layers gradually
- Verify each encoding adds meaning, not just decoration
- Test visualizations on real users; iterate based on feedback
- Document data attributes and chosen encodings for reproducibility
- Begin data preprocessing early to avoid last‑minute bottlenecks
