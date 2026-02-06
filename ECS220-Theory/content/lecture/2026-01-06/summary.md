# ECS220 THEORY - Course Homework & Peer Review Guidelines

## Logistics & Homework

- Submit homework & create scope on Gradescope (nice UI)
- Post generic questions on Piazza, not on private channels
- Peer‑review assignments can be done in any group; groups may change each time
- TA Mina will manually set up group sign‑ups via email (UC Davis privacy rules)
- Late‑penalty: sliding scale from 0–48 hrs, still &gt; 99 % if ≤ 12 hrs late

## Peer Review Guidelines

- Review another group’s proof as if you were the grader
- Check: clear explanations, precise statements, no ambiguous language
- Look for intuition, not just dense symbolic steps
- Cite any external sources you use for help
- Avoid AI‑generated answers; use websites only as references

## Eulerian vs. Hamiltonian Cycles

- **Eulerian cycle**: visits every edge exactly once; exists iff every vertex has even degree (connected graph)
- Easy to test: count neighbors of each node (O(n²) with adjacency matrix)
- **Hamiltonian cycle**: visits every vertex exactly once; no simple degree test known
- Naïve algorithm: check all n! permutations → exponential time (≥ 2ⁿ)

## NP‑Completeness Overview

- Decision problems: yes/no answer (e.g., “does a Hamiltonian cycle exist?”)
- Search problems: produce an actual solution (e.g., output the cycle)
- Verification of a candidate solution is polynomial for NP problems (e.g., check a claimed Hamiltonian cycle)
- Many natural problems (graph coloring, SAT, factoring) are NP‑complete; a fast algorithm for any would solve them all

## Euclidean Algorithm Review

- Compute GCD(a, b): if a mod b = 0 → GCD = b; else recurse on (b, a mod b)
- Example: GCD(24, 18) → 6 after two modulus steps
- Runs in polynomial time relative to input bit‑length, unlike naïve linear search

## Runtime & Complexity Basics

- Running time = worst‑case number of elementary steps as a function of input size
- “Step” ≈ one basic operation (e.g., integer addition, comparison) in your programming language
- Encoding matters: binary length of numbers, adjacency matrix size (n²) for graphs
- Polynomial vs. exponential distinction is crucial; constant‑factor differences (n² vs. n³) are less important here

## Encoding & Input Size

- Graphs can be encoded as binary strings (adjacency matrix flattened)
- Input size = number of bits needed for the chosen encoding
- Different reasonable encodings are polynomially inter‑convertible, so algorithmic classification stays the same
- Integer inputs: size measured in bits (log N), not in unary length

## Steps & Algorithm Definition

- Formal algorithm = program in your favorite language (equivalent to a Turing machine)
- A step may be a single line of code, but high‑level constructs (list comprehensions, library calls) can hide many underlying operations
- For analysis, treat constant‑time operations as one step; be cautious with big‑integer arithmetic or long string processing
- Pseudocode and Python‑style notation are used for clarity in the course.
