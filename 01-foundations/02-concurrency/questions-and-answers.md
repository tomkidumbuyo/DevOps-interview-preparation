# Concurrency — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CONCURRENCY-JN-01

- [ ] **Question:** What is Processes versus threads, and why does it matter in Concurrency?
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONCURRENCY-JN-02

- [ ] **Question:** What is Parallelism versus concurrency, and why does it matter in Concurrency?
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONCURRENCY-JN-03

- [ ] **Question:** What is Locks and mutexes, and why does it matter in Concurrency?
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONCURRENCY-JN-04

- [ ] **Question:** What is Semaphores, and why does it matter in Concurrency?
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONCURRENCY-JN-05

- [ ] **Question:** What is Race conditions, and why does it matter in Concurrency?
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONCURRENCY-JN-06

- [ ] **Question:** What is Deadlocks, and why does it matter in Concurrency?
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONCURRENCY-JN-07

- [ ] **Question:** What is Thread pools, and why does it matter in Concurrency?
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONCURRENCY-JN-08

- [ ] **Code:** **Question:** What does `dig NAME` help you verify for Concurrency?
> **Covered in:** [Concurrency — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation.

### CONCURRENCY-JN-09

- [ ] **Code:** **Question:** What does `lscpu; free -h; lsblk; ip -br addr` help you verify for Concurrency?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference.

### CONCURRENCY-JN-10

- [ ] **Code:** **Question:** What does `ss -s` help you verify for Concurrency?
> **Covered in:** [Concurrency — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference.

## Junior — procedural and command questions

### CONCURRENCY-JP-01

- [ ] **Code:** **Question:** A basic Processes versus threads check fails. What would you do first using the CLI?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-02

- [ ] **Question:** A basic Parallelism versus concurrency check fails. What would you do first?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-03

- [ ] **Question:** A basic Locks and mutexes check fails. What would you do first?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-04

- [ ] **Code:** **Question:** A basic Semaphores check fails. What would you do first using the CLI?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-05

- [ ] **Question:** A basic Race conditions check fails. What would you do first?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-06

- [ ] **Question:** A basic Deadlocks check fails. What would you do first?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-07

- [ ] **Code:** **Question:** A basic Thread pools check fails. What would you do first using the CLI?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-08

- [ ] **Question:** A basic Async I/O check fails. What would you do first?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-09

- [ ] **Question:** A basic Processes versus threads check fails. What would you do first?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONCURRENCY-JP-10

- [ ] **Code:** **Question:** A basic Parallelism versus concurrency check fails. What would you do first using the CLI?
> **Covered in:** [Concurrency — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CONCURRENCY-MN-01

- [ ] **Question:** Compare Processes versus threads with Parallelism versus concurrency. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Processes versus threads: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Parallelism versus concurrency: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-02

- [ ] **Question:** Compare Parallelism versus concurrency with Locks and mutexes. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Parallelism versus concurrency: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Locks and mutexes: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-03

- [ ] **Question:** Compare Locks and mutexes with Semaphores. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Locks and mutexes: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Semaphores: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-04

- [ ] **Configuration review:** **Question:** Compare Semaphores with Race conditions. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Semaphores: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Race conditions: make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-05

- [ ] **Question:** Compare Race conditions with Deadlocks. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Race conditions: make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. Deadlocks: occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-06

- [ ] **Question:** Compare Deadlocks with Thread pools. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Deadlocks: occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. Thread pools: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-07

- [ ] **Configuration review:** **Question:** Compare Thread pools with Async I/O. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Thread pools: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Async I/O: lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-08

- [ ] **Question:** Compare Async I/O with Processes versus threads. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Async I/O: lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation. Processes versus threads: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-09

- [ ] **Question:** Compare Processes versus threads with Parallelism versus concurrency. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Processes versus threads: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Parallelism versus concurrency: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONCURRENCY-MN-10

- [ ] **Configuration review:** **Question:** Compare Parallelism versus concurrency with Processes versus threads. When would each change your design?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Parallelism versus concurrency: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Processes versus threads: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CONCURRENCY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Processes versus threads; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-02

- [ ] **Question:** Production is degraded around Parallelism versus concurrency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Locks and mutexes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-04

- [ ] **Question:** Production is degraded around Semaphores; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Race conditions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-06

- [ ] **Question:** Production is degraded around Deadlocks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Thread pools; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-08

- [ ] **Question:** Production is degraded around Async I/O; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Processes versus threads; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONCURRENCY-MP-10

- [ ] **Question:** Production is degraded around Parallelism versus concurrency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CONCURRENCY-SN-01

- [ ] **Question:** Design a production Concurrency capability where Processes versus threads, Semaphores and Thread pools are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Concurrency capability where Parallelism versus concurrency, Race conditions and Async I/O are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-03

- [ ] **Question:** Design a production Concurrency capability where Locks and mutexes, Deadlocks and Processes versus threads are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Concurrency capability where Semaphores, Thread pools and Parallelism versus concurrency are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-05

- [ ] **Question:** Design a production Concurrency capability where Race conditions, Async I/O and Processes versus threads are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Concurrency capability where Deadlocks, Processes versus threads and Parallelism versus concurrency are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-07

- [ ] **Question:** Design a production Concurrency capability where Thread pools, Parallelism versus concurrency and Locks and mutexes are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Concurrency capability where Async I/O, Processes versus threads and Semaphores are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-09

- [ ] **Question:** Design a production Concurrency capability where Processes versus threads, Parallelism versus concurrency and Race conditions are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONCURRENCY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Concurrency capability where Parallelism versus concurrency, Locks and mutexes and Deadlocks are first-class requirements.
> **Covered in:** [Concurrency — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CONCURRENCY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Processes versus threads. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parallelism versus concurrency. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Locks and mutexes. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Semaphores. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Race conditions. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. make results depend on unsafe interleavings; remove them with ownership, immutability, atomic operations or correctly scoped synchronization. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deadlocks. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. occur when wait dependencies form a cycle; prevent with ordering, bounded acquisition, reduced lock scope and observable contention. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Thread pools. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of Concurrency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Async I/O. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. lets work progress without dedicating one blocked thread per operation, but still requires cancellation, deadlines, backpressure and error propagation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Processes versus threads. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONCURRENCY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parallelism versus concurrency. How do you lead it end to end?
> **Covered in:** [Concurrency — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Computing fundamentals](../01-computing-fundamentals/README.md) · [Study note](README.md) · [Next: Distributed systems →](../03-distributed-systems/README.md)

<!-- reading-navigation:end -->
