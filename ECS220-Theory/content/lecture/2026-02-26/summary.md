# ECS220-THEORY | W08-Thu | 2026-02-26

## Total vs. Partial Functions

- Total = defined on every input
- Partial = undefined on some inputs (non‑halting)
- Algorithms may compute partial functions when they can loop forever
- Goal: compute total functions for all inputs

## Bloop (Bounded Loop) Language

- Pseudo‑language where every program halts
- Intended to capture all total computable functions
- Ackermann function shows Bloop can’t express all total recursive functions
- No total language can compute every total recursive function

## Universal Function & Diagonalization

- Universal function U(p, x) simulates program p on input x
- If a language could compute U, we could build V(p) = U(p, p)+1 → contradiction
- Hence any total language lacks a universal interpreter for itself
- Shows impossibility of a fully total, yet universal, programming language

## Encoding Partial Recursive Functions

- Use prime factorization to encode functions as integers
- Base functions (zero, successor, projections) have unique encodings without 2, 3, 5 factors
- Composition encoded as 2^f · 3^g · 5^h, guaranteeing uniqueness
- Guarantees a one‑to‑one mapping between functions and natural numbers

## Lambda Calculus & Computability

- Church’s λ‑calculus equivalent to Turing machines & partial recursive functions
- Provides foundation for functional languages (Lisp, Haskell)
- Halting problem also unsolvable in λ‑calculus
- Early resistance due to intuition that λ‑definable = all computable functions

## Turing Machines and Universality

- Model of human “paper‑and‑pencil” computation
- Defined by finite set of states, tape symbols, and transition function δ
- Universal Turing machine can simulate any other Turing machine given its description
- Equivalence of Turing, λ‑calculus, and partial recursive models solidifies the Church‑Turing thesis

## Time vs. Space Complexity

- Time: number of steps; Space: number of tape cells visited (or memory used)
- Space can be reused; time cannot
- PSPACE = problems solvable with polynomial space
- NL ⊆ PSPACE; nondeterminism adds no power for space (Savitch’s theorem)

## Logarithmic Space (L) Example

- Palindrome check using two read‑only pointers (i, j)
- Only need O(log n) bits to store indices → L‑class algorithm
- Input is read‑only; only constant‑size work tape used

## Polynomial Space Example (PSPACE)

- Simulating cellular automaton configurations
- Number of possible configurations = 2^n → exponential time, polynomial space
- Detect periodic orbit by iterating up to 2^n steps, storing current configuration only

## Hypercomputation & Skepticism

- Claims of “beyond Turing” devices (e.g., neural nets encoding halting) usually hide the problem in the encoding
- Physical limits (e.g., second law of thermodynamics) parallel computability limits
- Caution advised when evaluating extraordinary computational claims
