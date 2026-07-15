# Workloads — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-WORKLOADS-JN-01

- [ ] **Question:** What is Pod sandbox, and why does it matter in Workloads?

**Answer:** containers share network namespace and can share IPC/process/volumes by configuration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-WORKLOADS-JN-02

- [ ] **Question:** What is Phase, and why does it matter in Workloads?

**Answer:** Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-WORKLOADS-JN-03

- [ ] **Question:** What is Deployment selector, and why does it matter in Workloads?

**Answer:** immutable label contract determines which ReplicaSets/Pods are owned. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-WORKLOADS-JN-04

- [ ] **Question:** What is Pod template hash, and why does it matter in Workloads?

**Answer:** creates a new ReplicaSet when template content changes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-WORKLOADS-JN-05

- [ ] **Question:** What is Stateful ordinal, and why does it matter in Workloads?

**Answer:** stable Pod name/identity persists across rescheduling but not physical node. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-WORKLOADS-JN-06

- [ ] **Question:** What is Headless Service, and why does it matter in Workloads?

**Answer:** publishes per-Pod DNS identity for StatefulSet membership. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-WORKLOADS-JN-07

- [ ] **Question:** What is Completion, and why does it matter in Workloads?

**Answer:** Job succeeds after required successful Pods/completions under mode semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-WORKLOADS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get statefulset,daemonset -A` help you verify for Workloads?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: number of Pods executing concurrently and downstream load.

### BRANCH-WORKLOADS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get job,cronjob -A` help you verify for Workloads?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: delays liveness/readiness scheduling until slow initialization succeeds.

### BRANCH-WORKLOADS-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` help you verify for Workloads?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: detects unrecoverable local process state and triggers restart.

## Junior — procedural and command questions

### BRANCH-WORKLOADS-JP-01

- [ ] **Code:** **Question:** A basic Pod sandbox check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o yaml` and capture exact status/reason/request ID. containers share network namespace and can share IPC/process/volumes by configuration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-02

- [ ] **Question:** A basic Phase check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/NAME -n NS` and capture exact status/reason/request ID. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-03

- [ ] **Question:** A basic Deployment selector check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get statefulset,daemonset -A` and capture exact status/reason/request ID. immutable label contract determines which ReplicaSets/Pods are owned. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-04

- [ ] **Code:** **Question:** A basic Pod template hash check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get job,cronjob -A` and capture exact status/reason/request ID. creates a new ReplicaSet when template content changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-05

- [ ] **Question:** A basic Stateful ordinal check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` and capture exact status/reason/request ID. stable Pod name/identity persists across rescheduling but not physical node. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-06

- [ ] **Question:** A basic Headless Service check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pod POD -n NS -o yaml` and capture exact status/reason/request ID. publishes per-Pod DNS identity for StatefulSet membership. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-07

- [ ] **Code:** **Question:** A basic Completion check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/NAME -n NS` and capture exact status/reason/request ID. Job succeeds after required successful Pods/completions under mode semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-08

- [ ] **Question:** A basic Parallelism check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get statefulset,daemonset -A` and capture exact status/reason/request ID. number of Pods executing concurrently and downstream load. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-09

- [ ] **Question:** A basic Startup probe check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get job,cronjob -A` and capture exact status/reason/request ID. delays liveness/readiness scheduling until slow initialization succeeds. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-WORKLOADS-JP-10

- [ ] **Code:** **Question:** A basic Liveness probe check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` and capture exact status/reason/request ID. detects unrecoverable local process state and triggers restart. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-WORKLOADS-MN-01

- [ ] **Question:** Compare Pod sandbox with Phase. When would each change your design?

**Answer:** Pod sandbox: containers share network namespace and can share IPC/process/volumes by configuration. Phase: Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-02

- [ ] **Question:** Compare Phase with Deployment selector. When would each change your design?

**Answer:** Phase: Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Deployment selector: immutable label contract determines which ReplicaSets/Pods are owned. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-03

- [ ] **Question:** Compare Deployment selector with Pod template hash. When would each change your design?

**Answer:** Deployment selector: immutable label contract determines which ReplicaSets/Pods are owned. Pod template hash: creates a new ReplicaSet when template content changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-04

- [ ] **Configuration review:** **Question:** Compare Pod template hash with Stateful ordinal. When would each change your design?

**Answer:** Pod template hash: creates a new ReplicaSet when template content changes. Stateful ordinal: stable Pod name/identity persists across rescheduling but not physical node. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-05

- [ ] **Question:** Compare Stateful ordinal with Headless Service. When would each change your design?

**Answer:** Stateful ordinal: stable Pod name/identity persists across rescheduling but not physical node. Headless Service: publishes per-Pod DNS identity for StatefulSet membership. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-06

- [ ] **Question:** Compare Headless Service with Completion. When would each change your design?

**Answer:** Headless Service: publishes per-Pod DNS identity for StatefulSet membership. Completion: Job succeeds after required successful Pods/completions under mode semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-07

- [ ] **Configuration review:** **Question:** Compare Completion with Parallelism. When would each change your design?

**Answer:** Completion: Job succeeds after required successful Pods/completions under mode semantics. Parallelism: number of Pods executing concurrently and downstream load. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-08

- [ ] **Question:** Compare Parallelism with Startup probe. When would each change your design?

**Answer:** Parallelism: number of Pods executing concurrently and downstream load. Startup probe: delays liveness/readiness scheduling until slow initialization succeeds. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-09

- [ ] **Question:** Compare Startup probe with Liveness probe. When would each change your design?

**Answer:** Startup probe: delays liveness/readiness scheduling until slow initialization succeeds. Liveness probe: detects unrecoverable local process state and triggers restart. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-WORKLOADS-MN-10

- [ ] **Configuration review:** **Question:** Compare Liveness probe with Pod sandbox. When would each change your design?

**Answer:** Liveness probe: detects unrecoverable local process state and triggers restart. Pod sandbox: containers share network namespace and can share IPC/process/volumes by configuration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-WORKLOADS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pod sandbox; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o yaml` plus recent events/changes, then correlate the service-specific SLI. containers share network namespace and can share IPC/process/volumes by configuration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-02

- [ ] **Question:** Production is degraded around Phase; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Deployment selector; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get statefulset,daemonset -A` plus recent events/changes, then correlate the service-specific SLI. immutable label contract determines which ReplicaSets/Pods are owned. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-04

- [ ] **Question:** Production is degraded around Pod template hash; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get job,cronjob -A` plus recent events/changes, then correlate the service-specific SLI. creates a new ReplicaSet when template content changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stateful ordinal; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` plus recent events/changes, then correlate the service-specific SLI. stable Pod name/identity persists across rescheduling but not physical node. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-06

- [ ] **Question:** Production is degraded around Headless Service; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pod POD -n NS -o yaml` plus recent events/changes, then correlate the service-specific SLI. publishes per-Pod DNS identity for StatefulSet membership. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Completion; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. Job succeeds after required successful Pods/completions under mode semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-08

- [ ] **Question:** Production is degraded around Parallelism; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get statefulset,daemonset -A` plus recent events/changes, then correlate the service-specific SLI. number of Pods executing concurrently and downstream load. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Startup probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get job,cronjob -A` plus recent events/changes, then correlate the service-specific SLI. delays liveness/readiness scheduling until slow initialization succeeds. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-WORKLOADS-MP-10

- [ ] **Question:** Production is degraded around Liveness probe; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` plus recent events/changes, then correlate the service-specific SLI. detects unrecoverable local process state and triggers restart. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-WORKLOADS-SN-01

- [ ] **Question:** Design a production Workloads capability where Pod sandbox, Pod template hash and Completion are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: containers share network namespace and can share IPC/process/volumes by configuration. creates a new ReplicaSet when template content changes. Job succeeds after required successful Pods/completions under mode semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Workloads capability where Phase, Stateful ordinal and Parallelism are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. stable Pod name/identity persists across rescheduling but not physical node. number of Pods executing concurrently and downstream load. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-03

- [ ] **Question:** Design a production Workloads capability where Deployment selector, Headless Service and Startup probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable label contract determines which ReplicaSets/Pods are owned. publishes per-Pod DNS identity for StatefulSet membership. delays liveness/readiness scheduling until slow initialization succeeds. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Workloads capability where Pod template hash, Completion and Liveness probe are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: creates a new ReplicaSet when template content changes. Job succeeds after required successful Pods/completions under mode semantics. detects unrecoverable local process state and triggers restart. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-05

- [ ] **Question:** Design a production Workloads capability where Stateful ordinal, Parallelism and Pod sandbox are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stable Pod name/identity persists across rescheduling but not physical node. number of Pods executing concurrently and downstream load. containers share network namespace and can share IPC/process/volumes by configuration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Workloads capability where Headless Service, Startup probe and Phase are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: publishes per-Pod DNS identity for StatefulSet membership. delays liveness/readiness scheduling until slow initialization succeeds. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-07

- [ ] **Question:** Design a production Workloads capability where Completion, Liveness probe and Deployment selector are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Job succeeds after required successful Pods/completions under mode semantics. detects unrecoverable local process state and triggers restart. immutable label contract determines which ReplicaSets/Pods are owned. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Workloads capability where Parallelism, Pod sandbox and Pod template hash are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: number of Pods executing concurrently and downstream load. containers share network namespace and can share IPC/process/volumes by configuration. creates a new ReplicaSet when template content changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-09

- [ ] **Question:** Design a production Workloads capability where Startup probe, Phase and Stateful ordinal are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: delays liveness/readiness scheduling until slow initialization succeeds. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. stable Pod name/identity persists across rescheduling but not physical node. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-WORKLOADS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Workloads capability where Liveness probe, Deployment selector and Headless Service are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: detects unrecoverable local process state and triggers restart. immutable label contract determines which ReplicaSets/Pods are owned. publishes per-Pod DNS identity for StatefulSet membership. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-WORKLOADS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod sandbox. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o yaml` as one read-only checkpoint, not the whole diagnosis. containers share network namespace and can share IPC/process/volumes by configuration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Phase. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. Pending/Running/Succeeded/Failed/Unknown is coarse and conditions/container states give real detail. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deployment selector. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get statefulset,daemonset -A` as one read-only checkpoint, not the whole diagnosis. immutable label contract determines which ReplicaSets/Pods are owned. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod template hash. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get job,cronjob -A` as one read-only checkpoint, not the whole diagnosis. creates a new ReplicaSet when template content changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stateful ordinal. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` as one read-only checkpoint, not the whole diagnosis. stable Pod name/identity persists across rescheduling but not physical node. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Headless Service. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pod POD -n NS -o yaml` as one read-only checkpoint, not the whole diagnosis. publishes per-Pod DNS identity for StatefulSet membership. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Completion. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. Job succeeds after required successful Pods/completions under mode semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parallelism. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get statefulset,daemonset -A` as one read-only checkpoint, not the whole diagnosis. number of Pods executing concurrently and downstream load. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Startup probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get job,cronjob -A` as one read-only checkpoint, not the whole diagnosis. delays liveness/readiness scheduling until slow initialization succeeds. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-WORKLOADS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Liveness probe. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe pod POD -n NS | sed -n '/Liveness:/,/Conditions:/p'` as one read-only checkpoint, not the whole diagnosis. detects unrecoverable local process state and triggers restart. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
