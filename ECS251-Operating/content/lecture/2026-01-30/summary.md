# ECS251-OS | W04-Fri | 2026-01-30

## Scheduling Challenges

- Per‑CPU schedulers lack global view → can’t share idle CPUs
- Tiny‑scale workloads suffer from frequent balance intervals (ms)
- Data‑plane offload bypasses OS but creates separate data paths per app
- Ideal scheduler: easy policy implementation, multi‑goal (latency + fairness), delegable decisions, modular CPU/NUMA support, non‑disruptive updates

## Introduction to Ghost (new Linux kernel scheduler)

- Runs scheduling policies in user‑space “agents” while kernel handles enforcement & context switches
- Provides fast, sensible scheduling with support for diverse performance goals
- Centralized “global agent” can schedule all CPUs for high‑scale workloads
- Supports multiple policies simultaneously on the same machine (partitioned or priority‑based)

## Architecture & Communication

- Kernel scheduling class ↔ user‑space agent via messages (event type, sequence #, data)
- Agents receive thread & CPU events, apply policy, send transaction back to kernel
- Transaction model: create → commit; atomic, rollback on state change
- Sequence numbers ensure agents act on up‑to‑date kernel state; stale transactions are rejected

## Centralized vs. Per‑CPU Models

- Centralized: single queue, one global agent, satellite agents stay idle → reduces coordination overhead
- Per‑CPU: each CPU has its own agent & queue → more parallelism but higher complexity
- Hybrid possible: mix layering, partition CPUs per policy

## Performance & Overhead

- Transaction creation + IPI ≈ 1 µs; total latency ≈ 2 µs per scheduling decision
- Overhead of first transaction \~19 ns, negligible compared to overall runtime
- Benchmarks show comparable or better performance vs. CFS despite extra indirection
- Fast policy updates: &lt; 1 s to load new agent code, no reboot, fallback to CFS if agent down

## Discussion Highlights

- Main overhead: central fast‑thread context switch & transaction processing (\~800 ns)
- Flexibility vs. correctness trade‑off: many custom policies increase complexity & maintenance burden
- Allowing user‑space policies can expose larger attack surface & make optimal universal design hard
- Ghost’s fallback to default scheduler ensures stability during agent failures

## Comparisons & Future Directions

- Ghost vs. traditional Linux scheduler: same kernel enforcement, user‑space policy layer adds flexibility
- Similarities to exokernel ideas: applications bypass kernel for scheduling, but still rely on kernel for safety checks
- Potential to extend Ghost concepts to other OSes or specialized hardware (e.g., exokernel‑style libraries)
- Adoption challenges: integration with existing OS infrastructure, developer learning curve, security considerations
