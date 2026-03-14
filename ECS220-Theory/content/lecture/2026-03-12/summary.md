# ECS220-THEORY | W10-Thu | 2026-03-12

## Non‑deterministic Reachability Algorithm

- guess neighbor, jump to it
- stop after too many nodes visited
- if correct guesses lead to t → accept, else reject
- works when s can reach t in same component

## NL Closed Under Complement

- show non‑reachability ∈ co‑NL
- use NL algorithm for “no‑path” case
- enumerate reachable nodes, verify none is t
- requires counting reachable nodes without linear space

## Inductive Counting for Reachable Nodes

- compute r = # nodes reachable from s
- store only previous endpoint, enforce lexicographic increase
- guarantees distinct endpoints, uses O(log n) space
- sequence of guesses exists for correct ordering

## Non‑deterministic Computation of Functions

- subroutine returns optional integer (the correct r) or “unknown”
- at least one computation path must output the integer
- all paths that output an integer must agree on the value

## Space vs. Time Trade‑off (t ↔ √t)

- any problem computable in time t can be done in space √t (up to log factors)
- contrapositive: not in √t‑space ⇒ not in t‑time
- implies separation results for P vs PSPACE

## Oblivious Turing Machines and Simulation

- oblivious: head movements depend only on input length
- simulate each step with O(t) work → total O(t²) space
- partition tape and time into √t blocks to save space
- construct DAG of time‑blocks, edges encode recent tape‑block accesses

## Tree Evaluation Problem

- tree: internal nodes are gates, leaves are input bits/strings
- evaluate recursively: compute children values, apply node function
- generalizes Boolean formula evaluation (d‑ary, b‑bit strings)

## Space Complexity of Tree Evaluation

- recursion depth h, each level stores O(d·b) bits
- naive space O(h·d·b) → improved to O(h·log b)
- overall space O(log n·log log n) for input size n

## Key Results and Implications

- NL closed under complement → NL = co‑NL
- Inductive counting yields NL algorithm for non‑reachability
- Time‑space trade‑off supports progress toward P ≠ PSPACE
- Tree evaluation shows space‑efficient computation for complex functions
- Oblivious simulation bridges time and space bounds for Turing machines
