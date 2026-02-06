# ECS220-THEORY | W04-Thu | 2026-01-29

## Action Items

- Review lecture slides on **graph cuts** to clarify min‑cut vs. max‑cut definitions.
- Work through the **extended Euclidean algorithm** example for solving (ax+by=c).
- Sketch the **gadget construction** used in the 3‑SAT → Max‑Cut reduction.
- Try the **integer partition → cosine‑integral reduction** on a small set of numbers.

## Graph Cuts & Decision Problems

- Cut = partition of nodes into two subsets; edges crossing the partition are the “cut”.
- Minimum‑size cut ↔ decision: “Is there a cut of weight ≤ k?”
- Maximum‑size cut ↔ decision: “Is there a cut of weight ≥ k?” (NP‑complete).
- Edge may be crossed an even number of times → not a true cut.
- Weighted graphs: sometimes assign weights to edges before optimizing.

## Reductions & Gadgets (3‑SAT → Max‑Cut)

- Variable gadget: pair of nodes representing true/false, linked by an edge.
- Clause gadget: triangle of three nodes, each connected to the appropriate variable nodes.
- Choice gadgets enforce opposite colors → truth assignment.
- Threshold (k) set just below the maximum possible crossing edges.
- Correct coloring yields at least (k) crossing edges; wrong coloring falls short.

## Optimization vs. Decision Perspective

- Optimization: “What is the maximum number of satisfiable clauses?”
- Decision version: “Can we satisfy ≥ k clauses?” (harder to solve).
- Negating weights does **not** turn max‑cut into min‑cut when negative weights are disallowed.
- Decision problems often reduce to optimization by comparing to known bounds.

## Integer Equations & Extended Euclidean Algorithm

- Linear Diophantine: find non‑negative integers (x,y) such that (ax+by=c).
- Solvable iff (\\gcd(a,b)) divides (c).
- Extended Euclidean algorithm produces one solution ((x_0,y_0)).
- General solution: (x = x_0 + (b/d)t,; y = y_0 - (a/d)t) for integer (t).

## Cosine Integral → Subset‑Sum Reduction

- Input: list of positive integers ({a_i}).
- Construct integral (\\int\_{-\\pi}^{\\pi} e^{i\\theta(\\sum\_{i\\in S} a_i - \\sum\_{i\\notin S} a_i)} d\\theta).
- Integral evaluates to (2\\pi) iff the exponent is zero → subset sums are equal.
- Hence deciding whether the integral is non‑zero is equivalent to the **partition problem** (NP‑complete).

## Cellular Automata Basics

- Elementary cellular automaton: 2 states, neighborhood of 3 cells → 256 possible rules.
- Rule 30 (Stephen Wolfram) cited as a classic example.
- Truth table lists 8 possible 3‑bit inputs → single output bit.
- Generalizations: more states, larger neighborhoods, higher dimensions.

## Tiling & NP‑Completeness (Tromino/Tiling Reduction)

- Tile a region with L‑shaped trominos (2×2 square missing one cell).
- Reduction from **3‑SAT**: each variable/ clause encoded as a placement constraint.
- Consistent tiling ↔ satisfying assignment.
- Demonstrates NP‑hardness of tiling problems.

## Circuit Minimization & Complexity Classes

- Problem: given circuit (C), does a smaller circuit (D) exist computing the same function?
- Formal statement uses quantifiers: (\\exists D; \\forall x; (C(x)=D(x))) with size((D) &lt;) size((C)).
- Relates to classes **NP**, **coNP**, **P**, and the notion of **NP‑completeness**.
- Highlights subtlety of “exists” vs. “for all” in defining decision problems.

## Miscellaneous Highlights

- Max‑cut is a classic example where decision and optimization differ sharply.
- Linear vs. quadratic Diophantine equations: quadratic version becomes NP‑hard.
- Integral of (e^{i\\theta}) over (\[-π,π\]) is zero unless the frequency is zero.
- “NP‑complete” problems often arise from simple, natural questions (e.g., tiling, partition).
