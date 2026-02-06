# ECS251-OS | W04-Wed | 2026-01-28

## Action Items

- Schedule meeting with advisor after class
- Draft weekly report summarizing lecture points and personal reflections
- Review the referenced paper’s “both one” bug for deeper understanding
- Explore sanity‑checker tool implementation details for future project

## Lecture Overview

- Linux uses CFS (Completely Fair Scheduler) for proportional‑share scheduling
- Each CPU has its own run queue; no single global queue
- Load balancing moves tasks between CPUs to improve utilization
- Balancing runs periodically; emergency balancing triggers on idle detection

## Scheduler Bugs Discussed

- **Group imbalance bug** – load metric diluted across large thread groups, causing under‑balancing
- **Sleeping‑node wake‑up bug** – wakes on short‑term idle core with active data, leading to cache thrashing
- **Scheduling‑domain bug** – domains limited to a single node, preventing cross‑node thread migration

## Load‑Balancing Mechanism

- Hierarchical domains: CPU → SMP group → node → system (2‑hop reach)
- Each CPU runs the algorithm, but only one designated CPU initiates balancing
- Decision based on average load of own group vs. other groups
- Balancing only occurs if own load &lt; group average; otherwise no action

## Bug Fixes Presented

- Wake sleeping node on the **longest‑idle** core; if none, pick any idle core
- Extend domain generation to span all nodes, allowing cross‑node thread placement
- Disable assembly‑level power‑state control to avoid unintended wake‑ups

## Detection Tools & Strategies

- **Sanity checker**: verifies invariant “idle core should stay idle”
- Monitors short‑burst scheduling after detecting idle core before flagging failure
- Adjustable parameters: max idle time, monitoring interval (e.g., 1 s) – trade‑off between false positives and missed bugs
- Low overhead, suitable for continuous integration

## Discussion & Student Insights

- Power‑consumption impact of wake‑up fixes not quantified in paper
- Trade‑off: slight scheduling delay vs. potential energy savings on low‑power devices
- Difficulty detecting bugs: they don’t crash, happen quickly, and generate noisy data
- Linux scheduler’s longevity attributed to broad developer base and uniform policy that works “well enough” for most workloads
- Interest in exploring framework that lets applications specify custom scheduling policies for tighter latency bounds
