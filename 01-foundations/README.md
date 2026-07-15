# Computer science and distributed-systems foundations

<!-- chapter-guide:start -->
> **Step 007 of 373 — 01**
>
> **Builds on:** [Contractor and remote-work readiness](../00-role-ownership/05-contractor-and-remote-work-readiness/README.md)
>
> **Now:** Learn **Computer science and distributed-systems foundations** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [Computing fundamentals](01-computing-fundamentals/README.md).
<!-- chapter-guide:end -->

## Computing model

CPU executes instructions; memory holds addressable working state; storage persists blocks/files/objects; networks move bounded packets with latency/loss/reordering; processes own isolated virtual address spaces/resources; threads share a process. System calls cross user/kernel boundary. Interrupts signal hardware; file descriptors name open files, sockets, pipes and devices. Limits on descriptors, processes, memory, disk, ports and queues often appear as application failures.

Concurrency is overlapping work; parallelism is simultaneous execution. Locks/mutexes protect invariants, semaphores bound concurrency, condition variables coordinate state, queues decouple producers/consumers and async I/O waits without dedicating a thread. Races arise when outcomes depend on unsynchronized timing; deadlocks require circular waiting conditions. Control concurrency with ownership, immutability, bounded queues, timeouts/cancellation and load tests.

## Distributed systems

Remote calls can be slow, duplicated, reordered or partially succeed while the client times out. You cannot infer “operation did not happen” from “response was not received.” Use deadlines, bounded retries with exponential backoff/jitter, idempotency keys/conditional writes, deduplication, durable state machines and reconciliation.

At-most-once may lose; at-least-once may duplicate; “exactly once” usually means a scoped effect achieved by idempotency/transactions/deduplication under stated failure assumptions. Backpressure slows producers; load shedding rejects lower-value work before collapse; circuit breakers stop futile calls; bulkheads isolate resource pools; graceful degradation preserves critical paths.

Replication improves availability/read scale but creates lag/conflict/failover concerns. Strong consistency makes a defined ordering/visibility promise; eventual consistency converges absent new writes; read-after-write may be session/key scoped. Quorums trade read/write participation and failure tolerance. Leader election needs leases/terms/fencing to prevent stale leaders. CAP applies under partitions: choose which operations remain available versus consistent; it is not a database ranking slogan.

## API and architecture

REST models resources over HTTP; gRPC provides typed RPC/streaming over HTTP/2; WebSockets are bidirectional long-lived connections; server-sent events are server-to-client streams; queues/events decouple time and availability. Define contracts, authentication/authorization, validation, versioning/compatibility, pagination/cursors, idempotency, error taxonomy, deadlines/cancellation, correlation/trace context and rate limits.

Synchronous calls simplify immediate flows but couple latency/availability. Async messaging buffers and isolates but adds delivery/order/replay/observability complexity. A modular monolith can be safer than premature microservices; microservices trade independent ownership/scale for distributed-systems and platform cost. Event-driven systems need schema evolution, ownership, idempotent consumers and replay. Serverless changes execution/cost/limits, not correctness.

Control planes accept desired state/policy and reconcile; data planes serve traffic/work. Multi-tenancy must isolate identity, data, compute, network, keys, telemetry and cost. Choose shared versus dedicated resources from threat model, regulatory/customer requirements, noisy-neighbor risk and economics.

## Resilience and operations

Set a total deadline and retry budget across hops; otherwise layered retries amplify load. Use randomized backoff, honor server hints, do not blindly retry non-idempotent or permanent errors. Bound queues and concurrency to protect memory/dependencies. Cache with freshness, invalidation, stampede and tenant/security design. Test failure at boundaries and observe latency distributions, error/saturation/queue, dependency outcomes and correctness.

## Revision summary

- Partial failure and ambiguity are normal.
- Bound time, concurrency, queues and retries.
- Make side effects idempotent or durably coordinated.
- State consistency and availability claims with scope and failure assumptions.
- Architecture is a trade of coupling, ownership, failure and operational cost.

## Practice checkpoint

Use a disposable local process or container to observe one bounded queue, timeout, retry and cancellation path. Inject one delayed or duplicated request, explain the resulting failure mode and reliability effect, then stop the process and remove the temporary files, network and test data. Cleanup is part of the proof: no background worker, listener or generated state should remain.

## Read further

- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — primary production guidance connecting capacity, request cost, throttling, criticality and graceful degradation.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Contractor and remote-work readiness](../00-role-ownership/05-contractor-and-remote-work-readiness/README.md) · [Questions](questions-and-answers.md) · [Next: Computing fundamentals →](01-computing-fundamentals/README.md)

<!-- reading-navigation:end -->
