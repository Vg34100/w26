# ECS251-OS | W05-Mon | 2026-02-02

## Virtual Memory Overview

- Gives each app its own private address space
- Virtual addresses start at 0, appear contiguous
- Size of virtual space independent of physical RAM
- Text, data, heap, stack grow in opposite directions
- Multiple processes share physical memory but stay isolated

## Address Translation

- CPU + OS translate virtual → physical addresses
- Uses page tables and MMU (memory‑management unit)
- Function maps (process ID, virtual address) → physical frame
- Translation can be slow; needs multiple look‑ups

## Paging and Page Tables

- Memory divided into equal‑size pages (virtual) and frames (physical)
- Fixed page size avoids external fragmentation
- Internal fragmentation when a page isn’t fully used
- Multi‑level page tables form a tree; CR3 holds root pointer
- Virtual address split into offsets for each table level

## TLB (Translation Lookaside Buffer)

- Small hardware cache for recent virtual‑to‑physical mappings
- Hits skip full page‑table walk, saving time
- Limited size → misses still require full walk
- Larger pages (superpages) reduce number of TLB entries needed

## Superpages / Large Pages

- Page sizes can be 4 KB, 2 MB, 1 GB, etc. (multiples of each other)
- Bigger pages cover more address space per TLB entry
- Shallower page‑table walks, fewer TLB misses
- May re‑introduce some internal fragmentation

## Swapping and Page Replacement

- Physical RAM often smaller than total virtual space
- Pages not in RAM are moved to swap space on storage (swap out)
- Needed pages are brought back into RAM (swap in) before use
- Linux approximates LRU: keeps recently used pages active, others inactive
- Choice of replacement algorithm heavily impacts performance

## Cache Interaction

- Cache lookup uses physical addresses after translation
- Some hardware can tag cache with virtual addresses, but norm is physical
- Process ID may be part of cache tag to avoid aliasing
- Correct mapping ensures each process sees its own data in cache
