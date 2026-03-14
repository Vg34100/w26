# ECS251-OS | W07-Wed | 2026-02-18

## File System History & Phases

- Phase 1: basic file ID, early reporting mechanisms
- Phase 2: focus on performance, efficiency, and modality
- Phase 3: larger blocks, faster access, layout optimizations
- Phase 4: network‑distributed file systems, sharing over networks
- Phase 5: scaling, fault tolerance, data replication

## Motivation & Design Considerations

- Underlying medium changes → file system must adapt
- Keep related blocks physically close to improve speed
- Balance capacity growth vs. performance gains
- Ensure fault‑tolerant behavior to avoid data loss
- Use policies to manage replication and storage layout

## Basic File System Example

- Tiny FS with 8 data blocks, each block tracked by an inode
- Updating a file may allocate a new block and modify metadata
- Multiple updates can interleave, requiring careful ordering

## Failure Scenarios & Outcomes

- Inode updated, data block not written → “inode‑bitmap mismatch”
- Data block written, inode not updated → orphaned data
- Both inode and data written correctly → normal state
- Inconsistent states lead to lost data or corrupted metadata

## Journaling & Consistency Strategies

- Write intent log (journal) before performing actual updates
- On crash, replay journal to restore intended state
- Two approaches:
  - Immediate checkpoint after each transaction → safe but slow
  - Batch checkpoints → faster, higher risk of data loss
- Order of writes matters: journal → data → inode → bitmap

## Practical Tips for Safe Updates

- Log only metadata changes when possible to reduce write overhead
- Ensure data write completes before logging transaction commit
- Never reset a pointer to a live resource before establishing a new reference
- Avoid initializing resources that may never be fully set up
- Review and nullify old references only after new ones are confirmed

## Q&A Highlights

- Clarified last point: must set new pointer before clearing old one to avoid losing the only reference to a node.
