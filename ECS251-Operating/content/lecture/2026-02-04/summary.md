# ECS251-OS | W05-Wed | 2026-02-04

## System Architecture

- Vertical memory system (VM) – each app gets its own OS “cards”
- Central domain shared, application domain isolated per app
- Goal: isolate CPU, memory, power resources per application

## Key Terminology

- **Stretch** – contiguous virtual‑address range with specific permissions
- **Contract** – exclusive reservation of resources for an app
- **Brainstack** – priority stack of frames (least important on top)

## Resource Management (Contracts & Stretches)

- App requests a stretch from the stretch allocator → gets a range
- Contract formed via framework, locking needed resources
- Stretch driver (middle of architecture) handles paging bandwidth, loads data onto “wrap”

## Drivers and Components

- **Chef driver types**
  - *All‑frames*: allocate everything up‑front
  - *Discover chef*: allocate on first stretch access (lazy)
  - *Patient stretch*: on‑demand allocation for comms
- Elementary entry → notification handler + worker thread → identifies address, calls dryer to fix issue
- IDC (inter‑domain communication) blocked during critical handling to avoid blocking

## Scheduling and Event Handling

- Scheduler activates app → staff vision inspects new events
- Each event routed to a handler (hand‑ler) in user‑space
- High‑level management (user space) sets/deletes page entries
- Low‑level lightweight layer tracks app memory usage, performs privileged mapping ops

## Performance Evaluation

- Microbenchmarks: dirty‑bit check (≈1.5 µs), protect/unprotect pages, trap handling
- Protection‑domain optimization cuts protect time from \~10 µs to \~0.3 µs
- Multi‑app experiment: varied latency (25 ms, 50 ms, 100 ms) shows bandwidth sharing, self‑paging keeps CPU busy

## Conclusions

- Self‑paging gives high‑quality virtual memory and better resource utilization
- Overhead mainly from stretch drivers and page‑change work
- Need for global optimization to reduce driver‑induced costs

## Discussion Points

- How strict partitioning affects parallelism and resource contention
- Policies for uniform resource accounting across apps
- Balancing security isolation with performance in the Nemesis design
- Potential improvements to stretch‑driver overhead and frame management
