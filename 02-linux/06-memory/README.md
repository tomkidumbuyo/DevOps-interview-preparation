# Memory

<!-- chapter-guide:start -->
> **Step 021 of 373 — 02.06**
>
> **Builds on:** [systemd](../05-systemd/README.md)
>
> **Now:** Learn **Memory** from its mental model through production ownership.
>
> **Then:** Rehearse the linked questions and continue to [CPU performance](../07-cpu-performance/README.md).
<!-- chapter-guide:end -->

> [Interview questions and answers](questions-and-answers.md) · [Master curriculum](../../curriculum/master-curriculum.txt) · Official starting point: <https://docs.kernel.org/>

## Easy mode: mental model

Master Memory from first principles through safe production operation and senior architecture decisions.

Learn this topic in layers: name the object or mechanism, trace its lifecycle/data path, configure it safely, observe a healthy and failed state, recover it, and then design it across failure domains and team boundaries.

```mermaid
flowchart LR
  R[requirement or symptom] --> M[Memory mechanism]
  M --> S[state and dependencies]
  S --> O[commands metrics logs traces audit]
  O --> D[decision mitigation or design]
  D --> V[user-facing verification]
```

## Complete curriculum checklist

| # | Topic | What you must understand and demonstrate |
|---:|---|---|
| 1 | **Virtual memory** | is part of Memory; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 2 | **Resident memory** | is part of Memory; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 3 | **Shared memory** | is part of Memory; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 4 | **Page cache** | uses reclaimable RAM for file data to reduce I/O; it is not automatically a leak, but writeback and dirty-page pressure affect latency. |
| 5 | **Buffers** | is part of Memory; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 6 | **Swap** | is part of Memory; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 7 | **Memory pressure** | is part of Memory; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 8 | **Out-of-memory killer** | selects a victim when memory cannot be reclaimed; host and cgroup OOM scopes, scores and memory events reveal why. |
| 9 | **Memory leaks** | is part of Memory; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 10 | **Huge pages** | is part of Memory; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. |
| 11 | **NUMA** | groups CPUs and local memory; remote-memory access and poor placement can reduce throughput even when aggregate capacity looks free. |

## Beginner → mid-level → senior learning path

1. **Beginner:** define every term; identify the relevant file, object, protocol, API, or command; explain one normal use.
2. **Mid-level:** configure it from source control, inspect effective runtime state, diagnose two failure modes, automate a safe change, and explain one trade-off.
3. **Senior:** clarify ambiguous requirements, map trust and failure domains, quantify capacity/SLO/RPO/RTO/cost, compare alternatives, plan migration/rollback, and assign ownership.

## Command and configuration lab

Run read-only checks first in a sandbox. For each command, predict healthy output, one failing result, the next discriminating check, and the safe rollback for any later mutation.

```bash
free -h; vmstat 1
cat /proc/meminfo; cat /proc/pressure/memory
ps -eo pid,comm,rss,vsz,pmem --sort=-rss | head
cat /sys/fs/cgroup/memory.current; cat /sys/fs/cgroup/memory.events
```

## Hands-on practice: setup → failure → verification → cleanup

Use a disposable Linux VM or container. Record `date -u`, `uname -a`, distribution, effective user and cgroup before the topic commands. Capture a healthy baseline, run one command with an intentionally nonexistent PID/path/unit to learn its error and exit code, then return to the real object and explain the discriminating fields. Do not change mounts, firewall, users, kernel settings or services on a shared host. Cleanup: exit and delete the disposable environment.

Expected result: you can show the healthy evidence, reproduce a safe failure, explain why each command distinguishes one layer from another, restore the baseline, and prove cleanup. Hard extension: automate the lab from source control, add a test or alert for the injected failure, and write a five-step runbook another engineer can execute.

For code/configuration, be ready to review an intentionally unsafe diff and improve idempotency, secret handling, timeouts, validation, logging, tests, and rollback.

## Senior design checklist

State assumptions for tenants, traffic/work units, latency and availability targets, data classification/residency, recovery, team skills and budget. Draw control/data planes and synchronous/asynchronous dependencies. Cover identity, policy, encryption/key lifecycle, delivery provenance, observability, capacity, unit cost, operational ownership, migration and exit criteria. Name the evidence that would cause you to revise the design.

## Revision and practice

Complete the separate [checkbox interview bank](questions-and-answers.md). Do not memorize wording: speak in the order **definition → mechanism → evidence/configuration → failure/trade-off → production example**. For procedures use **stabilize → scope → inspect → hypothesize → test → mitigate → verify → prevent**.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: systemd](../05-systemd/README.md) · [Questions](questions-and-answers.md) · [Next: CPU performance →](../07-cpu-performance/README.md)

<!-- reading-navigation:end -->
