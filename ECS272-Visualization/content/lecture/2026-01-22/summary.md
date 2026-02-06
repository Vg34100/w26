# ECS272-VIS | W03-Thu | 2026-01-22

## Challenges in Visualizing Large Geological Datasets

- Too many sample points overload the pixel grid → cluttered, hard to read
- Limited screen resolution forces trade‑off between detail and overview
- Overlapping symbols hide smaller or less frequent data points

## Strategies for Aggregation and Interaction

- Apply hierarchical aggregation to create a high‑level view first
- Enable zoom‑in to reveal raw samples in a focused region
- Use step‑by‑step drill‑down rather than displaying everything at once

## Visual Encoding: Position, Size, Color

- Position encodes primary variables (e.g., weight vs. horsepower)
- Size can indicate magnitude but may obscure when many points share similar sizes
- Color adds a second channel; careful palette choice avoids confusion
- Combine position + color for stronger grouping cues

## Misinterpretation Risks (Typhoon Forecast Example)

- Expanding uncertainty bubbles often mistaken for increasing storm strength
- Show multiple predicted paths with color‑coded categories to separate strength from uncertainty
- Clear legends are essential to prevent wrong conclusions

## AI‑Assisted Visualization Generation

- Large language models (LLMs) can produce code for charts from natural‑language prompts
- Diffusion models can suggest visual styles or generate mock‑ups
- AI can automate data cleaning, summarization, and basic statistical calculations

## Prompt Engineering for Generative Models

- Be specific: name exact variables, chart type, time range, and any filters
- Avoid vague requests like “make a chart” → refine to “scatter plot of horsepower vs. weight, colored by region”
- Iteratively refine prompts; each sub‑task can be broken down for better results

## Evaluating LLM Performance on Visual Tasks

- Studies compare GPT‑4, Gemini, and other models on visual‑literacy quizzes (line, pie, area charts)
- Accuracy varies with model training data and domain knowledge (e.g., finance vs. geology)
- Models still struggle with precise numerical reasoning and interpreting complex legends

## Practical Examples and Limitations

- Generated automobile dataset visualizations showed missing legends and over‑plotting issues
- Size‑only encodings often fail when many points share similar values
- AI‑generated code may need debugging; understanding programming basics remains crucial
- Model outputs can drift over time (different results in November vs. January) → track versioning of prompts and data.
