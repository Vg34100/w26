# ECS51-OS | W10-Fri | 2026-03-13

## Action Items

- Review professor’s question list before next lecture
- Prepare concise answer comparing thread‑pool, work‑stealing, and virtual‑thread performance
- Update slide deck with key latency and throughput numbers
- Verify repository URL and ensure all CSV results are accessible

## Overview

- Goal: compare three JVM concurrency models (fixed thread pool, work‑stealing, virtual threads)
- Workloads: CPU‑heavy, simulated IO, real file IO, mixed (sleep + CPU)
- Metrics: total time, average latency, p95/p99 tail latency, CPU utilization
- Same tasks run on each model → differences reflect scheduling only

## Design & Implementation

- Benchmark framework in Java 21, public repo https://github.com/Vg34100/ecs251-project
- Two core interfaces: ConcurrencyModel (runAll) and TaskFactoryWorkload (task generation)
- Runner wraps each task with nanosecond timer, warm‑up pass, three recorded trials, CSV output
- CPU utilization sampled every 50 ms by a daemon thread

## Concurrency Models

- **Fixed Thread Pool**: OS threads = logical cores, tasks submitted as futures
- **Work‑Stealing**: Java ForkJoinPool async mode (FIFO) with same parallelism as pool
- **Virtual Threads**: Java 21 Loom, one lightweight thread per task, unmounts on blocking

## CPU‑Heavy Workload Results

- All three models show near‑identical throughput on compute‑bound tasks
- Avg time for 50 k tasks ≈ 0.87 s across models; CPU load 0.87–0.97
- Fixed pool, work‑stealing, and virtual threads differ by only a few milliseconds
- Tail latency (p99) similar; slight jitter for work‑stealing on small task counts

## IO‑Heavy (Simulated) Results

- Virtual threads finish 50–200 tasks in \~0.015 s, far faster than pool models (\~0.2 s)
- Avg latency \~13–15 µs for virtual threads vs \~15–16 µs for pools; p95/p99 higher for pools
- CPU utilization near zero for pools (threads blocked), negligible for virtual threads
- Demonstrates effective overlap of blocking sleeps via carrier‑thread release

## Mixed Workload Results

- Mix = 5 ms sleep + CPU loop; virtual threads still achieve \~0.014 s total time
- Fixed pool & work‑stealing take \~0.045–0.16 s depending on task count
- Virtual threads’ wall‑clock advantage ≈ 3–10× despite added CPU work after sleep

## Real File IO Experiments

- Variables: file size (64 KB → 4 MB) and concurrency level (1, 2, 4, 8)
- Throughput peaks at moderate concurrency (4) then plateaus or drops at 8
- Larger files → lower throughput, higher average latency across all models
- Virtual threads excel at small I/O & low concurrency but lag at 4 MB × 8 (≈ 3× higher latency)
- No single model dominates; selection depends on I/O size and desired concurrency

## Discussion & Takeaways

- **CPU‑bound**: any parallel model works; scheduling overhead dominates, cores are the bottleneck
- **Blocking‑heavy**: virtual threads give dramatic wall‑clock speedups by freeing OS threads
- **Real I/O**: system limits (disk bandwidth, contention) cap benefits; higher concurrency yields diminishing returns
- Model choice should match workload profile (compute vs blocking) and hardware constraints

## Presentation Highlights (Audio Transcript)

- Team intro: Pablo, Jasmine, Manami – project compares JVM concurrency models
- Motivation: need a systematic, reproducible benchmark across diverse workloads
- Framework: two interfaces decouple scheduling from task definition, enabling fair swaps
- Model descriptions repeated: fixed pool, work‑stealing, virtual threads (Loom)
- Measurement approach: per‑task timing, warm‑up, three trials, CSV export
- CPU results: models virtually identical, cores fully utilized (≈ 0.9 CPU load)
- IO results: virtual threads finish all tasks in time of a single sleep; pools waste OS threads while blocked
- Mixed workload: virtual threads still fastest despite added computation after sleep
- File‑IO findings: throughput improves up to 4 concurrent tasks, then stalls; larger files increase latency; virtual threads not always best for heavy disk I/O
- Conclusions: no universal winner; pick based on workload characteristics and hardware limits
- Closing remarks: Java chosen for simplicity; future work could explore other languages or real network I/O

## Conclusion

- Systematic benchmark shows virtual threads excel for IO‑heavy and mixed workloads, while all models perform similarly on pure CPU work
- Real‑world performance hinges on I/O size, concurrency level, and underlying hardware
- Recommendation: use thread pools for compute‑intensive code, virtual threads for blocking‑heavy services, and evaluate file‑IO patterns before committing to a model.
