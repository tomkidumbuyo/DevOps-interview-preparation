# Migration scenarios — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-MIGRATION-SCENARIOS-JN-01

- [ ] **Question:** What is EC2 to Kubernetes, and why does it matter in Migration scenarios?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MIGRATION-SCENARIOS-JN-02

- [ ] **Question:** What is ECS to EKS, and why does it matter in Migration scenarios?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MIGRATION-SCENARIOS-JN-03

- [ ] **Question:** What is Self-managed Kubernetes to EKS or GKE, and why does it matter in Migration scenarios?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MIGRATION-SCENARIOS-JN-04

- [ ] **Question:** What is Terraform monolith to modules, and why does it matter in Migration scenarios?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MIGRATION-SCENARIOS-JN-05

- [ ] **Question:** What is Terraform to Pulumi, and why does it matter in Migration scenarios?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MIGRATION-SCENARIOS-JN-06

- [ ] **Question:** What is Manual infrastructure to IaC, and why does it matter in Migration scenarios?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MIGRATION-SCENARIOS-JN-07

- [ ] **Question:** What is Ingress to Gateway API, and why does it matter in Migration scenarios?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MIGRATION-SCENARIOS-JN-08

- [ ] **Code:** **Question:** What does `git log --since='2 hours ago' --oneline` help you verify for Migration scenarios?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-MIGRATION-SCENARIOS-JN-09

- [ ] **Code:** **Question:** What does `date -u; whoami; hostname` help you verify for Migration scenarios?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-MIGRATION-SCENARIOS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get events -A --sort-by=.lastTimestamp` help you verify for Migration scenarios?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-MIGRATION-SCENARIOS-JP-01

- [ ] **Code:** **Question:** A basic EC2 to Kubernetes check fails. What would you do first using the CLI?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `date -u; whoami; hostname` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-02

- [ ] **Question:** A basic ECS to EKS check fails. What would you do first?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-03

- [ ] **Question:** A basic Self-managed Kubernetes to EKS or GKE check fails. What would you do first?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-04

- [ ] **Code:** **Question:** A basic Terraform monolith to modules check fails. What would you do first using the CLI?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='2 hours ago' --oneline` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-05

- [ ] **Question:** A basic Terraform to Pulumi check fails. What would you do first?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `date -u; whoami; hostname` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-06

- [ ] **Question:** A basic Manual infrastructure to IaC check fails. What would you do first?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-07

- [ ] **Code:** **Question:** A basic Ingress to Gateway API check fails. What would you do first using the CLI?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-08

- [ ] **Question:** A basic Single-cloud to multi-cloud check fails. What would you do first?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='2 hours ago' --oneline` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-09

- [ ] **Question:** A basic Managed LLM API to self-hosted models check fails. What would you do first?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `date -u; whoami; hostname` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MIGRATION-SCENARIOS-JP-10

- [ ] **Code:** **Question:** A basic One model server to KServe check fails. What would you do first using the CLI?
> **Covered in:** [Migration scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-MIGRATION-SCENARIOS-MN-01

- [ ] **Question:** Compare EC2 to Kubernetes with ECS to EKS. When would each change your design?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** EC2 to Kubernetes: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. ECS to EKS: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-02

- [ ] **Question:** Compare ECS to EKS with Self-managed Kubernetes to EKS or GKE. When would each change your design?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** ECS to EKS: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Self-managed Kubernetes to EKS or GKE: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-03

- [ ] **Question:** Compare Self-managed Kubernetes to EKS or GKE with Terraform monolith to modules. When would each change your design?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Self-managed Kubernetes to EKS or GKE: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Terraform monolith to modules: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-04

- [ ] **Configuration review:** **Question:** Compare Terraform monolith to modules with Terraform to Pulumi. When would each change your design?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Terraform monolith to modules: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Terraform to Pulumi: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-05

- [ ] **Question:** Compare Terraform to Pulumi with Manual infrastructure to IaC. When would each change your design?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Terraform to Pulumi: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Manual infrastructure to IaC: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-06

- [ ] **Question:** Compare Manual infrastructure to IaC with Ingress to Gateway API. When would each change your design?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Manual infrastructure to IaC: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Ingress to Gateway API: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-07

- [ ] **Configuration review:** **Question:** Compare Ingress to Gateway API with Single-cloud to multi-cloud. When would each change your design?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Ingress to Gateway API: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Single-cloud to multi-cloud: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-08

- [ ] **Question:** Compare Single-cloud to multi-cloud with Managed LLM API to self-hosted models. When would each change your design?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Single-cloud to multi-cloud: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Managed LLM API to self-hosted models: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-09

- [ ] **Question:** Compare Managed LLM API to self-hosted models with One model server to KServe. When would each change your design?
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Managed LLM API to self-hosted models: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. One model server to KServe: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MIGRATION-SCENARIOS-MN-10

- [ ] **Configuration review:** **Question:** Compare One model server to KServe with EC2 to Kubernetes. When would each change your design?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** One model server to KServe: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. EC2 to Kubernetes: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-MIGRATION-SCENARIOS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around EC2 to Kubernetes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `date -u; whoami; hostname` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-02

- [ ] **Question:** Production is degraded around ECS to EKS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Self-managed Kubernetes to EKS or GKE; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-04

- [ ] **Question:** Production is degraded around Terraform monolith to modules; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='2 hours ago' --oneline` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Terraform to Pulumi; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `date -u; whoami; hostname` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-06

- [ ] **Question:** Production is degraded around Manual infrastructure to IaC; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Ingress to Gateway API; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-08

- [ ] **Question:** Production is degraded around Single-cloud to multi-cloud; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='2 hours ago' --oneline` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Managed LLM API to self-hosted models; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `date -u; whoami; hostname` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MIGRATION-SCENARIOS-MP-10

- [ ] **Question:** Production is degraded around One model server to KServe; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Migration scenarios — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-MIGRATION-SCENARIOS-SN-01

- [ ] **Question:** Design a production Migration scenarios capability where EC2 to Kubernetes, Terraform monolith to modules and Ingress to Gateway API are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Migration scenarios capability where ECS to EKS, Terraform to Pulumi and Single-cloud to multi-cloud are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-03

- [ ] **Question:** Design a production Migration scenarios capability where Self-managed Kubernetes to EKS or GKE, Manual infrastructure to IaC and Managed LLM API to self-hosted models are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Migration scenarios capability where Terraform monolith to modules, Ingress to Gateway API and One model server to KServe are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-05

- [ ] **Question:** Design a production Migration scenarios capability where Terraform to Pulumi, Single-cloud to multi-cloud and EC2 to Kubernetes are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Migration scenarios capability where Manual infrastructure to IaC, Managed LLM API to self-hosted models and ECS to EKS are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-07

- [ ] **Question:** Design a production Migration scenarios capability where Ingress to Gateway API, One model server to KServe and Self-managed Kubernetes to EKS or GKE are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Migration scenarios capability where Single-cloud to multi-cloud, EC2 to Kubernetes and Terraform monolith to modules are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-09

- [ ] **Question:** Design a production Migration scenarios capability where Managed LLM API to self-hosted models, ECS to EKS and Terraform to Pulumi are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MIGRATION-SCENARIOS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Migration scenarios capability where One model server to KServe, Self-managed Kubernetes to EKS or GKE and Manual infrastructure to IaC are first-class requirements.
> **Covered in:** [Migration scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-MIGRATION-SCENARIOS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving EC2 to Kubernetes. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `date -u; whoami; hostname` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ECS to EKS. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Self-managed Kubernetes to EKS or GKE. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Terraform monolith to modules. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='2 hours ago' --oneline` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Terraform to Pulumi. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `date -u; whoami; hostname` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Manual infrastructure to IaC. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingress to Gateway API. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Single-cloud to multi-cloud. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='2 hours ago' --oneline` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed LLM API to self-hosted models. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `date -u; whoami; hostname` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MIGRATION-SCENARIOS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving One model server to KServe. How do you lead it end to end?
> **Covered in:** [Migration scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Migration scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Troubleshooting scenarios](../02-troubleshooting-scenarios/README.md) · [Study note](README.md) · [Next: Security scenarios →](../04-security-scenarios/README.md)

<!-- reading-navigation:end -->
