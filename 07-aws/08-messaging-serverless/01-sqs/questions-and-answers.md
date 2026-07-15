# Amazon SQS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-SQS-JN-01

- [ ] **Question:** What is Standard queue, and why does it matter in Amazon SQS?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** at-least-once delivery and best-effort order at very high scale. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SQS-JN-02

- [ ] **Question:** What is FIFO queue, and why does it matter in Amazon SQS?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ordered message groups and deduplication with throughput/parallelism constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SQS-JN-03

- [ ] **Question:** What is Visibility timeout, and why does it matter in Amazon SQS?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** lease after receive must cover/extend processing or a message becomes visible again. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SQS-JN-04

- [ ] **Question:** What is Delete message, and why does it matter in Amazon SQS?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** consumer commit requires the latest receipt handle after successful effect. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SQS-JN-05

- [ ] **Question:** What is Long polling, and why does it matter in Amazon SQS?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** reduces empty receives/cost and latency compared with tight short polling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SQS-JN-06

- [ ] **Question:** What is DLQ redrive, and why does it matter in Amazon SQS?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** isolates poison/repeated failures and needs controlled diagnosis/replay tooling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SQS-JN-07

- [ ] **Question:** What is Retention, and why does it matter in Amazon SQS?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** bounds replay window and storage of unprocessed messages. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SQS-JN-08

- [ ] **Code:** **Question:** What does `aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END` help you verify for Amazon SQS?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: stable event/effect keys prevent duplicate business side effects.

### AMAZON-SQS-JN-09

- [ ] **Code:** **Question:** What does `aws sqs get-queue-attributes --queue-url URL --attribute-names All` help you verify for Amazon SQS?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: stronger backlog/SLO signal than queue count alone.

### AMAZON-SQS-JN-10

- [ ] **Code:** **Question:** What does `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` help you verify for Amazon SQS?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: excessive concurrency/long visibility can block further receive progress.

## Junior — procedural and command questions

### AMAZON-SQS-JP-01

- [ ] **Code:** **Question:** A basic Standard queue check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs get-queue-attributes --queue-url URL --attribute-names All` and capture exact status/reason/request ID. at-least-once delivery and best-effort order at very high scale. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-02

- [ ] **Question:** A basic FIFO queue check fails. What would you do first?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` and capture exact status/reason/request ID. ordered message groups and deduplication with throughput/parallelism constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-03

- [ ] **Question:** A basic Visibility timeout check fails. What would you do first?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs start-message-move-task --source-arn DLQ_ARN` and capture exact status/reason/request ID. lease after receive must cover/extend processing or a message becomes visible again. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-04

- [ ] **Code:** **Question:** A basic Delete message check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END` and capture exact status/reason/request ID. consumer commit requires the latest receipt handle after successful effect. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-05

- [ ] **Question:** A basic Long polling check fails. What would you do first?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs get-queue-attributes --queue-url URL --attribute-names All` and capture exact status/reason/request ID. reduces empty receives/cost and latency compared with tight short polling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-06

- [ ] **Question:** A basic DLQ redrive check fails. What would you do first?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` and capture exact status/reason/request ID. isolates poison/repeated failures and needs controlled diagnosis/replay tooling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-07

- [ ] **Code:** **Question:** A basic Retention check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs start-message-move-task --source-arn DLQ_ARN` and capture exact status/reason/request ID. bounds replay window and storage of unprocessed messages. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-08

- [ ] **Question:** A basic Idempotency check fails. What would you do first?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END` and capture exact status/reason/request ID. stable event/effect keys prevent duplicate business side effects. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-09

- [ ] **Question:** A basic Oldest message age check fails. What would you do first?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs get-queue-attributes --queue-url URL --attribute-names All` and capture exact status/reason/request ID. stronger backlog/SLO signal than queue count alone. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SQS-JP-10

- [ ] **Code:** **Question:** A basic In-flight quota check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SQS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` and capture exact status/reason/request ID. excessive concurrency/long visibility can block further receive progress. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-SQS-MN-01

- [ ] **Question:** Compare Standard queue with FIFO queue. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Standard queue: at-least-once delivery and best-effort order at very high scale. FIFO queue: ordered message groups and deduplication with throughput/parallelism constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-02

- [ ] **Question:** Compare FIFO queue with Visibility timeout. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** FIFO queue: ordered message groups and deduplication with throughput/parallelism constraints. Visibility timeout: lease after receive must cover/extend processing or a message becomes visible again. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-03

- [ ] **Question:** Compare Visibility timeout with Delete message. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Visibility timeout: lease after receive must cover/extend processing or a message becomes visible again. Delete message: consumer commit requires the latest receipt handle after successful effect. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-04

- [ ] **Configuration review:** **Question:** Compare Delete message with Long polling. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Delete message: consumer commit requires the latest receipt handle after successful effect. Long polling: reduces empty receives/cost and latency compared with tight short polling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-05

- [ ] **Question:** Compare Long polling with DLQ redrive. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Long polling: reduces empty receives/cost and latency compared with tight short polling. DLQ redrive: isolates poison/repeated failures and needs controlled diagnosis/replay tooling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-06

- [ ] **Question:** Compare DLQ redrive with Retention. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DLQ redrive: isolates poison/repeated failures and needs controlled diagnosis/replay tooling. Retention: bounds replay window and storage of unprocessed messages. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-07

- [ ] **Configuration review:** **Question:** Compare Retention with Idempotency. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Retention: bounds replay window and storage of unprocessed messages. Idempotency: stable event/effect keys prevent duplicate business side effects. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-08

- [ ] **Question:** Compare Idempotency with Oldest message age. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Idempotency: stable event/effect keys prevent duplicate business side effects. Oldest message age: stronger backlog/SLO signal than queue count alone. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-09

- [ ] **Question:** Compare Oldest message age with In-flight quota. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Oldest message age: stronger backlog/SLO signal than queue count alone. In-flight quota: excessive concurrency/long visibility can block further receive progress. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SQS-MN-10

- [ ] **Configuration review:** **Question:** Compare In-flight quota with Standard queue. When would each change your design?
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** In-flight quota: excessive concurrency/long visibility can block further receive progress. Standard queue: at-least-once delivery and best-effort order at very high scale. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-SQS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Standard queue; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs get-queue-attributes --queue-url URL --attribute-names All` plus recent events/changes, then correlate the service-specific SLI. at-least-once delivery and best-effort order at very high scale. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-02

- [ ] **Question:** Production is degraded around FIFO queue; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` plus recent events/changes, then correlate the service-specific SLI. ordered message groups and deduplication with throughput/parallelism constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Visibility timeout; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs start-message-move-task --source-arn DLQ_ARN` plus recent events/changes, then correlate the service-specific SLI. lease after receive must cover/extend processing or a message becomes visible again. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-04

- [ ] **Question:** Production is degraded around Delete message; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END` plus recent events/changes, then correlate the service-specific SLI. consumer commit requires the latest receipt handle after successful effect. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Long polling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs get-queue-attributes --queue-url URL --attribute-names All` plus recent events/changes, then correlate the service-specific SLI. reduces empty receives/cost and latency compared with tight short polling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-06

- [ ] **Question:** Production is degraded around DLQ redrive; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` plus recent events/changes, then correlate the service-specific SLI. isolates poison/repeated failures and needs controlled diagnosis/replay tooling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Retention; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs start-message-move-task --source-arn DLQ_ARN` plus recent events/changes, then correlate the service-specific SLI. bounds replay window and storage of unprocessed messages. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-08

- [ ] **Question:** Production is degraded around Idempotency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END` plus recent events/changes, then correlate the service-specific SLI. stable event/effect keys prevent duplicate business side effects. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Oldest message age; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs get-queue-attributes --queue-url URL --attribute-names All` plus recent events/changes, then correlate the service-specific SLI. stronger backlog/SLO signal than queue count alone. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SQS-MP-10

- [ ] **Question:** Production is degraded around In-flight quota; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` plus recent events/changes, then correlate the service-specific SLI. excessive concurrency/long visibility can block further receive progress. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-SQS-SN-01

- [ ] **Question:** Design a production Amazon SQS capability where Standard queue, Delete message and Retention are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: at-least-once delivery and best-effort order at very high scale. consumer commit requires the latest receipt handle after successful effect. bounds replay window and storage of unprocessed messages. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SQS capability where FIFO queue, Long polling and Idempotency are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered message groups and deduplication with throughput/parallelism constraints. reduces empty receives/cost and latency compared with tight short polling. stable event/effect keys prevent duplicate business side effects. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-03

- [ ] **Question:** Design a production Amazon SQS capability where Visibility timeout, DLQ redrive and Oldest message age are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: lease after receive must cover/extend processing or a message becomes visible again. isolates poison/repeated failures and needs controlled diagnosis/replay tooling. stronger backlog/SLO signal than queue count alone. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SQS capability where Delete message, Retention and In-flight quota are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: consumer commit requires the latest receipt handle after successful effect. bounds replay window and storage of unprocessed messages. excessive concurrency/long visibility can block further receive progress. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-05

- [ ] **Question:** Design a production Amazon SQS capability where Long polling, Idempotency and Standard queue are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reduces empty receives/cost and latency compared with tight short polling. stable event/effect keys prevent duplicate business side effects. at-least-once delivery and best-effort order at very high scale. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SQS capability where DLQ redrive, Oldest message age and FIFO queue are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: isolates poison/repeated failures and needs controlled diagnosis/replay tooling. stronger backlog/SLO signal than queue count alone. ordered message groups and deduplication with throughput/parallelism constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-07

- [ ] **Question:** Design a production Amazon SQS capability where Retention, In-flight quota and Visibility timeout are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bounds replay window and storage of unprocessed messages. excessive concurrency/long visibility can block further receive progress. lease after receive must cover/extend processing or a message becomes visible again. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SQS capability where Idempotency, Standard queue and Delete message are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stable event/effect keys prevent duplicate business side effects. at-least-once delivery and best-effort order at very high scale. consumer commit requires the latest receipt handle after successful effect. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-09

- [ ] **Question:** Design a production Amazon SQS capability where Oldest message age, FIFO queue and Long polling are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stronger backlog/SLO signal than queue count alone. ordered message groups and deduplication with throughput/parallelism constraints. reduces empty receives/cost and latency compared with tight short polling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SQS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SQS capability where In-flight quota, Visibility timeout and DLQ redrive are first-class requirements.
> **Covered in:** [Amazon SQS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: excessive concurrency/long visibility can block further receive progress. lease after receive must cover/extend processing or a message becomes visible again. isolates poison/repeated failures and needs controlled diagnosis/replay tooling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-SQS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Standard queue. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs get-queue-attributes --queue-url URL --attribute-names All` as one read-only checkpoint, not the whole diagnosis. at-least-once delivery and best-effort order at very high scale. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving FIFO queue. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` as one read-only checkpoint, not the whole diagnosis. ordered message groups and deduplication with throughput/parallelism constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Visibility timeout. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs start-message-move-task --source-arn DLQ_ARN` as one read-only checkpoint, not the whole diagnosis. lease after receive must cover/extend processing or a message becomes visible again. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Delete message. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END` as one read-only checkpoint, not the whole diagnosis. consumer commit requires the latest receipt handle after successful effect. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Long polling. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs get-queue-attributes --queue-url URL --attribute-names All` as one read-only checkpoint, not the whole diagnosis. reduces empty receives/cost and latency compared with tight short polling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DLQ redrive. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` as one read-only checkpoint, not the whole diagnosis. isolates poison/repeated failures and needs controlled diagnosis/replay tooling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retention. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs start-message-move-task --source-arn DLQ_ARN` as one read-only checkpoint, not the whole diagnosis. bounds replay window and storage of unprocessed messages. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Idempotency. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch get-metric-data --metric-data-queries file://sqs.json --start-time START --end-time END` as one read-only checkpoint, not the whole diagnosis. stable event/effect keys prevent duplicate business side effects. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Oldest message age. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs get-queue-attributes --queue-url URL --attribute-names All` as one read-only checkpoint, not the whole diagnosis. stronger backlog/SLO signal than queue count alone. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SQS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving In-flight quota. How do you lead it end to end?
> **Covered in:** [Amazon SQS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sqs receive-message --queue-url URL --wait-time-seconds 20 --max-number-of-messages 10` as one read-only checkpoint, not the whole diagnosis. excessive concurrency/long visibility can block further receive progress. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Messaging Serverless](../README.md) · [Study note](README.md) · [Next: Amazon SNS and EventBridge →](../02-sns-eventbridge/README.md)

<!-- reading-navigation:end -->
