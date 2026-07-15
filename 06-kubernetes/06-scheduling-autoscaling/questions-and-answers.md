# Scheduling Autoscaling — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-SCHEDULING-AUTOSCALING-JN-01

- [ ] **Question:** What is CPU request, and why does it matter in Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** scheduler reservation and HPA utilization denominator, expressed in cores/millicores. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SCHEDULING-AUTOSCALING-JN-02

- [ ] **Question:** What is CPU limit, and why does it matter in Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SCHEDULING-AUTOSCALING-JN-03

- [ ] **Question:** What is nodeSelector, and why does it matter in Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** exact label match for simple required placement. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SCHEDULING-AUTOSCALING-JN-04

- [ ] **Question:** What is Node affinity, and why does it matter in Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** expressive required/preferred label predicates evaluated at scheduling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SCHEDULING-AUTOSCALING-JN-05

- [ ] **Question:** What is HPA ratio, and why does it matter in Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** desired replicas derives current/target metric with tolerance and missing/not-ready handling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SCHEDULING-AUTOSCALING-JN-06

- [ ] **Question:** What is Resource utilization, and why does it matter in Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** usage divided by requests means bad/missing requests break CPU/memory scaling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SCHEDULING-AUTOSCALING-JN-07

- [ ] **Question:** What is Unschedulable Pod, and why does it matter in Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** requests/constraints are the node capacity specification. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SCHEDULING-AUTOSCALING-JN-08

- [ ] **Code:** **Question:** What does `kubectl get hpa -A` help you verify for Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: Cluster Autoscaler simulates predefined group capacity/labels/taints.

### BRANCH-SCHEDULING-AUTOSCALING-JN-09

- [ ] **Code:** **Question:** What does `kubectl get pods -A --field-selector=status.phase=Pending` help you verify for Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods.

### BRANCH-SCHEDULING-AUTOSCALING-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pdb,priorityclass -A` help you verify for Scheduling Autoscaling?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: admission checks PDB and graceful deletion compared with direct delete.

## Junior — procedural and command questions

### BRANCH-SCHEDULING-AUTOSCALING-JP-01

- [ ] **Code:** **Question:** A basic CPU request check fails. What would you do first using the CLI?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -A --containers` and capture exact status/reason/request ID. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-02

- [ ] **Question:** A basic CPU limit check fails. What would you do first?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes --show-labels` and capture exact status/reason/request ID. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-03

- [ ] **Question:** A basic nodeSelector check fails. What would you do first?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get hpa -A` and capture exact status/reason/request ID. exact label match for simple required placement. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-04

- [ ] **Code:** **Question:** A basic Node affinity check fails. What would you do first using the CLI?
> **Covered in:** [Resource requests, limits and QoS — Command lab](01-requests-limits-qos/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. expressive required/preferred label predicates evaluated at scheduling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-05

- [ ] **Question:** A basic HPA ratio check fails. What would you do first?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pdb,priorityclass -A` and capture exact status/reason/request ID. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-06

- [ ] **Question:** A basic Resource utilization check fails. What would you do first?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -A --containers` and capture exact status/reason/request ID. usage divided by requests means bad/missing requests break CPU/memory scaling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-07

- [ ] **Code:** **Question:** A basic Unschedulable Pod check fails. What would you do first using the CLI?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes --show-labels` and capture exact status/reason/request ID. requests/constraints are the node capacity specification. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-08

- [ ] **Question:** A basic Node group template check fails. What would you do first?
> **Covered in:** [Resource requests, limits and QoS — Command lab](01-requests-limits-qos/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get hpa -A` and capture exact status/reason/request ID. Cluster Autoscaler simulates predefined group capacity/labels/taints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-09

- [ ] **Question:** A basic PDB check fails. What would you do first?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SCHEDULING-AUTOSCALING-JP-10

- [ ] **Code:** **Question:** A basic Eviction API check fails. What would you do first using the CLI?
> **Covered in:** [Scheduling Autoscaling — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pdb,priorityclass -A` and capture exact status/reason/request ID. admission checks PDB and graceful deletion compared with direct delete. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-SCHEDULING-AUTOSCALING-MN-01

- [ ] **Question:** Compare CPU request with CPU limit. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CPU request: scheduler reservation and HPA utilization denominator, expressed in cores/millicores. CPU limit: cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-02

- [ ] **Question:** Compare CPU limit with nodeSelector. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CPU limit: cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. nodeSelector: exact label match for simple required placement. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-03

- [ ] **Question:** Compare nodeSelector with Node affinity. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** nodeSelector: exact label match for simple required placement. Node affinity: expressive required/preferred label predicates evaluated at scheduling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-04

- [ ] **Configuration review:** **Question:** Compare Node affinity with HPA ratio. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Node affinity: expressive required/preferred label predicates evaluated at scheduling. HPA ratio: desired replicas derives current/target metric with tolerance and missing/not-ready handling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-05

- [ ] **Question:** Compare HPA ratio with Resource utilization. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** HPA ratio: desired replicas derives current/target metric with tolerance and missing/not-ready handling. Resource utilization: usage divided by requests means bad/missing requests break CPU/memory scaling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-06

- [ ] **Question:** Compare Resource utilization with Unschedulable Pod. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Resource utilization: usage divided by requests means bad/missing requests break CPU/memory scaling. Unschedulable Pod: requests/constraints are the node capacity specification. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-07

- [ ] **Configuration review:** **Question:** Compare Unschedulable Pod with Node group template. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Unschedulable Pod: requests/constraints are the node capacity specification. Node group template: Cluster Autoscaler simulates predefined group capacity/labels/taints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-08

- [ ] **Question:** Compare Node group template with PDB. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Node group template: Cluster Autoscaler simulates predefined group capacity/labels/taints. PDB: minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-09

- [ ] **Question:** Compare PDB with Eviction API. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** PDB: minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Eviction API: admission checks PDB and graceful deletion compared with direct delete. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SCHEDULING-AUTOSCALING-MN-10

- [ ] **Configuration review:** **Question:** Compare Eviction API with CPU request. When would each change your design?
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Eviction API: admission checks PDB and graceful deletion compared with direct delete. CPU request: scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-SCHEDULING-AUTOSCALING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around CPU request; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-02

- [ ] **Question:** Production is degraded around CPU limit; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes --show-labels` plus recent events/changes, then correlate the service-specific SLI. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around nodeSelector; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](02-placement/README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get hpa -A` plus recent events/changes, then correlate the service-specific SLI. exact label match for simple required placement. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-04

- [ ] **Question:** Production is degraded around Node affinity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Affinity, taints and topology placement — Architecture and lifecycle](02-placement/README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. expressive required/preferred label predicates evaluated at scheduling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around HPA ratio; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pdb,priorityclass -A` plus recent events/changes, then correlate the service-specific SLI. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-06

- [ ] **Question:** Production is degraded around Resource utilization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. usage divided by requests means bad/missing requests break CPU/memory scaling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Unschedulable Pod; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes --show-labels` plus recent events/changes, then correlate the service-specific SLI. requests/constraints are the node capacity specification. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-08

- [ ] **Question:** Production is degraded around Node group template; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get hpa -A` plus recent events/changes, then correlate the service-specific SLI. Cluster Autoscaler simulates predefined group capacity/labels/taints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around PDB; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SCHEDULING-AUTOSCALING-MP-10

- [ ] **Question:** Production is degraded around Eviction API; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pdb,priorityclass -A` plus recent events/changes, then correlate the service-specific SLI. admission checks PDB and graceful deletion compared with direct delete. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-SCHEDULING-AUTOSCALING-SN-01

- [ ] **Question:** Design a production Scheduling Autoscaling capability where CPU request, Node affinity and Unschedulable Pod are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scheduler reservation and HPA utilization denominator, expressed in cores/millicores. expressive required/preferred label predicates evaluated at scheduling. requests/constraints are the node capacity specification. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduling Autoscaling capability where CPU limit, HPA ratio and Node group template are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Cluster Autoscaler simulates predefined group capacity/labels/taints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-03

- [ ] **Question:** Design a production Scheduling Autoscaling capability where nodeSelector, Resource utilization and PDB are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exact label match for simple required placement. usage divided by requests means bad/missing requests break CPU/memory scaling. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduling Autoscaling capability where Node affinity, Unschedulable Pod and Eviction API are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: expressive required/preferred label predicates evaluated at scheduling. requests/constraints are the node capacity specification. admission checks PDB and graceful deletion compared with direct delete. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-05

- [ ] **Question:** Design a production Scheduling Autoscaling capability where HPA ratio, Node group template and CPU request are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: desired replicas derives current/target metric with tolerance and missing/not-ready handling. Cluster Autoscaler simulates predefined group capacity/labels/taints. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduling Autoscaling capability where Resource utilization, PDB and CPU limit are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: usage divided by requests means bad/missing requests break CPU/memory scaling. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-07

- [ ] **Question:** Design a production Scheduling Autoscaling capability where Unschedulable Pod, Eviction API and nodeSelector are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: requests/constraints are the node capacity specification. admission checks PDB and graceful deletion compared with direct delete. exact label match for simple required placement. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduling Autoscaling capability where Node group template, CPU request and Node affinity are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Cluster Autoscaler simulates predefined group capacity/labels/taints. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. expressive required/preferred label predicates evaluated at scheduling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-09

- [ ] **Question:** Design a production Scheduling Autoscaling capability where PDB, CPU limit and HPA ratio are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SCHEDULING-AUTOSCALING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Scheduling Autoscaling capability where Eviction API, nodeSelector and Resource utilization are first-class requirements.
> **Covered in:** [Scheduling Autoscaling — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: admission checks PDB and graceful deletion compared with direct delete. exact label match for simple required placement. usage divided by requests means bad/missing requests break CPU/memory scaling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-SCHEDULING-AUTOSCALING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU request. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. scheduler reservation and HPA utilization denominator, expressed in cores/millicores. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CPU limit. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes --show-labels` as one read-only checkpoint, not the whole diagnosis. cgroup bandwidth cap can throttle latency-sensitive work even with idle host cores. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving nodeSelector. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get hpa -A` as one read-only checkpoint, not the whole diagnosis. exact label match for simple required placement. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node affinity. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. expressive required/preferred label predicates evaluated at scheduling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HPA ratio. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pdb,priorityclass -A` as one read-only checkpoint, not the whole diagnosis. desired replicas derives current/target metric with tolerance and missing/not-ready handling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource utilization. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. usage divided by requests means bad/missing requests break CPU/memory scaling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Unschedulable Pod. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes --show-labels` as one read-only checkpoint, not the whole diagnosis. requests/constraints are the node capacity specification. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node group template. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get hpa -A` as one read-only checkpoint, not the whole diagnosis. Cluster Autoscaler simulates predefined group capacity/labels/taints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PDB. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. minAvailable/maxUnavailable bounds voluntary API eviction for selected healthy Pods. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SCHEDULING-AUTOSCALING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Eviction API. How do you lead it end to end?
> **Covered in:** [Scheduling Autoscaling — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pdb,priorityclass -A` as one read-only checkpoint, not the whole diagnosis. admission checks PDB and graceful deletion compared with direct delete. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes multi-tenancy](../05-security/05-multitenancy/README.md) · [Study note](README.md) · [Next: Resource requests, limits and QoS →](01-requests-limits-qos/README.md)

<!-- reading-navigation:end -->
