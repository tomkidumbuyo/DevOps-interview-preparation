# AWS Step Functions — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-STEP-FUNCTIONS-JN-01

- [ ] **Question:** What is State machine, and why does it matter in AWS Step Functions?

**Answer:** Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STEP-FUNCTIONS-JN-02

- [ ] **Question:** What is Standard workflow, and why does it matter in AWS Step Functions?

**Answer:** durable exactly-once workflow execution semantics for long-running auditable flows. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STEP-FUNCTIONS-JN-03

- [ ] **Question:** What is Express workflow, and why does it matter in AWS Step Functions?

**Answer:** high-volume short workflows with different sync/async delivery/history semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STEP-FUNCTIONS-JN-04

- [ ] **Question:** What is Task integration, and why does it matter in AWS Step Functions?

**Answer:** optimized/AWS SDK/activity/callback patterns invoke external work. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STEP-FUNCTIONS-JN-05

- [ ] **Question:** What is Retry, and why does it matter in AWS Step Functions?

**Answer:** error-specific interval/backoff/max attempts must not duplicate unsafe effects. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STEP-FUNCTIONS-JN-06

- [ ] **Question:** What is Catch, and why does it matter in AWS Step Functions?

**Answer:** routes terminal task error into compensation/recovery paths. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STEP-FUNCTIONS-JN-07

- [ ] **Question:** What is Callback token, and why does it matter in AWS Step Functions?

**Answer:** pauses until an authorized external completion with timeout/heartbeat. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-STEP-FUNCTIONS-JN-08

- [ ] **Code:** **Question:** What does `aws stepfunctions get-execution-history --execution-arn ARN --reverse-order` help you verify for AWS Step Functions?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: processes collections with concurrency and failure thresholds.

### AWS-STEP-FUNCTIONS-JN-09

- [ ] **Code:** **Question:** What does `aws stepfunctions list-state-machines` help you verify for AWS Step Functions?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: records transitions/input/output and can leak sensitive data if unbounded.

### AWS-STEP-FUNCTIONS-JN-10

- [ ] **Code:** **Question:** What does `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` help you verify for AWS Step Functions?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: resumes eligible failed Standard executions while tasks remain idempotent.

## Junior — procedural and command questions

### AWS-STEP-FUNCTIONS-JP-01

- [ ] **Code:** **Question:** A basic State machine check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions list-state-machines` and capture exact status/reason/request ID. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-02

- [ ] **Question:** A basic Standard workflow check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` and capture exact status/reason/request ID. durable exactly-once workflow execution semantics for long-running auditable flows. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-03

- [ ] **Question:** A basic Express workflow check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions describe-execution --execution-arn ARN` and capture exact status/reason/request ID. high-volume short workflows with different sync/async delivery/history semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-04

- [ ] **Code:** **Question:** A basic Task integration check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions get-execution-history --execution-arn ARN --reverse-order` and capture exact status/reason/request ID. optimized/AWS SDK/activity/callback patterns invoke external work. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-05

- [ ] **Question:** A basic Retry check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions list-state-machines` and capture exact status/reason/request ID. error-specific interval/backoff/max attempts must not duplicate unsafe effects. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-06

- [ ] **Question:** A basic Catch check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` and capture exact status/reason/request ID. routes terminal task error into compensation/recovery paths. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-07

- [ ] **Code:** **Question:** A basic Callback token check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions describe-execution --execution-arn ARN` and capture exact status/reason/request ID. pauses until an authorized external completion with timeout/heartbeat. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-08

- [ ] **Question:** A basic Map state check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions get-execution-history --execution-arn ARN --reverse-order` and capture exact status/reason/request ID. processes collections with concurrency and failure thresholds. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-09

- [ ] **Question:** A basic Execution history check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions list-state-machines` and capture exact status/reason/request ID. records transitions/input/output and can leak sensitive data if unbounded. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-STEP-FUNCTIONS-JP-10

- [ ] **Code:** **Question:** A basic Redrive check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` and capture exact status/reason/request ID. resumes eligible failed Standard executions while tasks remain idempotent. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-STEP-FUNCTIONS-MN-01

- [ ] **Question:** Compare State machine with Standard workflow. When would each change your design?

**Answer:** State machine: Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Standard workflow: durable exactly-once workflow execution semantics for long-running auditable flows. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-02

- [ ] **Question:** Compare Standard workflow with Express workflow. When would each change your design?

**Answer:** Standard workflow: durable exactly-once workflow execution semantics for long-running auditable flows. Express workflow: high-volume short workflows with different sync/async delivery/history semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-03

- [ ] **Question:** Compare Express workflow with Task integration. When would each change your design?

**Answer:** Express workflow: high-volume short workflows with different sync/async delivery/history semantics. Task integration: optimized/AWS SDK/activity/callback patterns invoke external work. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Task integration with Retry. When would each change your design?

**Answer:** Task integration: optimized/AWS SDK/activity/callback patterns invoke external work. Retry: error-specific interval/backoff/max attempts must not duplicate unsafe effects. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-05

- [ ] **Question:** Compare Retry with Catch. When would each change your design?

**Answer:** Retry: error-specific interval/backoff/max attempts must not duplicate unsafe effects. Catch: routes terminal task error into compensation/recovery paths. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-06

- [ ] **Question:** Compare Catch with Callback token. When would each change your design?

**Answer:** Catch: routes terminal task error into compensation/recovery paths. Callback token: pauses until an authorized external completion with timeout/heartbeat. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Callback token with Map state. When would each change your design?

**Answer:** Callback token: pauses until an authorized external completion with timeout/heartbeat. Map state: processes collections with concurrency and failure thresholds. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-08

- [ ] **Question:** Compare Map state with Execution history. When would each change your design?

**Answer:** Map state: processes collections with concurrency and failure thresholds. Execution history: records transitions/input/output and can leak sensitive data if unbounded. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-09

- [ ] **Question:** Compare Execution history with Redrive. When would each change your design?

**Answer:** Execution history: records transitions/input/output and can leak sensitive data if unbounded. Redrive: resumes eligible failed Standard executions while tasks remain idempotent. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-STEP-FUNCTIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Redrive with State machine. When would each change your design?

**Answer:** Redrive: resumes eligible failed Standard executions while tasks remain idempotent. State machine: Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-STEP-FUNCTIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around State machine; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions list-state-machines` plus recent events/changes, then correlate the service-specific SLI. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-02

- [ ] **Question:** Production is degraded around Standard workflow; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` plus recent events/changes, then correlate the service-specific SLI. durable exactly-once workflow execution semantics for long-running auditable flows. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Express workflow; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions describe-execution --execution-arn ARN` plus recent events/changes, then correlate the service-specific SLI. high-volume short workflows with different sync/async delivery/history semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-04

- [ ] **Question:** Production is degraded around Task integration; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions get-execution-history --execution-arn ARN --reverse-order` plus recent events/changes, then correlate the service-specific SLI. optimized/AWS SDK/activity/callback patterns invoke external work. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Retry; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions list-state-machines` plus recent events/changes, then correlate the service-specific SLI. error-specific interval/backoff/max attempts must not duplicate unsafe effects. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-06

- [ ] **Question:** Production is degraded around Catch; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` plus recent events/changes, then correlate the service-specific SLI. routes terminal task error into compensation/recovery paths. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Callback token; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions describe-execution --execution-arn ARN` plus recent events/changes, then correlate the service-specific SLI. pauses until an authorized external completion with timeout/heartbeat. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-08

- [ ] **Question:** Production is degraded around Map state; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions get-execution-history --execution-arn ARN --reverse-order` plus recent events/changes, then correlate the service-specific SLI. processes collections with concurrency and failure thresholds. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Execution history; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions list-state-machines` plus recent events/changes, then correlate the service-specific SLI. records transitions/input/output and can leak sensitive data if unbounded. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-STEP-FUNCTIONS-MP-10

- [ ] **Question:** Production is degraded around Redrive; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` plus recent events/changes, then correlate the service-specific SLI. resumes eligible failed Standard executions while tasks remain idempotent. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-STEP-FUNCTIONS-SN-01

- [ ] **Question:** Design a production AWS Step Functions capability where State machine, Task integration and Callback token are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. optimized/AWS SDK/activity/callback patterns invoke external work. pauses until an authorized external completion with timeout/heartbeat. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Step Functions capability where Standard workflow, Retry and Map state are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: durable exactly-once workflow execution semantics for long-running auditable flows. error-specific interval/backoff/max attempts must not duplicate unsafe effects. processes collections with concurrency and failure thresholds. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-03

- [ ] **Question:** Design a production AWS Step Functions capability where Express workflow, Catch and Execution history are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-volume short workflows with different sync/async delivery/history semantics. routes terminal task error into compensation/recovery paths. records transitions/input/output and can leak sensitive data if unbounded. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Step Functions capability where Task integration, Callback token and Redrive are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: optimized/AWS SDK/activity/callback patterns invoke external work. pauses until an authorized external completion with timeout/heartbeat. resumes eligible failed Standard executions while tasks remain idempotent. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-05

- [ ] **Question:** Design a production AWS Step Functions capability where Retry, Map state and State machine are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: error-specific interval/backoff/max attempts must not duplicate unsafe effects. processes collections with concurrency and failure thresholds. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Step Functions capability where Catch, Execution history and Standard workflow are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: routes terminal task error into compensation/recovery paths. records transitions/input/output and can leak sensitive data if unbounded. durable exactly-once workflow execution semantics for long-running auditable flows. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-07

- [ ] **Question:** Design a production AWS Step Functions capability where Callback token, Redrive and Express workflow are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pauses until an authorized external completion with timeout/heartbeat. resumes eligible failed Standard executions while tasks remain idempotent. high-volume short workflows with different sync/async delivery/history semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Step Functions capability where Map state, State machine and Task integration are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: processes collections with concurrency and failure thresholds. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. optimized/AWS SDK/activity/callback patterns invoke external work. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-09

- [ ] **Question:** Design a production AWS Step Functions capability where Execution history, Standard workflow and Retry are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records transitions/input/output and can leak sensitive data if unbounded. durable exactly-once workflow execution semantics for long-running auditable flows. error-specific interval/backoff/max attempts must not duplicate unsafe effects. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-STEP-FUNCTIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Step Functions capability where Redrive, Express workflow and Catch are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resumes eligible failed Standard executions while tasks remain idempotent. high-volume short workflows with different sync/async delivery/history semantics. routes terminal task error into compensation/recovery paths. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-STEP-FUNCTIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving State machine. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions list-state-machines` as one read-only checkpoint, not the whole diagnosis. Amazon States Language graph defines tasks, choices, parallel/map, waits and terminal states. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Standard workflow. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` as one read-only checkpoint, not the whole diagnosis. durable exactly-once workflow execution semantics for long-running auditable flows. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Express workflow. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions describe-execution --execution-arn ARN` as one read-only checkpoint, not the whole diagnosis. high-volume short workflows with different sync/async delivery/history semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Task integration. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions get-execution-history --execution-arn ARN --reverse-order` as one read-only checkpoint, not the whole diagnosis. optimized/AWS SDK/activity/callback patterns invoke external work. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retry. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions list-state-machines` as one read-only checkpoint, not the whole diagnosis. error-specific interval/backoff/max attempts must not duplicate unsafe effects. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Catch. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` as one read-only checkpoint, not the whole diagnosis. routes terminal task error into compensation/recovery paths. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Callback token. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions describe-execution --execution-arn ARN` as one read-only checkpoint, not the whole diagnosis. pauses until an authorized external completion with timeout/heartbeat. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Map state. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions get-execution-history --execution-arn ARN --reverse-order` as one read-only checkpoint, not the whole diagnosis. processes collections with concurrency and failure thresholds. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Execution history. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions list-state-machines` as one read-only checkpoint, not the whole diagnosis. records transitions/input/output and can leak sensitive data if unbounded. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-STEP-FUNCTIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Redrive. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws stepfunctions validate-state-machine-definition --definition file://machine.asl.json` as one read-only checkpoint, not the whole diagnosis. resumes eligible failed Standard executions while tasks remain idempotent. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
