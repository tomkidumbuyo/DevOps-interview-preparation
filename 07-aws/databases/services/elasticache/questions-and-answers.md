# Amazon ElastiCache — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-ELASTICACHE-JN-01

- [ ] **Question:** What is Valkey/Redis replication group, and why does it matter in Amazon ElastiCache?

**Answer:** primary and replicas provide failover/read paths under node/AZ design. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ELASTICACHE-JN-02

- [ ] **Question:** What is Cluster mode, and why does it matter in Amazon ElastiCache?

**Answer:** shards keys across node groups and requires compatible clients/key strategy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ELASTICACHE-JN-03

- [ ] **Question:** What is Memcached, and why does it matter in Amazon ElastiCache?

**Answer:** simple distributed cache lacks Redis-style replication/persistence structures. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ELASTICACHE-JN-04

- [ ] **Question:** What is Eviction policy, and why does it matter in Amazon ElastiCache?

**Answer:** determines which keys are removed under max memory and can affect correctness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ELASTICACHE-JN-05

- [ ] **Question:** What is TTL, and why does it matter in Amazon ElastiCache?

**Answer:** bounds staleness/memory but synchronized expiry can cause stampedes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ELASTICACHE-JN-06

- [ ] **Question:** What is Persistence/backup, and why does it matter in Amazon ElastiCache?

**Answer:** snapshots/AOF support differs and a cache should not silently become source of truth. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ELASTICACHE-JN-07

- [ ] **Question:** What is Failover, and why does it matter in Amazon ElastiCache?

**Answer:** endpoint/client reconnect and data loss windows must be tested. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ELASTICACHE-JN-08

- [ ] **Code:** **Question:** What does `redis-cli --tls -h HOST SLOWLOG GET 20` help you verify for Amazon ElastiCache?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases.

### AMAZON-ELASTICACHE-JN-09

- [ ] **Code:** **Question:** What does `aws elasticache describe-replication-groups` help you verify for Amazon ElastiCache?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: one key can saturate a shard despite free aggregate capacity.

### AMAZON-ELASTICACHE-JN-10

- [ ] **Code:** **Question:** What does `aws elasticache describe-cache-clusters --show-cache-node-info` help you verify for Amazon ElastiCache?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: TLS, auth tokens/IAM features and subnet/SG protect access under client support.

## Junior — procedural and command questions

### AMAZON-ELASTICACHE-JP-01

- [ ] **Code:** **Question:** A basic Valkey/Redis replication group check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elasticache describe-replication-groups` and capture exact status/reason/request ID. primary and replicas provide failover/read paths under node/AZ design. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-02

- [ ] **Question:** A basic Cluster mode check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elasticache describe-cache-clusters --show-cache-node-info` and capture exact status/reason/request ID. shards keys across node groups and requires compatible clients/key strategy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-03

- [ ] **Question:** A basic Memcached check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `redis-cli --tls -h HOST INFO` and capture exact status/reason/request ID. simple distributed cache lacks Redis-style replication/persistence structures. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-04

- [ ] **Code:** **Question:** A basic Eviction policy check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `redis-cli --tls -h HOST SLOWLOG GET 20` and capture exact status/reason/request ID. determines which keys are removed under max memory and can affect correctness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-05

- [ ] **Question:** A basic TTL check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elasticache describe-replication-groups` and capture exact status/reason/request ID. bounds staleness/memory but synchronized expiry can cause stampedes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-06

- [ ] **Question:** A basic Persistence/backup check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elasticache describe-cache-clusters --show-cache-node-info` and capture exact status/reason/request ID. snapshots/AOF support differs and a cache should not silently become source of truth. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-07

- [ ] **Code:** **Question:** A basic Failover check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `redis-cli --tls -h HOST INFO` and capture exact status/reason/request ID. endpoint/client reconnect and data loss windows must be tested. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-08

- [ ] **Question:** A basic Cache stampede check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `redis-cli --tls -h HOST SLOWLOG GET 20` and capture exact status/reason/request ID. coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-09

- [ ] **Question:** A basic Hot key check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elasticache describe-replication-groups` and capture exact status/reason/request ID. one key can saturate a shard despite free aggregate capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ELASTICACHE-JP-10

- [ ] **Code:** **Question:** A basic Encryption/auth check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elasticache describe-cache-clusters --show-cache-node-info` and capture exact status/reason/request ID. TLS, auth tokens/IAM features and subnet/SG protect access under client support. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-ELASTICACHE-MN-01

- [ ] **Question:** Compare Valkey/Redis replication group with Cluster mode. When would each change your design?

**Answer:** Valkey/Redis replication group: primary and replicas provide failover/read paths under node/AZ design. Cluster mode: shards keys across node groups and requires compatible clients/key strategy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-02

- [ ] **Question:** Compare Cluster mode with Memcached. When would each change your design?

**Answer:** Cluster mode: shards keys across node groups and requires compatible clients/key strategy. Memcached: simple distributed cache lacks Redis-style replication/persistence structures. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-03

- [ ] **Question:** Compare Memcached with Eviction policy. When would each change your design?

**Answer:** Memcached: simple distributed cache lacks Redis-style replication/persistence structures. Eviction policy: determines which keys are removed under max memory and can affect correctness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-04

- [ ] **Configuration review:** **Question:** Compare Eviction policy with TTL. When would each change your design?

**Answer:** Eviction policy: determines which keys are removed under max memory and can affect correctness. TTL: bounds staleness/memory but synchronized expiry can cause stampedes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-05

- [ ] **Question:** Compare TTL with Persistence/backup. When would each change your design?

**Answer:** TTL: bounds staleness/memory but synchronized expiry can cause stampedes. Persistence/backup: snapshots/AOF support differs and a cache should not silently become source of truth. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-06

- [ ] **Question:** Compare Persistence/backup with Failover. When would each change your design?

**Answer:** Persistence/backup: snapshots/AOF support differs and a cache should not silently become source of truth. Failover: endpoint/client reconnect and data loss windows must be tested. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-07

- [ ] **Configuration review:** **Question:** Compare Failover with Cache stampede. When would each change your design?

**Answer:** Failover: endpoint/client reconnect and data loss windows must be tested. Cache stampede: coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-08

- [ ] **Question:** Compare Cache stampede with Hot key. When would each change your design?

**Answer:** Cache stampede: coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases. Hot key: one key can saturate a shard despite free aggregate capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-09

- [ ] **Question:** Compare Hot key with Encryption/auth. When would each change your design?

**Answer:** Hot key: one key can saturate a shard despite free aggregate capacity. Encryption/auth: TLS, auth tokens/IAM features and subnet/SG protect access under client support. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ELASTICACHE-MN-10

- [ ] **Configuration review:** **Question:** Compare Encryption/auth with Valkey/Redis replication group. When would each change your design?

**Answer:** Encryption/auth: TLS, auth tokens/IAM features and subnet/SG protect access under client support. Valkey/Redis replication group: primary and replicas provide failover/read paths under node/AZ design. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-ELASTICACHE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Valkey/Redis replication group; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elasticache describe-replication-groups` plus recent events/changes, then correlate the service-specific SLI. primary and replicas provide failover/read paths under node/AZ design. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-02

- [ ] **Question:** Production is degraded around Cluster mode; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elasticache describe-cache-clusters --show-cache-node-info` plus recent events/changes, then correlate the service-specific SLI. shards keys across node groups and requires compatible clients/key strategy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Memcached; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `redis-cli --tls -h HOST INFO` plus recent events/changes, then correlate the service-specific SLI. simple distributed cache lacks Redis-style replication/persistence structures. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-04

- [ ] **Question:** Production is degraded around Eviction policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `redis-cli --tls -h HOST SLOWLOG GET 20` plus recent events/changes, then correlate the service-specific SLI. determines which keys are removed under max memory and can affect correctness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around TTL; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elasticache describe-replication-groups` plus recent events/changes, then correlate the service-specific SLI. bounds staleness/memory but synchronized expiry can cause stampedes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-06

- [ ] **Question:** Production is degraded around Persistence/backup; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elasticache describe-cache-clusters --show-cache-node-info` plus recent events/changes, then correlate the service-specific SLI. snapshots/AOF support differs and a cache should not silently become source of truth. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Failover; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `redis-cli --tls -h HOST INFO` plus recent events/changes, then correlate the service-specific SLI. endpoint/client reconnect and data loss windows must be tested. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-08

- [ ] **Question:** Production is degraded around Cache stampede; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `redis-cli --tls -h HOST SLOWLOG GET 20` plus recent events/changes, then correlate the service-specific SLI. coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Hot key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elasticache describe-replication-groups` plus recent events/changes, then correlate the service-specific SLI. one key can saturate a shard despite free aggregate capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ELASTICACHE-MP-10

- [ ] **Question:** Production is degraded around Encryption/auth; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elasticache describe-cache-clusters --show-cache-node-info` plus recent events/changes, then correlate the service-specific SLI. TLS, auth tokens/IAM features and subnet/SG protect access under client support. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-ELASTICACHE-SN-01

- [ ] **Question:** Design a production Amazon ElastiCache capability where Valkey/Redis replication group, Eviction policy and Failover are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: primary and replicas provide failover/read paths under node/AZ design. determines which keys are removed under max memory and can affect correctness. endpoint/client reconnect and data loss windows must be tested. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ElastiCache capability where Cluster mode, TTL and Cache stampede are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shards keys across node groups and requires compatible clients/key strategy. bounds staleness/memory but synchronized expiry can cause stampedes. coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-03

- [ ] **Question:** Design a production Amazon ElastiCache capability where Memcached, Persistence/backup and Hot key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: simple distributed cache lacks Redis-style replication/persistence structures. snapshots/AOF support differs and a cache should not silently become source of truth. one key can saturate a shard despite free aggregate capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ElastiCache capability where Eviction policy, Failover and Encryption/auth are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: determines which keys are removed under max memory and can affect correctness. endpoint/client reconnect and data loss windows must be tested. TLS, auth tokens/IAM features and subnet/SG protect access under client support. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-05

- [ ] **Question:** Design a production Amazon ElastiCache capability where TTL, Cache stampede and Valkey/Redis replication group are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bounds staleness/memory but synchronized expiry can cause stampedes. coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases. primary and replicas provide failover/read paths under node/AZ design. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ElastiCache capability where Persistence/backup, Hot key and Cluster mode are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: snapshots/AOF support differs and a cache should not silently become source of truth. one key can saturate a shard despite free aggregate capacity. shards keys across node groups and requires compatible clients/key strategy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-07

- [ ] **Question:** Design a production Amazon ElastiCache capability where Failover, Encryption/auth and Memcached are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: endpoint/client reconnect and data loss windows must be tested. TLS, auth tokens/IAM features and subnet/SG protect access under client support. simple distributed cache lacks Redis-style replication/persistence structures. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ElastiCache capability where Cache stampede, Valkey/Redis replication group and Eviction policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases. primary and replicas provide failover/read paths under node/AZ design. determines which keys are removed under max memory and can affect correctness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-09

- [ ] **Question:** Design a production Amazon ElastiCache capability where Hot key, Cluster mode and TTL are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: one key can saturate a shard despite free aggregate capacity. shards keys across node groups and requires compatible clients/key strategy. bounds staleness/memory but synchronized expiry can cause stampedes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ELASTICACHE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ElastiCache capability where Encryption/auth, Memcached and Persistence/backup are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: TLS, auth tokens/IAM features and subnet/SG protect access under client support. simple distributed cache lacks Redis-style replication/persistence structures. snapshots/AOF support differs and a cache should not silently become source of truth. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-ELASTICACHE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Valkey/Redis replication group. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elasticache describe-replication-groups` as one read-only checkpoint, not the whole diagnosis. primary and replicas provide failover/read paths under node/AZ design. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster mode. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elasticache describe-cache-clusters --show-cache-node-info` as one read-only checkpoint, not the whole diagnosis. shards keys across node groups and requires compatible clients/key strategy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Memcached. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `redis-cli --tls -h HOST INFO` as one read-only checkpoint, not the whole diagnosis. simple distributed cache lacks Redis-style replication/persistence structures. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Eviction policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `redis-cli --tls -h HOST SLOWLOG GET 20` as one read-only checkpoint, not the whole diagnosis. determines which keys are removed under max memory and can affect correctness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TTL. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elasticache describe-replication-groups` as one read-only checkpoint, not the whole diagnosis. bounds staleness/memory but synchronized expiry can cause stampedes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Persistence/backup. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elasticache describe-cache-clusters --show-cache-node-info` as one read-only checkpoint, not the whole diagnosis. snapshots/AOF support differs and a cache should not silently become source of truth. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Failover. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `redis-cli --tls -h HOST INFO` as one read-only checkpoint, not the whole diagnosis. endpoint/client reconnect and data loss windows must be tested. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cache stampede. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `redis-cli --tls -h HOST SLOWLOG GET 20` as one read-only checkpoint, not the whole diagnosis. coalescing, jitter, soft TTL and stale-while-revalidate protect downstream databases. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hot key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elasticache describe-replication-groups` as one read-only checkpoint, not the whole diagnosis. one key can saturate a shard despite free aggregate capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ELASTICACHE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Encryption/auth. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elasticache describe-cache-clusters --show-cache-node-info` as one read-only checkpoint, not the whole diagnosis. TLS, auth tokens/IAM features and subnet/SG protect access under client support. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
