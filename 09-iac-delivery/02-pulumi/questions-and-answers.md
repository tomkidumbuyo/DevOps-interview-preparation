# Pulumi — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-PULUMI-JN-01

- [ ] **Question:** What is Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39, and why does it matter in Pulumi?
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PULUMI-JN-02

- [ ] **Question:** What is Projects, and why does it matter in Pulumi?
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PULUMI-JN-03

- [ ] **Question:** What is Stacks, and why does it matter in Pulumi?
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PULUMI-JN-04

- [ ] **Question:** What is Resources, and why does it matter in Pulumi?
> **Covered in:** [Pulumi — Pulumi YAML program structure](README.md#pulumi-yaml-program-structure)

**Answer:** is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PULUMI-JN-05

- [ ] **Question:** What is Inputs, and why does it matter in Pulumi?
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PULUMI-JN-06

- [ ] **Question:** What is Outputs, and why does it matter in Pulumi?
> **Covered in:** [Pulumi — Pulumi YAML program structure](README.md#pulumi-yaml-program-structure)

**Answer:** is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PULUMI-JN-07

- [ ] **Question:** What is Providers, and why does it matter in Pulumi?
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-PULUMI-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Pulumi?
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-PULUMI-JN-09

- [ ] **Code:** **Question:** What does `terraform fmt -check -recursive` help you verify for Pulumi?
> **Covered in:** [Pulumi — 10. Terraform versus Pulumi](README.md#10-terraform-versus-pulumi)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-PULUMI-JN-10

- [ ] **Code:** **Question:** What does `terraform validate; terraform plan` help you verify for Pulumi?
> **Covered in:** [Pulumi — 10. Terraform versus Pulumi](README.md#10-terraform-versus-pulumi)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-PULUMI-JP-01

- [ ] **Code:** **Question:** A basic Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39 check fails. What would you do first using the CLI?
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-02

- [ ] **Question:** A basic Projects check fails. What would you do first?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-03

- [ ] **Question:** A basic Stacks check fails. What would you do first?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-04

- [ ] **Code:** **Question:** A basic Resources check fails. What would you do first using the CLI?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-05

- [ ] **Question:** A basic Inputs check fails. What would you do first?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-06

- [ ] **Question:** A basic Outputs check fails. What would you do first?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-07

- [ ] **Code:** **Question:** A basic Providers check fails. What would you do first using the CLI?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-08

- [ ] **Question:** A basic Components check fails. What would you do first?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-09

- [ ] **Question:** A basic Configuration check fails. What would you do first?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-PULUMI-JP-10

- [ ] **Code:** **Question:** A basic Secrets check fails. What would you do first using the CLI?
> **Covered in:** [Pulumi — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-PULUMI-MN-01

- [ ] **Question:** Compare Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39 with Projects. When would each change your design?
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Projects: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-02

- [ ] **Question:** Compare Projects with Stacks. When would each change your design?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Projects: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stacks: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-03

- [ ] **Question:** Compare Stacks with Resources. When would each change your design?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Stacks: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Resources: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-04

- [ ] **Configuration review:** **Question:** Compare Resources with Inputs. When would each change your design?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Resources: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Inputs: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-05

- [ ] **Question:** Compare Inputs with Outputs. When would each change your design?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Inputs: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Outputs: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-06

- [ ] **Question:** Compare Outputs with Providers. When would each change your design?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Outputs: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Providers: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-07

- [ ] **Configuration review:** **Question:** Compare Providers with Components. When would each change your design?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Providers: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Components: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-08

- [ ] **Question:** Compare Components with Configuration. When would each change your design?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Components: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Configuration: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-09

- [ ] **Question:** Compare Configuration with Secrets. When would each change your design?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Configuration: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Secrets: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-PULUMI-MN-10

- [ ] **Configuration review:** **Question:** Compare Secrets with Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39. When would each change your design?
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Secrets: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-PULUMI-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-02

- [ ] **Question:** Production is degraded around Projects; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Stacks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-04

- [ ] **Question:** Production is degraded around Resources; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inputs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-06

- [ ] **Question:** Production is degraded around Outputs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Providers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-08

- [ ] **Question:** Production is degraded around Components; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Configuration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-PULUMI-MP-10

- [ ] **Question:** Production is degraded around Secrets; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-PULUMI-SN-01

- [ ] **Question:** Design a production Pulumi capability where Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39, Resources and Providers are first-class requirements.
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi capability where Projects, Inputs and Components are first-class requirements.
> **Covered in:** [Pulumi — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-03

- [ ] **Question:** Design a production Pulumi capability where Stacks, Outputs and Configuration are first-class requirements.
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi capability where Resources, Providers and Secrets are first-class requirements.
> **Covered in:** [Pulumi — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-05

- [ ] **Question:** Design a production Pulumi capability where Inputs, Components and Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39 are first-class requirements.
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi capability where Outputs, Configuration and Projects are first-class requirements.
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-07

- [ ] **Question:** Design a production Pulumi capability where Providers, Secrets and Stacks are first-class requirements.
> **Covered in:** [Pulumi — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi capability where Components, Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39 and Resources are first-class requirements.
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-09

- [ ] **Question:** Design a production Pulumi capability where Configuration, Projects and Inputs are first-class requirements.
> **Covered in:** [Pulumi — Pulumi.<stack>.yaml stack configuration](README.md#pulumistackyaml-stack-configuration)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-PULUMI-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi capability where Secrets, Stacks and Outputs are first-class requirements.
> **Covered in:** [Pulumi — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-PULUMI-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pulumi supports general-purpose programming languages, state backends, policy enforcement, CI/CD workflows and Automation API-driven turn589377search39. How do you lead it end to end?
> **Covered in:** [Pulumi — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Projects. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Stacks. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resources. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inputs. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Outputs. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Providers. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Components. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Configuration. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-PULUMI-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secrets. How do you lead it end to end?
> **Covered in:** [Pulumi — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Terraform security](../01-terraform/11-terraform-security/README.md) · [Study note](README.md) · [Next: Pulumi concepts →](01-pulumi-concepts/README.md)

<!-- reading-navigation:end -->
