# ECS251-OS | W03-Wed | 2026-01-21

## Action Items

- Review the scheduling papers that will be assigned in the next week‑or‑two
- Compare thread creation overhead with full process creation in Linux
- Look up definitions of “service level objectives” and “service level agreements” for data‑center context

## Overview of Scheduling Concepts

- Scheduler decides which process gets CPU time
- Goal: share limited resources (CPU, I/O, network) efficiently
- Needs knowledge of future resource needs (duration, I/O bursts)
- Balances multiple performance metrics (throughput, latency, fairness)

## Process States and Context Switching

- Three main states: **running**, **ready**, **blocked**
- **Running** – currently executing on the CPU
- **Ready** – can run but not selected yet
- **Blocked** – waiting for I/O or a lock
- Context switch saves all registers, program counter, open‑file info, then restores the next process’s state

## Scheduling Goals and Policies

- **Fairness** – avoid starvation; every process eventually runs
- **Real‑time responsiveness** – user‑interactive apps need short wait times
- **Priority handling** – high‑priority tasks should pre‑empt lower ones
- **Resource utilization** – keep CPU busy while I/O waits are minimized

## Priority and Starvation

- Example: low‑priority process L holds a lock needed by high‑priority H
- H can be blocked waiting for L, causing priority inversion
- Scheduler may need to boost L’s priority or pre‑empt it to release the lock
- Preventing indefinite blocking is a key design target

## Real‑Time and I/O Considerations

- I/O operations can be much slower than CPU instructions
- Processes performing long I/O should be moved to **blocked** state to free CPU
- Scheduler must predict I/O bursts to avoid wasting CPU cycles on waiting tasks

## Race Conditions and Locks

- Multiple threads updating the same data can cause inconsistent results
- Typical pattern: read‑modify‑write on a shared counter
- Use mutexes (locks) to ensure only one thread accesses critical section at a time
- Locks introduce scheduling challenges because a blocked thread holds a resource

## Threads vs. Processes

- Threads share the same address space; only execution context (registers, stack) switches
- Processes have separate address spaces; switching requires updating page tables, heavier overhead
- Thread creation is lightweight compared to full process creation
- Threads are useful for fine‑grained parallelism within a single application

## Scheduler Complexity and Challenges

- Scheduler often can’t see inside user‑level locks, leading to hidden contention
- Blocking on a lock may keep a thread in **ready** state but unable to make progress
- Balancing fairness, priority, and real‑time needs requires sophisticated policies
- Mis‑scheduling can cause “lock convoy” where many threads wait on a single blocked thread.
