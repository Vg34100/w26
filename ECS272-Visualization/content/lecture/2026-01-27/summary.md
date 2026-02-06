# ECS272-VIS | W04-Tue | 2026-01-27

## Action Items

- Read the LightBa (2024) paper; focus on UI flow and task proposal mechanism
- Review Tamara Rae’s *Introduction to Information Visualization* (online copy available)
- Check the survey section in the LightBa paper for additional related systems
- Prepare a short presentation of your final project (2‑3 min, up to three team members)
- Submit your visualization design early to get AI‑generated feedback before the deadline

## Lecture Overview

- Generative AI → large language models that create visualizations from data
- Three main topics: statistical chart generation, agentic visualization, design feedback loops
- Emphasis on “genetic” (agentic) systems that reason, plan, act, and evaluate results
- AI can suggest improvements, decompose tasks, and generate code automatically

## Agentic Visualization Systems

- LightBa (2024) – user uploads data, sets goal in chat, agent interprets and proposes tasks
- Agent generates code, produces visualizations, and provides findings
- User can accept, reject, or request new proposals; system evaluates quality internally
- Similar works surveyed in the paper; most target simple spreadsheet data → bar/line charts

## Design Feedback & Authoring Tools

- Genetic system can give domain‑specific feedback on visual encodings, interaction techniques, and abstraction design
- Tamara Rae’s guidelines: operation abstraction → encoding → interaction → visual design
- Feedback reports include textual description + example visualizations; users can iterate and track changes

## Network Visualization Research

- Large graphs (thousands of nodes) → force‑directed layout is accurate but slow
- Faster alternatives (e.g., r‑2) trade optimality for speed; parameter tuning affects layout quality
- Your group’s project: neural‑network‑based generative model to explore a latent “data space” for network layouts, with real‑time navigation

## 3‑D Material Rendering with AI

- Stable‑diffusion‑based material generation + illumination control
- Text prompt → material map grid → lighting synthesis → realistic 3‑D render (e.g., human body, agricultural land use)
- System supports single‑ and multi‑material objects; demonstrates high‑fidelity results

## Student Project & Course Logistics

- Final assignment should go beyond simple extensions; aim for novel AI‑augmented visualization
- Slots available for in‑person project presentations (up to three members per team)
- Plan early; avoid last‑minute work that limits iteration with AI feedback
- Maggie Curtis is the point of contact for AI‑related queries and presentation scheduling

## Observations on AI Use in Student Work

- Students using AI tend to produce simpler, more “straight‑forward” visualizations
- Non‑AI users explore richer designs and varied encodings
- Study suggests AI can accelerate completion but may reduce creative exploration
- Encourage balanced use: leverage AI for efficiency, retain critical design thinking and domain knowledge.
