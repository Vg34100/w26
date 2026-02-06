# ECS251-OS | W02-Wed | 2026-01-14

## Action Items

- Read the upcoming paper “demiurge” before the next class
- Review Arrakis P vs N trade‑offs and decide which model fits your project (greenfield vs porting)
- Prepare a couple of questions or points for the 10‑minute small‑group discussion

## Professor’s Core Points

- Storage side does only \~5 % of total processing; most cycles are spent in the network stack
- Network I/O (socket send/recv) consumes \~75 % of Redis server cycles – not the application logic
- Goal of Arrakis: bypass the kernel to eliminate this overhead
- SR‑IOV (Single Root I/O Virtualization) lets one physical NIC appear as many virtual NICs, handling routing & load balancing in hardware

## Control‑Plane vs Data‑Plane

- **Control plane** – policy & setup: creates NIC queues, sets permissions, configures filters, enforces resource limits, handles file‑system naming via VFS
- **Data plane** – fast path: moves packets or bytes directly between application and hardware, using DMA and doorbell interrupts
- Kernel stays in the control plane; user‑space libraries own the data plane

## Arrakis P vs Arrakis N

- **P** = POSIX compatibility – runs unmodified POSIX apps, lower performance gain, easier porting
- **N** = Native – uses Arrakis’s custom user‑level I/O API, highest performance, requires app changes
- Preference: use **N** for new (“greenfield”) apps, **P** when porting existing code

## Kernel Bypass – Benefits & Risks

- **Pros**: dramatically lower latency, higher throughput, avoids per‑I/O system calls
- **Cons**: loses uniform security checks, debugging support, and some kernel‑provided abstractions; may create vendor‑ or hardware‑lock‑in

## Lecture Details on Virtualization & Resource Management

- Hardware now provides multiplexing, protection, and scheduling directly (e.g., virtual NICs with isolated memory regions)
- Virtual Storage Interface Controller (VSIC) mirrors the NIC model for storage: maps many virtual storage areas to physical device space
- “Doorbells” = hardware interrupts that notify the application of new data on a virtual queue
- Filters are programmed in the control plane to direct specific packets or storage requests to the right virtual device
- Resource limits (e.g., per‑app bandwidth) are enforced by the control plane interacting with the hardware

## Library OS & Application Interaction

- Library OS runs in user space, handling I/O on the data plane while delegating only control‑plane tasks to the kernel
- Applications can query virtual file system metadata but the actual storage I/O is performed by the library OS itself
- This model lets apps customize storage layout and persistence strategies without relying on a traditional file system

## Trade‑offs Discussed

- **Complexity**: moving control logic to user space and hardware increases development effort
- **Portability**: native mode ties you to specific NIC/SSD features; POSIX mode remains more portable
- **Security**: fewer kernel checks mean you must trust the library OS and hardware enforcement mechanisms

---

*All points captured concisely for quick review.*
