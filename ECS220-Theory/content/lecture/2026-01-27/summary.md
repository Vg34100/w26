# ECS220-THEORY | W04-Tue | 2026-01-27

## Action Items

- Complete the homework gadget: design a tile‑based crossing replacement for non‑planar circuits.
- Build a tromino‑based XOR gadget that fits the reduction framework.
- Finish the missing final layer of the circuit that checks the halting/accepting state in the Turing‑machine‑to‑circuit reduction.
- Verify that the constructed circuit uses only polynomially many gates relative to the Turing‑machine’s time (t).

## Tiling Problems Overview

- Lecture moved from Boolean‑circuit‑simulating tiling to simpler cases.
- 1×1 squares tile any region trivially.
- Dominoes (1×2) give an intermediate, polynomial‑time problem.
- Trominoes (L‑shaped 2×2 missing one cell) jump to NP‑complete territory.

## Domino Tiling is in P

- Model the region as a bipartite graph: black/white squares on a checkerboard.
- Each domino must cover one black and one white cell → perfect‑matching problem.
- Perfect matching in bipartite graphs solvable in polynomial time (e.g., Hopcroft–Karp).

## Why Tromino Tiling is NP‑Complete

- No bipartite structure: trominoes can cover three squares of mixed colors.
- Local placement constraints can encode logical gates (TRUE/FALSE).
- Reduction from Boolean‑circuit evaluation → NP‑complete.

## Homework Review (from lecture)

- Only two tile shapes used so far: 2×2 square and the L‑tromino.
- Region construction forces a tiling to correspond to evaluating a Boolean circuit gate‑by‑gate.
- True/false represented by two orientations of the tromino.
- Missing pieces in the lecture: **crossing gadget** and **XOR gadget** – both required for the assignment.

## Circuit Simulation of a Single‑Tape Turing Machine

- Goal: represent a TM configuration as a binary string.
- Encode: state (log |Q| bits), head position (sparse “one‑hot” encoding), tape symbols (2 bits per cell for a 4‑symbol alphabet).
- Sub‑circuit per tape cell: takes its own symbol bits, neighbor symbols, and a flag indicating whether the head is on/adjacent.
- Most sub‑circuits just copy their symbol; the three cells involved in the head move perform the transition logic.
- Use a multiplexer‑style wiring so only the relevant sub‑circuit updates the state bits.

## Witness‑Existence Problem (NP‑Complete)

- Instance: program (P), input string (x), time bound (t) (unary).
- Question: does there exist a witness (w) (≤ (t) bits) that makes (P) accept within (t) steps?
- Serves as a convenient NP‑complete problem for reductions to circuit‑SAT.

## Reducing Witness‑Existence to Circuit‑SAT

- Build a circuit (C\_{P,x,t}) that simulates (P) on input ((x,w)) for (t) steps.
- Hard‑code (x) into the circuit; treat (w) as the circuit’s external input.
- The circuit’s output is 1 iff the simulated TM halts in an accepting state.
- Polynomial‑size because the circuit mirrors the TM’s space‑time diagram (size ≈ (t^2)).

## From Circuits to 3‑CNF Formulas

- Direct conversion can cause exponential blow‑up due to fan‑out duplication.
- Each gate → three clauses encoding its truth table (using auxiliary variables for internal wires).
- Need extra variables for every internal wire; overall formula size stays polynomial.
- Converting the resulting formula to proper 3‑CNF may still be exponential; avoid full CNF conversion when possible.

## Common SAT Variants Mentioned

- **3‑SAT**: canonical NP‑complete problem; any circuit can be reduced to it.
- **1‑in‑3‑SAT**: exactly one true literal per clause; also NP‑complete.
- **#SAT**: counting satisfying assignments – #P‑complete.
- **Unique‑SAT (USAT)**: does a formula have exactly one satisfying assignment? – complete for the class UP.
- **Sharp‑SAT**: decide if the number of solutions exceeds a threshold – related to probabilistic classes.

## Reduction Strategy Tips (from the instructor)

- Pick a source problem that matches the target’s object type (graphs → graph problems, formulas → SAT variants).
- When direct reduction is hard, look for intermediate problems (e.g., 3‑SAT → 1‑in‑3‑SAT).
- Use gadget constructions to simulate missing operations (crossings, XOR, OR).
- Keep an eye on polynomial‑size constraints; avoid steps that cause exponential blow‑up.
