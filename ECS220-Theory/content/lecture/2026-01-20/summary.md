# ECS220-THEORY | W03-Tue | 2026-01-20

## Complexity Classes and Verification

- VP (Verifiable‑tolerable) = class of problems with quick verification
- NP defined via polynomial‑time verifier that checks a witness
- Verifier view ↔ nondeterministic machine view; both interchangeable
- co‑NP = complements of NP languages; P = its own complement
- Belief: P ≠ NP and NP ≠ co‑NP, but no proof yet

## Hamiltonian Path and Proof Asymmetry

- No short certificate known for “graph has **no** Hamiltonian path”
- Existence of a Hamiltonian path gives a simple witness (the path)
- Negation requires proving non‑existence, which seems harder

## Diophantine Equations and Undecidability

- Question: does a multivariate polynomial have an integer solution?
- Hilbert conjectured decidable; proved undecidable (Matiyasevich, 1970)
- Looks like NP (existence of integer witness) but witnesses can be huge

## Independent Set and NP vs coNP

- Decision: “graph has independent set of size k?” → NP
- Complement: “no independent set of size k+1?” → co‑NP
- Conjunction of both (exact size k) not obviously in NP or co‑NP

## Circuit Minimization Problem

- Input: Boolean circuit C, ask if a smaller equivalent circuit exists
- Witness = smaller circuit (size bounded linearly) → NP‑like
- Verifying equivalence needs checking exponentially many inputs → not known poly‑time

## Integer Programming and Bounded Solutions

- Linear inequalities → solvable in poly‑time (Gaussian elimination)
- Adding integrality constraint → solutions, if they exist, can be bounded by exponential in input size
- Proven that integer solutions need only be at most exponential size

## Non‑deterministic Computation Model

- Nondeterministic program = tree of configurations, branches at “guess” steps
- Accept if **any** leaf accepts; reject if **all** reject
- Equivalent to NP verifier: guess witness, then run deterministic check

## Many‑one Reductions and NP‑Hardness

- Polynomial‑time computable function f maps instance x of A to instance f(x) of B
- A ≤ₘ B if x∈A ⇔ f(x)∈B; used to define NP‑hardness
- Reduction must be single‑call, output fed directly to B’s decision procedure

## Witness‑Existence Problem (MP Complete)

- Input: program p, string x, unary integer t
- Question: ∃ w, |w|≤t, such that p(x,w) halts with “yes” within t steps?
- Serves as artificial MP‑complete problem; witnesses bounded by t, time bound also t

## Unary vs Binary Encoding of Time Bound

- t in **unary** ⇒ length of input includes t copies of “1” → guessing w and running p are linear in input size → stays in NP
- t in **binary** ⇒ input length ≈ log t; guessing w may require exponential time → problem leaves NP (becomes NX‑complete)

## Machine Learning, Synthetic Data, and MP Problems

- LLMs can generate candidate solutions (e.g., theorem proofs)
- Deterministic verifier filters correct solutions → creates high‑quality training data
- MP problems (NP with verifiable “yes” answers) are prime targets for this loop

## Open Questions: P vs NP, NP vs coNP

- If NP = co‑NP, every “no” answer would have short proofs → collapses asymmetry
- P = NP would make all NP‑complete problems polynomially solvable
- These are major unsolved hypotheses since the 1970s; no proof either way yet.
