# Databases — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-DATABASES-JN-01

- [ ] **Question:** What is DB instance, and why does it matter in Databases?

**Answer:** managed engine compute/storage inside subnet/parameter/security configuration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-DATABASES-JN-02

- [ ] **Question:** What is Multi-AZ, and why does it matter in Databases?

**Answer:** synchronous standby/failover for availability rather than read scaling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-DATABASES-JN-03

- [ ] **Question:** What is Cluster volume, and why does it matter in Databases?

**Answer:** replicated distributed storage is shared by writer/readers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-DATABASES-JN-04

- [ ] **Question:** What is Writer endpoint, and why does it matter in Databases?

**Answer:** follows current writer and should be used for write-capable connections. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-DATABASES-JN-05

- [ ] **Question:** What is Partition key, and why does it matter in Databases?

**Answer:** hashes items across physical partitions and must distribute request volume. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-DATABASES-JN-06

- [ ] **Question:** What is Sort key, and why does it matter in Databases?

**Answer:** orders items within a partition and enables range/prefix access patterns. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-DATABASES-JN-07

- [ ] **Question:** What is Valkey/Redis replication group, and why does it matter in Databases?

**Answer:** primary and replicas provide failover/read paths under node/AZ design. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-DATABASES-JN-08

- [ ] **Code:** **Question:** What does `aws dynamodb describe-table --table-name TABLE` help you verify for Databases?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: shards keys across node groups and requires compatible clients/key strategy.

### BRANCH-DATABASES-JN-09

- [ ] **Code:** **Question:** What does `aws elasticache describe-replication-groups` help you verify for Databases?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: schema and analyzers determine searchable fields and cannot always be changed in place.

### BRANCH-DATABASES-JN-10

- [ ] **Code:** **Question:** What does `aws opensearch describe-domain --domain-name DOMAIN` help you verify for Databases?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: unit of index distribution whose count affects scale, recovery and overhead.

## Junior — procedural and command questions

### BRANCH-DATABASES-JP-01

- [ ] **Code:** **Question:** A basic DB instance check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-instances --db-instance-identifier DB` and capture exact status/reason/request ID. managed engine compute/storage inside subnet/parameter/security configuration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-02

- [ ] **Question:** A basic Multi-AZ check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` and capture exact status/reason/request ID. synchronous standby/failover for availability rather than read scaling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-03

- [ ] **Question:** A basic Cluster volume check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-table --table-name TABLE` and capture exact status/reason/request ID. replicated distributed storage is shared by writer/readers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-04

- [ ] **Code:** **Question:** A basic Writer endpoint check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elasticache describe-replication-groups` and capture exact status/reason/request ID. follows current writer and should be used for write-capable connections. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-05

- [ ] **Question:** A basic Partition key check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws opensearch describe-domain --domain-name DOMAIN` and capture exact status/reason/request ID. hashes items across physical partitions and must distribute request volume. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-06

- [ ] **Question:** A basic Sort key check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-instances --db-instance-identifier DB` and capture exact status/reason/request ID. orders items within a partition and enables range/prefix access patterns. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-07

- [ ] **Code:** **Question:** A basic Valkey/Redis replication group check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` and capture exact status/reason/request ID. primary and replicas provide failover/read paths under node/AZ design. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-08

- [ ] **Question:** A basic Cluster mode check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-table --table-name TABLE` and capture exact status/reason/request ID. shards keys across node groups and requires compatible clients/key strategy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-09

- [ ] **Question:** A basic Index/mapping check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elasticache describe-replication-groups` and capture exact status/reason/request ID. schema and analyzers determine searchable fields and cannot always be changed in place. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-DATABASES-JP-10

- [ ] **Code:** **Question:** A basic Primary shard check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws opensearch describe-domain --domain-name DOMAIN` and capture exact status/reason/request ID. unit of index distribution whose count affects scale, recovery and overhead. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-DATABASES-MN-01

- [ ] **Question:** Compare DB instance with Multi-AZ. When would each change your design?

**Answer:** DB instance: managed engine compute/storage inside subnet/parameter/security configuration. Multi-AZ: synchronous standby/failover for availability rather than read scaling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-02

- [ ] **Question:** Compare Multi-AZ with Cluster volume. When would each change your design?

**Answer:** Multi-AZ: synchronous standby/failover for availability rather than read scaling. Cluster volume: replicated distributed storage is shared by writer/readers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-03

- [ ] **Question:** Compare Cluster volume with Writer endpoint. When would each change your design?

**Answer:** Cluster volume: replicated distributed storage is shared by writer/readers. Writer endpoint: follows current writer and should be used for write-capable connections. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-04

- [ ] **Configuration review:** **Question:** Compare Writer endpoint with Partition key. When would each change your design?

**Answer:** Writer endpoint: follows current writer and should be used for write-capable connections. Partition key: hashes items across physical partitions and must distribute request volume. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-05

- [ ] **Question:** Compare Partition key with Sort key. When would each change your design?

**Answer:** Partition key: hashes items across physical partitions and must distribute request volume. Sort key: orders items within a partition and enables range/prefix access patterns. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-06

- [ ] **Question:** Compare Sort key with Valkey/Redis replication group. When would each change your design?

**Answer:** Sort key: orders items within a partition and enables range/prefix access patterns. Valkey/Redis replication group: primary and replicas provide failover/read paths under node/AZ design. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-07

- [ ] **Configuration review:** **Question:** Compare Valkey/Redis replication group with Cluster mode. When would each change your design?

**Answer:** Valkey/Redis replication group: primary and replicas provide failover/read paths under node/AZ design. Cluster mode: shards keys across node groups and requires compatible clients/key strategy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-08

- [ ] **Question:** Compare Cluster mode with Index/mapping. When would each change your design?

**Answer:** Cluster mode: shards keys across node groups and requires compatible clients/key strategy. Index/mapping: schema and analyzers determine searchable fields and cannot always be changed in place. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-09

- [ ] **Question:** Compare Index/mapping with Primary shard. When would each change your design?

**Answer:** Index/mapping: schema and analyzers determine searchable fields and cannot always be changed in place. Primary shard: unit of index distribution whose count affects scale, recovery and overhead. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-DATABASES-MN-10

- [ ] **Configuration review:** **Question:** Compare Primary shard with DB instance. When would each change your design?

**Answer:** Primary shard: unit of index distribution whose count affects scale, recovery and overhead. DB instance: managed engine compute/storage inside subnet/parameter/security configuration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-DATABASES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around DB instance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-instances --db-instance-identifier DB` plus recent events/changes, then correlate the service-specific SLI. managed engine compute/storage inside subnet/parameter/security configuration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-02

- [ ] **Question:** Production is degraded around Multi-AZ; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` plus recent events/changes, then correlate the service-specific SLI. synchronous standby/failover for availability rather than read scaling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cluster volume; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-table --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. replicated distributed storage is shared by writer/readers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-04

- [ ] **Question:** Production is degraded around Writer endpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elasticache describe-replication-groups` plus recent events/changes, then correlate the service-specific SLI. follows current writer and should be used for write-capable connections. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Partition key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws opensearch describe-domain --domain-name DOMAIN` plus recent events/changes, then correlate the service-specific SLI. hashes items across physical partitions and must distribute request volume. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-06

- [ ] **Question:** Production is degraded around Sort key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-instances --db-instance-identifier DB` plus recent events/changes, then correlate the service-specific SLI. orders items within a partition and enables range/prefix access patterns. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Valkey/Redis replication group; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` plus recent events/changes, then correlate the service-specific SLI. primary and replicas provide failover/read paths under node/AZ design. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-08

- [ ] **Question:** Production is degraded around Cluster mode; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-table --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. shards keys across node groups and requires compatible clients/key strategy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Index/mapping; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elasticache describe-replication-groups` plus recent events/changes, then correlate the service-specific SLI. schema and analyzers determine searchable fields and cannot always be changed in place. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-DATABASES-MP-10

- [ ] **Question:** Production is degraded around Primary shard; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws opensearch describe-domain --domain-name DOMAIN` plus recent events/changes, then correlate the service-specific SLI. unit of index distribution whose count affects scale, recovery and overhead. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-DATABASES-SN-01

- [ ] **Question:** Design a production Databases capability where DB instance, Writer endpoint and Valkey/Redis replication group are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed engine compute/storage inside subnet/parameter/security configuration. follows current writer and should be used for write-capable connections. primary and replicas provide failover/read paths under node/AZ design. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Databases capability where Multi-AZ, Partition key and Cluster mode are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: synchronous standby/failover for availability rather than read scaling. hashes items across physical partitions and must distribute request volume. shards keys across node groups and requires compatible clients/key strategy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-03

- [ ] **Question:** Design a production Databases capability where Cluster volume, Sort key and Index/mapping are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: replicated distributed storage is shared by writer/readers. orders items within a partition and enables range/prefix access patterns. schema and analyzers determine searchable fields and cannot always be changed in place. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Databases capability where Writer endpoint, Valkey/Redis replication group and Primary shard are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: follows current writer and should be used for write-capable connections. primary and replicas provide failover/read paths under node/AZ design. unit of index distribution whose count affects scale, recovery and overhead. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-05

- [ ] **Question:** Design a production Databases capability where Partition key, Cluster mode and DB instance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: hashes items across physical partitions and must distribute request volume. shards keys across node groups and requires compatible clients/key strategy. managed engine compute/storage inside subnet/parameter/security configuration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Databases capability where Sort key, Index/mapping and Multi-AZ are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: orders items within a partition and enables range/prefix access patterns. schema and analyzers determine searchable fields and cannot always be changed in place. synchronous standby/failover for availability rather than read scaling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-07

- [ ] **Question:** Design a production Databases capability where Valkey/Redis replication group, Primary shard and Cluster volume are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: primary and replicas provide failover/read paths under node/AZ design. unit of index distribution whose count affects scale, recovery and overhead. replicated distributed storage is shared by writer/readers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Databases capability where Cluster mode, DB instance and Writer endpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shards keys across node groups and requires compatible clients/key strategy. managed engine compute/storage inside subnet/parameter/security configuration. follows current writer and should be used for write-capable connections. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-09

- [ ] **Question:** Design a production Databases capability where Index/mapping, Multi-AZ and Partition key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: schema and analyzers determine searchable fields and cannot always be changed in place. synchronous standby/failover for availability rather than read scaling. hashes items across physical partitions and must distribute request volume. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-DATABASES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Databases capability where Primary shard, Cluster volume and Sort key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: unit of index distribution whose count affects scale, recovery and overhead. replicated distributed storage is shared by writer/readers. orders items within a partition and enables range/prefix access patterns. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-DATABASES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DB instance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-instances --db-instance-identifier DB` as one read-only checkpoint, not the whole diagnosis. managed engine compute/storage inside subnet/parameter/security configuration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multi-AZ. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` as one read-only checkpoint, not the whole diagnosis. synchronous standby/failover for availability rather than read scaling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster volume. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-table --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. replicated distributed storage is shared by writer/readers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Writer endpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elasticache describe-replication-groups` as one read-only checkpoint, not the whole diagnosis. follows current writer and should be used for write-capable connections. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Partition key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws opensearch describe-domain --domain-name DOMAIN` as one read-only checkpoint, not the whole diagnosis. hashes items across physical partitions and must distribute request volume. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sort key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-instances --db-instance-identifier DB` as one read-only checkpoint, not the whole diagnosis. orders items within a partition and enables range/prefix access patterns. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Valkey/Redis replication group. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws rds describe-db-clusters --db-cluster-identifier CLUSTER` as one read-only checkpoint, not the whole diagnosis. primary and replicas provide failover/read paths under node/AZ design. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster mode. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-table --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. shards keys across node groups and requires compatible clients/key strategy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Index/mapping. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elasticache describe-replication-groups` as one read-only checkpoint, not the whole diagnosis. schema and analyzers determine searchable fields and cannot always be changed in place. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-DATABASES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Primary shard. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws opensearch describe-domain --domain-name DOMAIN` as one read-only checkpoint, not the whole diagnosis. unit of index distribution whose count affects scale, recovery and overhead. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
