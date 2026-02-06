# ECS251-OS | W02-Fri | 2026-01-16

## Key Points on Demikernel and Kernel Bypass

- Common datapath API gives a unified abstraction across NICs, RDMA, DPDK, etc.
- POSIX too generic – blocking semantics and synchronization don’t map to zero‑copy, async paths.
- Demikernel limits: weak multiprogramming/preemption, harder legacy integration, per‑hardware porting effort, may hide device‑specific tweaks.
- Single‑threaded run‑to‑completion simplifies reasoning, cuts sync overhead, but caps scalability and can cause latency spikes under load.
- Bypassing storage is tougher than networking: strict ordering, persistence, consistency, and complex command semantics needed.

## Lecture Highlights: Data‑Center Overheads & Demikernel Design

- Typical apps spend \~75 % of CPU cycles in kernel overhead, only \~25 % in actual logic.
- Kernel bypass pushes OS protection to the hardware (e.g., SR‑IOV), letting apps talk directly to devices.
- Existing bypass solutions are ad‑hoc per device; Demikernel aims for a portable, general‑purpose library OS.
- Architecture: one lightweight libOS per device type, all exposing a uniform high‑performance datapath API (PDFS).
- PDFS replaces sockets with queue descriptors (QDs), is inherently asynchronous, and supports zero‑copy DMA buffers.
- Scheduling is cooperative via ultra‑lightweight coroutines; no kernel scheduler, keeping cache locality.
- Single‑threaded model preserves cache affinity between I/O processing and application code, reducing overhead.

## PDFS API & Memory Model

- QDs act like Go channels: push data into a queue, pop it out on the other side.
- wait combines readiness detection and data retrieval, avoiding extra system calls.
- Zero‑copy I/O enabled by DMA‑capable memory allocation; buffers have reference counts to prevent premature free.
- Memory registration (e.g., for RDMA) handled transparently by the libOS.

## Performance Results & Practical Experience

- Re‑implemented a Redis‑style key‑value store using Demikernel libOS; latency dropped from \~30 µs to single‑digit µs.
- Echo‑server benchmarks show Demikernel matching or beating custom kernel‑bypass stacks (e.g., PRPC, Angora).
- Cooperative scheduling and cache‑friendly single thread contribute most of the latency gain.

## Limitations & Open Questions

- Single‑threaded nature restricts multi‑application or multi‑core scaling; adding threads would require careful state sharing.
- Memory protection overhead (reference counting, DMA registration) kept minimal to meet microsecond targets.
- Need to explore combining multiple libOSes (network + storage) while preserving the uniform PDFS interface.
- Questions remain about handling out‑of‑order packets, retransmission, and higher‑level reliability in the bypass path.
