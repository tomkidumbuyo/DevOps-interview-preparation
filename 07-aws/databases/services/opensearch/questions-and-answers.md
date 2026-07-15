# Amazon OpenSearch Service — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-OPENSEARCH-SERVICE-JN-01

- [ ] **Question:** What is Index/mapping, and why does it matter in Amazon OpenSearch Service?

**Answer:** schema and analyzers determine searchable fields and cannot always be changed in place. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-OPENSEARCH-SERVICE-JN-02

- [ ] **Question:** What is Primary shard, and why does it matter in Amazon OpenSearch Service?

**Answer:** unit of index distribution whose count affects scale, recovery and overhead. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-OPENSEARCH-SERVICE-JN-03

- [ ] **Question:** What is Replica shard, and why does it matter in Amazon OpenSearch Service?

**Answer:** copies improve availability/read scale when placed on separate nodes/AZs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-OPENSEARCH-SERVICE-JN-04

- [ ] **Question:** What is Cluster manager, and why does it matter in Amazon OpenSearch Service?

**Answer:** coordinates metadata and needs dedicated capacity at production scale. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-OPENSEARCH-SERVICE-JN-05

- [ ] **Question:** What is JVM heap, and why does it matter in Amazon OpenSearch Service?

**Answer:** memory pressure/GC/circuit breakers often fail before disk/CPU averages. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-OPENSEARCH-SERVICE-JN-06

- [ ] **Question:** What is Segment/merge, and why does it matter in Amazon OpenSearch Service?

**Answer:** indexing creates segments and background merging consumes I/O/CPU. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-OPENSEARCH-SERVICE-JN-07

- [ ] **Question:** What is Vector search, and why does it matter in Amazon OpenSearch Service?

**Answer:** dimension/index method/recall/latency/memory and filter behavior need benchmark. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-OPENSEARCH-SERVICE-JN-08

- [ ] **Code:** **Question:** What does `curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty` help you verify for Amazon OpenSearch Service?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: service-managed/manual repositories support recovery but require restore testing.

### AMAZON-OPENSEARCH-SERVICE-JN-09

- [ ] **Code:** **Question:** What does `aws opensearch describe-domain --domain-name DOMAIN` help you verify for Amazon OpenSearch Service?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: IAM/domain policy, network and index/document permissions form layers.

### AMAZON-OPENSEARCH-SERVICE-JN-10

- [ ] **Code:** **Question:** What does `curl -s https://HOST/_cluster/health?pretty` help you verify for Amazon OpenSearch Service?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: too many small shards waste heap; too large slows recovery and relocation.

## Junior — procedural and command questions

### AMAZON-OPENSEARCH-SERVICE-JP-01

- [ ] **Code:** **Question:** A basic Index/mapping check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws opensearch describe-domain --domain-name DOMAIN` and capture exact status/reason/request ID. schema and analyzers determine searchable fields and cannot always be changed in place. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-02

- [ ] **Question:** A basic Primary shard check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s https://HOST/_cluster/health?pretty` and capture exact status/reason/request ID. unit of index distribution whose count affects scale, recovery and overhead. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-03

- [ ] **Question:** A basic Replica shard check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s https://HOST/_cat/shards?v` and capture exact status/reason/request ID. copies improve availability/read scale when placed on separate nodes/AZs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-04

- [ ] **Code:** **Question:** A basic Cluster manager check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty` and capture exact status/reason/request ID. coordinates metadata and needs dedicated capacity at production scale. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-05

- [ ] **Question:** A basic JVM heap check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws opensearch describe-domain --domain-name DOMAIN` and capture exact status/reason/request ID. memory pressure/GC/circuit breakers often fail before disk/CPU averages. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-06

- [ ] **Question:** A basic Segment/merge check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s https://HOST/_cluster/health?pretty` and capture exact status/reason/request ID. indexing creates segments and background merging consumes I/O/CPU. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-07

- [ ] **Code:** **Question:** A basic Vector search check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s https://HOST/_cat/shards?v` and capture exact status/reason/request ID. dimension/index method/recall/latency/memory and filter behavior need benchmark. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-08

- [ ] **Question:** A basic Snapshot check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty` and capture exact status/reason/request ID. service-managed/manual repositories support recovery but require restore testing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-09

- [ ] **Question:** A basic Fine-grained access check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws opensearch describe-domain --domain-name DOMAIN` and capture exact status/reason/request ID. IAM/domain policy, network and index/document permissions form layers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-OPENSEARCH-SERVICE-JP-10

- [ ] **Code:** **Question:** A basic Shard sizing check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s https://HOST/_cluster/health?pretty` and capture exact status/reason/request ID. too many small shards waste heap; too large slows recovery and relocation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-OPENSEARCH-SERVICE-MN-01

- [ ] **Question:** Compare Index/mapping with Primary shard. When would each change your design?

**Answer:** Index/mapping: schema and analyzers determine searchable fields and cannot always be changed in place. Primary shard: unit of index distribution whose count affects scale, recovery and overhead. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-02

- [ ] **Question:** Compare Primary shard with Replica shard. When would each change your design?

**Answer:** Primary shard: unit of index distribution whose count affects scale, recovery and overhead. Replica shard: copies improve availability/read scale when placed on separate nodes/AZs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-03

- [ ] **Question:** Compare Replica shard with Cluster manager. When would each change your design?

**Answer:** Replica shard: copies improve availability/read scale when placed on separate nodes/AZs. Cluster manager: coordinates metadata and needs dedicated capacity at production scale. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-04

- [ ] **Configuration review:** **Question:** Compare Cluster manager with JVM heap. When would each change your design?

**Answer:** Cluster manager: coordinates metadata and needs dedicated capacity at production scale. JVM heap: memory pressure/GC/circuit breakers often fail before disk/CPU averages. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-05

- [ ] **Question:** Compare JVM heap with Segment/merge. When would each change your design?

**Answer:** JVM heap: memory pressure/GC/circuit breakers often fail before disk/CPU averages. Segment/merge: indexing creates segments and background merging consumes I/O/CPU. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-06

- [ ] **Question:** Compare Segment/merge with Vector search. When would each change your design?

**Answer:** Segment/merge: indexing creates segments and background merging consumes I/O/CPU. Vector search: dimension/index method/recall/latency/memory and filter behavior need benchmark. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-07

- [ ] **Configuration review:** **Question:** Compare Vector search with Snapshot. When would each change your design?

**Answer:** Vector search: dimension/index method/recall/latency/memory and filter behavior need benchmark. Snapshot: service-managed/manual repositories support recovery but require restore testing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-08

- [ ] **Question:** Compare Snapshot with Fine-grained access. When would each change your design?

**Answer:** Snapshot: service-managed/manual repositories support recovery but require restore testing. Fine-grained access: IAM/domain policy, network and index/document permissions form layers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-09

- [ ] **Question:** Compare Fine-grained access with Shard sizing. When would each change your design?

**Answer:** Fine-grained access: IAM/domain policy, network and index/document permissions form layers. Shard sizing: too many small shards waste heap; too large slows recovery and relocation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-OPENSEARCH-SERVICE-MN-10

- [ ] **Configuration review:** **Question:** Compare Shard sizing with Index/mapping. When would each change your design?

**Answer:** Shard sizing: too many small shards waste heap; too large slows recovery and relocation. Index/mapping: schema and analyzers determine searchable fields and cannot always be changed in place. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-OPENSEARCH-SERVICE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Index/mapping; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws opensearch describe-domain --domain-name DOMAIN` plus recent events/changes, then correlate the service-specific SLI. schema and analyzers determine searchable fields and cannot always be changed in place. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-02

- [ ] **Question:** Production is degraded around Primary shard; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s https://HOST/_cluster/health?pretty` plus recent events/changes, then correlate the service-specific SLI. unit of index distribution whose count affects scale, recovery and overhead. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Replica shard; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s https://HOST/_cat/shards?v` plus recent events/changes, then correlate the service-specific SLI. copies improve availability/read scale when placed on separate nodes/AZs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-04

- [ ] **Question:** Production is degraded around Cluster manager; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty` plus recent events/changes, then correlate the service-specific SLI. coordinates metadata and needs dedicated capacity at production scale. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around JVM heap; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws opensearch describe-domain --domain-name DOMAIN` plus recent events/changes, then correlate the service-specific SLI. memory pressure/GC/circuit breakers often fail before disk/CPU averages. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-06

- [ ] **Question:** Production is degraded around Segment/merge; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s https://HOST/_cluster/health?pretty` plus recent events/changes, then correlate the service-specific SLI. indexing creates segments and background merging consumes I/O/CPU. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Vector search; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s https://HOST/_cat/shards?v` plus recent events/changes, then correlate the service-specific SLI. dimension/index method/recall/latency/memory and filter behavior need benchmark. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-08

- [ ] **Question:** Production is degraded around Snapshot; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty` plus recent events/changes, then correlate the service-specific SLI. service-managed/manual repositories support recovery but require restore testing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Fine-grained access; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws opensearch describe-domain --domain-name DOMAIN` plus recent events/changes, then correlate the service-specific SLI. IAM/domain policy, network and index/document permissions form layers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-OPENSEARCH-SERVICE-MP-10

- [ ] **Question:** Production is degraded around Shard sizing; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s https://HOST/_cluster/health?pretty` plus recent events/changes, then correlate the service-specific SLI. too many small shards waste heap; too large slows recovery and relocation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-OPENSEARCH-SERVICE-SN-01

- [ ] **Question:** Design a production Amazon OpenSearch Service capability where Index/mapping, Cluster manager and Vector search are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: schema and analyzers determine searchable fields and cannot always be changed in place. coordinates metadata and needs dedicated capacity at production scale. dimension/index method/recall/latency/memory and filter behavior need benchmark. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon OpenSearch Service capability where Primary shard, JVM heap and Snapshot are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: unit of index distribution whose count affects scale, recovery and overhead. memory pressure/GC/circuit breakers often fail before disk/CPU averages. service-managed/manual repositories support recovery but require restore testing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-03

- [ ] **Question:** Design a production Amazon OpenSearch Service capability where Replica shard, Segment/merge and Fine-grained access are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: copies improve availability/read scale when placed on separate nodes/AZs. indexing creates segments and background merging consumes I/O/CPU. IAM/domain policy, network and index/document permissions form layers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon OpenSearch Service capability where Cluster manager, Vector search and Shard sizing are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: coordinates metadata and needs dedicated capacity at production scale. dimension/index method/recall/latency/memory and filter behavior need benchmark. too many small shards waste heap; too large slows recovery and relocation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-05

- [ ] **Question:** Design a production Amazon OpenSearch Service capability where JVM heap, Snapshot and Index/mapping are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: memory pressure/GC/circuit breakers often fail before disk/CPU averages. service-managed/manual repositories support recovery but require restore testing. schema and analyzers determine searchable fields and cannot always be changed in place. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon OpenSearch Service capability where Segment/merge, Fine-grained access and Primary shard are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: indexing creates segments and background merging consumes I/O/CPU. IAM/domain policy, network and index/document permissions form layers. unit of index distribution whose count affects scale, recovery and overhead. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-07

- [ ] **Question:** Design a production Amazon OpenSearch Service capability where Vector search, Shard sizing and Replica shard are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: dimension/index method/recall/latency/memory and filter behavior need benchmark. too many small shards waste heap; too large slows recovery and relocation. copies improve availability/read scale when placed on separate nodes/AZs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon OpenSearch Service capability where Snapshot, Index/mapping and Cluster manager are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: service-managed/manual repositories support recovery but require restore testing. schema and analyzers determine searchable fields and cannot always be changed in place. coordinates metadata and needs dedicated capacity at production scale. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-09

- [ ] **Question:** Design a production Amazon OpenSearch Service capability where Fine-grained access, Primary shard and JVM heap are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: IAM/domain policy, network and index/document permissions form layers. unit of index distribution whose count affects scale, recovery and overhead. memory pressure/GC/circuit breakers often fail before disk/CPU averages. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-OPENSEARCH-SERVICE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon OpenSearch Service capability where Shard sizing, Replica shard and Segment/merge are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: too many small shards waste heap; too large slows recovery and relocation. copies improve availability/read scale when placed on separate nodes/AZs. indexing creates segments and background merging consumes I/O/CPU. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-OPENSEARCH-SERVICE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Index/mapping. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws opensearch describe-domain --domain-name DOMAIN` as one read-only checkpoint, not the whole diagnosis. schema and analyzers determine searchable fields and cannot always be changed in place. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Primary shard. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s https://HOST/_cluster/health?pretty` as one read-only checkpoint, not the whole diagnosis. unit of index distribution whose count affects scale, recovery and overhead. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Replica shard. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s https://HOST/_cat/shards?v` as one read-only checkpoint, not the whole diagnosis. copies improve availability/read scale when placed on separate nodes/AZs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster manager. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty` as one read-only checkpoint, not the whole diagnosis. coordinates metadata and needs dedicated capacity at production scale. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving JVM heap. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws opensearch describe-domain --domain-name DOMAIN` as one read-only checkpoint, not the whole diagnosis. memory pressure/GC/circuit breakers often fail before disk/CPU averages. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Segment/merge. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s https://HOST/_cluster/health?pretty` as one read-only checkpoint, not the whole diagnosis. indexing creates segments and background merging consumes I/O/CPU. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Vector search. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s https://HOST/_cat/shards?v` as one read-only checkpoint, not the whole diagnosis. dimension/index method/recall/latency/memory and filter behavior need benchmark. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Snapshot. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s https://HOST/_nodes/stats/jvm,fs,indices?pretty` as one read-only checkpoint, not the whole diagnosis. service-managed/manual repositories support recovery but require restore testing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fine-grained access. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws opensearch describe-domain --domain-name DOMAIN` as one read-only checkpoint, not the whole diagnosis. IAM/domain policy, network and index/document permissions form layers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-OPENSEARCH-SERVICE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Shard sizing. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s https://HOST/_cluster/health?pretty` as one read-only checkpoint, not the whole diagnosis. too many small shards waste heap; too large slows recovery and relocation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
