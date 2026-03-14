# ECS220-THEORY | W09-Tue | 2026-03-03

## Complexity Class Containments

- Time t ⊆ Space t (up to constants)
- Polynomial‑time ⊆ Polynomial‑space (P ⊆ PSPACE)
- Space s ⊆ Time 2^{O(s)} (exponential time bound)
- Logarithmic space ⊆ Polynomial time (L ⊆ P)
- Polynomial space ⊆ Exponential time (PSPACE ⊆ EXPTIME)

## Relating Time and Space

- Using at most s tape cells gives ≤ 2^{O(s)} possible configurations
- A computation that never repeats a configuration must halt within that many steps
- For s = log n, 2^{O(log n)} = poly(n) → L ⊆ P
- For s = poly(n), 2^{O(poly(n))} = exp(poly(n)) → PSPACE ⊆ EXPTIME

## Non‑deterministic Time vs Deterministic Space

- NTIME(t) ⊆ DTIME(2^{O(t)}) (e.g., NP ⊆ EXPTIME)
- Polynomial‑size witnesses can be enumerated in exponential time
- Verifier runs in polynomial time using the witness as read‑only input

## Verifier vs Non‑deterministic Characterizations

- Verifier view: input x + witness w, algorithm uses space s(|x|) (w can be huge)
- Space‑bounded verifier can read w sequentially, not randomly, to keep space low
- Non‑deterministic program view is simpler for space bounds; avoids tricky witness rules

## Reachability and NL‑Completeness

- Problem: given directed graph G and nodes s, t, is there a path s→t?
- Non‑deterministic log‑space algorithm: guess next neighbor, keep only current node and a step counter (≈ log n bits)
- Accept if a simple path (no repeats) reaches t within |V| steps
- Reachability ∈ NL and is NL‑complete under log‑space reductions

## Log‑Space Reductions

- Reduction must use O(log n) working memory; input is read‑only, output written sequentially
- Example: complementing edge set for Clique ↔ Independent Set uses only two pointers → log‑space
- Composing log‑space reductions requires recomputing intermediate outputs on‑the‑fly, not storing them

## Space Hierarchy Theorems (Brief)

- Strict hierarchies: L ⊂ NL ⊂ PSPACE ⊂ EXPSPACE, etc.
- More space ⇒ strictly more solvable problems (proved by diagonalization)

## Key Takeaways

- Time and space are tightly linked via configuration counts
- Non‑determinism changes acceptance asymmetry (one accepting path suffices)
- Reachability serves as a canonical NL‑complete problem, mirroring many space‑bounded computations
- Log‑space reductions preserve the low‑space nature of problems and are essential for NL‑completeness proofs.
