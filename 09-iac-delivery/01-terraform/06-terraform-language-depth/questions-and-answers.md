# Terraform language depth — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### TERRAFORM-LANGUAGE-DEPTH-JN-01

- [ ] **Question:** What is count, and why does it matter in Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-LANGUAGE-DEPTH-JN-02

- [ ] **Question:** What is for_each, and why does it matter in Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-LANGUAGE-DEPTH-JN-03

- [ ] **Question:** What is Dynamic blocks, and why does it matter in Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-LANGUAGE-DEPTH-JN-04

- [ ] **Question:** What is for expressions, and why does it matter in Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-LANGUAGE-DEPTH-JN-05

- [ ] **Question:** What is Conditional expressions, and why does it matter in Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-LANGUAGE-DEPTH-JN-06

- [ ] **Question:** What is Type constraints, and why does it matter in Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-LANGUAGE-DEPTH-JN-07

- [ ] **Question:** What is Optional attributes, and why does it matter in Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TERRAFORM-LANGUAGE-DEPTH-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### TERRAFORM-LANGUAGE-DEPTH-JN-09

- [ ] **Code:** **Question:** What does `terraform fmt -check -recursive` help you verify for Terraform language depth?
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### TERRAFORM-LANGUAGE-DEPTH-JN-10

- [ ] **Code:** **Question:** What does `terraform validate; terraform plan` help you verify for Terraform language depth?
> **Covered in:** [Terraform language depth — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### TERRAFORM-LANGUAGE-DEPTH-JP-01

- [ ] **Code:** **Question:** A basic count check fails. What would you do first using the CLI?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-02

- [ ] **Question:** A basic for_each check fails. What would you do first?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-03

- [ ] **Question:** A basic Dynamic blocks check fails. What would you do first?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-04

- [ ] **Code:** **Question:** A basic for expressions check fails. What would you do first using the CLI?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-05

- [ ] **Question:** A basic Conditional expressions check fails. What would you do first?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-06

- [ ] **Question:** A basic Type constraints check fails. What would you do first?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-07

- [ ] **Code:** **Question:** A basic Optional attributes check fails. What would you do first using the CLI?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-08

- [ ] **Question:** A basic Validation check fails. What would you do first?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-09

- [ ] **Question:** A basic Preconditions check fails. What would you do first?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TERRAFORM-LANGUAGE-DEPTH-JP-10

- [ ] **Code:** **Question:** A basic Postconditions check fails. What would you do first using the CLI?
> **Covered in:** [Terraform language depth — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### TERRAFORM-LANGUAGE-DEPTH-MN-01

- [ ] **Question:** Compare count with for_each. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** count: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. for_each: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-02

- [ ] **Question:** Compare for_each with Dynamic blocks. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** for_each: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dynamic blocks: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-03

- [ ] **Question:** Compare Dynamic blocks with for expressions. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Dynamic blocks: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. for expressions: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-04

- [ ] **Configuration review:** **Question:** Compare for expressions with Conditional expressions. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** for expressions: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Conditional expressions: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-05

- [ ] **Question:** Compare Conditional expressions with Type constraints. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Conditional expressions: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Type constraints: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-06

- [ ] **Question:** Compare Type constraints with Optional attributes. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Type constraints: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Optional attributes: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-07

- [ ] **Configuration review:** **Question:** Compare Optional attributes with Validation. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Optional attributes: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Validation: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-08

- [ ] **Question:** Compare Validation with Preconditions. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Validation: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Preconditions: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-09

- [ ] **Question:** Compare Preconditions with Postconditions. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Preconditions: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Postconditions: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TERRAFORM-LANGUAGE-DEPTH-MN-10

- [ ] **Configuration review:** **Question:** Compare Postconditions with count. When would each change your design?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Postconditions: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. count: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### TERRAFORM-LANGUAGE-DEPTH-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around count; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-02

- [ ] **Question:** Production is degraded around for_each; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Dynamic blocks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-04

- [ ] **Question:** Production is degraded around for expressions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Conditional expressions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-06

- [ ] **Question:** Production is degraded around Type constraints; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Optional attributes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-08

- [ ] **Question:** Production is degraded around Validation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Preconditions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TERRAFORM-LANGUAGE-DEPTH-MP-10

- [ ] **Question:** Production is degraded around Postconditions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### TERRAFORM-LANGUAGE-DEPTH-SN-01

- [ ] **Question:** Design a production Terraform language depth capability where count, for expressions and Optional attributes are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform language depth capability where for_each, Conditional expressions and Validation are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-03

- [ ] **Question:** Design a production Terraform language depth capability where Dynamic blocks, Type constraints and Preconditions are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform language depth capability where for expressions, Optional attributes and Postconditions are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-05

- [ ] **Question:** Design a production Terraform language depth capability where Conditional expressions, Validation and count are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform language depth capability where Type constraints, Preconditions and for_each are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-07

- [ ] **Question:** Design a production Terraform language depth capability where Optional attributes, Postconditions and Dynamic blocks are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform language depth capability where Validation, count and for expressions are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-09

- [ ] **Question:** Design a production Terraform language depth capability where Preconditions, for_each and Conditional expressions are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TERRAFORM-LANGUAGE-DEPTH-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Terraform language depth capability where Postconditions, Dynamic blocks and Type constraints are first-class requirements.
> **Covered in:** [Terraform language depth — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### TERRAFORM-LANGUAGE-DEPTH-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving count. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving for_each. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dynamic blocks. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving for expressions. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Conditional expressions. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Type constraints. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Optional attributes. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Validation. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Preconditions. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TERRAFORM-LANGUAGE-DEPTH-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Postconditions. How do you lead it end to end?
> **Covered in:** [Terraform language depth — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Terraform language depth; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Terraform modules](../05-terraform-modules/README.md) · [Study note](README.md) · [Next: Import and refactoring →](../07-import-and-refactoring/README.md)

<!-- reading-navigation:end -->
