# Cluster Autoscaler, Karpenter and node lifecycle — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-01

- [ ] **Question:** What is Unschedulable Pod, and why does it matter in Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** requests/constraints are the node capacity specification. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-02

- [ ] **Question:** What is Node group template, and why does it matter in Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** Cluster Autoscaler simulates predefined group capacity/labels/taints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-03

- [ ] **Question:** What is Karpenter NodePool, and why does it matter in Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** provisions flexible nodes directly from constraints/provider class. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-04

- [ ] **Question:** What is Scale-down candidate, and why does it matter in Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** utilization and movable Pods determine safe removal. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-05

- [ ] **Question:** What is PDB/local storage/system Pod, and why does it matter in Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** eviction constraints can block consolidation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-06

- [ ] **Question:** What is Cloud quota/capacity, and why does it matter in Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** autoscaler decision can be correct while provider launch fails. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-07

- [ ] **Question:** What is Node bootstrap, and why does it matter in Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-08

- [ ] **Code:** **Question:** What does `kubectl describe node NODE` help you verify for Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: multiple compatible types/AZs improve capacity and Spot resilience.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-09

- [ ] **Code:** **Question:** What does `kubectl get pods -A --field-selector=status.phase=Pending` help you verify for Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: node image/config updates require controlled replacement.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JN-10

- [ ] **Code:** **Question:** What does `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` help you verify for Cluster Autoscaler, Karpenter and node lifecycle?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: maximum nodes/resources plus admission and cloud budget prevent runaway scale.

## Junior — procedural and command questions

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-01

- [ ] **Code:** **Question:** A basic Unschedulable Pod check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. requests/constraints are the node capacity specification. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-02

- [ ] **Question:** A basic Node group template check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` and capture exact status/reason/request ID. Cluster Autoscaler simulates predefined group capacity/labels/taints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-03

- [ ] **Question:** A basic Karpenter NodePool check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/karpenter --since=30m` and capture exact status/reason/request ID. provisions flexible nodes directly from constraints/provider class. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-04

- [ ] **Code:** **Question:** A basic Scale-down candidate check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node NODE` and capture exact status/reason/request ID. utilization and movable Pods determine safe removal. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-05

- [ ] **Question:** A basic PDB/local storage/system Pod check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. eviction constraints can block consolidation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-06

- [ ] **Question:** A basic Cloud quota/capacity check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` and capture exact status/reason/request ID. autoscaler decision can be correct while provider launch fails. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-07

- [ ] **Code:** **Question:** A basic Node bootstrap check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/karpenter --since=30m` and capture exact status/reason/request ID. image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-08

- [ ] **Question:** A basic Diversification check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node NODE` and capture exact status/reason/request ID. multiple compatible types/AZs improve capacity and Spot resilience. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-09

- [ ] **Question:** A basic Drift/expiration check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. node image/config updates require controlled replacement. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-JP-10

- [ ] **Code:** **Question:** A basic Budget check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` and capture exact status/reason/request ID. maximum nodes/resources plus admission and cloud budget prevent runaway scale. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-01

- [ ] **Question:** Compare Unschedulable Pod with Node group template. When would each change your design?

**Answer:** Unschedulable Pod: requests/constraints are the node capacity specification. Node group template: Cluster Autoscaler simulates predefined group capacity/labels/taints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-02

- [ ] **Question:** Compare Node group template with Karpenter NodePool. When would each change your design?

**Answer:** Node group template: Cluster Autoscaler simulates predefined group capacity/labels/taints. Karpenter NodePool: provisions flexible nodes directly from constraints/provider class. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-03

- [ ] **Question:** Compare Karpenter NodePool with Scale-down candidate. When would each change your design?

**Answer:** Karpenter NodePool: provisions flexible nodes directly from constraints/provider class. Scale-down candidate: utilization and movable Pods determine safe removal. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-04

- [ ] **Configuration review:** **Question:** Compare Scale-down candidate with PDB/local storage/system Pod. When would each change your design?

**Answer:** Scale-down candidate: utilization and movable Pods determine safe removal. PDB/local storage/system Pod: eviction constraints can block consolidation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-05

- [ ] **Question:** Compare PDB/local storage/system Pod with Cloud quota/capacity. When would each change your design?

**Answer:** PDB/local storage/system Pod: eviction constraints can block consolidation. Cloud quota/capacity: autoscaler decision can be correct while provider launch fails. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-06

- [ ] **Question:** Compare Cloud quota/capacity with Node bootstrap. When would each change your design?

**Answer:** Cloud quota/capacity: autoscaler decision can be correct while provider launch fails. Node bootstrap: image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-07

- [ ] **Configuration review:** **Question:** Compare Node bootstrap with Diversification. When would each change your design?

**Answer:** Node bootstrap: image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. Diversification: multiple compatible types/AZs improve capacity and Spot resilience. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-08

- [ ] **Question:** Compare Diversification with Drift/expiration. When would each change your design?

**Answer:** Diversification: multiple compatible types/AZs improve capacity and Spot resilience. Drift/expiration: node image/config updates require controlled replacement. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-09

- [ ] **Question:** Compare Drift/expiration with Budget. When would each change your design?

**Answer:** Drift/expiration: node image/config updates require controlled replacement. Budget: maximum nodes/resources plus admission and cloud budget prevent runaway scale. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MN-10

- [ ] **Configuration review:** **Question:** Compare Budget with Unschedulable Pod. When would each change your design?

**Answer:** Budget: maximum nodes/resources plus admission and cloud budget prevent runaway scale. Unschedulable Pod: requests/constraints are the node capacity specification. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Unschedulable Pod; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. requests/constraints are the node capacity specification. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-02

- [ ] **Question:** Production is degraded around Node group template; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` plus recent events/changes, then correlate the service-specific SLI. Cluster Autoscaler simulates predefined group capacity/labels/taints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Karpenter NodePool; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/karpenter --since=30m` plus recent events/changes, then correlate the service-specific SLI. provisions flexible nodes directly from constraints/provider class. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-04

- [ ] **Question:** Production is degraded around Scale-down candidate; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node NODE` plus recent events/changes, then correlate the service-specific SLI. utilization and movable Pods determine safe removal. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around PDB/local storage/system Pod; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. eviction constraints can block consolidation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-06

- [ ] **Question:** Production is degraded around Cloud quota/capacity; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` plus recent events/changes, then correlate the service-specific SLI. autoscaler decision can be correct while provider launch fails. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Node bootstrap; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/karpenter --since=30m` plus recent events/changes, then correlate the service-specific SLI. image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-08

- [ ] **Question:** Production is degraded around Diversification; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node NODE` plus recent events/changes, then correlate the service-specific SLI. multiple compatible types/AZs improve capacity and Spot resilience. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Drift/expiration; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. node image/config updates require controlled replacement. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-MP-10

- [ ] **Question:** Production is degraded around Budget; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` plus recent events/changes, then correlate the service-specific SLI. maximum nodes/resources plus admission and cloud budget prevent runaway scale. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-01

- [ ] **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Unschedulable Pod, Scale-down candidate and Node bootstrap are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: requests/constraints are the node capacity specification. utilization and movable Pods determine safe removal. image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Node group template, PDB/local storage/system Pod and Diversification are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Cluster Autoscaler simulates predefined group capacity/labels/taints. eviction constraints can block consolidation. multiple compatible types/AZs improve capacity and Spot resilience. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-03

- [ ] **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Karpenter NodePool, Cloud quota/capacity and Drift/expiration are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provisions flexible nodes directly from constraints/provider class. autoscaler decision can be correct while provider launch fails. node image/config updates require controlled replacement. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Scale-down candidate, Node bootstrap and Budget are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: utilization and movable Pods determine safe removal. image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. maximum nodes/resources plus admission and cloud budget prevent runaway scale. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-05

- [ ] **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where PDB/local storage/system Pod, Diversification and Unschedulable Pod are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: eviction constraints can block consolidation. multiple compatible types/AZs improve capacity and Spot resilience. requests/constraints are the node capacity specification. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Cloud quota/capacity, Drift/expiration and Node group template are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: autoscaler decision can be correct while provider launch fails. node image/config updates require controlled replacement. Cluster Autoscaler simulates predefined group capacity/labels/taints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-07

- [ ] **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Node bootstrap, Budget and Karpenter NodePool are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. maximum nodes/resources plus admission and cloud budget prevent runaway scale. provisions flexible nodes directly from constraints/provider class. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Diversification, Unschedulable Pod and Scale-down candidate are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: multiple compatible types/AZs improve capacity and Spot resilience. requests/constraints are the node capacity specification. utilization and movable Pods determine safe removal. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-09

- [ ] **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Drift/expiration, Node group template and PDB/local storage/system Pod are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: node image/config updates require controlled replacement. Cluster Autoscaler simulates predefined group capacity/labels/taints. eviction constraints can block consolidation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Cluster Autoscaler, Karpenter and node lifecycle capability where Budget, Karpenter NodePool and Cloud quota/capacity are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: maximum nodes/resources plus admission and cloud budget prevent runaway scale. provisions flexible nodes directly from constraints/provider class. autoscaler decision can be correct while provider launch fails. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Unschedulable Pod. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. requests/constraints are the node capacity specification. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node group template. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` as one read-only checkpoint, not the whole diagnosis. Cluster Autoscaler simulates predefined group capacity/labels/taints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Karpenter NodePool. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/karpenter --since=30m` as one read-only checkpoint, not the whole diagnosis. provisions flexible nodes directly from constraints/provider class. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scale-down candidate. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node NODE` as one read-only checkpoint, not the whole diagnosis. utilization and movable Pods determine safe removal. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PDB/local storage/system Pod. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. eviction constraints can block consolidation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cloud quota/capacity. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` as one read-only checkpoint, not the whole diagnosis. autoscaler decision can be correct while provider launch fails. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Node bootstrap. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/karpenter --since=30m` as one read-only checkpoint, not the whole diagnosis. image, kubelet, runtime, CNI/CSI/device plugin must become Ready before capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Diversification. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node NODE` as one read-only checkpoint, not the whole diagnosis. multiple compatible types/AZs improve capacity and Spot resilience. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Drift/expiration. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. node image/config updates require controlled replacement. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CLUSTER-AUTOSCALER-KARPENTER-AND-NODE-LIFECYCLE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Budget. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/cluster-autoscaler --since=30m` as one read-only checkpoint, not the whole diagnosis. maximum nodes/resources plus admission and cloud budget prevent runaway scale. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
