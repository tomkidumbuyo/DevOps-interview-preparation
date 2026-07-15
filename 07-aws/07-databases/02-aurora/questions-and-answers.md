# Amazon Aurora — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-AURORA-JN-01

- [ ] **Question:** What is Cluster volume, and why does it matter in Amazon Aurora?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** replicated distributed storage is shared by writer/readers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-AURORA-JN-02

- [ ] **Question:** What is Writer endpoint, and why does it matter in Amazon Aurora?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** follows current writer and should be used for write-capable connections. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-AURORA-JN-03

- [ ] **Question:** What is Reader endpoint, and why does it matter in Amazon Aurora?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** balances new reader connections but not individual queries or existing sessions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-AURORA-JN-04

- [ ] **Question:** What is Replica failover tier, and why does it matter in Amazon Aurora?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** influences which reader is promoted and how quickly compatible capacity is available. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-AURORA-JN-05

- [ ] **Question:** What is Aurora Serverless, and why does it matter in Amazon Aurora?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-AURORA-JN-06

- [ ] **Question:** What is Global Database, and why does it matter in Amazon Aurora?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-AURORA-JN-07

- [ ] **Question:** What is Backtrack, and why does it matter in Amazon Aurora?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** supported engines/configs can rewind logical time but it is not a substitute for backup. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-AURORA-JN-08

- [ ] **Code:** **Question:** What does `aws rds describe-blue-green-deployments` help you verify for Amazon Aurora?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: stabilizes connection storms under session/transaction semantics.

### AMAZON-AURORA-JN-09

- [ ] **Code:** **Question:** What does `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` help you verify for Amazon Aurora?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: long transactions/I/O/load can make readers stale and delay failover readiness.

### AMAZON-AURORA-JN-10

- [ ] **Code:** **Question:** What does `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` help you verify for Amazon Aurora?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: supports engine/change rehearsal with replication/switchover constraints.

## Junior — procedural and command questions

### AMAZON-AURORA-JP-01

- [ ] **Code:** **Question:** A basic Cluster volume check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` and capture exact status/reason/request ID. replicated distributed storage is shared by writer/readers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-02

- [ ] **Question:** A basic Writer endpoint check fails. What would you do first?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` and capture exact status/reason/request ID. follows current writer and should be used for write-capable connections. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-03

- [ ] **Question:** A basic Reader endpoint check fails. What would you do first?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-global-clusters` and capture exact status/reason/request ID. balances new reader connections but not individual queries or existing sessions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-04

- [ ] **Code:** **Question:** A basic Replica failover tier check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-blue-green-deployments` and capture exact status/reason/request ID. influences which reader is promoted and how quickly compatible capacity is available. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-05

- [ ] **Question:** A basic Aurora Serverless check fails. What would you do first?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` and capture exact status/reason/request ID. capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-06

- [ ] **Question:** A basic Global Database check fails. What would you do first?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` and capture exact status/reason/request ID. asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-07

- [ ] **Code:** **Question:** A basic Backtrack check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-global-clusters` and capture exact status/reason/request ID. supported engines/configs can rewind logical time but it is not a substitute for backup. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-08

- [ ] **Question:** A basic RDS Proxy/pooling check fails. What would you do first?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-blue-green-deployments` and capture exact status/reason/request ID. stabilizes connection storms under session/transaction semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-09

- [ ] **Question:** A basic Replica lag check fails. What would you do first?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` and capture exact status/reason/request ID. long transactions/I/O/load can make readers stale and delay failover readiness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-AURORA-JP-10

- [ ] **Code:** **Question:** A basic Blue/green deployment check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Aurora — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` and capture exact status/reason/request ID. supports engine/change rehearsal with replication/switchover constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-AURORA-MN-01

- [ ] **Question:** Compare Cluster volume with Writer endpoint. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cluster volume: replicated distributed storage is shared by writer/readers. Writer endpoint: follows current writer and should be used for write-capable connections. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-02

- [ ] **Question:** Compare Writer endpoint with Reader endpoint. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Writer endpoint: follows current writer and should be used for write-capable connections. Reader endpoint: balances new reader connections but not individual queries or existing sessions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-03

- [ ] **Question:** Compare Reader endpoint with Replica failover tier. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Reader endpoint: balances new reader connections but not individual queries or existing sessions. Replica failover tier: influences which reader is promoted and how quickly compatible capacity is available. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-04

- [ ] **Configuration review:** **Question:** Compare Replica failover tier with Aurora Serverless. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Replica failover tier: influences which reader is promoted and how quickly compatible capacity is available. Aurora Serverless: capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-05

- [ ] **Question:** Compare Aurora Serverless with Global Database. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Aurora Serverless: capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. Global Database: asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-06

- [ ] **Question:** Compare Global Database with Backtrack. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Global Database: asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. Backtrack: supported engines/configs can rewind logical time but it is not a substitute for backup. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-07

- [ ] **Configuration review:** **Question:** Compare Backtrack with RDS Proxy/pooling. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Backtrack: supported engines/configs can rewind logical time but it is not a substitute for backup. RDS Proxy/pooling: stabilizes connection storms under session/transaction semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-08

- [ ] **Question:** Compare RDS Proxy/pooling with Replica lag. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** RDS Proxy/pooling: stabilizes connection storms under session/transaction semantics. Replica lag: long transactions/I/O/load can make readers stale and delay failover readiness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-09

- [ ] **Question:** Compare Replica lag with Blue/green deployment. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Replica lag: long transactions/I/O/load can make readers stale and delay failover readiness. Blue/green deployment: supports engine/change rehearsal with replication/switchover constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-AURORA-MN-10

- [ ] **Configuration review:** **Question:** Compare Blue/green deployment with Cluster volume. When would each change your design?
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Blue/green deployment: supports engine/change rehearsal with replication/switchover constraints. Cluster volume: replicated distributed storage is shared by writer/readers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-AURORA-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cluster volume; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` plus recent events/changes, then correlate the service-specific SLI. replicated distributed storage is shared by writer/readers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-02

- [ ] **Question:** Production is degraded around Writer endpoint; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` plus recent events/changes, then correlate the service-specific SLI. follows current writer and should be used for write-capable connections. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Reader endpoint; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-global-clusters` plus recent events/changes, then correlate the service-specific SLI. balances new reader connections but not individual queries or existing sessions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-04

- [ ] **Question:** Production is degraded around Replica failover tier; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-blue-green-deployments` plus recent events/changes, then correlate the service-specific SLI. influences which reader is promoted and how quickly compatible capacity is available. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Aurora Serverless; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` plus recent events/changes, then correlate the service-specific SLI. capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-06

- [ ] **Question:** Production is degraded around Global Database; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` plus recent events/changes, then correlate the service-specific SLI. asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backtrack; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-global-clusters` plus recent events/changes, then correlate the service-specific SLI. supported engines/configs can rewind logical time but it is not a substitute for backup. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-08

- [ ] **Question:** Production is degraded around RDS Proxy/pooling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-blue-green-deployments` plus recent events/changes, then correlate the service-specific SLI. stabilizes connection storms under session/transaction semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Replica lag; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` plus recent events/changes, then correlate the service-specific SLI. long transactions/I/O/load can make readers stale and delay failover readiness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-AURORA-MP-10

- [ ] **Question:** Production is degraded around Blue/green deployment; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` plus recent events/changes, then correlate the service-specific SLI. supports engine/change rehearsal with replication/switchover constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-AURORA-SN-01

- [ ] **Question:** Design a production Amazon Aurora capability where Cluster volume, Replica failover tier and Backtrack are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: replicated distributed storage is shared by writer/readers. influences which reader is promoted and how quickly compatible capacity is available. supported engines/configs can rewind logical time but it is not a substitute for backup. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Aurora capability where Writer endpoint, Aurora Serverless and RDS Proxy/pooling are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: follows current writer and should be used for write-capable connections. capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. stabilizes connection storms under session/transaction semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-03

- [ ] **Question:** Design a production Amazon Aurora capability where Reader endpoint, Global Database and Replica lag are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: balances new reader connections but not individual queries or existing sessions. asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. long transactions/I/O/load can make readers stale and delay failover readiness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Aurora capability where Replica failover tier, Backtrack and Blue/green deployment are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: influences which reader is promoted and how quickly compatible capacity is available. supported engines/configs can rewind logical time but it is not a substitute for backup. supports engine/change rehearsal with replication/switchover constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-05

- [ ] **Question:** Design a production Amazon Aurora capability where Aurora Serverless, RDS Proxy/pooling and Cluster volume are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. stabilizes connection storms under session/transaction semantics. replicated distributed storage is shared by writer/readers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Aurora capability where Global Database, Replica lag and Writer endpoint are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. long transactions/I/O/load can make readers stale and delay failover readiness. follows current writer and should be used for write-capable connections. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-07

- [ ] **Question:** Design a production Amazon Aurora capability where Backtrack, Blue/green deployment and Reader endpoint are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported engines/configs can rewind logical time but it is not a substitute for backup. supports engine/change rehearsal with replication/switchover constraints. balances new reader connections but not individual queries or existing sessions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Aurora capability where RDS Proxy/pooling, Cluster volume and Replica failover tier are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stabilizes connection storms under session/transaction semantics. replicated distributed storage is shared by writer/readers. influences which reader is promoted and how quickly compatible capacity is available. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-09

- [ ] **Question:** Design a production Amazon Aurora capability where Replica lag, Writer endpoint and Aurora Serverless are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: long transactions/I/O/load can make readers stale and delay failover readiness. follows current writer and should be used for write-capable connections. capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-AURORA-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Aurora capability where Blue/green deployment, Reader endpoint and Global Database are first-class requirements.
> **Covered in:** [Amazon Aurora — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supports engine/change rehearsal with replication/switchover constraints. balances new reader connections but not individual queries or existing sessions. asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-AURORA-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster volume. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` as one read-only checkpoint, not the whole diagnosis. replicated distributed storage is shared by writer/readers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Writer endpoint. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` as one read-only checkpoint, not the whole diagnosis. follows current writer and should be used for write-capable connections. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reader endpoint. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-global-clusters` as one read-only checkpoint, not the whole diagnosis. balances new reader connections but not individual queries or existing sessions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Replica failover tier. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-blue-green-deployments` as one read-only checkpoint, not the whole diagnosis. influences which reader is promoted and how quickly compatible capacity is available. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Aurora Serverless. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` as one read-only checkpoint, not the whole diagnosis. capacity units/auto-pause/version behavior trade idle cost against scaling/cold response. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Global Database. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` as one read-only checkpoint, not the whole diagnosis. asynchronous cross-Region replication supports DR/read locality with RPO/failback considerations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backtrack. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-global-clusters` as one read-only checkpoint, not the whole diagnosis. supported engines/configs can rewind logical time but it is not a substitute for backup. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RDS Proxy/pooling. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-blue-green-deployments` as one read-only checkpoint, not the whole diagnosis. stabilizes connection storms under session/transaction semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Replica lag. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` as one read-only checkpoint, not the whole diagnosis. long transactions/I/O/load can make readers stale and delay failover readiness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-AURORA-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Blue/green deployment. How do you lead it end to end?
> **Covered in:** [Amazon Aurora — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds failover-db-cluster --db-cluster-identifier CLUSTER` as one read-only checkpoint, not the whole diagnosis. supports engine/change rehearsal with replication/switchover constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon RDS](../01-rds/README.md) · [Study note](README.md) · [Next: Amazon DynamoDB →](../03-dynamodb/README.md)

<!-- reading-navigation:end -->
