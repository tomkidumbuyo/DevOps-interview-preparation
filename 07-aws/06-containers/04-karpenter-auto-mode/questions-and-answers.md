# Karpenter and EKS Auto Mode — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### KARPENTER-AND-EKS-AUTO-MODE-JN-01

- [ ] **Question:** What is Pending-Pod demand, and why does it matter in Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** autoscaler reads unschedulable constraints/requests rather than average node CPU alone. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KARPENTER-AND-EKS-AUTO-MODE-JN-02

- [ ] **Question:** What is NodePool, and why does it matter in Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** constrains labels, taints, requirements, disruption and aggregate resource limits. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KARPENTER-AND-EKS-AUTO-MODE-JN-03

- [ ] **Question:** What is NodeClass, and why does it matter in Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** AWS-specific subnets, security groups, AMI, role and storage configuration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KARPENTER-AND-EKS-AUTO-MODE-JN-04

- [ ] **Question:** What is Instance diversification, and why does it matter in Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** compatible families/sizes/AZs improve capacity and Spot resilience. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KARPENTER-AND-EKS-AUTO-MODE-JN-05

- [ ] **Question:** What is Consolidation, and why does it matter in Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** removes/replaces underutilized nodes after respecting disruption policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KARPENTER-AND-EKS-AUTO-MODE-JN-06

- [ ] **Question:** What is Disruption budget, and why does it matter in Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** limits voluntary Karpenter actions but does not stop instance failure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KARPENTER-AND-EKS-AUTO-MODE-JN-07

- [ ] **Question:** What is Expiration/drift, and why does it matter in Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** rotates nodes for image/config lifecycle under workload availability constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### KARPENTER-AND-EKS-AUTO-MODE-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 describe-instance-type-offerings --location-type availability-zone` help you verify for Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: Pod constraints and NodePool metadata must still identify a compatible node.

### KARPENTER-AND-EKS-AUTO-MODE-JN-09

- [ ] **Code:** **Question:** What does `kubectl get nodepool,ec2nodeclass,nodeclaim` help you verify for Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: managed node/storage/network automation builds on Karpenter concepts with supported constraints.

### KARPENTER-AND-EKS-AUTO-MODE-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe nodeclaim NAME` help you verify for Karpenter and EKS Auto Mode?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: NodePool resource limits, quotas/budgets and admission prevent runaway provisioning.

## Junior — procedural and command questions

### KARPENTER-AND-EKS-AUTO-MODE-JP-01

- [ ] **Code:** **Question:** A basic Pending-Pod demand check fails. What would you do first using the CLI?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodepool,ec2nodeclass,nodeclaim` and capture exact status/reason/request ID. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-02

- [ ] **Question:** A basic NodePool check fails. What would you do first?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe nodeclaim NAME` and capture exact status/reason/request ID. constrains labels, taints, requirements, disruption and aggregate resource limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-03

- [ ] **Question:** A basic NodeClass check fails. What would you do first?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/karpenter --since=30m` and capture exact status/reason/request ID. AWS-specific subnets, security groups, AMI, role and storage configuration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-04

- [ ] **Code:** **Question:** A basic Instance diversification check fails. What would you do first using the CLI?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-type-offerings --location-type availability-zone` and capture exact status/reason/request ID. compatible families/sizes/AZs improve capacity and Spot resilience. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-05

- [ ] **Question:** A basic Consolidation check fails. What would you do first?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodepool,ec2nodeclass,nodeclaim` and capture exact status/reason/request ID. removes/replaces underutilized nodes after respecting disruption policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-06

- [ ] **Question:** A basic Disruption budget check fails. What would you do first?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe nodeclaim NAME` and capture exact status/reason/request ID. limits voluntary Karpenter actions but does not stop instance failure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-07

- [ ] **Code:** **Question:** A basic Expiration/drift check fails. What would you do first using the CLI?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/karpenter --since=30m` and capture exact status/reason/request ID. rotates nodes for image/config lifecycle under workload availability constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-08

- [ ] **Question:** A basic Scale from zero check fails. What would you do first?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-type-offerings --location-type availability-zone` and capture exact status/reason/request ID. Pod constraints and NodePool metadata must still identify a compatible node. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-09

- [ ] **Question:** A basic EKS Auto Mode check fails. What would you do first?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodepool,ec2nodeclass,nodeclaim` and capture exact status/reason/request ID. managed node/storage/network automation builds on Karpenter concepts with supported constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### KARPENTER-AND-EKS-AUTO-MODE-JP-10

- [ ] **Code:** **Question:** A basic Spend limits check fails. What would you do first using the CLI?
> **Covered in:** [Karpenter and EKS Auto Mode — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe nodeclaim NAME` and capture exact status/reason/request ID. NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### KARPENTER-AND-EKS-AUTO-MODE-MN-01

- [ ] **Question:** Compare Pending-Pod demand with NodePool. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pending-Pod demand: autoscaler reads unschedulable constraints/requests rather than average node CPU alone. NodePool: constrains labels, taints, requirements, disruption and aggregate resource limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-02

- [ ] **Question:** Compare NodePool with NodeClass. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** NodePool: constrains labels, taints, requirements, disruption and aggregate resource limits. NodeClass: AWS-specific subnets, security groups, AMI, role and storage configuration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-03

- [ ] **Question:** Compare NodeClass with Instance diversification. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** NodeClass: AWS-specific subnets, security groups, AMI, role and storage configuration. Instance diversification: compatible families/sizes/AZs improve capacity and Spot resilience. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-04

- [ ] **Configuration review:** **Question:** Compare Instance diversification with Consolidation. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Instance diversification: compatible families/sizes/AZs improve capacity and Spot resilience. Consolidation: removes/replaces underutilized nodes after respecting disruption policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-05

- [ ] **Question:** Compare Consolidation with Disruption budget. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Consolidation: removes/replaces underutilized nodes after respecting disruption policy. Disruption budget: limits voluntary Karpenter actions but does not stop instance failure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-06

- [ ] **Question:** Compare Disruption budget with Expiration/drift. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Disruption budget: limits voluntary Karpenter actions but does not stop instance failure. Expiration/drift: rotates nodes for image/config lifecycle under workload availability constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-07

- [ ] **Configuration review:** **Question:** Compare Expiration/drift with Scale from zero. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Expiration/drift: rotates nodes for image/config lifecycle under workload availability constraints. Scale from zero: Pod constraints and NodePool metadata must still identify a compatible node. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-08

- [ ] **Question:** Compare Scale from zero with EKS Auto Mode. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Scale from zero: Pod constraints and NodePool metadata must still identify a compatible node. EKS Auto Mode: managed node/storage/network automation builds on Karpenter concepts with supported constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-09

- [ ] **Question:** Compare EKS Auto Mode with Spend limits. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** EKS Auto Mode: managed node/storage/network automation builds on Karpenter concepts with supported constraints. Spend limits: NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### KARPENTER-AND-EKS-AUTO-MODE-MN-10

- [ ] **Configuration review:** **Question:** Compare Spend limits with Pending-Pod demand. When would each change your design?
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Spend limits: NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. Pending-Pod demand: autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### KARPENTER-AND-EKS-AUTO-MODE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pending-Pod demand; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodepool,ec2nodeclass,nodeclaim` plus recent events/changes, then correlate the service-specific SLI. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-02

- [ ] **Question:** Production is degraded around NodePool; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe nodeclaim NAME` plus recent events/changes, then correlate the service-specific SLI. constrains labels, taints, requirements, disruption and aggregate resource limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around NodeClass; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/karpenter --since=30m` plus recent events/changes, then correlate the service-specific SLI. AWS-specific subnets, security groups, AMI, role and storage configuration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-04

- [ ] **Question:** Production is degraded around Instance diversification; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-type-offerings --location-type availability-zone` plus recent events/changes, then correlate the service-specific SLI. compatible families/sizes/AZs improve capacity and Spot resilience. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Consolidation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodepool,ec2nodeclass,nodeclaim` plus recent events/changes, then correlate the service-specific SLI. removes/replaces underutilized nodes after respecting disruption policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-06

- [ ] **Question:** Production is degraded around Disruption budget; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe nodeclaim NAME` plus recent events/changes, then correlate the service-specific SLI. limits voluntary Karpenter actions but does not stop instance failure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Expiration/drift; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/karpenter --since=30m` plus recent events/changes, then correlate the service-specific SLI. rotates nodes for image/config lifecycle under workload availability constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-08

- [ ] **Question:** Production is degraded around Scale from zero; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-type-offerings --location-type availability-zone` plus recent events/changes, then correlate the service-specific SLI. Pod constraints and NodePool metadata must still identify a compatible node. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around EKS Auto Mode; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodepool,ec2nodeclass,nodeclaim` plus recent events/changes, then correlate the service-specific SLI. managed node/storage/network automation builds on Karpenter concepts with supported constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### KARPENTER-AND-EKS-AUTO-MODE-MP-10

- [ ] **Question:** Production is degraded around Spend limits; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe nodeclaim NAME` plus recent events/changes, then correlate the service-specific SLI. NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### KARPENTER-AND-EKS-AUTO-MODE-SN-01

- [ ] **Question:** Design a production Karpenter and EKS Auto Mode capability where Pending-Pod demand, Instance diversification and Expiration/drift are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: autoscaler reads unschedulable constraints/requests rather than average node CPU alone. compatible families/sizes/AZs improve capacity and Spot resilience. rotates nodes for image/config lifecycle under workload availability constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Karpenter and EKS Auto Mode capability where NodePool, Consolidation and Scale from zero are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: constrains labels, taints, requirements, disruption and aggregate resource limits. removes/replaces underutilized nodes after respecting disruption policy. Pod constraints and NodePool metadata must still identify a compatible node. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-03

- [ ] **Question:** Design a production Karpenter and EKS Auto Mode capability where NodeClass, Disruption budget and EKS Auto Mode are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AWS-specific subnets, security groups, AMI, role and storage configuration. limits voluntary Karpenter actions but does not stop instance failure. managed node/storage/network automation builds on Karpenter concepts with supported constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Karpenter and EKS Auto Mode capability where Instance diversification, Expiration/drift and Spend limits are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: compatible families/sizes/AZs improve capacity and Spot resilience. rotates nodes for image/config lifecycle under workload availability constraints. NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-05

- [ ] **Question:** Design a production Karpenter and EKS Auto Mode capability where Consolidation, Scale from zero and Pending-Pod demand are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: removes/replaces underutilized nodes after respecting disruption policy. Pod constraints and NodePool metadata must still identify a compatible node. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Karpenter and EKS Auto Mode capability where Disruption budget, EKS Auto Mode and NodePool are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: limits voluntary Karpenter actions but does not stop instance failure. managed node/storage/network automation builds on Karpenter concepts with supported constraints. constrains labels, taints, requirements, disruption and aggregate resource limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-07

- [ ] **Question:** Design a production Karpenter and EKS Auto Mode capability where Expiration/drift, Spend limits and NodeClass are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rotates nodes for image/config lifecycle under workload availability constraints. NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. AWS-specific subnets, security groups, AMI, role and storage configuration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Karpenter and EKS Auto Mode capability where Scale from zero, Pending-Pod demand and Instance diversification are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Pod constraints and NodePool metadata must still identify a compatible node. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. compatible families/sizes/AZs improve capacity and Spot resilience. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-09

- [ ] **Question:** Design a production Karpenter and EKS Auto Mode capability where EKS Auto Mode, NodePool and Consolidation are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed node/storage/network automation builds on Karpenter concepts with supported constraints. constrains labels, taints, requirements, disruption and aggregate resource limits. removes/replaces underutilized nodes after respecting disruption policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### KARPENTER-AND-EKS-AUTO-MODE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Karpenter and EKS Auto Mode capability where Spend limits, NodeClass and Disruption budget are first-class requirements.
> **Covered in:** [Karpenter and EKS Auto Mode — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. AWS-specific subnets, security groups, AMI, role and storage configuration. limits voluntary Karpenter actions but does not stop instance failure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### KARPENTER-AND-EKS-AUTO-MODE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pending-Pod demand. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodepool,ec2nodeclass,nodeclaim` as one read-only checkpoint, not the whole diagnosis. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NodePool. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe nodeclaim NAME` as one read-only checkpoint, not the whole diagnosis. constrains labels, taints, requirements, disruption and aggregate resource limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NodeClass. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/karpenter --since=30m` as one read-only checkpoint, not the whole diagnosis. AWS-specific subnets, security groups, AMI, role and storage configuration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance diversification. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-type-offerings --location-type availability-zone` as one read-only checkpoint, not the whole diagnosis. compatible families/sizes/AZs improve capacity and Spot resilience. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Consolidation. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodepool,ec2nodeclass,nodeclaim` as one read-only checkpoint, not the whole diagnosis. removes/replaces underutilized nodes after respecting disruption policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Disruption budget. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe nodeclaim NAME` as one read-only checkpoint, not the whole diagnosis. limits voluntary Karpenter actions but does not stop instance failure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Expiration/drift. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/karpenter --since=30m` as one read-only checkpoint, not the whole diagnosis. rotates nodes for image/config lifecycle under workload availability constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scale from zero. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-type-offerings --location-type availability-zone` as one read-only checkpoint, not the whole diagnosis. Pod constraints and NodePool metadata must still identify a compatible node. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving EKS Auto Mode. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodepool,ec2nodeclass,nodeclaim` as one read-only checkpoint, not the whole diagnosis. managed node/storage/network automation builds on Karpenter concepts with supported constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### KARPENTER-AND-EKS-AUTO-MODE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Spend limits. How do you lead it end to end?
> **Covered in:** [Karpenter and EKS Auto Mode — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe nodeclaim NAME` as one read-only checkpoint, not the whole diagnosis. NodePool resource limits, quotas/budgets and admission prevent runaway provisioning. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon EKS](../03-eks/README.md) · [Study note](README.md) · [Next: AWS Load Balancer Controller →](../05-aws-load-balancer-controller/README.md)

<!-- reading-navigation:end -->
