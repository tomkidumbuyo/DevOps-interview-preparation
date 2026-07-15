# Messaging Serverless — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-MESSAGING-SERVERLESS-JN-01

- [ ] **Question:** What is Standard queue, and why does it matter in Messaging Serverless?

**Answer:** at-least-once delivery and best-effort order at very high scale. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MESSAGING-SERVERLESS-JN-02

- [ ] **Question:** What is FIFO queue, and why does it matter in Messaging Serverless?

**Answer:** ordered message groups and deduplication with throughput/parallelism constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MESSAGING-SERVERLESS-JN-03

- [ ] **Question:** What is SNS topic, and why does it matter in Messaging Serverless?

**Answer:** publisher fan-out to protocol subscriptions under topic policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MESSAGING-SERVERLESS-JN-04

- [ ] **Question:** What is Subscription filter, and why does it matter in Messaging Serverless?

**Answer:** routes messages by attributes/body and can drop unexpected schemas. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MESSAGING-SERVERLESS-JN-05

- [ ] **Question:** What is State machine, and why does it matter in Messaging Serverless?

**Answer:** Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MESSAGING-SERVERLESS-JN-06

- [ ] **Question:** What is Standard workflow, and why does it matter in Messaging Serverless?

**Answer:** durable exactly-once workflow execution semantics for long-running auditable flows. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MESSAGING-SERVERLESS-JN-07

- [ ] **Question:** What is Shard/partition, and why does it matter in Messaging Serverless?

**Answer:** ordered log unit and primary throughput/parallelism boundary. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MESSAGING-SERVERLESS-JN-08

- [ ] **Code:** **Question:** What does `aws sns list-topics` help you verify for Messaging Serverless?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: determines shard/partition and can create hot spots.

### BRANCH-MESSAGING-SERVERLESS-JN-09

- [ ] **Code:** **Question:** What does `aws stepfunctions list-state-machines` help you verify for Messaging Serverless?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: initialization may be reused across invocations but must not hold unsafe tenant state.

### BRANCH-MESSAGING-SERVERLESS-JN-10

- [ ] **Code:** **Question:** What does `aws kinesis describe-stream-summary --stream-name STREAM` help you verify for Messaging Serverless?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: package/runtime/init/VPC and extensions contribute before handler execution.

## Junior — procedural and command questions

### BRANCH-MESSAGING-SERVERLESS-JP-01

- [ ] **Code:** **Question:** A basic Standard queue check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs get-queue-attributes --queue-url URL --attribute-names All` and capture exact status/reason/request ID. at-least-once delivery and best-effort order at very high scale. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-02

- [ ] **Question:** A basic FIFO queue check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sns list-topics` and capture exact status/reason/request ID. ordered message groups and deduplication with throughput/parallelism constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-03

- [ ] **Question:** A basic SNS topic check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions list-state-machines` and capture exact status/reason/request ID. publisher fan-out to protocol subscriptions under topic policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-04

- [ ] **Code:** **Question:** A basic Subscription filter check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kinesis describe-stream-summary --stream-name STREAM` and capture exact status/reason/request ID. routes messages by attributes/body and can drop unexpected schemas. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-05

- [ ] **Question:** A basic State machine check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda get-function-configuration --function-name FUNCTION` and capture exact status/reason/request ID. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-06

- [ ] **Question:** A basic Standard workflow check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws apigateway get-rest-apis` and capture exact status/reason/request ID. durable exactly-once workflow execution semantics for long-running auditable flows. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-07

- [ ] **Code:** **Question:** A basic Shard/partition check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs get-queue-attributes --queue-url URL --attribute-names All` and capture exact status/reason/request ID. ordered log unit and primary throughput/parallelism boundary. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-08

- [ ] **Question:** A basic Partition key check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sns list-topics` and capture exact status/reason/request ID. determines shard/partition and can create hot spots. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-09

- [ ] **Question:** A basic Execution environment check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions list-state-machines` and capture exact status/reason/request ID. initialization may be reused across invocations but must not hold unsafe tenant state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MESSAGING-SERVERLESS-JP-10

- [ ] **Code:** **Question:** A basic Cold start check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kinesis describe-stream-summary --stream-name STREAM` and capture exact status/reason/request ID. package/runtime/init/VPC and extensions contribute before handler execution. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-MESSAGING-SERVERLESS-MN-01

- [ ] **Question:** Compare Standard queue with FIFO queue. When would each change your design?

**Answer:** Standard queue: at-least-once delivery and best-effort order at very high scale. FIFO queue: ordered message groups and deduplication with throughput/parallelism constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-02

- [ ] **Question:** Compare FIFO queue with SNS topic. When would each change your design?

**Answer:** FIFO queue: ordered message groups and deduplication with throughput/parallelism constraints. SNS topic: publisher fan-out to protocol subscriptions under topic policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-03

- [ ] **Question:** Compare SNS topic with Subscription filter. When would each change your design?

**Answer:** SNS topic: publisher fan-out to protocol subscriptions under topic policy. Subscription filter: routes messages by attributes/body and can drop unexpected schemas. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-04

- [ ] **Configuration review:** **Question:** Compare Subscription filter with State machine. When would each change your design?

**Answer:** Subscription filter: routes messages by attributes/body and can drop unexpected schemas. State machine: Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-05

- [ ] **Question:** Compare State machine with Standard workflow. When would each change your design?

**Answer:** State machine: Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Standard workflow: durable exactly-once workflow execution semantics for long-running auditable flows. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-06

- [ ] **Question:** Compare Standard workflow with Shard/partition. When would each change your design?

**Answer:** Standard workflow: durable exactly-once workflow execution semantics for long-running auditable flows. Shard/partition: ordered log unit and primary throughput/parallelism boundary. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-07

- [ ] **Configuration review:** **Question:** Compare Shard/partition with Partition key. When would each change your design?

**Answer:** Shard/partition: ordered log unit and primary throughput/parallelism boundary. Partition key: determines shard/partition and can create hot spots. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-08

- [ ] **Question:** Compare Partition key with Execution environment. When would each change your design?

**Answer:** Partition key: determines shard/partition and can create hot spots. Execution environment: initialization may be reused across invocations but must not hold unsafe tenant state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-09

- [ ] **Question:** Compare Execution environment with Cold start. When would each change your design?

**Answer:** Execution environment: initialization may be reused across invocations but must not hold unsafe tenant state. Cold start: package/runtime/init/VPC and extensions contribute before handler execution. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MESSAGING-SERVERLESS-MN-10

- [ ] **Configuration review:** **Question:** Compare Cold start with Standard queue. When would each change your design?

**Answer:** Cold start: package/runtime/init/VPC and extensions contribute before handler execution. Standard queue: at-least-once delivery and best-effort order at very high scale. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-MESSAGING-SERVERLESS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Standard queue; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs get-queue-attributes --queue-url URL --attribute-names All` plus recent events/changes, then correlate the service-specific SLI. at-least-once delivery and best-effort order at very high scale. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-02

- [ ] **Question:** Production is degraded around FIFO queue; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sns list-topics` plus recent events/changes, then correlate the service-specific SLI. ordered message groups and deduplication with throughput/parallelism constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around SNS topic; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions list-state-machines` plus recent events/changes, then correlate the service-specific SLI. publisher fan-out to protocol subscriptions under topic policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-04

- [ ] **Question:** Production is degraded around Subscription filter; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kinesis describe-stream-summary --stream-name STREAM` plus recent events/changes, then correlate the service-specific SLI. routes messages by attributes/body and can drop unexpected schemas. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around State machine; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda get-function-configuration --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-06

- [ ] **Question:** Production is degraded around Standard workflow; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws apigateway get-rest-apis` plus recent events/changes, then correlate the service-specific SLI. durable exactly-once workflow execution semantics for long-running auditable flows. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Shard/partition; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs get-queue-attributes --queue-url URL --attribute-names All` plus recent events/changes, then correlate the service-specific SLI. ordered log unit and primary throughput/parallelism boundary. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-08

- [ ] **Question:** Production is degraded around Partition key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sns list-topics` plus recent events/changes, then correlate the service-specific SLI. determines shard/partition and can create hot spots. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Execution environment; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions list-state-machines` plus recent events/changes, then correlate the service-specific SLI. initialization may be reused across invocations but must not hold unsafe tenant state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MESSAGING-SERVERLESS-MP-10

- [ ] **Question:** Production is degraded around Cold start; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kinesis describe-stream-summary --stream-name STREAM` plus recent events/changes, then correlate the service-specific SLI. package/runtime/init/VPC and extensions contribute before handler execution. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-MESSAGING-SERVERLESS-SN-01

- [ ] **Question:** Design a production Messaging Serverless capability where Standard queue, Subscription filter and Shard/partition are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: at-least-once delivery and best-effort order at very high scale. routes messages by attributes/body and can drop unexpected schemas. ordered log unit and primary throughput/parallelism boundary. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Messaging Serverless capability where FIFO queue, State machine and Partition key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered message groups and deduplication with throughput/parallelism constraints. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. determines shard/partition and can create hot spots. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-03

- [ ] **Question:** Design a production Messaging Serverless capability where SNS topic, Standard workflow and Execution environment are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: publisher fan-out to protocol subscriptions under topic policy. durable exactly-once workflow execution semantics for long-running auditable flows. initialization may be reused across invocations but must not hold unsafe tenant state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Messaging Serverless capability where Subscription filter, Shard/partition and Cold start are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: routes messages by attributes/body and can drop unexpected schemas. ordered log unit and primary throughput/parallelism boundary. package/runtime/init/VPC and extensions contribute before handler execution. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-05

- [ ] **Question:** Design a production Messaging Serverless capability where State machine, Partition key and Standard queue are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. determines shard/partition and can create hot spots. at-least-once delivery and best-effort order at very high scale. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Messaging Serverless capability where Standard workflow, Execution environment and FIFO queue are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: durable exactly-once workflow execution semantics for long-running auditable flows. initialization may be reused across invocations but must not hold unsafe tenant state. ordered message groups and deduplication with throughput/parallelism constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-07

- [ ] **Question:** Design a production Messaging Serverless capability where Shard/partition, Cold start and SNS topic are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered log unit and primary throughput/parallelism boundary. package/runtime/init/VPC and extensions contribute before handler execution. publisher fan-out to protocol subscriptions under topic policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Messaging Serverless capability where Partition key, Standard queue and Subscription filter are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: determines shard/partition and can create hot spots. at-least-once delivery and best-effort order at very high scale. routes messages by attributes/body and can drop unexpected schemas. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-09

- [ ] **Question:** Design a production Messaging Serverless capability where Execution environment, FIFO queue and State machine are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: initialization may be reused across invocations but must not hold unsafe tenant state. ordered message groups and deduplication with throughput/parallelism constraints. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MESSAGING-SERVERLESS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Messaging Serverless capability where Cold start, SNS topic and Standard workflow are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: package/runtime/init/VPC and extensions contribute before handler execution. publisher fan-out to protocol subscriptions under topic policy. durable exactly-once workflow execution semantics for long-running auditable flows. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-MESSAGING-SERVERLESS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Standard queue. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs get-queue-attributes --queue-url URL --attribute-names All` as one read-only checkpoint, not the whole diagnosis. at-least-once delivery and best-effort order at very high scale. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving FIFO queue. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sns list-topics` as one read-only checkpoint, not the whole diagnosis. ordered message groups and deduplication with throughput/parallelism constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SNS topic. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions list-state-machines` as one read-only checkpoint, not the whole diagnosis. publisher fan-out to protocol subscriptions under topic policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Subscription filter. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kinesis describe-stream-summary --stream-name STREAM` as one read-only checkpoint, not the whole diagnosis. routes messages by attributes/body and can drop unexpected schemas. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving State machine. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda get-function-configuration --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Standard workflow. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws apigateway get-rest-apis` as one read-only checkpoint, not the whole diagnosis. durable exactly-once workflow execution semantics for long-running auditable flows. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Shard/partition. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs get-queue-attributes --queue-url URL --attribute-names All` as one read-only checkpoint, not the whole diagnosis. ordered log unit and primary throughput/parallelism boundary. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Partition key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sns list-topics` as one read-only checkpoint, not the whole diagnosis. determines shard/partition and can create hot spots. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Execution environment. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions list-state-machines` as one read-only checkpoint, not the whole diagnosis. initialization may be reused across invocations but must not hold unsafe tenant state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MESSAGING-SERVERLESS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cold start. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kinesis describe-stream-summary --stream-name STREAM` as one read-only checkpoint, not the whole diagnosis. package/runtime/init/VPC and extensions contribute before handler execution. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
