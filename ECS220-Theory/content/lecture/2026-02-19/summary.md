# ECS220-THEORY | W07-Thu | 2026-02-19

## Consistent Guessing Problem

- Need algorithm to decide behavior of program P on empty input
- Accept if P accepts, reject if P rejects; if P loops, any answer allowed but must halt
- Simple “run P on ε” fails because P may diverge → not a valid algorithm
- Problem is undecidable (uncomputable) – proved via diagonalization similar to Halting Problem
- Not reducible from Halting Problem → a Turing‑intermediate problem

## Turing‑Intermediate Problems

- Example: undecidable but not as hard as Halting Problem
- Related to Ladner’s theorem: if P ≠ NP, NP‑intermediate problems exist
- Consistent‑guessing problem feels more natural than earlier artificial examples

## Proof Sketch Using Consistency

- Assume formal system expressive enough to talk about programs; for any statement T, either T or ¬T is provable (but not both)
- Run two searches in parallel:
  1. Look for proof that P(ε) accepts (i.e., a computation trace)
  2. Look for proof that P(ε) rejects (or runs forever)
- Consistency guarantees only one of these proofs can exist; the algorithm halts with the correct answer
- If P loops, neither proof appears, but completeness gives a proof of the opposite statement, still yielding a decision

## Counter / Register Machines

- Simple computational model: finite‑state control + unbounded integer registers (bins of balls)
- Instructions: increment, decrement (with zero‑test and jump), and a “jump if zero” shorthand
- Example program: decrement R, increment S three times, repeat – demonstrates looping via zero‑test jumps

## Sample Register‑Machine Programs

- **Multiplication by 2**: loop decrementing A, incrementing B twice each iteration
- **Parity test**: uses zero‑test to accept if input is odd, reject if even
- **Copying registers**: repeatedly decrement B, increment C and D to add B into both registers, then restore B
- Notation: “while R ≠ 0 do …” as shorthand for zero‑test jump loops

## Universality of Counter Machines

- Three registers suffice to simulate any Turing machine (universal)
- Encoding tape: split into left and right halves stored in two registers; head position tracked by a third register
- Simulation requires maintaining a “1” sentinel at tape ends for easier encoding
- Shows that a minimal instruction set (inc/dec/zero‑test) is computationally powerful

## Primitive Recursive Functions

- Base functions: constant 0, successor (x ↦ x+1), projection (identity)
- Closed under composition and primitive recursion (define f by base case and recursive step using previously computed values)
- Examples: addition, multiplication, exponentiation built from these primitives

## Ackermann‑Like Fast‑Growing Functions

- Ackermann hierarchy:\
  - A₁ ≈ successor repeated y times (x + y)\
  - A₂ ≈ multiplication (x·y)\
  - A₃ ≈ exponentiation (xʸ)\
  - A₄ ≈ tetration, etc. – grows extremely fast
- Demonstrates functions beyond primitive recursion (cannot be bounded by any fixed Ackermann level)

## Non‑Primitive‑Recursive but Computable Functions

- Constructed function f(n) that outgrows every Ackermann level via diagonalization
- f is computable using an unbounded while‑loop (not primitive recursive)
- Shows primitive recursion is insufficient to capture all intuitively computable functions

## Historical Context & Computability Foundations

- Early attempts: define computable functions via primitive recursion → later found inadequate
- Hilbert‑Gödel era: goal of a complete, consistent formal system for reasoning about programs proved impossible (Gödel’s incompleteness)
- Counter machines provide a clean, low‑level model for proving universality and undecidability results

## Open Questions / Student Notes

- Inverse Ackermann function appears in data‑structure analysis – still unclear why it shows up
- Clarify base cases for Ackermann‑style definitions (e.g., handling y = 0)
- Explore encoding tricks for simulating multi‑register machines with fewer registers (e.g., prime‑factor encoding)
