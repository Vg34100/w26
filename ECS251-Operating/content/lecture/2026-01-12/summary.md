# ECS251 OS - 01/12

## Action Items

- Submit group member names in the designated text box (by Monday)
- Prepare a brief project proposal (topic, open‑ended scope) for next Wednesday
- Review the two assigned papers (“Rockets” and “Any Journal”) before the next class
- Explore Cloud Lab or student credits on AWS/Azure for hardware access
- Check with the TA for any clarification on discussion‑section logistics

## Lecture Overview

- Data‑center OS design is evolving with modern hardware
- Traditional OS assumptions (CPU ≫ I/O) no longer hold
- Papers discuss leveraging current hardware capabilities

## Hardware Evolution

- More cores, larger RAM, abundant SSD storage vs. old disks/tape
- Network bandwidth and NIC capabilities have dramatically increased
- CPUs hit Moore’s law limits; performance now from specialized units

## I/O and Networking Changes

- SSDs give microsecond latency, eliminating mechanical delays
- NICs can perform DMA, offloading work from the CPU
- SR‑IOV lets one NIC appear as multiple virtual devices to the OS

## OS APIs and Sockets

- Standard socket API works across Linux, macOS, other Unix‑like OSes
- Example server: create socket → bind → listen → accept → recv/send
- Portable code runs on any compliant OS without changes

## Zero‑Copy & Direct Memory Access

- Goal: avoid copying data between user space and kernel buffers
- Devices can write/read directly to application memory via DMA
- Requires careful buffer lifetime management (no reuse until device done)

## Research Project Guidelines

- Open‑ended, 3‑4‑person teams; choose a topic with a research question
- Must involve some system work (e.g., OS, networking, storage)
- Not required to modify the kernel; user‑space experiments OK
- Projects can be exploratory; negative results are still valuable

## Project Deliverables

- Short (10‑15 min) presentation in final week’s project session
- Written paper with methodology, results, and discussion
- Optional video demo of the prototype or experiments
- Group members submit names; TA available for questions

## Resources & Tools

- Cloud Lab (free university resource) for diverse hardware access
- Student credits on AWS/Azure for additional compute/storage
- Low‑level libraries: DPDK (network), SPDK (storage), RDMA APIs
- eBPF for low‑overhead tracing and custom kernel instrumentation

## Scheduling & Logistics

- Membership list due Monday; project kickoff next Wednesday
- Discussion sections for group meetings, but meetings can be elsewhere
- TA will be present during discussion sections for support
- Final week includes project presentations and paper submission.
