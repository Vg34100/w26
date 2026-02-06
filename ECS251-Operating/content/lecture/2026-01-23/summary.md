# ECS251-OS | W03-Fri | 2026-01-23

## Challenges in Designing Fast & Correct Thread Systems

- Coordination needed between user‑level and kernel schedulers
- Fast performance → minimal kernel traps; correctness → proper sync on block/preempt
- Multiprocessor safety: handling blocking, preemption, and processor allocation across CPUs
- Balancing low‑overhead switches with safe state transitions

## Kernel Threads vs. User‑Level Threads

- Kernel threads shine when blocking on I/O or needing true parallelism
- User‑level threads excel for compute‑bound work with ultra‑fast create/switch
- Kernel involvement adds latency; user‑level avoids kernel traps but lacks visibility
- Choice depends on workload I/O intensity vs. pure CPU computation

## Preventing Processor Hoarding by Misbehaving Applications

- System assumes cooperative return of idle processors
- Malicious/buggy apps could keep processors indefinitely
- Kernel can enforce fairness: preempt after time‑slices, priority checks, revocation policies
- Penalties or credit‑based allocation discourage resource hoarding

## Recursive Locking Issue with Processor‑Preempted Upcalls

- Upcall may interrupt scheduler while it holds locks → deadlock risk
- Solutions: defer upcall handling, use non‑blocking synchronization, run critical section briefly to release lock
- Kernel can detect if preempted thread is in a critical region and schedule it to finish

## Why N‑Body Benchmark Is Useful for Scheduler Evaluation

- Fine‑grained parallelism with many independent particle calculations
- Dynamic load imbalance forces frequent blocking/resume cycles
- Highlights scheduler’s ability to adapt processor allocation efficiently
- Provides clear performance scaling across added CPUs

## Scheduler Activations: Core Concepts & Rules

- Activation = execution context delivering kernel events to user scheduler
- Acts as vessel for user‑level threads, notifies on events, saves processor state on block
- Kernel never runs user threads directly; user decides next thread to run
- Communication includes adding/removing processors, locking/unlocking activations

## Processor Allocation Policies & Overhead Considerations

- Dynamic sharing: processors split evenly among active tasks
- Overhead sources: page sharing, time‑slicing, universal compatibility layer
- Policies aim for application autonomy while keeping kernel control minimal
- Zero‑overhead possession via code copying and activation reuse

## Handling Critical Sections & Deadlock Prevention

- If a thread holding a lock is preempted, others may spin‑wait
- Kernel checks if blocked inside critical section, runs it briefly to release lock
- Guarantees eventual lock release without sacrificing overall performance

## Implementation Highlights & Code Overhead

- Added \~1,200 lines to existing OS (e.g., native scheduler) to support activations
- Modified native OS priority handling and user‑level package for activation management
- Uses activation return to kernel when unused, optimizing resource use

## Performance Evaluation Findings (N‑Body Simulation)

- Kernel‑thread performance improves then plateaus as CPUs increase (overhead limits)
- New activation‑based threads keep processors busy via immediate notifications
- Demonstrated better scaling for fine‑grained parallel workloads compared to pure kernel threads

## Practical Concerns & Real‑World Adoption

- User‑level threads lack visibility into page faults, I/O blocks → correctness issues
- Many production systems favor kernel threads due to implementation complexity of activations
- Hybrid approaches aim to combine low‑overhead user scheduling with kernel safety

## Open Questions & Clarifications

- How to define and enforce “preemptive” behavior for user‑level threads in practice
- Strategies for penalizing or revoking resources from non‑cooperative applications
- Balancing credit‑based allocation vs. strict revocation policies for fairness
- Real‑world examples of systems successfully deploying scheduler activations beyond research prototypes.
