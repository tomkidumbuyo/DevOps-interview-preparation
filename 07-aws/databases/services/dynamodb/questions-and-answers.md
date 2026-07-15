# Amazon DynamoDB — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-DYNAMODB-JN-01

- [ ] **Question:** What is Partition key, and why does it matter in Amazon DynamoDB?

**Answer:** hashes items across physical partitions and must distribute request volume. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-DYNAMODB-JN-02

- [ ] **Question:** What is Sort key, and why does it matter in Amazon DynamoDB?

**Answer:** orders items within a partition and enables range/prefix access patterns. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-DYNAMODB-JN-03

- [ ] **Question:** What is GSI, and why does it matter in Amazon DynamoDB?

**Answer:** asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-DYNAMODB-JN-04

- [ ] **Question:** What is LSI, and why does it matter in Amazon DynamoDB?

**Answer:** alternate sort key sharing table partition key and creation-time/size constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-DYNAMODB-JN-05

- [ ] **Question:** What is On-demand/provisioned, and why does it matter in Amazon DynamoDB?

**Answer:** capacity modes trade predictability/control and can still throttle hot keys. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-DYNAMODB-JN-06

- [ ] **Question:** What is Conditional write, and why does it matter in Amazon DynamoDB?

**Answer:** atomically enforces version/idempotency/state transition predicates. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-DYNAMODB-JN-07

- [ ] **Question:** What is Transaction, and why does it matter in Amazon DynamoDB?

**Answer:** coordinates multiple items at higher cost/limits and is not a relational query model. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-DYNAMODB-JN-08

- [ ] **Code:** **Question:** What does `aws dynamodb describe-kinesis-streaming-destination --table-name TABLE` help you verify for Amazon DynamoDB?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: ordered per-item change records feed consumers under retention/idempotency needs.

### AMAZON-DYNAMODB-JN-09

- [ ] **Code:** **Question:** What does `aws dynamodb describe-table --table-name TABLE` help you verify for Amazon DynamoDB?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: multi-Region active replication with conflict resolution semantics.

### AMAZON-DYNAMODB-JN-10

- [ ] **Code:** **Question:** What does `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` help you verify for Amazon DynamoDB?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: asynchronous best-effort expiration; applications must not assume immediate deletion.

## Junior — procedural and command questions

### AMAZON-DYNAMODB-JP-01

- [ ] **Code:** **Question:** A basic Partition key check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-table --table-name TABLE` and capture exact status/reason/request ID. hashes items across physical partitions and must distribute request volume. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-02

- [ ] **Question:** A basic Sort key check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` and capture exact status/reason/request ID. orders items within a partition and enables range/prefix access patterns. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-03

- [ ] **Question:** A basic GSI check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-continuous-backups --table-name TABLE` and capture exact status/reason/request ID. asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-04

- [ ] **Code:** **Question:** A basic LSI check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-kinesis-streaming-destination --table-name TABLE` and capture exact status/reason/request ID. alternate sort key sharing table partition key and creation-time/size constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-05

- [ ] **Question:** A basic On-demand/provisioned check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-table --table-name TABLE` and capture exact status/reason/request ID. capacity modes trade predictability/control and can still throttle hot keys. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-06

- [ ] **Question:** A basic Conditional write check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` and capture exact status/reason/request ID. atomically enforces version/idempotency/state transition predicates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-07

- [ ] **Code:** **Question:** A basic Transaction check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-continuous-backups --table-name TABLE` and capture exact status/reason/request ID. coordinates multiple items at higher cost/limits and is not a relational query model. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-08

- [ ] **Question:** A basic Streams check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-kinesis-streaming-destination --table-name TABLE` and capture exact status/reason/request ID. ordered per-item change records feed consumers under retention/idempotency needs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-09

- [ ] **Question:** A basic Global Tables check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb describe-table --table-name TABLE` and capture exact status/reason/request ID. multi-Region active replication with conflict resolution semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-DYNAMODB-JP-10

- [ ] **Code:** **Question:** A basic TTL check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` and capture exact status/reason/request ID. asynchronous best-effort expiration; applications must not assume immediate deletion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-DYNAMODB-MN-01

- [ ] **Question:** Compare Partition key with Sort key. When would each change your design?

**Answer:** Partition key: hashes items across physical partitions and must distribute request volume. Sort key: orders items within a partition and enables range/prefix access patterns. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-02

- [ ] **Question:** Compare Sort key with GSI. When would each change your design?

**Answer:** Sort key: orders items within a partition and enables range/prefix access patterns. GSI: asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-03

- [ ] **Question:** Compare GSI with LSI. When would each change your design?

**Answer:** GSI: asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. LSI: alternate sort key sharing table partition key and creation-time/size constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-04

- [ ] **Configuration review:** **Question:** Compare LSI with On-demand/provisioned. When would each change your design?

**Answer:** LSI: alternate sort key sharing table partition key and creation-time/size constraints. On-demand/provisioned: capacity modes trade predictability/control and can still throttle hot keys. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-05

- [ ] **Question:** Compare On-demand/provisioned with Conditional write. When would each change your design?

**Answer:** On-demand/provisioned: capacity modes trade predictability/control and can still throttle hot keys. Conditional write: atomically enforces version/idempotency/state transition predicates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-06

- [ ] **Question:** Compare Conditional write with Transaction. When would each change your design?

**Answer:** Conditional write: atomically enforces version/idempotency/state transition predicates. Transaction: coordinates multiple items at higher cost/limits and is not a relational query model. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-07

- [ ] **Configuration review:** **Question:** Compare Transaction with Streams. When would each change your design?

**Answer:** Transaction: coordinates multiple items at higher cost/limits and is not a relational query model. Streams: ordered per-item change records feed consumers under retention/idempotency needs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-08

- [ ] **Question:** Compare Streams with Global Tables. When would each change your design?

**Answer:** Streams: ordered per-item change records feed consumers under retention/idempotency needs. Global Tables: multi-Region active replication with conflict resolution semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-09

- [ ] **Question:** Compare Global Tables with TTL. When would each change your design?

**Answer:** Global Tables: multi-Region active replication with conflict resolution semantics. TTL: asynchronous best-effort expiration; applications must not assume immediate deletion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-DYNAMODB-MN-10

- [ ] **Configuration review:** **Question:** Compare TTL with Partition key. When would each change your design?

**Answer:** TTL: asynchronous best-effort expiration; applications must not assume immediate deletion. Partition key: hashes items across physical partitions and must distribute request volume. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-DYNAMODB-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Partition key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-table --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. hashes items across physical partitions and must distribute request volume. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-02

- [ ] **Question:** Production is degraded around Sort key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` plus recent events/changes, then correlate the service-specific SLI. orders items within a partition and enables range/prefix access patterns. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around GSI; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-continuous-backups --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-04

- [ ] **Question:** Production is degraded around LSI; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-kinesis-streaming-destination --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. alternate sort key sharing table partition key and creation-time/size constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around On-demand/provisioned; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-table --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. capacity modes trade predictability/control and can still throttle hot keys. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-06

- [ ] **Question:** Production is degraded around Conditional write; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` plus recent events/changes, then correlate the service-specific SLI. atomically enforces version/idempotency/state transition predicates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Transaction; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-continuous-backups --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. coordinates multiple items at higher cost/limits and is not a relational query model. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-08

- [ ] **Question:** Production is degraded around Streams; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-kinesis-streaming-destination --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. ordered per-item change records feed consumers under retention/idempotency needs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Global Tables; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb describe-table --table-name TABLE` plus recent events/changes, then correlate the service-specific SLI. multi-Region active replication with conflict resolution semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-DYNAMODB-MP-10

- [ ] **Question:** Production is degraded around TTL; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` plus recent events/changes, then correlate the service-specific SLI. asynchronous best-effort expiration; applications must not assume immediate deletion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-DYNAMODB-SN-01

- [ ] **Question:** Design a production Amazon DynamoDB capability where Partition key, LSI and Transaction are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: hashes items across physical partitions and must distribute request volume. alternate sort key sharing table partition key and creation-time/size constraints. coordinates multiple items at higher cost/limits and is not a relational query model. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon DynamoDB capability where Sort key, On-demand/provisioned and Streams are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: orders items within a partition and enables range/prefix access patterns. capacity modes trade predictability/control and can still throttle hot keys. ordered per-item change records feed consumers under retention/idempotency needs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-03

- [ ] **Question:** Design a production Amazon DynamoDB capability where GSI, Conditional write and Global Tables are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. atomically enforces version/idempotency/state transition predicates. multi-Region active replication with conflict resolution semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon DynamoDB capability where LSI, Transaction and TTL are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: alternate sort key sharing table partition key and creation-time/size constraints. coordinates multiple items at higher cost/limits and is not a relational query model. asynchronous best-effort expiration; applications must not assume immediate deletion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-05

- [ ] **Question:** Design a production Amazon DynamoDB capability where On-demand/provisioned, Streams and Partition key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: capacity modes trade predictability/control and can still throttle hot keys. ordered per-item change records feed consumers under retention/idempotency needs. hashes items across physical partitions and must distribute request volume. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon DynamoDB capability where Conditional write, Global Tables and Sort key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: atomically enforces version/idempotency/state transition predicates. multi-Region active replication with conflict resolution semantics. orders items within a partition and enables range/prefix access patterns. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-07

- [ ] **Question:** Design a production Amazon DynamoDB capability where Transaction, TTL and GSI are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: coordinates multiple items at higher cost/limits and is not a relational query model. asynchronous best-effort expiration; applications must not assume immediate deletion. asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon DynamoDB capability where Streams, Partition key and LSI are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered per-item change records feed consumers under retention/idempotency needs. hashes items across physical partitions and must distribute request volume. alternate sort key sharing table partition key and creation-time/size constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-09

- [ ] **Question:** Design a production Amazon DynamoDB capability where Global Tables, Sort key and On-demand/provisioned are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: multi-Region active replication with conflict resolution semantics. orders items within a partition and enables range/prefix access patterns. capacity modes trade predictability/control and can still throttle hot keys. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-DYNAMODB-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon DynamoDB capability where TTL, GSI and Conditional write are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: asynchronous best-effort expiration; applications must not assume immediate deletion. asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. atomically enforces version/idempotency/state transition predicates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-DYNAMODB-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Partition key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-table --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. hashes items across physical partitions and must distribute request volume. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sort key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` as one read-only checkpoint, not the whole diagnosis. orders items within a partition and enables range/prefix access patterns. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GSI. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-continuous-backups --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. asynchronous alternate partition/sort key with its own storage/capacity/failure behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving LSI. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-kinesis-streaming-destination --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. alternate sort key sharing table partition key and creation-time/size constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving On-demand/provisioned. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-table --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. capacity modes trade predictability/control and can still throttle hot keys. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Conditional write. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` as one read-only checkpoint, not the whole diagnosis. atomically enforces version/idempotency/state transition predicates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Transaction. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-continuous-backups --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. coordinates multiple items at higher cost/limits and is not a relational query model. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Streams. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-kinesis-streaming-destination --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. ordered per-item change records feed consumers under retention/idempotency needs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Global Tables. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb describe-table --table-name TABLE` as one read-only checkpoint, not the whole diagnosis. multi-Region active replication with conflict resolution semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-DYNAMODB-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TTL. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws dynamodb query --table-name TABLE --key-condition-expression EXPR --expression-attribute-values file://values.json` as one read-only checkpoint, not the whole diagnosis. asynchronous best-effort expiration; applications must not assume immediate deletion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
