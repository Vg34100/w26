# ECS251-OS | W08-Mon | 2026-02-23

## Introduction & Motivation

- Lecture covers design & implementation of Log‑Structured File System (LFS)
- Originated 1991 to match fast memory growth vs. slow HDD improvements
- Goal: batch writes in memory, flush sequentially to disk
- Traditional Unix FFS uses only 5‑10 % of disk bandwidth, suffers random‑seek overhead

## Core LFS Concept

- Log **is** the file system – primary data structure, not just journaling
- Append‑only log divided into large on‑disk segments
- Each segment holds data, inode info, inode map, and summary metadata
- In‑memory indexing (inode map) points to latest version of each node

## Design Trade‑offs

- **Data placement:** reorganize later vs. place optimally now → LFS chooses later
- **Write strategy:** synchronous writes vs. batch in memory → LFS batches
- **Consistency vs. latency:** tolerate brief windows of stale state for higher throughput

## Requirements & Goals

- Fast large sequential writes
- Minimize internal fragmentation
- Preserve read performance (equal or better than FFS)
- Avoid costly free‑list management

## Free‑Space Management & Segment Cleaning

- Segments become partially filled → need cleaning to reclaim space
- Two basic approaches:
  1. **Threaded cleaning** – may cause fragmentation
  2. **Copy‑live‑data cleaning** – moves live blocks, frees whole segment
- LFS combines both: identify live blocks, copy them, then reclaim segment

## Inode Map & Checkpointing

- Inode map stores address of latest version of each inode
- Stored in log and cached in RAM (checkpoint region)
- Checkpoint includes: current log head, segment order, segment summaries (live inode locations)
- Enables fast recovery: locate newest checkpoint, rebuild inode map from segment summaries

## Performance Evaluation

- Micro‑benchmarks vs. SunOS/Unix FS on 300 MB test volume
- **Small‑file workload:** \~10× higher creates/deletes per second
- **Large‑file workload:** similar read performance, better sequential write throughput
- Simulated faster CPUs predict further gains; real‑world overhead modest (≈1.1‑1.6×)

## Related Work

- Early log‑structured designs (e.g., *Log‑Only* file system)
- Garbage‑collection techniques from log‑structured storage
- LSM‑tree databases share append‑only, compaction ideas

## SSDs & Modern Hardware Considerations

- SSDs have erase‑block constraints; small random writes costly
- LFS concepts map well to SSD wear‑leveling & block erasure patterns
- Debate: implement LFS purely in software, purely in firmware, or hybrid middle layer
- Hybrid approach could exploit software’s workload awareness and SSD’s low‑level block management

## Discussion Highlights

- Question on write amplification formula: **2 / (1 − c³)** where *c* = segment utilization
- Clarified that LFS shifts from in‑place updates to batch‑append, reducing fragmentation
- Explored use cases: Facebook’s MySQL on LSM‑based storage, AI model training pipelines with heavy write phases
- Raised concerns about page‑table updates and consistency during log cleaning

## Key Takeaways

- LFS treats the log as the sole source of truth, simplifying crash recovery
- Batching writes yields near‑full disk bandwidth utilization
- Segment cleaning is essential to reclaim space without degrading performance
- Modern SSD characteristics revive interest in log‑structured designs, especially with hybrid software‑hardware solutions
