# Containers — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-CONTAINERS-JN-01

- [ ] **Question:** What is Repository, and why does it matter in Containers?

**Answer:** regional namespace with IAM/resource policy and encryption. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINERS-JN-02

- [ ] **Question:** What is Tag immutability, and why does it matter in Containers?

**Answer:** prevents overwriting release tags while deployment by digest is stronger identity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINERS-JN-03

- [ ] **Question:** What is Task definition, and why does it matter in Containers?

**Answer:** versioned container, resource, network, log, secret, volume and role specification. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINERS-JN-04

- [ ] **Question:** What is Task, and why does it matter in Containers?

**Answer:** running/scheduled instantiation of a task definition. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINERS-JN-05

- [ ] **Question:** What is Managed control plane, and why does it matter in Containers?

**Answer:** AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINERS-JN-06

- [ ] **Question:** What is Access entries, and why does it matter in Containers?

**Answer:** EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINERS-JN-07

- [ ] **Question:** What is Pending-Pod demand, and why does it matter in Containers?

**Answer:** autoscaler reads unschedulable constraints/requests rather than average node CPU alone. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINERS-JN-08

- [ ] **Code:** **Question:** What does `aws eks describe-cluster --name CLUSTER` help you verify for Containers?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: constrains labels, taints, requirements, disruption and aggregate resource limits.

### BRANCH-CONTAINERS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get nodepool,ec2nodeclass,nodeclaim` help you verify for Containers?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: annotations/spec/class generate ALB listeners/rules/target groups.

### BRANCH-CONTAINERS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get ingress,service -A` help you verify for Containers?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: controller provisions NLB behavior from Service annotations/spec.

## Junior — procedural and command questions

### BRANCH-CONTAINERS-JP-01

- [ ] **Code:** **Question:** A basic Repository check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr describe-repositories` and capture exact status/reason/request ID. regional namespace with IAM/resource policy and encryption. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-02

- [ ] **Question:** A basic Tag immutability check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-clusters --clusters CLUSTER` and capture exact status/reason/request ID. prevents overwriting release tags while deployment by digest is stronger identity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-03

- [ ] **Question:** A basic Task definition check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks describe-cluster --name CLUSTER` and capture exact status/reason/request ID. versioned container, resource, network, log, secret, volume and role specification. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-04

- [ ] **Code:** **Question:** A basic Task check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodepool,ec2nodeclass,nodeclaim` and capture exact status/reason/request ID. running/scheduled instantiation of a task definition. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-05

- [ ] **Question:** A basic Managed control plane check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingress,service -A` and capture exact status/reason/request ID. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-06

- [ ] **Question:** A basic Access entries check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecr describe-repositories` and capture exact status/reason/request ID. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-07

- [ ] **Code:** **Question:** A basic Pending-Pod demand check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ecs describe-clusters --clusters CLUSTER` and capture exact status/reason/request ID. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-08

- [ ] **Question:** A basic NodePool check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks describe-cluster --name CLUSTER` and capture exact status/reason/request ID. constrains labels, taints, requirements, disruption and aggregate resource limits. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-09

- [ ] **Question:** A basic Ingress reconciliation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodepool,ec2nodeclass,nodeclaim` and capture exact status/reason/request ID. annotations/spec/class generate ALB listeners/rules/target groups. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINERS-JP-10

- [ ] **Code:** **Question:** A basic Service LoadBalancer check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingress,service -A` and capture exact status/reason/request ID. controller provisions NLB behavior from Service annotations/spec. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-CONTAINERS-MN-01

- [ ] **Question:** Compare Repository with Tag immutability. When would each change your design?

**Answer:** Repository: regional namespace with IAM/resource policy and encryption. Tag immutability: prevents overwriting release tags while deployment by digest is stronger identity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-02

- [ ] **Question:** Compare Tag immutability with Task definition. When would each change your design?

**Answer:** Tag immutability: prevents overwriting release tags while deployment by digest is stronger identity. Task definition: versioned container, resource, network, log, secret, volume and role specification. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-03

- [ ] **Question:** Compare Task definition with Task. When would each change your design?

**Answer:** Task definition: versioned container, resource, network, log, secret, volume and role specification. Task: running/scheduled instantiation of a task definition. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-04

- [ ] **Configuration review:** **Question:** Compare Task with Managed control plane. When would each change your design?

**Answer:** Task: running/scheduled instantiation of a task definition. Managed control plane: AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-05

- [ ] **Question:** Compare Managed control plane with Access entries. When would each change your design?

**Answer:** Managed control plane: AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Access entries: EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-06

- [ ] **Question:** Compare Access entries with Pending-Pod demand. When would each change your design?

**Answer:** Access entries: EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Pending-Pod demand: autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-07

- [ ] **Configuration review:** **Question:** Compare Pending-Pod demand with NodePool. When would each change your design?

**Answer:** Pending-Pod demand: autoscaler reads unschedulable constraints/requests rather than average node CPU alone. NodePool: constrains labels, taints, requirements, disruption and aggregate resource limits. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-08

- [ ] **Question:** Compare NodePool with Ingress reconciliation. When would each change your design?

**Answer:** NodePool: constrains labels, taints, requirements, disruption and aggregate resource limits. Ingress reconciliation: annotations/spec/class generate ALB listeners/rules/target groups. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-09

- [ ] **Question:** Compare Ingress reconciliation with Service LoadBalancer. When would each change your design?

**Answer:** Ingress reconciliation: annotations/spec/class generate ALB listeners/rules/target groups. Service LoadBalancer: controller provisions NLB behavior from Service annotations/spec. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINERS-MN-10

- [ ] **Configuration review:** **Question:** Compare Service LoadBalancer with Repository. When would each change your design?

**Answer:** Service LoadBalancer: controller provisions NLB behavior from Service annotations/spec. Repository: regional namespace with IAM/resource policy and encryption. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-CONTAINERS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Repository; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr describe-repositories` plus recent events/changes, then correlate the service-specific SLI. regional namespace with IAM/resource policy and encryption. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-02

- [ ] **Question:** Production is degraded around Tag immutability; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-clusters --clusters CLUSTER` plus recent events/changes, then correlate the service-specific SLI. prevents overwriting release tags while deployment by digest is stronger identity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Task definition; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks describe-cluster --name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. versioned container, resource, network, log, secret, volume and role specification. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-04

- [ ] **Question:** Production is degraded around Task; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodepool,ec2nodeclass,nodeclaim` plus recent events/changes, then correlate the service-specific SLI. running/scheduled instantiation of a task definition. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Managed control plane; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingress,service -A` plus recent events/changes, then correlate the service-specific SLI. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-06

- [ ] **Question:** Production is degraded around Access entries; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecr describe-repositories` plus recent events/changes, then correlate the service-specific SLI. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pending-Pod demand; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ecs describe-clusters --clusters CLUSTER` plus recent events/changes, then correlate the service-specific SLI. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-08

- [ ] **Question:** Production is degraded around NodePool; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks describe-cluster --name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. constrains labels, taints, requirements, disruption and aggregate resource limits. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Ingress reconciliation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodepool,ec2nodeclass,nodeclaim` plus recent events/changes, then correlate the service-specific SLI. annotations/spec/class generate ALB listeners/rules/target groups. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINERS-MP-10

- [ ] **Question:** Production is degraded around Service LoadBalancer; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingress,service -A` plus recent events/changes, then correlate the service-specific SLI. controller provisions NLB behavior from Service annotations/spec. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-CONTAINERS-SN-01

- [ ] **Question:** Design a production Containers capability where Repository, Task and Pending-Pod demand are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: regional namespace with IAM/resource policy and encryption. running/scheduled instantiation of a task definition. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Containers capability where Tag immutability, Managed control plane and NodePool are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prevents overwriting release tags while deployment by digest is stronger identity. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. constrains labels, taints, requirements, disruption and aggregate resource limits. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-03

- [ ] **Question:** Design a production Containers capability where Task definition, Access entries and Ingress reconciliation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned container, resource, network, log, secret, volume and role specification. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. annotations/spec/class generate ALB listeners/rules/target groups. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Containers capability where Task, Pending-Pod demand and Service LoadBalancer are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: running/scheduled instantiation of a task definition. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. controller provisions NLB behavior from Service annotations/spec. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-05

- [ ] **Question:** Design a production Containers capability where Managed control plane, NodePool and Repository are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. constrains labels, taints, requirements, disruption and aggregate resource limits. regional namespace with IAM/resource policy and encryption. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Containers capability where Access entries, Ingress reconciliation and Tag immutability are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. annotations/spec/class generate ALB listeners/rules/target groups. prevents overwriting release tags while deployment by digest is stronger identity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-07

- [ ] **Question:** Design a production Containers capability where Pending-Pod demand, Service LoadBalancer and Task definition are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: autoscaler reads unschedulable constraints/requests rather than average node CPU alone. controller provisions NLB behavior from Service annotations/spec. versioned container, resource, network, log, secret, volume and role specification. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Containers capability where NodePool, Repository and Task are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: constrains labels, taints, requirements, disruption and aggregate resource limits. regional namespace with IAM/resource policy and encryption. running/scheduled instantiation of a task definition. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-09

- [ ] **Question:** Design a production Containers capability where Ingress reconciliation, Tag immutability and Managed control plane are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: annotations/spec/class generate ALB listeners/rules/target groups. prevents overwriting release tags while deployment by digest is stronger identity. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINERS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Containers capability where Service LoadBalancer, Task definition and Access entries are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controller provisions NLB behavior from Service annotations/spec. versioned container, resource, network, log, secret, volume and role specification. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-CONTAINERS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Repository. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr describe-repositories` as one read-only checkpoint, not the whole diagnosis. regional namespace with IAM/resource policy and encryption. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tag immutability. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-clusters --clusters CLUSTER` as one read-only checkpoint, not the whole diagnosis. prevents overwriting release tags while deployment by digest is stronger identity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Task definition. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks describe-cluster --name CLUSTER` as one read-only checkpoint, not the whole diagnosis. versioned container, resource, network, log, secret, volume and role specification. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Task. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodepool,ec2nodeclass,nodeclaim` as one read-only checkpoint, not the whole diagnosis. running/scheduled instantiation of a task definition. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed control plane. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingress,service -A` as one read-only checkpoint, not the whole diagnosis. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access entries. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecr describe-repositories` as one read-only checkpoint, not the whole diagnosis. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pending-Pod demand. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ecs describe-clusters --clusters CLUSTER` as one read-only checkpoint, not the whole diagnosis. autoscaler reads unschedulable constraints/requests rather than average node CPU alone. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NodePool. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks describe-cluster --name CLUSTER` as one read-only checkpoint, not the whole diagnosis. constrains labels, taints, requirements, disruption and aggregate resource limits. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingress reconciliation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodepool,ec2nodeclass,nodeclaim` as one read-only checkpoint, not the whole diagnosis. annotations/spec/class generate ALB listeners/rules/target groups. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINERS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service LoadBalancer. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingress,service -A` as one read-only checkpoint, not the whole diagnosis. controller provisions NLB behavior from Service annotations/spec. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
