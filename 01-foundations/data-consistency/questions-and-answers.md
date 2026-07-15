# Data consistency — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### DATA-CONSISTENCY-JN-01

- [ ] **Question:** What is Strong consistency, and why does it matter in Data consistency?

**Answer:** makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-CONSISTENCY-JN-02

- [ ] **Question:** What is Eventual consistency, and why does it matter in Data consistency?

**Answer:** allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-CONSISTENCY-JN-03

- [ ] **Question:** What is Read-after-write consistency, and why does it matter in Data consistency?

**Answer:** is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-CONSISTENCY-JN-04

- [ ] **Question:** What is Quorums, and why does it matter in Data consistency?

**Answer:** require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-CONSISTENCY-JN-05

- [ ] **Question:** What is Replication, and why does it matter in Data consistency?

**Answer:** is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-CONSISTENCY-JN-06

- [ ] **Question:** What is Leader election, and why does it matter in Data consistency?

**Answer:** is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-CONSISTENCY-JN-07

- [ ] **Question:** What is Split brain, and why does it matter in Data consistency?

**Answer:** is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DATA-CONSISTENCY-JN-08

- [ ] **Code:** **Question:** What does `dig NAME` help you verify for Data consistency?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request.

### DATA-CONSISTENCY-JN-09

- [ ] **Code:** **Question:** What does `lscpu; free -h; lsblk; ip -br addr` help you verify for Data consistency?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions.

### DATA-CONSISTENCY-JN-10

- [ ] **Code:** **Question:** What does `ss -s` help you verify for Data consistency?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts.

## Junior — procedural and command questions

### DATA-CONSISTENCY-JP-01

- [ ] **Code:** **Question:** A basic Strong consistency check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-02

- [ ] **Question:** A basic Eventual consistency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-03

- [ ] **Question:** A basic Read-after-write consistency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-04

- [ ] **Code:** **Question:** A basic Quorums check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-05

- [ ] **Question:** A basic Replication check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-06

- [ ] **Question:** A basic Leader election check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-07

- [ ] **Code:** **Question:** A basic Split brain check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-08

- [ ] **Question:** A basic CAP theorem check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-09

- [ ] **Question:** A basic Strong consistency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DATA-CONSISTENCY-JP-10

- [ ] **Code:** **Question:** A basic Eventual consistency check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### DATA-CONSISTENCY-MN-01

- [ ] **Question:** Compare Strong consistency with Eventual consistency. When would each change your design?

**Answer:** Strong consistency: makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Eventual consistency: allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-02

- [ ] **Question:** Compare Eventual consistency with Read-after-write consistency. When would each change your design?

**Answer:** Eventual consistency: allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Read-after-write consistency: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-03

- [ ] **Question:** Compare Read-after-write consistency with Quorums. When would each change your design?

**Answer:** Read-after-write consistency: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Quorums: require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-04

- [ ] **Configuration review:** **Question:** Compare Quorums with Replication. When would each change your design?

**Answer:** Quorums: require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. Replication: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-05

- [ ] **Question:** Compare Replication with Leader election. When would each change your design?

**Answer:** Replication: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Leader election: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-06

- [ ] **Question:** Compare Leader election with Split brain. When would each change your design?

**Answer:** Leader election: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Split brain: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-07

- [ ] **Configuration review:** **Question:** Compare Split brain with CAP theorem. When would each change your design?

**Answer:** Split brain: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. CAP theorem: states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-08

- [ ] **Question:** Compare CAP theorem with Strong consistency. When would each change your design?

**Answer:** CAP theorem: states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request. Strong consistency: makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-09

- [ ] **Question:** Compare Strong consistency with Eventual consistency. When would each change your design?

**Answer:** Strong consistency: makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Eventual consistency: allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DATA-CONSISTENCY-MN-10

- [ ] **Configuration review:** **Question:** Compare Eventual consistency with Strong consistency. When would each change your design?

**Answer:** Eventual consistency: allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Strong consistency: makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### DATA-CONSISTENCY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Strong consistency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-02

- [ ] **Question:** Production is degraded around Eventual consistency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Read-after-write consistency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-04

- [ ] **Question:** Production is degraded around Quorums; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Replication; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-06

- [ ] **Question:** Production is degraded around Leader election; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Split brain; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-08

- [ ] **Question:** Production is degraded around CAP theorem; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Strong consistency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DATA-CONSISTENCY-MP-10

- [ ] **Question:** Production is degraded around Eventual consistency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### DATA-CONSISTENCY-SN-01

- [ ] **Question:** Design a production Data consistency capability where Strong consistency, Quorums and Split brain are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Data consistency capability where Eventual consistency, Replication and CAP theorem are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-03

- [ ] **Question:** Design a production Data consistency capability where Read-after-write consistency, Leader election and Strong consistency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Data consistency capability where Quorums, Split brain and Eventual consistency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-05

- [ ] **Question:** Design a production Data consistency capability where Replication, CAP theorem and Strong consistency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Data consistency capability where Leader election, Strong consistency and Eventual consistency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-07

- [ ] **Question:** Design a production Data consistency capability where Split brain, Eventual consistency and Read-after-write consistency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Data consistency capability where CAP theorem, Strong consistency and Quorums are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-09

- [ ] **Question:** Design a production Data consistency capability where Strong consistency, Eventual consistency and Replication are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DATA-CONSISTENCY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Data consistency capability where Eventual consistency, Read-after-write consistency and Leader election are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### DATA-CONSISTENCY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Strong consistency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Eventual consistency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Read-after-write consistency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Quorums. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. require overlapping read/write or voting majorities so operations intersect authoritative state, with latency and partition trade-offs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Replication. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Leader election. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Split brain. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of Data consistency; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CAP theorem. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. states that during a network partition a distributed system cannot guarantee both linearizable consistency and availability for every request. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Strong consistency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. makes reads observe a single agreed ordering under the system's contract, usually trading latency or availability during partitions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DATA-CONSISTENCY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Eventual consistency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. allows replicas to diverge temporarily and converge later, requiring UX and workflows that tolerate stale reads/conflicts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
