# Kinesis Data Streams and Amazon MSK — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-01

- [ ] **Question:** What is Shard/partition, and why does it matter in Kinesis Data Streams and Amazon MSK?

**Answer:** ordered log unit and primary throughput/parallelism boundary. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-02

- [ ] **Question:** What is Partition key, and why does it matter in Kinesis Data Streams and Amazon MSK?

**Answer:** determines shard/partition and can create hot spots. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-03

- [ ] **Question:** What is Sequence/offset, and why does it matter in Kinesis Data Streams and Amazon MSK?

**Answer:** consumer position supports checkpoint and replay. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-04

- [ ] **Question:** What is Consumer group, and why does it matter in Kinesis Data Streams and Amazon MSK?

**Answer:** Kafka partitions are assigned/rebalanced among group members. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-05

- [ ] **Question:** What is Enhanced fan-out, and why does it matter in Kinesis Data Streams and Amazon MSK?

**Answer:** Kinesis consumers get dedicated throughput under additional cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-06

- [ ] **Question:** What is Retention, and why does it matter in Kinesis Data Streams and Amazon MSK?

**Answer:** bounds replay/recovery and storage cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-07

- [ ] **Question:** What is Lag/iterator age, and why does it matter in Kinesis Data Streams and Amazon MSK?

**Answer:** measures how far consumers are behind and drives capacity response. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-08

- [ ] **Code:** **Question:** What does `kafka-consumer-groups.sh --bootstrap-server BROKERS --describe --group GROUP` help you verify for Kinesis Data Streams and Amazon MSK?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: changes parallelism and ordering/key distribution constraints.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-09

- [ ] **Code:** **Question:** What does `aws kinesis describe-stream-summary --stream-name STREAM` help you verify for Kinesis Data Streams and Amazon MSK?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: broker/partition count, replication and disk headroom affect recovery.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JN-10

- [ ] **Code:** **Question:** What does `aws kinesis list-shards --stream-name STREAM` help you verify for Kinesis Data Streams and Amazon MSK?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: event evolution and at-least-once processing require compatible consumers/effects.

## Junior — procedural and command questions

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-01

- [ ] **Code:** **Question:** A basic Shard/partition check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kinesis describe-stream-summary --stream-name STREAM` and capture exact status/reason/request ID. ordered log unit and primary throughput/parallelism boundary. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-02

- [ ] **Question:** A basic Partition key check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kinesis list-shards --stream-name STREAM` and capture exact status/reason/request ID. determines shard/partition and can create hot spots. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-03

- [ ] **Question:** A basic Sequence/offset check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kafka describe-cluster-v2 --cluster-arn ARN` and capture exact status/reason/request ID. consumer position supports checkpoint and replay. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-04

- [ ] **Code:** **Question:** A basic Consumer group check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kafka-consumer-groups.sh --bootstrap-server BROKERS --describe --group GROUP` and capture exact status/reason/request ID. Kafka partitions are assigned/rebalanced among group members. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-05

- [ ] **Question:** A basic Enhanced fan-out check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kinesis describe-stream-summary --stream-name STREAM` and capture exact status/reason/request ID. Kinesis consumers get dedicated throughput under additional cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-06

- [ ] **Question:** A basic Retention check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kinesis list-shards --stream-name STREAM` and capture exact status/reason/request ID. bounds replay/recovery and storage cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-07

- [ ] **Code:** **Question:** A basic Lag/iterator age check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kafka describe-cluster-v2 --cluster-arn ARN` and capture exact status/reason/request ID. measures how far consumers are behind and drives capacity response. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-08

- [ ] **Question:** A basic Reshard/repartition check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kafka-consumer-groups.sh --bootstrap-server BROKERS --describe --group GROUP` and capture exact status/reason/request ID. changes parallelism and ordering/key distribution constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-09

- [ ] **Question:** A basic MSK broker storage/network check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kinesis describe-stream-summary --stream-name STREAM` and capture exact status/reason/request ID. broker/partition count, replication and disk headroom affect recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-JP-10

- [ ] **Code:** **Question:** A basic Schema/idempotency check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kinesis list-shards --stream-name STREAM` and capture exact status/reason/request ID. event evolution and at-least-once processing require compatible consumers/effects. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-01

- [ ] **Question:** Compare Shard/partition with Partition key. When would each change your design?

**Answer:** Shard/partition: ordered log unit and primary throughput/parallelism boundary. Partition key: determines shard/partition and can create hot spots. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-02

- [ ] **Question:** Compare Partition key with Sequence/offset. When would each change your design?

**Answer:** Partition key: determines shard/partition and can create hot spots. Sequence/offset: consumer position supports checkpoint and replay. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-03

- [ ] **Question:** Compare Sequence/offset with Consumer group. When would each change your design?

**Answer:** Sequence/offset: consumer position supports checkpoint and replay. Consumer group: Kafka partitions are assigned/rebalanced among group members. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-04

- [ ] **Configuration review:** **Question:** Compare Consumer group with Enhanced fan-out. When would each change your design?

**Answer:** Consumer group: Kafka partitions are assigned/rebalanced among group members. Enhanced fan-out: Kinesis consumers get dedicated throughput under additional cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-05

- [ ] **Question:** Compare Enhanced fan-out with Retention. When would each change your design?

**Answer:** Enhanced fan-out: Kinesis consumers get dedicated throughput under additional cost. Retention: bounds replay/recovery and storage cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-06

- [ ] **Question:** Compare Retention with Lag/iterator age. When would each change your design?

**Answer:** Retention: bounds replay/recovery and storage cost. Lag/iterator age: measures how far consumers are behind and drives capacity response. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-07

- [ ] **Configuration review:** **Question:** Compare Lag/iterator age with Reshard/repartition. When would each change your design?

**Answer:** Lag/iterator age: measures how far consumers are behind and drives capacity response. Reshard/repartition: changes parallelism and ordering/key distribution constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-08

- [ ] **Question:** Compare Reshard/repartition with MSK broker storage/network. When would each change your design?

**Answer:** Reshard/repartition: changes parallelism and ordering/key distribution constraints. MSK broker storage/network: broker/partition count, replication and disk headroom affect recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-09

- [ ] **Question:** Compare MSK broker storage/network with Schema/idempotency. When would each change your design?

**Answer:** MSK broker storage/network: broker/partition count, replication and disk headroom affect recovery. Schema/idempotency: event evolution and at-least-once processing require compatible consumers/effects. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MN-10

- [ ] **Configuration review:** **Question:** Compare Schema/idempotency with Shard/partition. When would each change your design?

**Answer:** Schema/idempotency: event evolution and at-least-once processing require compatible consumers/effects. Shard/partition: ordered log unit and primary throughput/parallelism boundary. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Shard/partition; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kinesis describe-stream-summary --stream-name STREAM` plus recent events/changes, then correlate the service-specific SLI. ordered log unit and primary throughput/parallelism boundary. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-02

- [ ] **Question:** Production is degraded around Partition key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kinesis list-shards --stream-name STREAM` plus recent events/changes, then correlate the service-specific SLI. determines shard/partition and can create hot spots. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Sequence/offset; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kafka describe-cluster-v2 --cluster-arn ARN` plus recent events/changes, then correlate the service-specific SLI. consumer position supports checkpoint and replay. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-04

- [ ] **Question:** Production is degraded around Consumer group; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kafka-consumer-groups.sh --bootstrap-server BROKERS --describe --group GROUP` plus recent events/changes, then correlate the service-specific SLI. Kafka partitions are assigned/rebalanced among group members. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Enhanced fan-out; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kinesis describe-stream-summary --stream-name STREAM` plus recent events/changes, then correlate the service-specific SLI. Kinesis consumers get dedicated throughput under additional cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-06

- [ ] **Question:** Production is degraded around Retention; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kinesis list-shards --stream-name STREAM` plus recent events/changes, then correlate the service-specific SLI. bounds replay/recovery and storage cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Lag/iterator age; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kafka describe-cluster-v2 --cluster-arn ARN` plus recent events/changes, then correlate the service-specific SLI. measures how far consumers are behind and drives capacity response. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-08

- [ ] **Question:** Production is degraded around Reshard/repartition; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kafka-consumer-groups.sh --bootstrap-server BROKERS --describe --group GROUP` plus recent events/changes, then correlate the service-specific SLI. changes parallelism and ordering/key distribution constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around MSK broker storage/network; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kinesis describe-stream-summary --stream-name STREAM` plus recent events/changes, then correlate the service-specific SLI. broker/partition count, replication and disk headroom affect recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-MP-10

- [ ] **Question:** Production is degraded around Schema/idempotency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kinesis list-shards --stream-name STREAM` plus recent events/changes, then correlate the service-specific SLI. event evolution and at-least-once processing require compatible consumers/effects. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-01

- [ ] **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Shard/partition, Consumer group and Lag/iterator age are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered log unit and primary throughput/parallelism boundary. Kafka partitions are assigned/rebalanced among group members. measures how far consumers are behind and drives capacity response. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Partition key, Enhanced fan-out and Reshard/repartition are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: determines shard/partition and can create hot spots. Kinesis consumers get dedicated throughput under additional cost. changes parallelism and ordering/key distribution constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-03

- [ ] **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Sequence/offset, Retention and MSK broker storage/network are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: consumer position supports checkpoint and replay. bounds replay/recovery and storage cost. broker/partition count, replication and disk headroom affect recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Consumer group, Lag/iterator age and Schema/idempotency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Kafka partitions are assigned/rebalanced among group members. measures how far consumers are behind and drives capacity response. event evolution and at-least-once processing require compatible consumers/effects. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-05

- [ ] **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Enhanced fan-out, Reshard/repartition and Shard/partition are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Kinesis consumers get dedicated throughput under additional cost. changes parallelism and ordering/key distribution constraints. ordered log unit and primary throughput/parallelism boundary. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Retention, MSK broker storage/network and Partition key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bounds replay/recovery and storage cost. broker/partition count, replication and disk headroom affect recovery. determines shard/partition and can create hot spots. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-07

- [ ] **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Lag/iterator age, Schema/idempotency and Sequence/offset are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: measures how far consumers are behind and drives capacity response. event evolution and at-least-once processing require compatible consumers/effects. consumer position supports checkpoint and replay. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Reshard/repartition, Shard/partition and Consumer group are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: changes parallelism and ordering/key distribution constraints. ordered log unit and primary throughput/parallelism boundary. Kafka partitions are assigned/rebalanced among group members. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-09

- [ ] **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where MSK broker storage/network, Partition key and Enhanced fan-out are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: broker/partition count, replication and disk headroom affect recovery. determines shard/partition and can create hot spots. Kinesis consumers get dedicated throughput under additional cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Kinesis Data Streams and Amazon MSK capability where Schema/idempotency, Sequence/offset and Retention are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: event evolution and at-least-once processing require compatible consumers/effects. consumer position supports checkpoint and replay. bounds replay/recovery and storage cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Shard/partition. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kinesis describe-stream-summary --stream-name STREAM` as one read-only checkpoint, not the whole diagnosis. ordered log unit and primary throughput/parallelism boundary. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Partition key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kinesis list-shards --stream-name STREAM` as one read-only checkpoint, not the whole diagnosis. determines shard/partition and can create hot spots. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sequence/offset. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kafka describe-cluster-v2 --cluster-arn ARN` as one read-only checkpoint, not the whole diagnosis. consumer position supports checkpoint and replay. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Consumer group. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kafka-consumer-groups.sh --bootstrap-server BROKERS --describe --group GROUP` as one read-only checkpoint, not the whole diagnosis. Kafka partitions are assigned/rebalanced among group members. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Enhanced fan-out. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kinesis describe-stream-summary --stream-name STREAM` as one read-only checkpoint, not the whole diagnosis. Kinesis consumers get dedicated throughput under additional cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retention. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kinesis list-shards --stream-name STREAM` as one read-only checkpoint, not the whole diagnosis. bounds replay/recovery and storage cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lag/iterator age. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kafka describe-cluster-v2 --cluster-arn ARN` as one read-only checkpoint, not the whole diagnosis. measures how far consumers are behind and drives capacity response. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reshard/repartition. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kafka-consumer-groups.sh --bootstrap-server BROKERS --describe --group GROUP` as one read-only checkpoint, not the whole diagnosis. changes parallelism and ordering/key distribution constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving MSK broker storage/network. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kinesis describe-stream-summary --stream-name STREAM` as one read-only checkpoint, not the whole diagnosis. broker/partition count, replication and disk headroom affect recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KINESIS-DATA-STREAMS-AND-AMAZON-MSK-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Schema/idempotency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kinesis list-shards --stream-name STREAM` as one read-only checkpoint, not the whole diagnosis. event evolution and at-least-once processing require compatible consumers/effects. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
