# ECS220-THEORY | W06-Tue | 2026-02-10

## Oracle Concepts & Simulation Arguments

- Oracle = hypothetical subroutine for solving a problem in one step
- Used to model “what if” an NP‑complete problem had an efficient algorithm
- Simulation arguments: if both machines get the same oracle, time‑hierarchy proofs still work
- Any instruction set that includes oracle calls preserves relative separations (e.g., TIME(t₁) ⊂ TIME(t₂))

## Time Hierarchy & Diagonalization

- Construct a problem that disagrees with every program running in time t
- Diagonalization shows a language solvable in t + ε but not in t alone
- Extends to show lower bounds for specific time classes (e.g., n², n³)
- Simple simulation arguments cannot separate P from NP or NP from co‑NP

## Relativization: P = NP with Oracle A

- Define problem **Predict** (program q, input x, step bound t)
- Query oracle A with (q, x, 2^{|x|^c}) written in binary (polynomial‑size)
- Any EXP‑time language reduces to **Predict**, so EXP ⊆ P^A
- Since NP^A ⊆ EXP, we get P^A = NP^A = EXP

## Relativization: Random Oracle B Separates P and NP

- Generate B by picking, for each length n, either zero or one random string of that length
- With probability 1, B is sparse enough that P^B ≠ NP^B
- NP^B contains language “∃ w ∈ B of length n” (guess w, query B) – easy in NP^B
- Any polynomial‑time machine with oracle B can query only polynomially many strings; probability it hits the unique string of length n → 0
- Union bound over countably many machines ⇒ probability that any P^B machine decides the language is 0

## Random Oracle Results & Implications

- Random oracle model: each string independently placed in the language with probability ½ (or the sparse version above)
- Shows that many statements (e.g., P ≠ NP) hold relative to a random oracle, but this does **not** prove the unrelativized statement
- Highlights need for non‑relativizing techniques (e.g., interactive proofs, circuit lower bounds)

## NP‑Intermediate Problems (Ladner’s Theorem)

- Assuming P ≠ NP, there exist languages in NP that are neither in P nor NP‑complete
- Construct language A using a slowly growing function f that toggles between SAT and the empty set based on input length parity
- When f(|x|) is even → A(x)=SAT(x); when odd → A(x)=false\
  - f computable in polynomial time, so A ∈ NP; but A cannot be NP‑complete (otherwise SAT would reduce to a trivial language)
- Also not in P because solving A requires solving SAT on infinitely many lengths

## Sketch of Ladner’s Construction

- Enumerate all polynomial‑time machines Q₀, Q₁,…
- Stage i searches for an input x where Q_i disagrees with the current definition of A and then flips the parity of f to force disagreement
- Guarantees each Q_i fails on some input, so no polynomial‑time algorithm decides A
- Because f grows slowly, the “SAT‑like” stretches are long enough to keep A outside P yet short enough to stay in NP

## Key Takeaways

- Oracle arguments illustrate why many classic proof techniques cannot resolve P vs NP.
- Random oracles give strong relative separations but do not settle the absolute question.
- Ladner’s theorem provides concrete examples of NP‑intermediate problems under the P ≠ NP assumption.
