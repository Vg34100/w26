# ECS251 OPERATING - Class Discussion on Paper Selection

## Everything Is a File – Key Takeaways

- Simple unified API: open, read/write, close works on many resources
- Enables powerful composition: pipes, redirection, tooling uniformity
- Facilitates debugging & scripting via pseudo‑files (/proc, /sys)
- Extensible: new resources exposed without new interfaces
- Limits: not all resources fit byte‑stream model (e.g., GPUs, high‑perf networking)
- Control‑path awkwardness: ioctls, sysfs strings for commands
- Security mismatch: POSIX perms can’t express fine‑grained capabilities

## Fork System Call – Essentials

- Creates a new process by duplicating the calling process
- Return values: parent gets child PID (&gt;0), child gets 0, error → –1
- Child gets copy‑on‑write address space, same open file descriptors, inherited env & cwd
- Typical pattern: fork() → child exec\*() → parent waitpid()
- Caveats: only async‑signal‑safe functions between fork and exec in multithreaded programs
- Zombie risk if parent never waits; vfork is a specialized, stricter variant

## Unix History & Design Philosophy

- Ken Thompson & Dennis Ritchie built Unix at Bell Labs to improve on Multics
- Goal: opposite of Multics’ complexity → simple, portable OS
- Early development on PDP‑11 with 144 KB memory, 22 KB usable space
- Emphasis on interactive use (timesharing) vs. batch processing
- Design driven by limited resources: minimal APIs, small kernel, modularity

## File System & Device Model

- Everything appears as a file: regular files, directories, special device files, sockets
- Directories are special files containing pointers to other files (tree structure)
- Devices exposed as character or block files; read/write maps to hardware I/O
- Uniform naming & permission model (owner/group/others bits) applies across all objects
- Allows simple tools (e.g., cat, dd) to operate on diverse resources

## Process Management & Execution

- Fork creates a duplicate process; exec replaces its image with a new program
- Parent can launch background jobs, pipelines, and redirect I/O using &lt;, &gt;, |
- Wait/waitpid reaps child processes, preventing zombies
- Modern alternatives (e.g., posix_spawn) aim to reduce overhead of fork+exec
- Fork’s copy‑on‑write semantics keep memory usage low despite “copy” wording

## Student Concerns & Next Steps

- Reviewed lecture material on Unix fundamentals and fork semantics
- Confirmed code submission on Gradescope passed all tests
- No pending action items identified; continue reviewing fork usage in assignments
- Keep an eye on upcoming quiz covering “everything is a file” abstraction and process creation basics.
