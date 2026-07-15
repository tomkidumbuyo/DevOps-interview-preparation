# Amazon ECS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-ECS-JN-01

- [ ] **Question:** What is Task definition, and why does it matter in Amazon ECS?

**Answer:** versioned container, resource, network, log, secret, volume and role specification. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECS-JN-02

- [ ] **Question:** What is Task, and why does it matter in Amazon ECS?

**Answer:** running/scheduled instantiation of a task definition. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECS-JN-03

- [ ] **Question:** What is Service, and why does it matter in Amazon ECS?

**Answer:** maintains desired tasks and integrates deployment, load balancing and discovery. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECS-JN-04

- [ ] **Question:** What is Task role, and why does it matter in Amazon ECS?

**Answer:** application AWS permissions exposed to containers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECS-JN-05

- [ ] **Question:** What is Execution role, and why does it matter in Amazon ECS?

**Answer:** agent permissions for image pull, logs and startup secret retrieval. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECS-JN-06

- [ ] **Question:** What is awsvpc networking, and why does it matter in Amazon ECS?

**Answer:** each task gets an ENI/IP/security groups and consumes subnet capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECS-JN-07

- [ ] **Question:** What is Fargate, and why does it matter in Amazon ECS?

**Answer:** managed task compute removes node operations with feature, startup and pricing trade-offs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ECS-JN-08

- [ ] **Code:** **Question:** What does `aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh` help you verify for Amazon ECS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: associates EC2 ASG/Fargate capacity and placement strategy with services.

### AMAZON-ECS-JN-09

- [ ] **Code:** **Question:** What does `aws ecs describe-clusters --clusters CLUSTER` help you verify for Amazon ECS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: detects failed service stabilization and can roll back.

### AMAZON-ECS-JN-10

- [ ] **Code:** **Question:** What does `aws ecs describe-services --cluster CLUSTER --services SERVICE` help you verify for Amazon ECS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: load balancer, stop timeout and application signal handling protect in-flight work.

## Junior — procedural and command questions

### AMAZON-ECS-JP-01

- [ ] **Code:** **Question:** A basic Task definition check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-clusters --clusters CLUSTER` and capture exact status/reason/request ID. versioned container, resource, network, log, secret, volume and role specification. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-02

- [ ] **Question:** A basic Task check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-services --cluster CLUSTER --services SERVICE` and capture exact status/reason/request ID. running/scheduled instantiation of a task definition. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-03

- [ ] **Question:** A basic Service check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-tasks --cluster CLUSTER --tasks TASK` and capture exact status/reason/request ID. maintains desired tasks and integrates deployment, load balancing and discovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-04

- [ ] **Code:** **Question:** A basic Task role check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh` and capture exact status/reason/request ID. application AWS permissions exposed to containers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-05

- [ ] **Question:** A basic Execution role check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-clusters --clusters CLUSTER` and capture exact status/reason/request ID. agent permissions for image pull, logs and startup secret retrieval. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-06

- [ ] **Question:** A basic awsvpc networking check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-services --cluster CLUSTER --services SERVICE` and capture exact status/reason/request ID. each task gets an ENI/IP/security groups and consumes subnet capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-07

- [ ] **Code:** **Question:** A basic Fargate check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-tasks --cluster CLUSTER --tasks TASK` and capture exact status/reason/request ID. managed task compute removes node operations with feature, startup and pricing trade-offs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-08

- [ ] **Question:** A basic Capacity provider check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh` and capture exact status/reason/request ID. associates EC2 ASG/Fargate capacity and placement strategy with services. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-09

- [ ] **Question:** A basic Deployment circuit breaker check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-clusters --clusters CLUSTER` and capture exact status/reason/request ID. detects failed service stabilization and can roll back. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ECS-JP-10

- [ ] **Code:** **Question:** A basic Task draining check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-services --cluster CLUSTER --services SERVICE` and capture exact status/reason/request ID. load balancer, stop timeout and application signal handling protect in-flight work. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-ECS-MN-01

- [ ] **Question:** Compare Task definition with Task. When would each change your design?

**Answer:** Task definition: versioned container, resource, network, log, secret, volume and role specification. Task: running/scheduled instantiation of a task definition. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-02

- [ ] **Question:** Compare Task with Service. When would each change your design?

**Answer:** Task: running/scheduled instantiation of a task definition. Service: maintains desired tasks and integrates deployment, load balancing and discovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-03

- [ ] **Question:** Compare Service with Task role. When would each change your design?

**Answer:** Service: maintains desired tasks and integrates deployment, load balancing and discovery. Task role: application AWS permissions exposed to containers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-04

- [ ] **Configuration review:** **Question:** Compare Task role with Execution role. When would each change your design?

**Answer:** Task role: application AWS permissions exposed to containers. Execution role: agent permissions for image pull, logs and startup secret retrieval. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-05

- [ ] **Question:** Compare Execution role with awsvpc networking. When would each change your design?

**Answer:** Execution role: agent permissions for image pull, logs and startup secret retrieval. awsvpc networking: each task gets an ENI/IP/security groups and consumes subnet capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-06

- [ ] **Question:** Compare awsvpc networking with Fargate. When would each change your design?

**Answer:** awsvpc networking: each task gets an ENI/IP/security groups and consumes subnet capacity. Fargate: managed task compute removes node operations with feature, startup and pricing trade-offs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-07

- [ ] **Configuration review:** **Question:** Compare Fargate with Capacity provider. When would each change your design?

**Answer:** Fargate: managed task compute removes node operations with feature, startup and pricing trade-offs. Capacity provider: associates EC2 ASG/Fargate capacity and placement strategy with services. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-08

- [ ] **Question:** Compare Capacity provider with Deployment circuit breaker. When would each change your design?

**Answer:** Capacity provider: associates EC2 ASG/Fargate capacity and placement strategy with services. Deployment circuit breaker: detects failed service stabilization and can roll back. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-09

- [ ] **Question:** Compare Deployment circuit breaker with Task draining. When would each change your design?

**Answer:** Deployment circuit breaker: detects failed service stabilization and can roll back. Task draining: load balancer, stop timeout and application signal handling protect in-flight work. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ECS-MN-10

- [ ] **Configuration review:** **Question:** Compare Task draining with Task definition. When would each change your design?

**Answer:** Task draining: load balancer, stop timeout and application signal handling protect in-flight work. Task definition: versioned container, resource, network, log, secret, volume and role specification. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-ECS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Task definition; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-clusters --clusters CLUSTER` plus recent events/changes, then correlate the service-specific SLI. versioned container, resource, network, log, secret, volume and role specification. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-02

- [ ] **Question:** Production is degraded around Task; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-services --cluster CLUSTER --services SERVICE` plus recent events/changes, then correlate the service-specific SLI. running/scheduled instantiation of a task definition. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Service; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-tasks --cluster CLUSTER --tasks TASK` plus recent events/changes, then correlate the service-specific SLI. maintains desired tasks and integrates deployment, load balancing and discovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-04

- [ ] **Question:** Production is degraded around Task role; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh` plus recent events/changes, then correlate the service-specific SLI. application AWS permissions exposed to containers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Execution role; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-clusters --clusters CLUSTER` plus recent events/changes, then correlate the service-specific SLI. agent permissions for image pull, logs and startup secret retrieval. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-06

- [ ] **Question:** Production is degraded around awsvpc networking; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-services --cluster CLUSTER --services SERVICE` plus recent events/changes, then correlate the service-specific SLI. each task gets an ENI/IP/security groups and consumes subnet capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Fargate; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-tasks --cluster CLUSTER --tasks TASK` plus recent events/changes, then correlate the service-specific SLI. managed task compute removes node operations with feature, startup and pricing trade-offs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-08

- [ ] **Question:** Production is degraded around Capacity provider; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh` plus recent events/changes, then correlate the service-specific SLI. associates EC2 ASG/Fargate capacity and placement strategy with services. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Deployment circuit breaker; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-clusters --clusters CLUSTER` plus recent events/changes, then correlate the service-specific SLI. detects failed service stabilization and can roll back. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ECS-MP-10

- [ ] **Question:** Production is degraded around Task draining; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-services --cluster CLUSTER --services SERVICE` plus recent events/changes, then correlate the service-specific SLI. load balancer, stop timeout and application signal handling protect in-flight work. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-ECS-SN-01

- [ ] **Question:** Design a production Amazon ECS capability where Task definition, Task role and Fargate are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned container, resource, network, log, secret, volume and role specification. application AWS permissions exposed to containers. managed task compute removes node operations with feature, startup and pricing trade-offs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECS capability where Task, Execution role and Capacity provider are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: running/scheduled instantiation of a task definition. agent permissions for image pull, logs and startup secret retrieval. associates EC2 ASG/Fargate capacity and placement strategy with services. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-03

- [ ] **Question:** Design a production Amazon ECS capability where Service, awsvpc networking and Deployment circuit breaker are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maintains desired tasks and integrates deployment, load balancing and discovery. each task gets an ENI/IP/security groups and consumes subnet capacity. detects failed service stabilization and can roll back. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECS capability where Task role, Fargate and Task draining are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: application AWS permissions exposed to containers. managed task compute removes node operations with feature, startup and pricing trade-offs. load balancer, stop timeout and application signal handling protect in-flight work. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-05

- [ ] **Question:** Design a production Amazon ECS capability where Execution role, Capacity provider and Task definition are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: agent permissions for image pull, logs and startup secret retrieval. associates EC2 ASG/Fargate capacity and placement strategy with services. versioned container, resource, network, log, secret, volume and role specification. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECS capability where awsvpc networking, Deployment circuit breaker and Task are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: each task gets an ENI/IP/security groups and consumes subnet capacity. detects failed service stabilization and can roll back. running/scheduled instantiation of a task definition. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-07

- [ ] **Question:** Design a production Amazon ECS capability where Fargate, Task draining and Service are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed task compute removes node operations with feature, startup and pricing trade-offs. load balancer, stop timeout and application signal handling protect in-flight work. maintains desired tasks and integrates deployment, load balancing and discovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECS capability where Capacity provider, Task definition and Task role are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: associates EC2 ASG/Fargate capacity and placement strategy with services. versioned container, resource, network, log, secret, volume and role specification. application AWS permissions exposed to containers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-09

- [ ] **Question:** Design a production Amazon ECS capability where Deployment circuit breaker, Task and Execution role are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: detects failed service stabilization and can roll back. running/scheduled instantiation of a task definition. agent permissions for image pull, logs and startup secret retrieval. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ECS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon ECS capability where Task draining, Service and awsvpc networking are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: load balancer, stop timeout and application signal handling protect in-flight work. maintains desired tasks and integrates deployment, load balancing and discovery. each task gets an ENI/IP/security groups and consumes subnet capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-ECS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Task definition. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-clusters --clusters CLUSTER` as one read-only checkpoint, not the whole diagnosis. versioned container, resource, network, log, secret, volume and role specification. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Task. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-services --cluster CLUSTER --services SERVICE` as one read-only checkpoint, not the whole diagnosis. running/scheduled instantiation of a task definition. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-tasks --cluster CLUSTER --tasks TASK` as one read-only checkpoint, not the whole diagnosis. maintains desired tasks and integrates deployment, load balancing and discovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Task role. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh` as one read-only checkpoint, not the whole diagnosis. application AWS permissions exposed to containers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Execution role. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-clusters --clusters CLUSTER` as one read-only checkpoint, not the whole diagnosis. agent permissions for image pull, logs and startup secret retrieval. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving awsvpc networking. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-services --cluster CLUSTER --services SERVICE` as one read-only checkpoint, not the whole diagnosis. each task gets an ENI/IP/security groups and consumes subnet capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fargate. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-tasks --cluster CLUSTER --tasks TASK` as one read-only checkpoint, not the whole diagnosis. managed task compute removes node operations with feature, startup and pricing trade-offs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Capacity provider. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs execute-command --cluster CLUSTER --task TASK --container CONTAINER --interactive --command /bin/sh` as one read-only checkpoint, not the whole diagnosis. associates EC2 ASG/Fargate capacity and placement strategy with services. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deployment circuit breaker. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-clusters --clusters CLUSTER` as one read-only checkpoint, not the whole diagnosis. detects failed service stabilization and can roll back. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ECS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Task draining. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-services --cluster CLUSTER --services SERVICE` as one read-only checkpoint, not the whole diagnosis. load balancer, stop timeout and application signal handling protect in-flight work. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
