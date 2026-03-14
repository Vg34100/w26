# ECS251-OS | W08-Fri | 2026-02-27

## Action Items

- Explore static analysis / race‑detector tools for Java/C++
- Review current codebase for missing lock protection on shared variables (e.g., x)
- Add missing locks around all accesses to shared state in multithreaded sections
- Practice writing small programs that use both locks and non‑blocking primitives
- Read up on bounded‑waiting algorithms (e.g., ticket lock, bakery algorithm)

## Key Concepts

- **Race condition**: two threads read same value, both write back, final result nondeterministic
- **Critical section**: code region where only one thread may execute at a time
- **Lock (mutex)**: simple way to enforce exclusive access to a critical section
- **Non‑blocking synchronization**: atomic operations, lock‑free data structures, harder to implement
- **Safety property**: at most one thread in critical section simultaneously

## Race Condition Example

- Counter initialized to 0, two threads each read‑increment‑write
- Possible final values: 0, 1, or 2 depending on interleaving
- Without synchronization, both threads may write back 1 → lost update
- Adding locks forces both threads to see updates, final value becomes 2

## Locks & Synchronization

- Use lock() before accessing shared state, unlock() after
- Locks guarantee safety but may hurt progress if not managed well
- Non‑blocking approaches rely on atomic CPU instructions (e.g., compare_and_swap)
- Implementing lock‑free structures (lists, queues) is research‑intensive

## Correctness & Progress Properties

- **Safety**: only one thread in critical section at a time
- **Liveness (progress)**: some thread waiting will eventually enter critical section
- **Bounded waiting**: limit on how many other threads can enter before a waiting thread
- Fairness not required; just guarantee eventual entry for at least one waiting thread

## Tooling Ideas

- Static analysis to flag unsynchronized accesses to shared variables
- Runtime detectors that monitor lock acquisition patterns and report potential races
- Prototype tool: list all variables, check each access for associated lock protection

## Additional Points

- Critical section broken into entry, execution, and exit phases
- Entry phase: acquire lock; exit phase: release lock
- Non‑blocking synchronization is powerful but complex; usually left for advanced courses
- Research area: designing correct lock‑free data structures and algorithms
- Final week of class will focus on lock‑based solutions rather than non‑blocking techniques
