# ECS251-OS | W04-Mon | 2026-01-26

## Scheduling and Ready List Design

- Single ready list shared by all cores
- Risk of scheduling same process on multiple CPUs
- Cache affinity issues when a process moves to a different core
- Potential priority queue to handle importance of tasks
- Per‑core ready lists can avoid lock contention and improve scalability

## Load Balancing Challenges

- Without a load balancer, some cores can become overloaded while others sit idle
- Balancing many processes across many cores is non‑trivial at microsecond scale
- Existing Linux scheduler balances at millisecond granularity, too coarse for our needs
- Need mechanisms to prevent “stacking” of processes on a single core

## Microsecond‑Scale Latency

- Nanosecond events (out‑of‑order exec, cache hits) are well hidden by hardware
- Millisecond events (disk I/O, network RTT) are hidden by OS scheduling
- Microsecond events (data‑center round‑trip, SSD/GPU transfers) are hard to mask
- Not enough independent instructions or hyper‑threads to hide these delays

## Hardware vs. Software Hiding of Delays

- Hardware excels at nanosecond‑level latency hiding (few extra instructions)
- OS can hide millisecond‑level latency via context switches and blocking I/O
- Microsecond‑level work requires both hardware tricks and smarter OS scheduling

## Compiler and CPU Reordering

- Compilers analyze data dependencies to safely reorder instructions
- CPUs can also perform dynamic reordering, looking ahead for independent ops
- Out‑of‑order execution helps hide latency when no data hazards exist

## Implications for Real‑Time Applications

- Tight response bounds (microseconds) demand careful OS scheduling and load balancing
- Packet processing must reach the application quickly; scheduling delays add overhead
- Designing per‑core ready queues and lightweight load balancers can improve latency
- Asynchronous programming models become harder to reason about at this scale
