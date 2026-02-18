# ECS220-THEORY | W07-Tue | 2026-02-17

## Action Items

- Draft email to professor introducing yourself (start with “Hi, this is Pablo…”)
- Review proof of the halting problem using diagonalization; write a concise summary
- Practice constructing reductions from the halting problem to other undecidable problems (e.g., the “empty input” problem)
- Re‑read notes on cardinalities of sets, especially the proof that 𝒫(N) is uncountable
- Prepare a short explanation of consistency vs. completeness for the next class discussion

## Undecidability & the Halting Problem

- Turing showed the halting problem is undecidable – no program can decide for every other program whether it halts
- Universal program (interpreter) takes two inputs: description of a program and its input, then runs it
- Diagonalization argument: assume a halting decider exists, construct a program that contradicts its own output
- Result: there must be programs that never halt on themselves, proving the impossibility of a universal halting checker

## Diagonalization & Power Sets

- Comparing sizes of infinite sets: finite sets are easy, infinite sets need functions to compare cardinalities
- Mapping natural numbers N to subsets of N (𝒫(N)) via binary representation of characteristic functions
- Cantor’s diagonal argument shows no surjection from N to 𝒫(N); thus 𝒫(N) has strictly larger cardinality (uncountable)
- Extension: 𝒫(𝒫(N)) is even larger; each power‑set step jumps to a higher infinity

## Reductions & Other Undecidable Problems

- To prove a new problem undecidable, reduce the known halting problem to it
- Example reduction: given ⟨p, x⟩ for the halting problem, build a program q that ignores its own input, runs p on x, and outputs a fixed value (e.g., 42) if p halts
- If q halts, we infer p halts; if q loops, p loops – establishing equivalence
- Similar reductions apply to “empty‑input” halting, “does program output 42?” and other decision problems

## Formal Systems: Consistency & Completeness

- Formal system = finite set of axioms + inference rules; aims to capture mathematics rigorously
- **Consistency**: cannot derive both a statement t and its negation ¬t
- **Completeness**: for every statement t, either t or ¬t is derivable
- Combining both would make every statement decidable, which Gödel’s incompleteness theorems show is impossible for sufficiently rich systems

## Personal & Administrative Notes

- Pablo was up late (midnight‑3 am) and feeling exhausted; plans to grab a snack before the next meeting
- Needs to finalize email to professors; reminder to keep tone polite and concise
- Quick mental check: “quick” note that the lecture material is dense; schedule a short review session later today.
