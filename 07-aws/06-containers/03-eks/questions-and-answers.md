# Amazon EKS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-EKS-JN-01

- [ ] **Question:** What is Managed control plane, and why does it matter in Amazon EKS?
> **Covered in:** [Amazon EKS — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EKS-JN-02

- [ ] **Question:** What is Access entries, and why does it matter in Amazon EKS?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EKS-JN-03

- [ ] **Question:** What is Managed node group, and why does it matter in Amazon EKS?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** AWS-integrated ASG lifecycle for tested AMI/update patterns. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EKS-JN-04

- [ ] **Question:** What is IRSA, and why does it matter in Amazon EKS?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** OIDC service-account token assumes an IAM role with trust conditions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EKS-JN-05

- [ ] **Question:** What is EKS Pod Identity, and why does it matter in Amazon EKS?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** association/agent-based workload role delivery with separate operational semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EKS-JN-06

- [ ] **Question:** What is VPC CNI, and why does it matter in Amazon EKS?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** assigns VPC IPs and is constrained by subnet/ENI/prefix settings. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EKS-JN-07

- [ ] **Question:** What is Managed add-on, and why does it matter in Amazon EKS?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** versioned EKS distribution of components still needs compatibility/config ownership. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-EKS-JN-08

- [ ] **Code:** **Question:** What does `kubectl get nodes,pods -A -o wide` help you verify for Amazon EKS?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: EBS/EFS drivers need workload identity, topology and version management.

### AMAZON-EKS-JN-09

- [ ] **Code:** **Question:** What does `aws eks describe-cluster --name CLUSTER` help you verify for Amazon EKS?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: control plane, APIs, add-ons and nodes roll under skew/deprecation constraints.

### AMAZON-EKS-JN-10

- [ ] **Code:** **Question:** What does `aws eks list-addons --cluster-name CLUSTER` help you verify for Amazon EKS?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost.

## Junior — procedural and command questions

### AMAZON-EKS-JP-01

- [ ] **Code:** **Question:** A basic Managed control plane check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks describe-cluster --name CLUSTER` and capture exact status/reason/request ID. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-02

- [ ] **Question:** A basic Access entries check fails. What would you do first?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks list-addons --cluster-name CLUSTER` and capture exact status/reason/request ID. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-03

- [ ] **Question:** A basic Managed node group check fails. What would you do first?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks list-access-entries --cluster-name CLUSTER` and capture exact status/reason/request ID. AWS-integrated ASG lifecycle for tested AMI/update patterns. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-04

- [ ] **Code:** **Question:** A basic IRSA check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes,pods -A -o wide` and capture exact status/reason/request ID. OIDC service-account token assumes an IAM role with trust conditions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-05

- [ ] **Question:** A basic EKS Pod Identity check fails. What would you do first?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks describe-cluster --name CLUSTER` and capture exact status/reason/request ID. association/agent-based workload role delivery with separate operational semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-06

- [ ] **Question:** A basic VPC CNI check fails. What would you do first?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks list-addons --cluster-name CLUSTER` and capture exact status/reason/request ID. assigns VPC IPs and is constrained by subnet/ENI/prefix settings. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-07

- [ ] **Code:** **Question:** A basic Managed add-on check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks list-access-entries --cluster-name CLUSTER` and capture exact status/reason/request ID. versioned EKS distribution of components still needs compatibility/config ownership. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-08

- [ ] **Question:** A basic CSI drivers check fails. What would you do first?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes,pods -A -o wide` and capture exact status/reason/request ID. EBS/EFS drivers need workload identity, topology and version management. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-09

- [ ] **Question:** A basic Cluster upgrade check fails. What would you do first?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks describe-cluster --name CLUSTER` and capture exact status/reason/request ID. control plane, APIs, add-ons and nodes roll under skew/deprecation constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-EKS-JP-10

- [ ] **Code:** **Question:** A basic Control-plane logging check fails. What would you do first using the CLI?
> **Covered in:** [Amazon EKS — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws eks list-addons --cluster-name CLUSTER` and capture exact status/reason/request ID. API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-EKS-MN-01

- [ ] **Question:** Compare Managed control plane with Access entries. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Managed control plane: AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Access entries: EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-02

- [ ] **Question:** Compare Access entries with Managed node group. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Access entries: EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Managed node group: AWS-integrated ASG lifecycle for tested AMI/update patterns. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-03

- [ ] **Question:** Compare Managed node group with IRSA. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Managed node group: AWS-integrated ASG lifecycle for tested AMI/update patterns. IRSA: OIDC service-account token assumes an IAM role with trust conditions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-04

- [ ] **Configuration review:** **Question:** Compare IRSA with EKS Pod Identity. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** IRSA: OIDC service-account token assumes an IAM role with trust conditions. EKS Pod Identity: association/agent-based workload role delivery with separate operational semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-05

- [ ] **Question:** Compare EKS Pod Identity with VPC CNI. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** EKS Pod Identity: association/agent-based workload role delivery with separate operational semantics. VPC CNI: assigns VPC IPs and is constrained by subnet/ENI/prefix settings. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-06

- [ ] **Question:** Compare VPC CNI with Managed add-on. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** VPC CNI: assigns VPC IPs and is constrained by subnet/ENI/prefix settings. Managed add-on: versioned EKS distribution of components still needs compatibility/config ownership. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-07

- [ ] **Configuration review:** **Question:** Compare Managed add-on with CSI drivers. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Managed add-on: versioned EKS distribution of components still needs compatibility/config ownership. CSI drivers: EBS/EFS drivers need workload identity, topology and version management. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-08

- [ ] **Question:** Compare CSI drivers with Cluster upgrade. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CSI drivers: EBS/EFS drivers need workload identity, topology and version management. Cluster upgrade: control plane, APIs, add-ons and nodes roll under skew/deprecation constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-09

- [ ] **Question:** Compare Cluster upgrade with Control-plane logging. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cluster upgrade: control plane, APIs, add-ons and nodes roll under skew/deprecation constraints. Control-plane logging: API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-EKS-MN-10

- [ ] **Configuration review:** **Question:** Compare Control-plane logging with Managed control plane. When would each change your design?
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Control-plane logging: API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost. Managed control plane: AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-EKS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Managed control plane; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks describe-cluster --name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-02

- [ ] **Question:** Production is degraded around Access entries; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks list-addons --cluster-name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Managed node group; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks list-access-entries --cluster-name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. AWS-integrated ASG lifecycle for tested AMI/update patterns. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-04

- [ ] **Question:** Production is degraded around IRSA; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes,pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. OIDC service-account token assumes an IAM role with trust conditions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around EKS Pod Identity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks describe-cluster --name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. association/agent-based workload role delivery with separate operational semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-06

- [ ] **Question:** Production is degraded around VPC CNI; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks list-addons --cluster-name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. assigns VPC IPs and is constrained by subnet/ENI/prefix settings. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Managed add-on; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks list-access-entries --cluster-name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. versioned EKS distribution of components still needs compatibility/config ownership. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-08

- [ ] **Question:** Production is degraded around CSI drivers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes,pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. EBS/EFS drivers need workload identity, topology and version management. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cluster upgrade; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks describe-cluster --name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. control plane, APIs, add-ons and nodes roll under skew/deprecation constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-EKS-MP-10

- [ ] **Question:** Production is degraded around Control-plane logging; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws eks list-addons --cluster-name CLUSTER` plus recent events/changes, then correlate the service-specific SLI. API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-EKS-SN-01

- [ ] **Question:** Design a production Amazon EKS capability where Managed control plane, IRSA and Managed add-on are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. OIDC service-account token assumes an IAM role with trust conditions. versioned EKS distribution of components still needs compatibility/config ownership. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EKS capability where Access entries, EKS Pod Identity and CSI drivers are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. association/agent-based workload role delivery with separate operational semantics. EBS/EFS drivers need workload identity, topology and version management. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-03

- [ ] **Question:** Design a production Amazon EKS capability where Managed node group, VPC CNI and Cluster upgrade are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AWS-integrated ASG lifecycle for tested AMI/update patterns. assigns VPC IPs and is constrained by subnet/ENI/prefix settings. control plane, APIs, add-ons and nodes roll under skew/deprecation constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EKS capability where IRSA, Managed add-on and Control-plane logging are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: OIDC service-account token assumes an IAM role with trust conditions. versioned EKS distribution of components still needs compatibility/config ownership. API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-05

- [ ] **Question:** Design a production Amazon EKS capability where EKS Pod Identity, CSI drivers and Managed control plane are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: association/agent-based workload role delivery with separate operational semantics. EBS/EFS drivers need workload identity, topology and version management. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EKS capability where VPC CNI, Cluster upgrade and Access entries are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: assigns VPC IPs and is constrained by subnet/ENI/prefix settings. control plane, APIs, add-ons and nodes roll under skew/deprecation constraints. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-07

- [ ] **Question:** Design a production Amazon EKS capability where Managed add-on, Control-plane logging and Managed node group are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned EKS distribution of components still needs compatibility/config ownership. API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost. AWS-integrated ASG lifecycle for tested AMI/update patterns. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EKS capability where CSI drivers, Managed control plane and IRSA are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: EBS/EFS drivers need workload identity, topology and version management. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. OIDC service-account token assumes an IAM role with trust conditions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-09

- [ ] **Question:** Design a production Amazon EKS capability where Cluster upgrade, Access entries and EKS Pod Identity are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: control plane, APIs, add-ons and nodes roll under skew/deprecation constraints. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. association/agent-based workload role delivery with separate operational semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-EKS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon EKS capability where Control-plane logging, Managed node group and VPC CNI are first-class requirements.
> **Covered in:** [Amazon EKS — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost. AWS-integrated ASG lifecycle for tested AMI/update patterns. assigns VPC IPs and is constrained by subnet/ENI/prefix settings. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-EKS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed control plane. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks describe-cluster --name CLUSTER` as one read-only checkpoint, not the whole diagnosis. AWS runs API/etcd availability while customers own access, workloads and most data-plane choices. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access entries. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks list-addons --cluster-name CLUSTER` as one read-only checkpoint, not the whole diagnosis. EKS API manages cluster access mappings; Kubernetes RBAC still authorizes resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed node group. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks list-access-entries --cluster-name CLUSTER` as one read-only checkpoint, not the whole diagnosis. AWS-integrated ASG lifecycle for tested AMI/update patterns. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IRSA. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes,pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. OIDC service-account token assumes an IAM role with trust conditions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving EKS Pod Identity. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks describe-cluster --name CLUSTER` as one read-only checkpoint, not the whole diagnosis. association/agent-based workload role delivery with separate operational semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC CNI. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks list-addons --cluster-name CLUSTER` as one read-only checkpoint, not the whole diagnosis. assigns VPC IPs and is constrained by subnet/ENI/prefix settings. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed add-on. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks list-access-entries --cluster-name CLUSTER` as one read-only checkpoint, not the whole diagnosis. versioned EKS distribution of components still needs compatibility/config ownership. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CSI drivers. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes,pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. EBS/EFS drivers need workload identity, topology and version management. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cluster upgrade. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks describe-cluster --name CLUSTER` as one read-only checkpoint, not the whole diagnosis. control plane, APIs, add-ons and nodes roll under skew/deprecation constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-EKS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control-plane logging. How do you lead it end to end?
> **Covered in:** [Amazon EKS — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws eks list-addons --cluster-name CLUSTER` as one read-only checkpoint, not the whole diagnosis. API/audit/authenticator/controller/scheduler logs support security and diagnosis at a cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon ECS](../02-ecs/README.md) · [Study note](README.md) · [Next: Karpenter and EKS Auto Mode →](../04-karpenter-auto-mode/README.md)

<!-- reading-navigation:end -->
