# CMN SESSION 3 - Social Network Analysis

## Homophily

- “Birds of a feather flock together” – core definition
- People tend to connect with similar others (attributes, behaviors)
- Can arise from choice (homophily) vs. shared context (environment)
- Influences spread of obesity, smoking, happiness, generosity, voting

## Prof. Fowler Studies

- Stronger friendships → stronger influence; mutual ties strongest
- Photo‑tagging identifies real‑world friends on Facebook (reduces connections)
- 2010 election experiment: \~1 in 5 Americans (61 M) exposed to voting message
- Direct effect modest; indirect effect (friends of friends) drove \~240 K extra votes
- Obesity, smoking, drinking, happiness clusters extend up to 3 degrees of separation
- Context (e.g., nearby gym) can create spurious apparent influence

## Network Elements: Nodes & Links

- **Nodes**: people, organizations, products, countries, skills, tasks, etc.
- **Links**: communication, co‑occurrence, visual contact, joint use, temporal flow
- Directed links = one‑way (e.g., tweet, advice request)
- Undirected links = mutual (e.g., friendship, playing tennis together)

## Types of Networks

- **Multimode / Multimodal** – different node types (people, skills, tasks)
- **Multiplex** – same nodes, multiple link types (advice vs. trust)
- **Adjacency matrix** – binary 0/1 representation of ties
- **Edge list** – source‑target rows for software import

## Centrality Measures

- **Degree** – total connections (in‑degree + out‑degree for directed)
- **Closeness** – inverse of sum of shortest‑path distances to all others
- **Betweenness** – count of shortest paths passing through a node (bridge)
- **Eigenvector** – ties to well‑connected nodes; basis of PageRank
- **PageRank** – importance weighted by links from other important pages

## Community Detection & Modularity

- **Modularity** – ratio of internal vs. external link density; higher = better partition
- **Girvan‑Newman** algorithm removes high‑betweenness links to reveal clusters
- Detected groups often correspond to real‑world divisions (e.g., world regions, political echo chambers)

## Network Metrics & Path Concepts

- **Geodesic** – shortest path between two nodes (e.g., 2 → 6 via 2‑3‑5‑6)
- **Average path length** – minimum possible is 1 (complete graph)
- Star hub structure yields average path ≈ 2 with few links
- **Walk vs. Path** – walk may revisit nodes; path visits each node once
- **Clustering coefficient** – proportion of closed triangles among connected triples
- **Triad census** – counts of 16 possible directed three‑node motifs

## Visualization & Representation

- Layout algorithms (e.g., Yifan Hu) dramatically change visual appearance
- Same network can look like a “spaghetti” or a clear hub‑spoke diagram
- Color, shape, and size encode node attributes (race, country, role)

## Software Workflow (Gephi)

- Prepare data as CSV edge list with columns **Source**, **Target**, **Weight**
- Import into Gephi → Data Laboratory → verify nodes/edges
- Choose layout, run statistics (degree, modularity, PageRank, eigenvector)
- Inspect clusters, identify bridge nodes, explore link strengths (weak vs. strong ties)

## Additional Examples & Applications

- Granovetter’s “strength of weak ties”: weak connections bridge disparate groups, aid job finding
- Generosity experiment: each extra dollar given spurs $3 extra network‑wide giving
- Microfinance diffusion: eigenvector centrality better predictor of adoption than degree
- Voting message experiment: indirect influence far outweighs direct effect
- Structural holes: brokers between otherwise disconnected groups, crucial for information flow

---

**Action Items**

- When drawing your own network, decide on node definition, tie direction, and strength; consider using photo‑tagging data to identify real‑world friends if analyzing online platforms.
- Use Gephi (or similar) to import your edge list, apply a layout, and compute centrality and modularity to uncover key actors and community structure.
