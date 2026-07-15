# Amazon SNS and EventBridge — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-SNS-AND-EVENTBRIDGE-JN-01

- [ ] **Question:** What is SNS topic, and why does it matter in Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** publisher fan-out to protocol subscriptions under topic policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-02

- [ ] **Question:** What is Subscription filter, and why does it matter in Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** routes messages by attributes/body and can drop unexpected schemas. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-03

- [ ] **Question:** What is Delivery retry/DLQ, and why does it matter in Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** endpoint-specific retry and dead-letter behavior must be observed. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-04

- [ ] **Question:** What is EventBridge bus, and why does it matter in Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** account/custom/partner buses receive events under resource policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-05

- [ ] **Question:** What is Rule pattern, and why does it matter in Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** matches structured event fields and routes to targets. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-06

- [ ] **Question:** What is Input transformation, and why does it matter in Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** reshapes event for a target but creates schema coupling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-07

- [ ] **Question:** What is Archive/replay, and why does it matter in Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** retained bus events can be replayed with duplicate/side-effect controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-08

- [ ] **Code:** **Question:** What does `aws events list-event-buses` help you verify for Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: documents/discovers schemas but compatibility governance remains owned.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-09

- [ ] **Code:** **Question:** What does `aws events list-rules --event-bus-name BUS` help you verify for Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: organization/resource policies and target roles define trust.

### AMAZON-SNS-AND-EVENTBRIDGE-JN-10

- [ ] **Code:** **Question:** What does `aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json` help you verify for Amazon SNS and EventBridge?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: invokes targets on time patterns with retry/DLQ and idempotency requirements.

## Junior — procedural and command questions

### AMAZON-SNS-AND-EVENTBRIDGE-JP-01

- [ ] **Code:** **Question:** A basic SNS topic check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sns list-topics` and capture exact status/reason/request ID. publisher fan-out to protocol subscriptions under topic policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-02

- [ ] **Question:** A basic Subscription filter check fails. What would you do first?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sns list-subscriptions-by-topic --topic-arn ARN` and capture exact status/reason/request ID. routes messages by attributes/body and can drop unexpected schemas. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-03

- [ ] **Question:** A basic Delivery retry/DLQ check fails. What would you do first?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws events list-event-buses` and capture exact status/reason/request ID. endpoint-specific retry and dead-letter behavior must be observed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-04

- [ ] **Code:** **Question:** A basic EventBridge bus check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws events list-rules --event-bus-name BUS` and capture exact status/reason/request ID. account/custom/partner buses receive events under resource policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-05

- [ ] **Question:** A basic Rule pattern check fails. What would you do first?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json` and capture exact status/reason/request ID. matches structured event fields and routes to targets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-06

- [ ] **Question:** A basic Input transformation check fails. What would you do first?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sns list-topics` and capture exact status/reason/request ID. reshapes event for a target but creates schema coupling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-07

- [ ] **Code:** **Question:** A basic Archive/replay check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sns list-subscriptions-by-topic --topic-arn ARN` and capture exact status/reason/request ID. retained bus events can be replayed with duplicate/side-effect controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-08

- [ ] **Question:** A basic Schema registry check fails. What would you do first?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws events list-event-buses` and capture exact status/reason/request ID. documents/discovers schemas but compatibility governance remains owned. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-09

- [ ] **Question:** A basic Cross-account routing check fails. What would you do first?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws events list-rules --event-bus-name BUS` and capture exact status/reason/request ID. organization/resource policies and target roles define trust. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SNS-AND-EVENTBRIDGE-JP-10

- [ ] **Code:** **Question:** A basic Scheduler check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SNS and EventBridge — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json` and capture exact status/reason/request ID. invokes targets on time patterns with retry/DLQ and idempotency requirements. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-SNS-AND-EVENTBRIDGE-MN-01

- [ ] **Question:** Compare SNS topic with Subscription filter. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** SNS topic: publisher fan-out to protocol subscriptions under topic policy. Subscription filter: routes messages by attributes/body and can drop unexpected schemas. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-02

- [ ] **Question:** Compare Subscription filter with Delivery retry/DLQ. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Subscription filter: routes messages by attributes/body and can drop unexpected schemas. Delivery retry/DLQ: endpoint-specific retry and dead-letter behavior must be observed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-03

- [ ] **Question:** Compare Delivery retry/DLQ with EventBridge bus. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Delivery retry/DLQ: endpoint-specific retry and dead-letter behavior must be observed. EventBridge bus: account/custom/partner buses receive events under resource policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-04

- [ ] **Configuration review:** **Question:** Compare EventBridge bus with Rule pattern. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** EventBridge bus: account/custom/partner buses receive events under resource policy. Rule pattern: matches structured event fields and routes to targets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-05

- [ ] **Question:** Compare Rule pattern with Input transformation. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Rule pattern: matches structured event fields and routes to targets. Input transformation: reshapes event for a target but creates schema coupling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-06

- [ ] **Question:** Compare Input transformation with Archive/replay. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Input transformation: reshapes event for a target but creates schema coupling. Archive/replay: retained bus events can be replayed with duplicate/side-effect controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-07

- [ ] **Configuration review:** **Question:** Compare Archive/replay with Schema registry. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Archive/replay: retained bus events can be replayed with duplicate/side-effect controls. Schema registry: documents/discovers schemas but compatibility governance remains owned. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-08

- [ ] **Question:** Compare Schema registry with Cross-account routing. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Schema registry: documents/discovers schemas but compatibility governance remains owned. Cross-account routing: organization/resource policies and target roles define trust. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-09

- [ ] **Question:** Compare Cross-account routing with Scheduler. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cross-account routing: organization/resource policies and target roles define trust. Scheduler: invokes targets on time patterns with retry/DLQ and idempotency requirements. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SNS-AND-EVENTBRIDGE-MN-10

- [ ] **Configuration review:** **Question:** Compare Scheduler with SNS topic. When would each change your design?
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Scheduler: invokes targets on time patterns with retry/DLQ and idempotency requirements. SNS topic: publisher fan-out to protocol subscriptions under topic policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-SNS-AND-EVENTBRIDGE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around SNS topic; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sns list-topics` plus recent events/changes, then correlate the service-specific SLI. publisher fan-out to protocol subscriptions under topic policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-02

- [ ] **Question:** Production is degraded around Subscription filter; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sns list-subscriptions-by-topic --topic-arn ARN` plus recent events/changes, then correlate the service-specific SLI. routes messages by attributes/body and can drop unexpected schemas. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Delivery retry/DLQ; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws events list-event-buses` plus recent events/changes, then correlate the service-specific SLI. endpoint-specific retry and dead-letter behavior must be observed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-04

- [ ] **Question:** Production is degraded around EventBridge bus; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws events list-rules --event-bus-name BUS` plus recent events/changes, then correlate the service-specific SLI. account/custom/partner buses receive events under resource policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rule pattern; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json` plus recent events/changes, then correlate the service-specific SLI. matches structured event fields and routes to targets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-06

- [ ] **Question:** Production is degraded around Input transformation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sns list-topics` plus recent events/changes, then correlate the service-specific SLI. reshapes event for a target but creates schema coupling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Archive/replay; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sns list-subscriptions-by-topic --topic-arn ARN` plus recent events/changes, then correlate the service-specific SLI. retained bus events can be replayed with duplicate/side-effect controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-08

- [ ] **Question:** Production is degraded around Schema registry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws events list-event-buses` plus recent events/changes, then correlate the service-specific SLI. documents/discovers schemas but compatibility governance remains owned. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cross-account routing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws events list-rules --event-bus-name BUS` plus recent events/changes, then correlate the service-specific SLI. organization/resource policies and target roles define trust. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SNS-AND-EVENTBRIDGE-MP-10

- [ ] **Question:** Production is degraded around Scheduler; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json` plus recent events/changes, then correlate the service-specific SLI. invokes targets on time patterns with retry/DLQ and idempotency requirements. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-SNS-AND-EVENTBRIDGE-SN-01

- [ ] **Question:** Design a production Amazon SNS and EventBridge capability where SNS topic, EventBridge bus and Archive/replay are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: publisher fan-out to protocol subscriptions under topic policy. account/custom/partner buses receive events under resource policy. retained bus events can be replayed with duplicate/side-effect controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SNS and EventBridge capability where Subscription filter, Rule pattern and Schema registry are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: routes messages by attributes/body and can drop unexpected schemas. matches structured event fields and routes to targets. documents/discovers schemas but compatibility governance remains owned. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-03

- [ ] **Question:** Design a production Amazon SNS and EventBridge capability where Delivery retry/DLQ, Input transformation and Cross-account routing are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: endpoint-specific retry and dead-letter behavior must be observed. reshapes event for a target but creates schema coupling. organization/resource policies and target roles define trust. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SNS and EventBridge capability where EventBridge bus, Archive/replay and Scheduler are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: account/custom/partner buses receive events under resource policy. retained bus events can be replayed with duplicate/side-effect controls. invokes targets on time patterns with retry/DLQ and idempotency requirements. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-05

- [ ] **Question:** Design a production Amazon SNS and EventBridge capability where Rule pattern, Schema registry and SNS topic are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: matches structured event fields and routes to targets. documents/discovers schemas but compatibility governance remains owned. publisher fan-out to protocol subscriptions under topic policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SNS and EventBridge capability where Input transformation, Cross-account routing and Subscription filter are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reshapes event for a target but creates schema coupling. organization/resource policies and target roles define trust. routes messages by attributes/body and can drop unexpected schemas. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-07

- [ ] **Question:** Design a production Amazon SNS and EventBridge capability where Archive/replay, Scheduler and Delivery retry/DLQ are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retained bus events can be replayed with duplicate/side-effect controls. invokes targets on time patterns with retry/DLQ and idempotency requirements. endpoint-specific retry and dead-letter behavior must be observed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SNS and EventBridge capability where Schema registry, SNS topic and EventBridge bus are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: documents/discovers schemas but compatibility governance remains owned. publisher fan-out to protocol subscriptions under topic policy. account/custom/partner buses receive events under resource policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-09

- [ ] **Question:** Design a production Amazon SNS and EventBridge capability where Cross-account routing, Subscription filter and Rule pattern are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: organization/resource policies and target roles define trust. routes messages by attributes/body and can drop unexpected schemas. matches structured event fields and routes to targets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SNS-AND-EVENTBRIDGE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SNS and EventBridge capability where Scheduler, Delivery retry/DLQ and Input transformation are first-class requirements.
> **Covered in:** [Amazon SNS and EventBridge — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: invokes targets on time patterns with retry/DLQ and idempotency requirements. endpoint-specific retry and dead-letter behavior must be observed. reshapes event for a target but creates schema coupling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-SNS-AND-EVENTBRIDGE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SNS topic. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sns list-topics` as one read-only checkpoint, not the whole diagnosis. publisher fan-out to protocol subscriptions under topic policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Subscription filter. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sns list-subscriptions-by-topic --topic-arn ARN` as one read-only checkpoint, not the whole diagnosis. routes messages by attributes/body and can drop unexpected schemas. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Delivery retry/DLQ. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws events list-event-buses` as one read-only checkpoint, not the whole diagnosis. endpoint-specific retry and dead-letter behavior must be observed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving EventBridge bus. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws events list-rules --event-bus-name BUS` as one read-only checkpoint, not the whole diagnosis. account/custom/partner buses receive events under resource policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rule pattern. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json` as one read-only checkpoint, not the whole diagnosis. matches structured event fields and routes to targets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Input transformation. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sns list-topics` as one read-only checkpoint, not the whole diagnosis. reshapes event for a target but creates schema coupling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Archive/replay. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sns list-subscriptions-by-topic --topic-arn ARN` as one read-only checkpoint, not the whole diagnosis. retained bus events can be replayed with duplicate/side-effect controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Schema registry. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws events list-event-buses` as one read-only checkpoint, not the whole diagnosis. documents/discovers schemas but compatibility governance remains owned. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cross-account routing. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws events list-rules --event-bus-name BUS` as one read-only checkpoint, not the whole diagnosis. organization/resource policies and target roles define trust. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SNS-AND-EVENTBRIDGE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scheduler. How do you lead it end to end?
> **Covered in:** [Amazon SNS and EventBridge — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws events test-event-pattern --event-pattern file://pattern.json --event file://event.json` as one read-only checkpoint, not the whole diagnosis. invokes targets on time patterns with retry/DLQ and idempotency requirements. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon SQS](../01-sqs/README.md) · [Study note](README.md) · [Next: AWS Step Functions →](../03-step-functions/README.md)

<!-- reading-navigation:end -->
