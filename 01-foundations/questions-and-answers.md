# Computer science and distributed-systems foundations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-01

- [ ] **Question:** What is CPU, and why does it matter in Computer science and distributed-systems foundations?

**Answer:** executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-02

- [ ] **Question:** What is Memory, and why does it matter in Computer science and distributed-systems foundations?

**Answer:** maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-03

- [ ] **Question:** What is Disk, and why does it matter in Computer science and distributed-systems foundations?

**Answer:** persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-04

- [ ] **Question:** What is Network, and why does it matter in Computer science and distributed-systems foundations?

**Answer:** moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-05

- [ ] **Question:** What is Processes, and why does it matter in Computer science and distributed-systems foundations?

**Answer:** are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-06

- [ ] **Question:** What is Threads, and why does it matter in Computer science and distributed-systems foundations?

**Answer:** share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-07

- [ ] **Question:** What is File descriptors, and why does it matter in Computer science and distributed-systems foundations?

**Answer:** are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-08

- [ ] **Code:** **Question:** What does `dig NAME` help you verify for Computer science and distributed-systems foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-09

- [ ] **Code:** **Question:** What does `lscpu; free -h; lsblk; ip -br addr` help you verify for Computer science and distributed-systems foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JN-10

- [ ] **Code:** **Question:** What does `ss -s` help you verify for Computer science and distributed-systems foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference.

## Junior — procedural and command questions

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-01

- [ ] **Code:** **Question:** A basic CPU check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-02

- [ ] **Question:** A basic Memory check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-03

- [ ] **Question:** A basic Disk check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-04

- [ ] **Code:** **Question:** A basic Network check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-05

- [ ] **Question:** A basic Processes check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-06

- [ ] **Question:** A basic Threads check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-07

- [ ] **Code:** **Question:** A basic File descriptors check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-08

- [ ] **Question:** A basic Interrupts check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-09

- [ ] **Question:** A basic System calls check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--JP-10

- [ ] **Code:** **Question:** A basic Processes versus threads check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-01

- [ ] **Question:** Compare CPU with Memory. When would each change your design?

**Answer:** CPU: executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. Memory: maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-02

- [ ] **Question:** Compare Memory with Disk. When would each change your design?

**Answer:** Memory: maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. Disk: persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-03

- [ ] **Question:** Compare Disk with Network. When would each change your design?

**Answer:** Disk: persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. Network: moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-04

- [ ] **Configuration review:** **Question:** Compare Network with Processes. When would each change your design?

**Answer:** Network: moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. Processes: are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-05

- [ ] **Question:** Compare Processes with Threads. When would each change your design?

**Answer:** Processes: are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. Threads: share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-06

- [ ] **Question:** Compare Threads with File descriptors. When would each change your design?

**Answer:** Threads: share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. File descriptors: are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-07

- [ ] **Configuration review:** **Question:** Compare File descriptors with Interrupts. When would each change your design?

**Answer:** File descriptors: are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. Interrupts: is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-08

- [ ] **Question:** Compare Interrupts with System calls. When would each change your design?

**Answer:** Interrupts: is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. System calls: cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-09

- [ ] **Question:** Compare System calls with Processes versus threads. When would each change your design?

**Answer:** System calls: cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O. Processes versus threads: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MN-10

- [ ] **Configuration review:** **Question:** Compare Processes versus threads with CPU. When would each change your design?

**Answer:** Processes versus threads: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. CPU: executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around CPU; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-02

- [ ] **Question:** Production is degraded around Memory; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Disk; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-04

- [ ] **Question:** Production is degraded around Network; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Processes; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-06

- [ ] **Question:** Production is degraded around Threads; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around File descriptors; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-08

- [ ] **Question:** Production is degraded around Interrupts; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around System calls; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--MP-10

- [ ] **Question:** Production is degraded around Processes versus threads; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-01

- [ ] **Question:** Design a production Computer science and distributed-systems foundations capability where CPU, Network and File descriptors are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Computer science and distributed-systems foundations capability where Memory, Processes and Interrupts are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-03

- [ ] **Question:** Design a production Computer science and distributed-systems foundations capability where Disk, Threads and System calls are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Computer science and distributed-systems foundations capability where Network, File descriptors and Processes versus threads are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-05

- [ ] **Question:** Design a production Computer science and distributed-systems foundations capability where Processes, Interrupts and CPU are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Computer science and distributed-systems foundations capability where Threads, System calls and Memory are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O. maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-07

- [ ] **Question:** Design a production Computer science and distributed-systems foundations capability where File descriptors, Processes versus threads and Disk are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Computer science and distributed-systems foundations capability where Interrupts, CPU and Network are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-09

- [ ] **Question:** Design a production Computer science and distributed-systems foundations capability where System calls, Memory and Processes are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O. maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Computer science and distributed-systems foundations capability where Processes versus threads, Disk and Threads are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. executes instructions on logical processors; run-queue pressure, per-core saturation, steal time, affinity, quotas and throttling determine effective compute. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Memory. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. maps virtual pages to RAM or swap; RSS, cache, faults, reclaim, PSI, NUMA locality and cgroup limits explain pressure better than one free-memory number. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Disk. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. persists blocks through filesystem, page cache, block queue and device; IOPS, throughput, latency, queue depth, durability and failure are distinct. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. moves packets through name resolution, routing, policy/NAT, transport, TLS and application layers; each hop has independent state and failure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Processes. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. are kernel-scheduled execution/resource containers with address space, credentials, descriptors, namespaces, cgroups, signals and lifecycle state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Threads. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. share a process address space and resources while retaining independent stacks and scheduling state, trading lower communication cost for synchronization risk. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving File descriptors. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. are per-process integer handles to open files, sockets, pipes and kernel objects; process and system limits can exhaust independently. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Interrupts. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. is part of Computer science and distributed-systems foundations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving System calls. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. cross the user/kernel boundary to request controlled operations such as open, read, write, mmap, clone and network I/O. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-COMPUTER-SCIENCE-AND-DISTRIBUTED-SYSTEMS--SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Processes versus threads. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
