# ECS220 Theory - 01/13 W2/T

## Edge‑Crossing Elimination & Planar Reduction

- Replace each crossing (two edges intersecting) with a larger subgraph that removes the crossing.
- Iterate over all crossings until the graph becomes planar.
- The replacement preserves three‑colorability of the original graph.
- Gadget forces the two new “prime” nodes to share the original node’s color.

## Forward Direction (Original → Planar)

- If the original graph is three‑colorable, the planar gadget can be colored consistently.
- Colors of original nodes are copied to their corresponding “prime” nodes.
- Internal gadget nodes become forced (e.g., a node adjacent to green and orange must be blue).

## Reverse Direction (Planar → Original)

- Need to show any three‑coloring of the planar gadget forces the original nodes to have the same colors.
- Case analysis:
  - **Case 1:** Original nodes a and b receive different colors → gadget forces a′, b′ to match them.
  - **Case 2:** a and b receive the same color → gadget still forces a′, b′ to share that color.
- Thus, a valid coloring of the planar graph implies a valid coloring of the original non‑planar graph.

## Reduction from 3‑Coloring to CNF‑SAT

- For each graph node u, introduce three Boolean variables: uᵣ, u𝓰, u𝚋 (one per color).
- Add clauses to enforce **exactly one** of the three is true:
  - At least one: (uᵣ ∨ u𝓰 ∨ u𝚋).
  - At most one: pairwise negations (¬uᵣ ∨ ¬u𝓰), (¬uᵣ ∨ ¬u𝚋), (¬u𝓰 ∨ ¬u𝚋).
- For each edge (u, v), add clauses preventing same‑color assignments:
  - (¬uᵣ ∨ ¬vᵣ), (¬u𝓰 ∨ ¬v𝓰), (¬u𝚋 ∨ ¬v𝚋).
- Satisfiability of the resulting CNF ↔ existence of a proper 3‑coloring.

## Handling Clause Sizes in CNF Reductions

- **2‑literal clauses** are already in CNF; they correspond to simple implications (¬a → b, ¬b → a).
- **k‑literal clauses (k ≠ 3)** are transformed using auxiliary variables (z₁, z₂, …) to produce an equivalent set of 3‑literal clauses.
- The construction preserves satisfiability: the original clause is true iff the new 3‑CNF block is true.

## Implication Graphs & 2‑SAT Solving

- Build a directed graph with a node for each literal and its negation.
- Each clause (a ∨ b) yields edges (¬a → b) and (¬b → a).
- A formula is unsatisfiable iff some variable and its negation belong to the same strongly connected component (a contradictory loop).
- Reachability queries between x and ¬x for all variables decide satisfiability in linear time (BFS/DFS).

## Why 3‑SAT Remains Hard While 2‑SAT Is Easy

- 2‑SAT reduces to checking for contradictory loops in the implication graph → polynomial‑time.
- 3‑SAT requires gadgets that introduce clauses with three literals; the same graph‑reachability technique no longer suffices, preserving NP‑completeness.

## Miscellaneous Points

- Planar‑graph three‑coloring is a special case of the general three‑coloring problem.
- Polynomial‑time planarity testing exists, but the reduction assumes we can reject non‑planar inputs.
- The lecture emphasized case‑by‑case reasoning to enforce color equivalences in the gadget constructions.
