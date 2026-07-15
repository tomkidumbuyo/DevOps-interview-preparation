# Terraform environments — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### TERRAFORM-ENVIRONMENTS-JN-01

- [ ] **Question:** What is Separate state files, and why does it matter in Terraform environments?
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-ENVIRONMENTS-JN-02

- [ ] **Question:** What is Directory-based environments, and why does it matter in Terraform environments?
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-ENVIRONMENTS-JN-03

- [ ] **Question:** What is Workspaces, and why does it matter in Terraform environments?
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-ENVIRONMENTS-JN-04

- [ ] **Question:** What is Account and project separation, and why does it matter in Terraform environments?
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-ENVIRONMENTS-JN-05

- [ ] **Question:** What is Environment promotion, and why does it matter in Terraform environments?
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-ENVIRONMENTS-JN-06

- [ ] **Question:** What is Variable management, and why does it matter in Terraform environments?
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-ENVIRONMENTS-JN-07

- [ ] **Question:** What is Separate state files, and why does it matter in Terraform environments?
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-ENVIRONMENTS-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Terraform environments?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### TERRAFORM-ENVIRONMENTS-JN-09

- [ ] **Code:** **Question:** What does `terraform fmt -check -recursive` help you verify for Terraform environments?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### TERRAFORM-ENVIRONMENTS-JN-10

- [ ] **Code:** **Question:** What does `terraform validate; terraform plan` help you verify for Terraform environments?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### TERRAFORM-ENVIRONMENTS-JP-01

- [ ] **Code:** **Question:** A basic Separate state files check fails. What would you do first using the CLI?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-02

- [ ] **Question:** A basic Directory-based environments check fails. What would you do first?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-03

- [ ] **Question:** A basic Workspaces check fails. What would you do first?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-04

- [ ] **Code:** **Question:** A basic Account and project separation check fails. What would you do first using the CLI?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-05

- [ ] **Question:** A basic Environment promotion check fails. What would you do first?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-06

- [ ] **Question:** A basic Variable management check fails. What would you do first?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-07

- [ ] **Code:** **Question:** A basic Separate state files check fails. What would you do first using the CLI?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-08

- [ ] **Question:** A basic Directory-based environments check fails. What would you do first?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-09

- [ ] **Question:** A basic Workspaces check fails. What would you do first?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-ENVIRONMENTS-JP-10

- [ ] **Code:** **Question:** A basic Account and project separation check fails. What would you do first using the CLI?
> **Covered in:** [Terraform environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### TERRAFORM-ENVIRONMENTS-MN-01

- [ ] **Question:** Compare Separate state files with Directory-based environments. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Separate state files: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Directory-based environments: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-02

- [ ] **Question:** Compare Directory-based environments with Workspaces. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Directory-based environments: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Workspaces: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-03

- [ ] **Question:** Compare Workspaces with Account and project separation. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Workspaces: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Account and project separation: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-04

- [ ] **Configuration review:** **Question:** Compare Account and project separation with Environment promotion. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Account and project separation: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Environment promotion: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-05

- [ ] **Question:** Compare Environment promotion with Variable management. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Environment promotion: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Variable management: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-06

- [ ] **Question:** Compare Variable management with Separate state files. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Variable management: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate state files: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-07

- [ ] **Configuration review:** **Question:** Compare Separate state files with Directory-based environments. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Separate state files: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Directory-based environments: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-08

- [ ] **Question:** Compare Directory-based environments with Workspaces. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Directory-based environments: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Workspaces: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-09

- [ ] **Question:** Compare Workspaces with Account and project separation. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Workspaces: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Account and project separation: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-ENVIRONMENTS-MN-10

- [ ] **Configuration review:** **Question:** Compare Account and project separation with Separate state files. When would each change your design?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Account and project separation: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate state files: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### TERRAFORM-ENVIRONMENTS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Separate state files; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-02

- [ ] **Question:** Production is degraded around Directory-based environments; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Workspaces; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-04

- [ ] **Question:** Production is degraded around Account and project separation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Environment promotion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-06

- [ ] **Question:** Production is degraded around Variable management; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Separate state files; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-08

- [ ] **Question:** Production is degraded around Directory-based environments; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Workspaces; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-ENVIRONMENTS-MP-10

- [ ] **Question:** Production is degraded around Account and project separation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### TERRAFORM-ENVIRONMENTS-SN-01

- [ ] **Question:** Design a production Terraform environments capability where Separate state files, Account and project separation and Separate state files are first-class requirements.
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform environments capability where Directory-based environments, Environment promotion and Directory-based environments are first-class requirements.
> **Covered in:** [Terraform environments — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-03

- [ ] **Question:** Design a production Terraform environments capability where Workspaces, Variable management and Workspaces are first-class requirements.
> **Covered in:** [Terraform environments — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform environments capability where Account and project separation, Separate state files and Account and project separation are first-class requirements.
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-05

- [ ] **Question:** Design a production Terraform environments capability where Environment promotion, Directory-based environments and Separate state files are first-class requirements.
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform environments capability where Variable management, Workspaces and Directory-based environments are first-class requirements.
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-07

- [ ] **Question:** Design a production Terraform environments capability where Separate state files, Account and project separation and Workspaces are first-class requirements.
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform environments capability where Directory-based environments, Separate state files and Account and project separation are first-class requirements.
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-09

- [ ] **Question:** Design a production Terraform environments capability where Workspaces, Directory-based environments and Environment promotion are first-class requirements.
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-ENVIRONMENTS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform environments capability where Account and project separation, Workspaces and Variable management are first-class requirements.
> **Covered in:** [Terraform environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### TERRAFORM-ENVIRONMENTS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Separate state files. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Directory-based environments. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workspaces. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Account and project separation. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Environment promotion. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Variable management. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Separate state files. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Directory-based environments. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workspaces. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-ENVIRONMENTS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Account and project separation. How do you lead it end to end?
> **Covered in:** [Terraform environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Terraform environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Import and refactoring](../07-import-and-refactoring/README.md) · [Study note](README.md) · [Next: Terraform testing and validation →](../09-terraform-testing-and-validation/README.md)

<!-- reading-navigation:end -->
