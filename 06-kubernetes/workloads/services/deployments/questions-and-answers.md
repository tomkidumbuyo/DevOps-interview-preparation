# Deployments and ReplicaSets — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### DEPLOYMENTS-AND-REPLICASETS-JN-01

- [ ] **Question:** What is Deployment selector, and why does it matter in Deployments and ReplicaSets?

**Answer:** immutable label contract determines which ReplicaSets/Pods are owned. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEPLOYMENTS-AND-REPLICASETS-JN-02

- [ ] **Question:** What is Pod template hash, and why does it matter in Deployments and ReplicaSets?

**Answer:** creates a new ReplicaSet when template content changes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEPLOYMENTS-AND-REPLICASETS-JN-03

- [ ] **Question:** What is RollingUpdate, and why does it matter in Deployments and ReplicaSets?

**Answer:** maxSurge/maxUnavailable bound temporary capacity and disruption. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEPLOYMENTS-AND-REPLICASETS-JN-04

- [ ] **Question:** What is Recreate, and why does it matter in Deployments and ReplicaSets?

**Answer:** terminates old Pods before new when coexistence is unsafe. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEPLOYMENTS-AND-REPLICASETS-JN-05

- [ ] **Question:** What is minReadySeconds, and why does it matter in Deployments and ReplicaSets?

**Answer:** requires sustained readiness before a Pod counts available. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEPLOYMENTS-AND-REPLICASETS-JN-06

- [ ] **Question:** What is progressDeadlineSeconds, and why does it matter in Deployments and ReplicaSets?

**Answer:** marks rollout stalled but does not automatically roll back. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEPLOYMENTS-AND-REPLICASETS-JN-07

- [ ] **Question:** What is Revision history, and why does it matter in Deployments and ReplicaSets?

**Answer:** retained ReplicaSets enable undo at storage/resource cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEPLOYMENTS-AND-REPLICASETS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get rs -n NS --sort-by=.metadata.creationTimestamp` help you verify for Deployments and ReplicaSets?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: batches template changes before a new rollout.

### DEPLOYMENTS-AND-REPLICASETS-JN-09

- [ ] **Code:** **Question:** What does `kubectl rollout status deployment/NAME -n NS` help you verify for Deployments and ReplicaSets?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: desired/updated/ready/available replicas explain rollout state.

### DEPLOYMENTS-AND-REPLICASETS-JN-10

- [ ] **Code:** **Question:** What does `kubectl rollout history deployment/NAME -n NS` help you verify for Deployments and ReplicaSets?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: readiness, preStop, grace and LB endpoint propagation protect in-flight work.

## Junior — procedural and command questions

### DEPLOYMENTS-AND-REPLICASETS-JP-01

- [ ] **Code:** **Question:** A basic Deployment selector check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/NAME -n NS` and capture exact status/reason/request ID. immutable label contract determines which ReplicaSets/Pods are owned. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-02

- [ ] **Question:** A basic Pod template hash check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/NAME -n NS` and capture exact status/reason/request ID. creates a new ReplicaSet when template content changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-03

- [ ] **Question:** A basic RollingUpdate check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout undo deployment/NAME -n NS --to-revision=REV` and capture exact status/reason/request ID. maxSurge/maxUnavailable bound temporary capacity and disruption. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-04

- [ ] **Code:** **Question:** A basic Recreate check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get rs -n NS --sort-by=.metadata.creationTimestamp` and capture exact status/reason/request ID. terminates old Pods before new when coexistence is unsafe. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-05

- [ ] **Question:** A basic minReadySeconds check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/NAME -n NS` and capture exact status/reason/request ID. requires sustained readiness before a Pod counts available. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-06

- [ ] **Question:** A basic progressDeadlineSeconds check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/NAME -n NS` and capture exact status/reason/request ID. marks rollout stalled but does not automatically roll back. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-07

- [ ] **Code:** **Question:** A basic Revision history check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout undo deployment/NAME -n NS --to-revision=REV` and capture exact status/reason/request ID. retained ReplicaSets enable undo at storage/resource cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-08

- [ ] **Question:** A basic Pause/resume check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get rs -n NS --sort-by=.metadata.creationTimestamp` and capture exact status/reason/request ID. batches template changes before a new rollout. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-09

- [ ] **Question:** A basic Availability condition check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout status deployment/NAME -n NS` and capture exact status/reason/request ID. desired/updated/ready/available replicas explain rollout state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEPLOYMENTS-AND-REPLICASETS-JP-10

- [ ] **Code:** **Question:** A basic Drain compatibility check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/NAME -n NS` and capture exact status/reason/request ID. readiness, preStop, grace and LB endpoint propagation protect in-flight work. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### DEPLOYMENTS-AND-REPLICASETS-MN-01

- [ ] **Question:** Compare Deployment selector with Pod template hash. When would each change your design?

**Answer:** Deployment selector: immutable label contract determines which ReplicaSets/Pods are owned. Pod template hash: creates a new ReplicaSet when template content changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-02

- [ ] **Question:** Compare Pod template hash with RollingUpdate. When would each change your design?

**Answer:** Pod template hash: creates a new ReplicaSet when template content changes. RollingUpdate: maxSurge/maxUnavailable bound temporary capacity and disruption. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-03

- [ ] **Question:** Compare RollingUpdate with Recreate. When would each change your design?

**Answer:** RollingUpdate: maxSurge/maxUnavailable bound temporary capacity and disruption. Recreate: terminates old Pods before new when coexistence is unsafe. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-04

- [ ] **Configuration review:** **Question:** Compare Recreate with minReadySeconds. When would each change your design?

**Answer:** Recreate: terminates old Pods before new when coexistence is unsafe. minReadySeconds: requires sustained readiness before a Pod counts available. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-05

- [ ] **Question:** Compare minReadySeconds with progressDeadlineSeconds. When would each change your design?

**Answer:** minReadySeconds: requires sustained readiness before a Pod counts available. progressDeadlineSeconds: marks rollout stalled but does not automatically roll back. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-06

- [ ] **Question:** Compare progressDeadlineSeconds with Revision history. When would each change your design?

**Answer:** progressDeadlineSeconds: marks rollout stalled but does not automatically roll back. Revision history: retained ReplicaSets enable undo at storage/resource cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-07

- [ ] **Configuration review:** **Question:** Compare Revision history with Pause/resume. When would each change your design?

**Answer:** Revision history: retained ReplicaSets enable undo at storage/resource cost. Pause/resume: batches template changes before a new rollout. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-08

- [ ] **Question:** Compare Pause/resume with Availability condition. When would each change your design?

**Answer:** Pause/resume: batches template changes before a new rollout. Availability condition: desired/updated/ready/available replicas explain rollout state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-09

- [ ] **Question:** Compare Availability condition with Drain compatibility. When would each change your design?

**Answer:** Availability condition: desired/updated/ready/available replicas explain rollout state. Drain compatibility: readiness, preStop, grace and LB endpoint propagation protect in-flight work. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEPLOYMENTS-AND-REPLICASETS-MN-10

- [ ] **Configuration review:** **Question:** Compare Drain compatibility with Deployment selector. When would each change your design?

**Answer:** Drain compatibility: readiness, preStop, grace and LB endpoint propagation protect in-flight work. Deployment selector: immutable label contract determines which ReplicaSets/Pods are owned. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### DEPLOYMENTS-AND-REPLICASETS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Deployment selector; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. immutable label contract determines which ReplicaSets/Pods are owned. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-02

- [ ] **Question:** Production is degraded around Pod template hash; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. creates a new ReplicaSet when template content changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around RollingUpdate; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout undo deployment/NAME -n NS --to-revision=REV` plus recent events/changes, then correlate the service-specific SLI. maxSurge/maxUnavailable bound temporary capacity and disruption. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-04

- [ ] **Question:** Production is degraded around Recreate; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get rs -n NS --sort-by=.metadata.creationTimestamp` plus recent events/changes, then correlate the service-specific SLI. terminates old Pods before new when coexistence is unsafe. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around minReadySeconds; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. requires sustained readiness before a Pod counts available. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-06

- [ ] **Question:** Production is degraded around progressDeadlineSeconds; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. marks rollout stalled but does not automatically roll back. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Revision history; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout undo deployment/NAME -n NS --to-revision=REV` plus recent events/changes, then correlate the service-specific SLI. retained ReplicaSets enable undo at storage/resource cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-08

- [ ] **Question:** Production is degraded around Pause/resume; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get rs -n NS --sort-by=.metadata.creationTimestamp` plus recent events/changes, then correlate the service-specific SLI. batches template changes before a new rollout. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Availability condition; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout status deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. desired/updated/ready/available replicas explain rollout state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEPLOYMENTS-AND-REPLICASETS-MP-10

- [ ] **Question:** Production is degraded around Drain compatibility; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. readiness, preStop, grace and LB endpoint propagation protect in-flight work. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### DEPLOYMENTS-AND-REPLICASETS-SN-01

- [ ] **Question:** Design a production Deployments and ReplicaSets capability where Deployment selector, Recreate and Revision history are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable label contract determines which ReplicaSets/Pods are owned. terminates old Pods before new when coexistence is unsafe. retained ReplicaSets enable undo at storage/resource cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Deployments and ReplicaSets capability where Pod template hash, minReadySeconds and Pause/resume are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: creates a new ReplicaSet when template content changes. requires sustained readiness before a Pod counts available. batches template changes before a new rollout. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-03

- [ ] **Question:** Design a production Deployments and ReplicaSets capability where RollingUpdate, progressDeadlineSeconds and Availability condition are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maxSurge/maxUnavailable bound temporary capacity and disruption. marks rollout stalled but does not automatically roll back. desired/updated/ready/available replicas explain rollout state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Deployments and ReplicaSets capability where Recreate, Revision history and Drain compatibility are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: terminates old Pods before new when coexistence is unsafe. retained ReplicaSets enable undo at storage/resource cost. readiness, preStop, grace and LB endpoint propagation protect in-flight work. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-05

- [ ] **Question:** Design a production Deployments and ReplicaSets capability where minReadySeconds, Pause/resume and Deployment selector are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: requires sustained readiness before a Pod counts available. batches template changes before a new rollout. immutable label contract determines which ReplicaSets/Pods are owned. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Deployments and ReplicaSets capability where progressDeadlineSeconds, Availability condition and Pod template hash are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: marks rollout stalled but does not automatically roll back. desired/updated/ready/available replicas explain rollout state. creates a new ReplicaSet when template content changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-07

- [ ] **Question:** Design a production Deployments and ReplicaSets capability where Revision history, Drain compatibility and RollingUpdate are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retained ReplicaSets enable undo at storage/resource cost. readiness, preStop, grace and LB endpoint propagation protect in-flight work. maxSurge/maxUnavailable bound temporary capacity and disruption. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Deployments and ReplicaSets capability where Pause/resume, Deployment selector and Recreate are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: batches template changes before a new rollout. immutable label contract determines which ReplicaSets/Pods are owned. terminates old Pods before new when coexistence is unsafe. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-09

- [ ] **Question:** Design a production Deployments and ReplicaSets capability where Availability condition, Pod template hash and minReadySeconds are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: desired/updated/ready/available replicas explain rollout state. creates a new ReplicaSet when template content changes. requires sustained readiness before a Pod counts available. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEPLOYMENTS-AND-REPLICASETS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Deployments and ReplicaSets capability where Drain compatibility, RollingUpdate and progressDeadlineSeconds are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: readiness, preStop, grace and LB endpoint propagation protect in-flight work. maxSurge/maxUnavailable bound temporary capacity and disruption. marks rollout stalled but does not automatically roll back. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### DEPLOYMENTS-AND-REPLICASETS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deployment selector. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. immutable label contract determines which ReplicaSets/Pods are owned. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod template hash. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. creates a new ReplicaSet when template content changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RollingUpdate. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout undo deployment/NAME -n NS --to-revision=REV` as one read-only checkpoint, not the whole diagnosis. maxSurge/maxUnavailable bound temporary capacity and disruption. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Recreate. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get rs -n NS --sort-by=.metadata.creationTimestamp` as one read-only checkpoint, not the whole diagnosis. terminates old Pods before new when coexistence is unsafe. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving minReadySeconds. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. requires sustained readiness before a Pod counts available. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving progressDeadlineSeconds. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. marks rollout stalled but does not automatically roll back. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Revision history. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout undo deployment/NAME -n NS --to-revision=REV` as one read-only checkpoint, not the whole diagnosis. retained ReplicaSets enable undo at storage/resource cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pause/resume. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get rs -n NS --sort-by=.metadata.creationTimestamp` as one read-only checkpoint, not the whole diagnosis. batches template changes before a new rollout. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Availability condition. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout status deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. desired/updated/ready/available replicas explain rollout state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEPLOYMENTS-AND-REPLICASETS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Drain compatibility. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/NAME -n NS` as one read-only checkpoint, not the whole diagnosis. readiness, preStop, grace and LB endpoint propagation protect in-flight work. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
