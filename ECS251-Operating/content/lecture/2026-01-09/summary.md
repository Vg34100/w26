# ECS251 OPERATING - OS Design Lecture and Group Assignments

## Action Items

- Finalize musical / project groups; ensure every registered student is placed in a group.
- Post project ideas for groups; due in about 1½ weeks.
- Prepare the upcoming quiz (paper‑and‑pencil); remind students to bring paper and a pencil.
- Submit the final group‑membership list on Canvas (or “Candice”) promptly.
- Review the exokernel (exoplanet) paper before the next class.
- Allocate time this weekend (by midnight or Monday morning) to tidy up group assignments.

## Lecture Overview – Exokernel Concepts

- Kernel only provides protection; all policy (memory, I/O, scheduling) lives in user‑level library OSes.
- “Secure bindings” let the kernel track which library OS owns which hardware resource.
- When the kernel revokes a binding it raises a repossession exception; the app must free or swap the resource.
- Guarantees are soft – the kernel tries not to take critical per‑app structures but can if needed.
- Design goal: lower‑level primitives give higher performance and more flexibility for applications.
- Example system: Aegis kernel + SLS library OS used to demonstrate feasibility and speedups over a monolithic OS.

## Student Q&A – Brief Answers

- **User‑level resource management:** Good when the kernel enforces isolation, accounting, and fast revocation; otherwise adds complexity.
- **Do app developers need to be OS developers?** No – they write to a library OS; only a small OS team builds and maintains those libraries.
- **Downloading code into the kernel:** Possible if sandboxed, verified, and audited; otherwise risky.
- **Why limited commercial adoption?** Ecosystem lock‑in, driver compatibility, debugging difficulty, and higher development risk outweigh performance gains.

## Key Points from the Lecture (mic)

- Group work: “I’ll go through and make musical groups… if you’re still registered and haven’t joined, do it now.”
- Quiz details: will be paper‑and‑pencil, covering units and exopurnal; bring both paper and a pencil.
- Paper discussion: exoplanet paper is a classic OS design paper; it challenges traditional Unix abstractions.
- OS abstraction layers: hardware → kernel (protection) → library OSes (policy) → applications.
- Problems with monolithic abstractions: inflexible, hard to modify, performance compromises for some workloads.
- Exokernel’s “end‑to‑end” argument: lower‑level primitives enable more efficient implementations and greater flexibility.
- Protection vs. management: kernel protects resources; library OSes manage them and can be customized per application.
- Revocation flow: kernel assigns resources, tracks ownership, can reclaim them; apps participate by swapping out unneeded pages.
- Benefits: better resource‑use decisions, fewer heavyweight kernel crossings, higher performance for specialized workloads.
- Trade‑offs: added developer burden, need for reusable libraries, potential scalability issues on specific hardware.
- Real‑world adoption: Linux incorporates some user‑space services, but full exokernel designs remain niche due to tooling and ecosystem inertia.
