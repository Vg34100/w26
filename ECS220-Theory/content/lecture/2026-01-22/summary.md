# ECS220-THEORY | W03-Thu | 2026-01-22

## Reductions and NP‑Completeness

- Reduction = polynomial‑time translation of one decision problem into another
- Show hardness by reducing a known NP‑complete problem to the new problem
- Common mistake: reduce new problem to known hard one (wrong direction)
- Transitivity: if A ≤ B and B ≤ C, then A ≤ C
- Reduction must not “solve” the original problem while translating

## NAE‑3SAT and Variants

- NAE = “Not All Equal”: each clause must have at least one true and one false literal
- NAE‑3SAT is symmetric in true/false, unlike ordinary SAT
- NAE‑3SAT ⇒ SAT, but SAT does **not** always imply NAE‑SAT
- Reduce ordinary 3‑SAT to NAE‑4SAT by adding a fresh variable to every clause
- Flip all bits of a NAE‑satisfying assignment → still NAE‑satisfying (useful for proofs)

## Reducing NAE‑3SAT to 3‑Coloring

- Use **choice gadgets**: a pair of nodes per variable plus a universal node
- Top node forced to one color (e.g., blue); its neighbors must pick the other two colors
- Assign green = true, orange = false (or vice‑versa) based on which node gets which color
- **Constraint gadgets** encode each clause (e.g., a triangle linked to the three literals)
- If a clause is NAE‑satisfied, the gadget can be colored consistently; otherwise it forces a conflict

## Independent Set Reduction

- Replace each original graph vertex with a triangle (complete subgraph of size 3)
- Connect triangles according to original edges using “dashed” edges between corresponding positions
- Independent set of size k (k = number of original vertices) ↔ pick exactly one node from each triangle, respecting adjacency constraints
- Forward direction: a proper 3‑coloring yields such an independent set
- Reverse direction: an independent set of size k yields a valid 3‑coloring of the original graph

## Tiling Problems and NP

- Tiles = polyominoes (connected unit squares); region = larger shape to cover
- Decision: can the region be tiled without overlap, using rotations, from a given tile set?
- Parity argument: dominoes cover two squares → region must have even number of squares
- Checkerboard coloring trick shows some even‑sized regions still impossible to tile
- NP‑verification: given a placement list, check overlap, bounds, and coverage in polynomial time

## Circuits vs. Formulas

- **Circuit**: DAG with arbitrary fan‑out; gates can feed multiple downstream gates
- **Formula**: tree (or DAG with fan‑out 1); each sub‑formula used at most once
- Circuits can reuse sub‑computations → potentially more succinct than formulas
- SAT for circuits: existence of an input making the output true; same for formulas but with structural restrictions

## Planar Circuit Gadgets for Tiling Reduction

- Encode wires, inputs, and gates as geometric tile patterns (gadgets)
- **Choice gadget**: two possible tilings represent true/false for an input variable
- **Wire gadget**: forces consistent propagation of truth value along a path
- **Gate gadgets** (e.g., NAND, NOT) built from tile arrangements that only tile correctly when logical constraints are satisfied
- Non‑planar circuits can be made planar by replacing crossings with a small “swap” gadget (XOR‑style construction)
- Overall reduction: circuit is satisfiable ⇔ corresponding tiled region can be fully covered.
