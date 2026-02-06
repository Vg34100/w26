# ECS220-THEORY | W05-Tue | 2026-02-03

## Quantifier Negation & De Morgan’s Laws

- Negating a ∀ becomes ∃ and vice‑versa
- Apply De Morgan when pushing negation through logical connectives
- Example: “not (∀ w P(w))” → “∃ w ¬P(w)”
- Useful for converting statements into prenex normal form

## Polynomial Hierarchy (PH) Basics

- Infinite sequence of classes Σ\_k^P and Π\_k^P for k ≥ 0
- PH = ⋃\_{k≥0} Σ\_k^P (also equals ⋃ Π\_k^P)
- Σ\_0^P = Π\_0^P = P (problems decidable in polynomial time)
- Σ\_1^P = NP, Π\_1^P = coNP; P ⊆ NP ∩ coNP

## Subset Relationships Between Levels

- Σ\_k^P ⊆ Σ\_{k+1}^P and Π\_k^P ⊆ Π\_{k+1}^P
- First‑level classes contain each other: NP and coNP both contain P
- Higher levels strictly contain lower ones (believed, not proved)

## Natural Problems Appear Low in the Hierarchy

- Most textbook problems sit in Σ\_1^P, Π\_1^P, or Σ\_2^P
- Occasionally a problem lands in Σ\_3^P (rare)
- No known natural problems beyond the third level

## What Happens If P = NP?

- If a single existential quantifier adds no power, then no extra quantifiers help either
- PH would collapse all the way down to P (i.e., PH = P)
- This is considered highly unlikely by complexity theorists

## Sketch of Collapse Proof (Assuming P = NP)

1. Take a language A ∈ Σ\_3^P: ∃w₁ ∀w₂ ∃w₃ B(x,w₁,w₂,w₃) with B poly‑time computable.
2. Use P = NP to replace the inner ∃w₃ B with a deterministic poly‑time predicate C₁(x,w₁,w₂).
3. Apply P = NP again to eliminate the universal ∀w₂, yielding C₂(x,w₁).
4. Finally eliminate the outer ∃w₁, obtaining a deterministic poly‑time decision for A.

- Same argument works for any Σ\_k^P, so PH collapses to P.

## General Collapse Condition

- If for some k, Σ\_k^P = Π\_k^P, then all higher levels equal Σ\_k^P (and Π\_k^P).
- Equality at level k forces equality at level k + 1, and so on upward.
- The “strongest” collapse is Σ\_0^P = Π\_0^P = P, which would collapse the entire PH.

## Example: NP = coNP Scenario

- Suppose every NP problem also has short certificates for “no” answers.
- This does **not** immediately give a polynomial‑time algorithm, but it forces PH to collapse to the first level (Σ\_1^P = Π\_1^P = NP = coNP).
- Many open problems (e.g., factoring) sit in NP ∩ coNP; proving NP = coNP would have huge consequences.

## Reduction Trick Using an Artificial Problem C

- Define C(x, 1ⁿ) to be the same decision as some NP problem, but with a huge unary second argument.
- Because P = NP, C is solvable in deterministic polynomial time (maybe O((n + k)^5)).
- Reduce a target problem A (input size n) to C by feeding x and a string of 2^{n³} ones as the second argument.
- The reduction runs in polynomial time relative to |x|, even though the second argument is exponential in n.
- This shows A is decidable (though not efficiently) and illustrates how P = NP lets us “pad” inputs to force deterministic algorithms.

## Key Takeaways

- Quantifier manipulation (De Morgan, moving negations) is essential for PH definitions.
- PH is built from alternating existential/universal quantifiers over poly‑time predicates.
- Collapsing any level (especially Σ\_k^P = Π\_k^P) would flatten the whole hierarchy.
- The widely believed conjecture: P ≠ NP ≠ coNP, so PH likely does **not** collapse.
- Understanding these hypothetical collapses helps gauge the strength of complexity assumptions.
