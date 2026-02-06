# CMN SESSION 7 - Agent-Based

## Overview

- Professor Paul Smaldino introduces agent‑based modeling (ABM)
- Emphasizes need for clear definitions of parts & relationships in any model
- No single “best” decomposition; choice depends on research question

## Modeling Basics

- Models = abstract or physical structures representing real‑world phenomena
- Physical models (e.g., scale Bay model) help test costly interventions
- Computational models encode assumptions as equations or code
- Uses: clarify hypotheses, explore consequences, test counter‑factuals, make predictions, guide empirical work

## Predator–Prey Example

- Snowshoe hare ↔ lynx dynamics illustrate simple differential‑equation model
- Isolated hare → exponential growth; isolated lynx → decline
- Interaction → oscillations (hares rise → lynx rise → hare drop → lynx drop)
- Model matches observed natural cycles

## Self‑Organization & Boids

- Starling murmurations, fish schools, bee swarms emerge without central control
- Boids rules:
  - **Separation** – avoid collisions
  - **Alignment** – match neighbors’ direction
  - **Cohesion** – move toward group center
- Simple local rules → realistic flocking behavior

## Axelrod Cultural Model

- Agents carry a vector of cultural traits (e.g., music, language)
- Two core assumptions:
  - **Homophily** – interact more with similar others
  - **Social influence** – interaction makes agents more alike
- Spatial grid; similarity % → interaction probability; interaction → one trait copied
- Leads to cultural clusters and boundaries over time

## Schelling Segregation Model

- Agents prefer a minimum % of similar neighbors (tolerance level)
- Random moves reduce unhappiness; segregation emerges even with high tolerance
- Small changes in tolerance can cause tipping points → abrupt shift from mixed to highly segregated societies
- Demonstrates non‑linear, emergent social outcomes

## Sugarscape Model – Core Concepts

- Grid of patches each holding a limited amount of “sugar” (resource)
- Agents have fixed traits (vision range, metabolism, storage capacity) and variable traits (sugar holdings)
- Rules: move to richest visible patch, consume sugar, die if sugar = 0, reproduce when enough sugar
- Environment is a torus (donut) – edges wrap around

## Sugarscape Variations

### Immediate Grow‑Back (Model 1)

- Sugar regenerates instantly to max each tick
- Four emergent income “terraces” (few rich, many poor)

### Gradual Grow‑Back (Model 2)

- Sugar regrows slowly → agents must keep moving
- Higher evolutionary pressure: vision increases, metabolism decreases

### Wealth Distribution (Model 3)

- Tracks income inequality via Lorenz curve & Gini coefficient
- Produces a Pareto‑type distribution (few very rich, many very poor)

### Inheritance (Model 4)

- When agents die, half their sugar passes to offspring
- Reduces evolutionary pressure; less fit agents survive longer

### Loans & Borrowers (Model 5)

- Fertile agents can borrow sugar; lenders earn interest after 10 ticks
- Creates social hierarchy: lenders → wealthy, borrowers → mid‑tier, non‑participants → lowest

### Pollution (Model 6)

- Sugar extraction generates pollution; agents avoid polluted patches
- Leads to dispersal, lower overall wealth, altered evolutionary trajectories

### Trade & Multi‑Resource (Models 7‑8)

- Introduce a second resource (spice) and a market mechanism
- Agents specialize or trade to satisfy both needs
- Price emerges from supply‑demand balance; trade reduces extreme specialization and improves survival

## Key Findings & Insights

- Simple local rules can generate complex macro‑patterns (segregation, income inequality, flocking)
- Non‑linear tipping points mean tiny policy tweaks can have huge effects
- Evolutionary pressure depends on environmental dynamics (instant vs. gradual resource renewal)
- Inheritance and credit systems markedly alter social stratification and evolutionary speed
- Pollution and resource scarcity dramatically reshape movement and wealth distribution

## Policy Implications (Student Take‑aways)

- Adjusting tolerance thresholds (e.g., housing integration policies) may prevent runaway segregation
- Redistributive mechanisms (e.g., inheritance tax, universal basic resources) can lower inequality but may affect incentives
- Credit markets can foster growth but also entrench hierarchies; design interest rates carefully
- Environmental regulations (pollution control) influence settlement patterns and economic outcomes
- Multi‑resource planning and trade facilitation can increase societal resilience to scarcity

---

*No specific action items were assigned to Pablo during the lecture.*
