# AWS Lambda — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-LAMBDA-JN-01

- [ ] **Question:** What is Execution environment, and why does it matter in AWS Lambda?

**Answer:** initialization may be reused across invocations but must not hold unsafe tenant state. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LAMBDA-JN-02

- [ ] **Question:** What is Cold start, and why does it matter in AWS Lambda?

**Answer:** package/runtime/init/VPC and extensions contribute before handler execution. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LAMBDA-JN-03

- [ ] **Question:** What is Reserved concurrency, and why does it matter in AWS Lambda?

**Answer:** reserves and caps concurrency for a function, protecting account/downstream. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LAMBDA-JN-04

- [ ] **Question:** What is Provisioned concurrency, and why does it matter in AWS Lambda?

**Answer:** pre-initializes environments for latency at continuous cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LAMBDA-JN-05

- [ ] **Question:** What is Event source mapping, and why does it matter in AWS Lambda?

**Answer:** polls streams/queues and manages batches, concurrency, retries and checkpoints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LAMBDA-JN-06

- [ ] **Question:** What is Idempotency, and why does it matter in AWS Lambda?

**Answer:** retried/duplicate events need stable business-effect keys and durable records. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LAMBDA-JN-07

- [ ] **Question:** What is VPC networking, and why does it matter in AWS Lambda?

**Answer:** subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-LAMBDA-JN-08

- [ ] **Code:** **Question:** What does `aws logs tail /aws/lambda/FUNCTION --since 30m --follow` help you verify for AWS Lambda?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: function AWS permissions should exclude deployment/administrative capabilities.

### AWS-LAMBDA-JN-09

- [ ] **Code:** **Question:** What does `aws lambda get-function-configuration --function-name FUNCTION` help you verify for AWS Lambda?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: async outcomes capture failed/successful invocation metadata under service-specific rules.

### AWS-LAMBDA-JN-10

- [ ] **Code:** **Question:** What does `aws lambda get-function-concurrency --function-name FUNCTION` help you verify for AWS Lambda?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: function timeout must fit caller/dependency deadlines and leave effects consistent.

## Junior — procedural and command questions

### AWS-LAMBDA-JP-01

- [ ] **Code:** **Question:** A basic Execution environment check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda get-function-configuration --function-name FUNCTION` and capture exact status/reason/request ID. initialization may be reused across invocations but must not hold unsafe tenant state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-02

- [ ] **Question:** A basic Cold start check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda get-function-concurrency --function-name FUNCTION` and capture exact status/reason/request ID. package/runtime/init/VPC and extensions contribute before handler execution. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-03

- [ ] **Question:** A basic Reserved concurrency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda list-event-source-mappings --function-name FUNCTION` and capture exact status/reason/request ID. reserves and caps concurrency for a function, protecting account/downstream. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-04

- [ ] **Code:** **Question:** A basic Provisioned concurrency check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws logs tail /aws/lambda/FUNCTION --since 30m --follow` and capture exact status/reason/request ID. pre-initializes environments for latency at continuous cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-05

- [ ] **Question:** A basic Event source mapping check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda get-function-configuration --function-name FUNCTION` and capture exact status/reason/request ID. polls streams/queues and manages batches, concurrency, retries and checkpoints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-06

- [ ] **Question:** A basic Idempotency check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda get-function-concurrency --function-name FUNCTION` and capture exact status/reason/request ID. retried/duplicate events need stable business-effect keys and durable records. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-07

- [ ] **Code:** **Question:** A basic VPC networking check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda list-event-source-mappings --function-name FUNCTION` and capture exact status/reason/request ID. subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-08

- [ ] **Question:** A basic Execution role check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws logs tail /aws/lambda/FUNCTION --since 30m --follow` and capture exact status/reason/request ID. function AWS permissions should exclude deployment/administrative capabilities. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-09

- [ ] **Question:** A basic Destinations/DLQ check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda get-function-configuration --function-name FUNCTION` and capture exact status/reason/request ID. async outcomes capture failed/successful invocation metadata under service-specific rules. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-LAMBDA-JP-10

- [ ] **Code:** **Question:** A basic Timeout/cancellation check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws lambda get-function-concurrency --function-name FUNCTION` and capture exact status/reason/request ID. function timeout must fit caller/dependency deadlines and leave effects consistent. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-LAMBDA-MN-01

- [ ] **Question:** Compare Execution environment with Cold start. When would each change your design?

**Answer:** Execution environment: initialization may be reused across invocations but must not hold unsafe tenant state. Cold start: package/runtime/init/VPC and extensions contribute before handler execution. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-02

- [ ] **Question:** Compare Cold start with Reserved concurrency. When would each change your design?

**Answer:** Cold start: package/runtime/init/VPC and extensions contribute before handler execution. Reserved concurrency: reserves and caps concurrency for a function, protecting account/downstream. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-03

- [ ] **Question:** Compare Reserved concurrency with Provisioned concurrency. When would each change your design?

**Answer:** Reserved concurrency: reserves and caps concurrency for a function, protecting account/downstream. Provisioned concurrency: pre-initializes environments for latency at continuous cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-04

- [ ] **Configuration review:** **Question:** Compare Provisioned concurrency with Event source mapping. When would each change your design?

**Answer:** Provisioned concurrency: pre-initializes environments for latency at continuous cost. Event source mapping: polls streams/queues and manages batches, concurrency, retries and checkpoints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-05

- [ ] **Question:** Compare Event source mapping with Idempotency. When would each change your design?

**Answer:** Event source mapping: polls streams/queues and manages batches, concurrency, retries and checkpoints. Idempotency: retried/duplicate events need stable business-effect keys and durable records. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-06

- [ ] **Question:** Compare Idempotency with VPC networking. When would each change your design?

**Answer:** Idempotency: retried/duplicate events need stable business-effect keys and durable records. VPC networking: subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-07

- [ ] **Configuration review:** **Question:** Compare VPC networking with Execution role. When would each change your design?

**Answer:** VPC networking: subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. Execution role: function AWS permissions should exclude deployment/administrative capabilities. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-08

- [ ] **Question:** Compare Execution role with Destinations/DLQ. When would each change your design?

**Answer:** Execution role: function AWS permissions should exclude deployment/administrative capabilities. Destinations/DLQ: async outcomes capture failed/successful invocation metadata under service-specific rules. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-09

- [ ] **Question:** Compare Destinations/DLQ with Timeout/cancellation. When would each change your design?

**Answer:** Destinations/DLQ: async outcomes capture failed/successful invocation metadata under service-specific rules. Timeout/cancellation: function timeout must fit caller/dependency deadlines and leave effects consistent. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-LAMBDA-MN-10

- [ ] **Configuration review:** **Question:** Compare Timeout/cancellation with Execution environment. When would each change your design?

**Answer:** Timeout/cancellation: function timeout must fit caller/dependency deadlines and leave effects consistent. Execution environment: initialization may be reused across invocations but must not hold unsafe tenant state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-LAMBDA-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Execution environment; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda get-function-configuration --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. initialization may be reused across invocations but must not hold unsafe tenant state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-02

- [ ] **Question:** Production is degraded around Cold start; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda get-function-concurrency --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. package/runtime/init/VPC and extensions contribute before handler execution. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Reserved concurrency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda list-event-source-mappings --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. reserves and caps concurrency for a function, protecting account/downstream. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-04

- [ ] **Question:** Production is degraded around Provisioned concurrency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws logs tail /aws/lambda/FUNCTION --since 30m --follow` plus recent events/changes, then correlate the service-specific SLI. pre-initializes environments for latency at continuous cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Event source mapping; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda get-function-configuration --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. polls streams/queues and manages batches, concurrency, retries and checkpoints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-06

- [ ] **Question:** Production is degraded around Idempotency; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda get-function-concurrency --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. retried/duplicate events need stable business-effect keys and durable records. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC networking; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda list-event-source-mappings --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-08

- [ ] **Question:** Production is degraded around Execution role; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws logs tail /aws/lambda/FUNCTION --since 30m --follow` plus recent events/changes, then correlate the service-specific SLI. function AWS permissions should exclude deployment/administrative capabilities. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Destinations/DLQ; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda get-function-configuration --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. async outcomes capture failed/successful invocation metadata under service-specific rules. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-LAMBDA-MP-10

- [ ] **Question:** Production is degraded around Timeout/cancellation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws lambda get-function-concurrency --function-name FUNCTION` plus recent events/changes, then correlate the service-specific SLI. function timeout must fit caller/dependency deadlines and leave effects consistent. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-LAMBDA-SN-01

- [ ] **Question:** Design a production AWS Lambda capability where Execution environment, Provisioned concurrency and VPC networking are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: initialization may be reused across invocations but must not hold unsafe tenant state. pre-initializes environments for latency at continuous cost. subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Lambda capability where Cold start, Event source mapping and Execution role are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: package/runtime/init/VPC and extensions contribute before handler execution. polls streams/queues and manages batches, concurrency, retries and checkpoints. function AWS permissions should exclude deployment/administrative capabilities. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-03

- [ ] **Question:** Design a production AWS Lambda capability where Reserved concurrency, Idempotency and Destinations/DLQ are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reserves and caps concurrency for a function, protecting account/downstream. retried/duplicate events need stable business-effect keys and durable records. async outcomes capture failed/successful invocation metadata under service-specific rules. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Lambda capability where Provisioned concurrency, VPC networking and Timeout/cancellation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pre-initializes environments for latency at continuous cost. subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. function timeout must fit caller/dependency deadlines and leave effects consistent. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-05

- [ ] **Question:** Design a production AWS Lambda capability where Event source mapping, Execution role and Execution environment are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: polls streams/queues and manages batches, concurrency, retries and checkpoints. function AWS permissions should exclude deployment/administrative capabilities. initialization may be reused across invocations but must not hold unsafe tenant state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Lambda capability where Idempotency, Destinations/DLQ and Cold start are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retried/duplicate events need stable business-effect keys and durable records. async outcomes capture failed/successful invocation metadata under service-specific rules. package/runtime/init/VPC and extensions contribute before handler execution. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-07

- [ ] **Question:** Design a production AWS Lambda capability where VPC networking, Timeout/cancellation and Reserved concurrency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. function timeout must fit caller/dependency deadlines and leave effects consistent. reserves and caps concurrency for a function, protecting account/downstream. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Lambda capability where Execution role, Execution environment and Provisioned concurrency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: function AWS permissions should exclude deployment/administrative capabilities. initialization may be reused across invocations but must not hold unsafe tenant state. pre-initializes environments for latency at continuous cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-09

- [ ] **Question:** Design a production AWS Lambda capability where Destinations/DLQ, Cold start and Event source mapping are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: async outcomes capture failed/successful invocation metadata under service-specific rules. package/runtime/init/VPC and extensions contribute before handler execution. polls streams/queues and manages batches, concurrency, retries and checkpoints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-LAMBDA-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Lambda capability where Timeout/cancellation, Reserved concurrency and Idempotency are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: function timeout must fit caller/dependency deadlines and leave effects consistent. reserves and caps concurrency for a function, protecting account/downstream. retried/duplicate events need stable business-effect keys and durable records. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-LAMBDA-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Execution environment. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda get-function-configuration --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. initialization may be reused across invocations but must not hold unsafe tenant state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cold start. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda get-function-concurrency --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. package/runtime/init/VPC and extensions contribute before handler execution. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reserved concurrency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda list-event-source-mappings --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. reserves and caps concurrency for a function, protecting account/downstream. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Provisioned concurrency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws logs tail /aws/lambda/FUNCTION --since 30m --follow` as one read-only checkpoint, not the whole diagnosis. pre-initializes environments for latency at continuous cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Event source mapping. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda get-function-configuration --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. polls streams/queues and manages batches, concurrency, retries and checkpoints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Idempotency. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda get-function-concurrency --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. retried/duplicate events need stable business-effect keys and durable records. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC networking. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda list-event-source-mappings --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. subnets, IP capacity, SG, NAT/endpoints/DNS become function dependencies. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Execution role. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws logs tail /aws/lambda/FUNCTION --since 30m --follow` as one read-only checkpoint, not the whole diagnosis. function AWS permissions should exclude deployment/administrative capabilities. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Destinations/DLQ. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda get-function-configuration --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. async outcomes capture failed/successful invocation metadata under service-specific rules. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-LAMBDA-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Timeout/cancellation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws lambda get-function-concurrency --function-name FUNCTION` as one read-only checkpoint, not the whole diagnosis. function timeout must fit caller/dependency deadlines and leave effects consistent. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
