# GitHub Actions — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### GITHUB-ACTIONS-JN-01

- [ ] **Question:** What is Workflows, and why does it matter in GitHub Actions?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GITHUB-ACTIONS-JN-02

- [ ] **Question:** What is Events, and why does it matter in GitHub Actions?
> **Covered in:** [GitHub Actions — Events and filters](README.md#events-and-filters)

**Answer:** is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GITHUB-ACTIONS-JN-03

- [ ] **Question:** What is Jobs, and why does it matter in GitHub Actions?
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GITHUB-ACTIONS-JN-04

- [ ] **Question:** What is Steps, and why does it matter in GitHub Actions?
> **Covered in:** [GitHub Actions — Steps, shells and workflow commands](README.md#steps-shells-and-workflow-commands)

**Answer:** is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GITHUB-ACTIONS-JN-05

- [ ] **Question:** What is Actions, and why does it matter in GitHub Actions?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GITHUB-ACTIONS-JN-06

- [ ] **Question:** What is Runners, and why does it matter in GitHub Actions?
> **Covered in:** [GitHub Actions — Runners and isolation](README.md#runners-and-isolation)

**Answer:** is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GITHUB-ACTIONS-JN-07

- [ ] **Question:** What is Matrices, and why does it matter in GitHub Actions?
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GITHUB-ACTIONS-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for GitHub Actions?
> **Covered in:** [GitHub Actions — CLI, debugging and operations](README.md#cli-debugging-and-operations)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### GITHUB-ACTIONS-JN-09

- [ ] **Code:** **Question:** What does `terraform fmt -check -recursive` help you verify for GitHub Actions?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### GITHUB-ACTIONS-JN-10

- [ ] **Code:** **Question:** What does `terraform validate; terraform plan` help you verify for GitHub Actions?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### GITHUB-ACTIONS-JP-01

- [ ] **Code:** **Question:** A basic Workflows check fails. What would you do first using the CLI?
> **Covered in:** [GitHub Actions — CLI, debugging and operations](README.md#cli-debugging-and-operations)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-02

- [ ] **Question:** A basic Events check fails. What would you do first?
> **Covered in:** [GitHub Actions — Events and filters](README.md#events-and-filters)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-03

- [ ] **Question:** A basic Jobs check fails. What would you do first?
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-04

- [ ] **Code:** **Question:** A basic Steps check fails. What would you do first using the CLI?
> **Covered in:** [GitHub Actions — Steps, shells and workflow commands](README.md#steps-shells-and-workflow-commands)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-05

- [ ] **Question:** A basic Actions check fails. What would you do first?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-06

- [ ] **Question:** A basic Runners check fails. What would you do first?
> **Covered in:** [GitHub Actions — Runners and isolation](README.md#runners-and-isolation)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-07

- [ ] **Code:** **Question:** A basic Matrices check fails. What would you do first using the CLI?
> **Covered in:** [GitHub Actions — CLI, debugging and operations](README.md#cli-debugging-and-operations)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `pulumi preview --diff` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-08

- [ ] **Question:** A basic Reusable workflows check fails. What would you do first?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-09

- [ ] **Question:** A basic Environments check fails. What would you do first?
> **Covered in:** [GitHub Actions — Security and supply-chain checklist](README.md#security-and-supply-chain-checklist)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform fmt -check -recursive` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GITHUB-ACTIONS-JP-10

- [ ] **Code:** **Question:** A basic Secrets check fails. What would you do first using the CLI?
> **Covered in:** [GitHub Actions — CLI, debugging and operations](README.md#cli-debugging-and-operations)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform validate; terraform plan` and capture exact status/reason/request ID. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### GITHUB-ACTIONS-MN-01

- [ ] **Question:** Compare Workflows with Events. When would each change your design?
> **Covered in:** [GitHub Actions — Events and filters](README.md#events-and-filters)

**Answer:** Workflows: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Events: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-02

- [ ] **Question:** Compare Events with Jobs. When would each change your design?
> **Covered in:** [GitHub Actions — Events and filters](README.md#events-and-filters)

**Answer:** Events: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Jobs: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-03

- [ ] **Question:** Compare Jobs with Steps. When would each change your design?
> **Covered in:** [GitHub Actions — Steps, shells and workflow commands](README.md#steps-shells-and-workflow-commands)

**Answer:** Jobs: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Steps: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Steps with Actions. When would each change your design?
> **Covered in:** [GitHub Actions — Steps, shells and workflow commands](README.md#steps-shells-and-workflow-commands)

**Answer:** Steps: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Actions: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-05

- [ ] **Question:** Compare Actions with Runners. When would each change your design?
> **Covered in:** [GitHub Actions — Runners and isolation](README.md#runners-and-isolation)

**Answer:** Actions: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Runners: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-06

- [ ] **Question:** Compare Runners with Matrices. When would each change your design?
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** Runners: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Matrices: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Matrices with Reusable workflows. When would each change your design?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Matrices: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Reusable workflows: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-08

- [ ] **Question:** Compare Reusable workflows with Environments. When would each change your design?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Reusable workflows: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Environments: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-09

- [ ] **Question:** Compare Environments with Secrets. When would each change your design?
> **Covered in:** [GitHub Actions — Contexts, expressions, variables and secrets](README.md#contexts-expressions-variables-and-secrets)

**Answer:** Environments: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Secrets: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GITHUB-ACTIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Secrets with Workflows. When would each change your design?
> **Covered in:** [GitHub Actions — Contexts, expressions, variables and secrets](README.md#contexts-expressions-variables-and-secrets)

**Answer:** Secrets: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Workflows: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### GITHUB-ACTIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Workflows; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-02

- [ ] **Question:** Production is degraded around Events; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — Events and filters](README.md#events-and-filters)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Jobs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-04

- [ ] **Question:** Production is degraded around Steps; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — Steps, shells and workflow commands](README.md#steps-shells-and-workflow-commands)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Actions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — CLI, debugging and operations](README.md#cli-debugging-and-operations)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-06

- [ ] **Question:** Production is degraded around Runners; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — Runners and isolation](README.md#runners-and-isolation)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Matrices; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `pulumi preview --diff` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-08

- [ ] **Question:** Production is degraded around Reusable workflows; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Environments; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — CLI, debugging and operations](README.md#cli-debugging-and-operations)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform fmt -check -recursive` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GITHUB-ACTIONS-MP-10

- [ ] **Question:** Production is degraded around Secrets; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GitHub Actions — Contexts, expressions, variables and secrets](README.md#contexts-expressions-variables-and-secrets)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform validate; terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### GITHUB-ACTIONS-SN-01

- [ ] **Question:** Design a production GitHub Actions capability where Workflows, Steps and Matrices are first-class requirements.
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GitHub Actions capability where Events, Actions and Reusable workflows are first-class requirements.
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-03

- [ ] **Question:** Design a production GitHub Actions capability where Jobs, Runners and Environments are first-class requirements.
> **Covered in:** [GitHub Actions — Runners and isolation](README.md#runners-and-isolation)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GitHub Actions capability where Steps, Matrices and Secrets are first-class requirements.
> **Covered in:** [GitHub Actions — Contexts, expressions, variables and secrets](README.md#contexts-expressions-variables-and-secrets)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-05

- [ ] **Question:** Design a production GitHub Actions capability where Actions, Reusable workflows and Workflows are first-class requirements.
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GitHub Actions capability where Runners, Environments and Events are first-class requirements.
> **Covered in:** [GitHub Actions — Events and filters](README.md#events-and-filters)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-07

- [ ] **Question:** Design a production GitHub Actions capability where Matrices, Secrets and Jobs are first-class requirements.
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GitHub Actions capability where Reusable workflows, Workflows and Steps are first-class requirements.
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-09

- [ ] **Question:** Design a production GitHub Actions capability where Environments, Events and Actions are first-class requirements.
> **Covered in:** [GitHub Actions — Events and filters](README.md#events-and-filters)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GITHUB-ACTIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GitHub Actions capability where Secrets, Jobs and Runners are first-class requirements.
> **Covered in:** [GitHub Actions — Contexts, expressions, variables and secrets](README.md#contexts-expressions-variables-and-secrets)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### GITHUB-ACTIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workflows. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Hands-on lab: beginner → senior](README.md#hands-on-lab-beginner-senior)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Events. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Events and filters](README.md#events-and-filters)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Jobs. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Steps. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Steps, shells and workflow commands](README.md#steps-shells-and-workflow-commands)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Actions. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Runners. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Runners and isolation](README.md#runners-and-isolation)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Matrices. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Jobs, dependencies and matrices](README.md#jobs-dependencies-and-matrices)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `pulumi preview --diff` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reusable workflows. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Reusable workflows, composite actions and custom actions](README.md#reusable-workflows-composite-actions-and-custom-actions)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Environments. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Hands-on lab: beginner → senior](README.md#hands-on-lab-beginner-senior)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform fmt -check -recursive` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GITHUB-ACTIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secrets. How do you lead it end to end?
> **Covered in:** [GitHub Actions — Contexts, expressions, variables and secrets](README.md#contexts-expressions-variables-and-secrets)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform validate; terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of GitHub Actions; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: CD fundamentals](../02-cd-fundamentals/README.md) · [Study note](README.md) · [Next: GitLab CI →](../04-gitlab-ci/README.md)

<!-- reading-navigation:end -->
