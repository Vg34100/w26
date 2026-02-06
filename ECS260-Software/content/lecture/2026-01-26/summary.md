# ECS260-SE | W04-Mon | 2026-01-26

## Code Complexity Overview

- definition: how hard code is to understand, maintain, run
- important for new readers and even the original author later
- ties to understandability, maintainability, resource use, performance

## Metrics Discussed

- **Lines of Code (LOC)** – basic, first line of defense
- **Control‑flow graph components** – count edges, nodes, connected components
- **Average vs. max complexity** – look at both for a fuller picture
- **Halstead measures** – operators, operands, vocabulary, volume, difficulty
- **Psychometric (cyclomatic) complexity** – paths through code, often correlated with LOC
- **Other research metrics** – many exist, but few add clear value

## Control‑Flow Graph & Connected Components

- nodes = functions/procedures, edges = calls or argument passing
- must pick a start (main) to count components correctly
- number of components = how many isolated sub‑graphs exist
- complexity can be taken as max component size or average across components

## Implications of Complexity

- higher complexity → lower understandability, higher maintenance cost
- may increase runtime, memory, or bug risk
- not all code can be simple; some algorithms need inherent complexity
- over‑simplifying can hurt competitiveness or functionality

## Language & Vocabulary Analogy

- code “vocabulary” = distinct operators & operands
- **Volume** = total operators + operands → capacity to express ideas
- **Difficulty** = ratio of distinct to total elements → maintenance effort
- richer vocabulary gives more expressive power but costs learning energy
- relationship between vocabulary growth and code size is nonlinear

## Social & Technical Network Analysis

- treat developers, files, bugs, reviews as nodes in a sociotechnical graph
- metrics like centrality reveal key contributors or problematic areas
- social network patterns (cliques, edge strength) can guide bug‑fix priorities
- tools exist to combine code metrics with social data for project health checks

## Takeaways

- multiple complexity metrics exist; many correlate strongly with LOC
- choose metrics that align with the specific behavior you want to monitor
- consider both technical code structure and the social context of development
- use network‑based tools to get a holistic view of project sustainability and risk.
