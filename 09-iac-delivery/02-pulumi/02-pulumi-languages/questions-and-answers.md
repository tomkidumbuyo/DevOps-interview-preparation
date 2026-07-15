# Pulumi languages — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### PULUMI-LANGUAGES-JN-01

- [ ] **Question:** What is TypeScript, and why does it matter in Pulumi languages?
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PULUMI-LANGUAGES-JN-02

- [ ] **Question:** What is Python, and why does it matter in Pulumi languages?
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PULUMI-LANGUAGES-JN-03

- [ ] **Question:** What is Go, and why does it matter in Pulumi languages?
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PULUMI-LANGUAGES-JN-04

- [ ] **Question:** What is C#, and why does it matter in Pulumi languages?
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PULUMI-LANGUAGES-JN-05

- [ ] **Question:** What is Java, and why does it matter in Pulumi languages?
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PULUMI-LANGUAGES-JN-06

- [ ] **Question:** What is YAML, and why does it matter in Pulumi languages?
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PULUMI-LANGUAGES-JN-07

- [ ] **Question:** What is Language-selection trade-offs, and why does it matter in Pulumi languages?
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PULUMI-LANGUAGES-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Pulumi languages?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### PULUMI-LANGUAGES-JN-09

- [ ] **Code:** **Question:** What does `terraform fmt -check -recursive` help you verify for Pulumi languages?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### PULUMI-LANGUAGES-JN-10

- [ ] **Code:** **Question:** What does `terraform validate; terraform plan` help you verify for Pulumi languages?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### PULUMI-LANGUAGES-JP-01

- [ ] **Code:** **Question:** A basic TypeScript check fails. What would you do first using the CLI?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-02

- [ ] **Question:** A basic Python check fails. What would you do first?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-03

- [ ] **Question:** A basic Go check fails. What would you do first?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-04

- [ ] **Code:** **Question:** A basic C# check fails. What would you do first using the CLI?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-05

- [ ] **Question:** A basic Java check fails. What would you do first?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-06

- [ ] **Question:** A basic YAML check fails. What would you do first?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-07

- [ ] **Code:** **Question:** A basic Language-selection trade-offs check fails. What would you do first using the CLI?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-08

- [ ] **Question:** A basic TypeScript check fails. What would you do first?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-09

- [ ] **Question:** A basic Python check fails. What would you do first?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PULUMI-LANGUAGES-JP-10

- [ ] **Code:** **Question:** A basic Go check fails. What would you do first using the CLI?
> **Covered in:** [Pulumi languages — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### PULUMI-LANGUAGES-MN-01

- [ ] **Question:** Compare TypeScript with Python. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** TypeScript: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Python: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-02

- [ ] **Question:** Compare Python with Go. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Python: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Go: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-03

- [ ] **Question:** Compare Go with C#. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Go: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. C#: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-04

- [ ] **Configuration review:** **Question:** Compare C# with Java. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** C#: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Java: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-05

- [ ] **Question:** Compare Java with YAML. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Java: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. YAML: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-06

- [ ] **Question:** Compare YAML with Language-selection trade-offs. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** YAML: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Language-selection trade-offs: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-07

- [ ] **Configuration review:** **Question:** Compare Language-selection trade-offs with TypeScript. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Language-selection trade-offs: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. TypeScript: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-08

- [ ] **Question:** Compare TypeScript with Python. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** TypeScript: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Python: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-09

- [ ] **Question:** Compare Python with Go. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Python: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Go: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PULUMI-LANGUAGES-MN-10

- [ ] **Configuration review:** **Question:** Compare Go with TypeScript. When would each change your design?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Go: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. TypeScript: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### PULUMI-LANGUAGES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around TypeScript; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-02

- [ ] **Question:** Production is degraded around Python; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Go; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-04

- [ ] **Question:** Production is degraded around C#; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Java; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-06

- [ ] **Question:** Production is degraded around YAML; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Language-selection trade-offs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-08

- [ ] **Question:** Production is degraded around TypeScript; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Python; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PULUMI-LANGUAGES-MP-10

- [ ] **Question:** Production is degraded around Go; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### PULUMI-LANGUAGES-SN-01

- [ ] **Question:** Design a production Pulumi languages capability where TypeScript, C# and Language-selection trade-offs are first-class requirements.
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi languages capability where Python, Java and TypeScript are first-class requirements.
> **Covered in:** [Pulumi languages — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-03

- [ ] **Question:** Design a production Pulumi languages capability where Go, YAML and Python are first-class requirements.
> **Covered in:** [Pulumi languages — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi languages capability where C#, Language-selection trade-offs and Go are first-class requirements.
> **Covered in:** [Pulumi languages — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-05

- [ ] **Question:** Design a production Pulumi languages capability where Java, TypeScript and TypeScript are first-class requirements.
> **Covered in:** [Pulumi languages — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi languages capability where YAML, Python and Python are first-class requirements.
> **Covered in:** [Pulumi languages — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-07

- [ ] **Question:** Design a production Pulumi languages capability where Language-selection trade-offs, Go and Go are first-class requirements.
> **Covered in:** [Pulumi languages — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi languages capability where TypeScript, TypeScript and C# are first-class requirements.
> **Covered in:** [Pulumi languages — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-09

- [ ] **Question:** Design a production Pulumi languages capability where Python, Python and Java are first-class requirements.
> **Covered in:** [Pulumi languages — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PULUMI-LANGUAGES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Pulumi languages capability where Go, Go and YAML are first-class requirements.
> **Covered in:** [Pulumi languages — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### PULUMI-LANGUAGES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TypeScript. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Python. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Go. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving C#. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Java. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving YAML. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Language-selection trade-offs. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TypeScript. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Python. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PULUMI-LANGUAGES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Go. How do you lead it end to end?
> **Covered in:** [Pulumi languages — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Pulumi languages; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Pulumi concepts](../01-pulumi-concepts/README.md) · [Study note](README.md) · [Next: Pulumi state →](../03-pulumi-state/README.md)

<!-- reading-navigation:end -->
