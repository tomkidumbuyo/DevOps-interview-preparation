# GCP foundations and governance — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-01

- [ ] **Question:** What is Organizations, and why does it matter in GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-02

- [ ] **Question:** What is Folders, and why does it matter in GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-03

- [ ] **Question:** What is Projects, and why does it matter in GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-04

- [ ] **Question:** What is Billing accounts, and why does it matter in GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-05

- [ ] **Question:** What is Resource hierarchy, and why does it matter in GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-06

- [ ] **Question:** What is IAM principals, and why does it matter in GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-07

- [ ] **Question:** What is Roles, and why does it matter in GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-08

- [ ] **Code:** **Question:** What does `gcloud logging read 'severity>=ERROR' --limit=20` help you verify for GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-09

- [ ] **Code:** **Question:** What does `gcloud auth list` help you verify for GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JN-10

- [ ] **Code:** **Question:** What does `gcloud config list` help you verify for GCP foundations and governance?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-01

- [ ] **Code:** **Question:** A basic Organizations check fails. What would you do first using the CLI?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-02

- [ ] **Question:** A basic Folders check fails. What would you do first?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-03

- [ ] **Question:** A basic Projects check fails. What would you do first?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-04

- [ ] **Code:** **Question:** A basic Billing accounts check fails. What would you do first using the CLI?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-05

- [ ] **Question:** A basic Resource hierarchy check fails. What would you do first?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-06

- [ ] **Question:** A basic IAM principals check fails. What would you do first?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-07

- [ ] **Code:** **Question:** A basic Roles check fails. What would you do first using the CLI?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-08

- [ ] **Question:** A basic Service accounts check fails. What would you do first?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-09

- [ ] **Question:** A basic Workload Identity Federation check fails. What would you do first?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-JP-10

- [ ] **Code:** **Question:** A basic Organization policies check fails. What would you do first using the CLI?
> **Covered in:** [GCP foundations and governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-01

- [ ] **Question:** Compare Organizations with Folders. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Organizations: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Folders: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-02

- [ ] **Question:** Compare Folders with Projects. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Folders: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Projects: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-03

- [ ] **Question:** Compare Projects with Billing accounts. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Projects: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Billing accounts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-04

- [ ] **Configuration review:** **Question:** Compare Billing accounts with Resource hierarchy. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Billing accounts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Resource hierarchy: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-05

- [ ] **Question:** Compare Resource hierarchy with IAM principals. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Resource hierarchy: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. IAM principals: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-06

- [ ] **Question:** Compare IAM principals with Roles. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** IAM principals: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Roles: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-07

- [ ] **Configuration review:** **Question:** Compare Roles with Service accounts. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Roles: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Service accounts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-08

- [ ] **Question:** Compare Service accounts with Workload Identity Federation. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Service accounts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Workload Identity Federation: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-09

- [ ] **Question:** Compare Workload Identity Federation with Organization policies. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Workload Identity Federation: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Organization policies: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MN-10

- [ ] **Configuration review:** **Question:** Compare Organization policies with Organizations. When would each change your design?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Organization policies: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Organizations: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Organizations; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-02

- [ ] **Question:** Production is degraded around Folders; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Projects; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-04

- [ ] **Question:** Production is degraded around Billing accounts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Resource hierarchy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-06

- [ ] **Question:** Production is degraded around IAM principals; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Roles; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-08

- [ ] **Question:** Production is degraded around Service accounts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Workload Identity Federation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-MP-10

- [ ] **Question:** Production is degraded around Organization policies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-01

- [ ] **Question:** Design a production GCP foundations and governance capability where Organizations, Billing accounts and Roles are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GCP foundations and governance capability where Folders, Resource hierarchy and Service accounts are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-03

- [ ] **Question:** Design a production GCP foundations and governance capability where Projects, IAM principals and Workload Identity Federation are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GCP foundations and governance capability where Billing accounts, Roles and Organization policies are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-05

- [ ] **Question:** Design a production GCP foundations and governance capability where Resource hierarchy, Service accounts and Organizations are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GCP foundations and governance capability where IAM principals, Workload Identity Federation and Folders are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-07

- [ ] **Question:** Design a production GCP foundations and governance capability where Roles, Organization policies and Projects are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GCP foundations and governance capability where Service accounts, Organizations and Billing accounts are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-09

- [ ] **Question:** Design a production GCP foundations and governance capability where Workload Identity Federation, Folders and Resource hierarchy are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GCP foundations and governance capability where Organization policies, Projects and IAM principals are first-class requirements.
> **Covered in:** [GCP foundations and governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Organizations. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Folders. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Projects. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Billing accounts. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource hierarchy. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IAM principals. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Roles. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service accounts. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workload Identity Federation. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-FOUNDATIONS-AND-GOVERNANCE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Organization policies. How do you lead it end to end?
> **Covered in:** [GCP foundations and governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP foundations and governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Google Cloud Platform](../README.md) · [Study note](README.md) · [Next: GCP networking →](../02-gcp-networking/README.md)

<!-- reading-navigation:end -->
