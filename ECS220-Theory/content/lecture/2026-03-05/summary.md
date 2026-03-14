# ECS220-THEORY | W09-Thu | 2026-03-05

## Reachability & NL‑Completeness

- Reachability is NL‑complete, central to space‑bounded computation
- Configuration graph of a nondeterministic machine captures acceptance
- Nodes = configurations using ≤ s(n) space; edges = one‑step transitions
- Accepting iff start configuration reaches unique accepting configuration

## Verifier Characterization of Nondeterministic Space

- Nondeterministic space = existence of a verifier V(x,w)
- V reads original input x (read‑only) and a witness w (unbounded length)
- Space bound depends only on |x|, not on |w|
- w must be accessed sequentially, each bit read at most once

## Witness Access Restrictions

- Prevents V from rereading bits of w, which would require storing them
- Without the restriction, simulating V nondeterministically would need extra space
- Sequential, single‑pass access lets the nondeterministic machine guess bits on‑the‑fly

## 3‑SAT Verifier Sketch

- Input: 3‑CNF formula φ, assignment w
- For each clause (a ∨ b ∨ c): read literals a,b,c, fetch their values from w
- If all three literals false → reject; otherwise continue
- Accept if every clause satisfied

## Space Usage of the Verifier

- Needs only constant number of indices into w (three per clause)
- Stores current clause pointer and a few Boolean flags → O(log n) bits total
- All other data (φ, w) are read‑only, no extra workspace

## Savitch’s Recursive Reachability Algorithm

- Define s →ₖ t: path of length ≤ k exists
- Recurrence: s →ₖ t iff ∃ u (s →ₖ⁄₂ u ∧ u →ₖ⁄₂ t)
- Base case k = 1: direct edge or s = t
- Recursively search middle node u over all graph vertices

## Space Analysis of the Recursive Algorithm

- Each recursion level stores s, t, u, k → O(log n) bits each
- Recursion depth = log₂ n (k halved each call)
- Total space = O(log n · log n) = O(log² n)
- No need to keep both recursive calls simultaneously → stack‑only usage

## Consequences for Space Complexity

- Savitch’s theorem: NSPACE(s) ⊆ DSPACE(s²) for s ≥ log n
- Implies PSPACE = NPSPACE (polynomial‑space nondeterminism collapses)
- NL ⊆ DSPACE(log² n) via reachability algorithm

## Quantifier Formulas & QBF

- Reachability can be expressed with alternating ∃/∀ quantifiers over intermediate nodes
- Naïve encoding yields formula size proportional to graph size (too large)
- Goal: keep formula size polylogarithmic in input, suitable for exponentially large graphs

## Reducing Space‑Bounded Computation to QBF

- Build configuration graph G of a space‑s machine on input x
- Encode “∃ w ∀ … ∃ …” quantifier pattern to assert a path from start to accept node
- Adjust formula so each quantifier alternates on individual bits (add dummy variables if needed)
- Ensure invalid bit strings make the formula trivially true, preserving correctness

## Interactive Proofs & IP = PSPACE

- IP: verifier runs in polynomial space, can use randomness, bounded error
- Even with only polynomial‑time verifier plus randomness, IP = PSPACE
- Shows that allowing a small amount of randomness does not increase power beyond PSPACE

## Miscellaneous Observations

- Sublinear‑space algorithms require read‑only input; linear‑space can treat input as writable
- Games (e.g., geography) correspond to quantified formulas; prover vs. skeptic analogy
- Alternating quantifiers model winning strategies in two‑player games
- Polynomial hierarchy defined via bounded alternations of ∃/∀ with polynomial‑size witnesses

---
