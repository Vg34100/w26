# ECS220-THEORY | W06-Thu | 2026-02-12

## Stage Structure and Switching Conditions

- Search proceeds without resetting; each new string follows the previous one.
- Stage 0 A defines decisions on strings; Stage 0 B continues from the next string after the switch point.
- For strings in Stage 0 B set a(x)=false; switch when **q₀(x)** fails to reduce **Clique** to **a**.
- Reduction definition: if **q₀(x)=Clique(x)** for all x, then **q₀** reduces Clique to a.
- Subtlety: the intermediate value **y = q₀(x)** may appear before or after x in the ordering.
- Switching occurs as soon as an x is found where **q₀** does **not** reduce Clique to a.

## Polynomial‑Time Program Enumeration Challenges

- Need to ensure **A ⊆ B** (A‑stage strings are also in B‑stage).
- Enumerating all polynomial‑time programs isn’t trivial; can’t just filter all programs by runtime.
- Must guarantee each stage eventually ends—must find an x that triggers the switch.
- Rely on the hypothesis **P ≠ NP** to argue infinitely many suitable x exist.
- Without a guaranteed x, a stage could stall indefinitely.

## Self‑Clocked Program Construction

- Attach a header with constants **c** and **k** to any program (e.g., GCD).
- Header defines a global step counter; aborts if steps exceed **c·nᵏ**.
- In low‑level languages each instruction counts as one step; high‑level languages need careful mapping.
- Example: with **c=3**, **k=7**, the program runs under a **3·n⁷** time bound.
- The alarm never fires for genuinely polynomial‑time programs because the bound exceeds their actual runtime.

## Using Self‑Clocked Programs for Reductions

- Enumerate only programs that include the self‑clock header (“self‑alarm”).
- This syntactic filter is decidable and easy to check.
- For every problem in **P**, at least one self‑clocked program decides it; we only need one representative per language.
- Define **qᵢ** as the i‑th self‑clocked program; discard those that fail the alarm test.
- Combine **qᵢ** with a nondeterministic SAT solver to build the **a**‑program:
  - If input length parity is odd → output **false**.
  - If even → run the nondeterministic SAT decider.

## Mutual Recursion and Termination Arguments

- **a** calls **qᵢ**, and **qᵢ** may invoke **a** on smaller inputs; recursion depth shrinks with each step.
- Because the input size strictly decreases, infinite mutual recursion is impossible.
- Guarantees that each stage eventually finds an x where **qᵢ(x) ≠ a(x)** and switches.

## Conclusions and Upcoming Schedule

- Chapter 6 wraps up; next week Pablo will be absent (attending a workshop).
- Mina will cover part of the material; a student will lead another session.
- Reminder to watch the Veritasium video “The Whole Math” for additional insight.

## Reflections on P vs NP and Independent Statements

- Proving **P ≠ NP** may be impossible; could be an independent statement like those in set theory.
- Human intuition struggles with algorithms that have huge polynomial exponents (e.g., n¹⁰⁰).
- If **P = NP**, there would exist relatively small‑gate Boolean circuits for large‑n SAT instances.
- Mention of the classic **IP = PSPACE** proof idea (simulating circuits with polynomials).
- Historical note: unification of physical laws (Newton, Maxwell) parallels attempts to unify models of computation.
