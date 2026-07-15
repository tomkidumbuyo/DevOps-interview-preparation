# Customer private-cloud deployment — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-01

- [ ] **Question:** What is Customer-owned cloud account, and why does it matter in Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-02

- [ ] **Question:** What is Vendor-managed deployment, and why does it matter in Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-03

- [ ] **Question:** What is Customer-managed deployment, and why does it matter in Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-04

- [ ] **Question:** What is Cross-account access, and why does it matter in Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-05

- [ ] **Question:** What is Private networking, and why does it matter in Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-06

- [ ] **Question:** What is Private registries, and why does it matter in Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-07

- [ ] **Question:** What is Customer KMS, and why does it matter in Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JN-10

- [ ] **Code:** **Question:** What does `go test ./...` help you verify for Customer private-cloud deployment?
> **Covered in:** [Customer private-cloud deployment — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion.

## Junior — procedural and command questions

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-01

- [ ] **Code:** **Question:** A basic Customer-owned cloud account check fails. What would you do first using the CLI?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-02

- [ ] **Question:** A basic Vendor-managed deployment check fails. What would you do first?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-03

- [ ] **Question:** A basic Customer-managed deployment check fails. What would you do first?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-04

- [ ] **Code:** **Question:** A basic Cross-account access check fails. What would you do first using the CLI?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-05

- [ ] **Question:** A basic Private networking check fails. What would you do first?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-06

- [ ] **Question:** A basic Private registries check fails. What would you do first?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-07

- [ ] **Code:** **Question:** A basic Customer KMS check fails. What would you do first using the CLI?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-08

- [ ] **Question:** A basic Restricted egress check fails. What would you do first?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-09

- [ ] **Question:** A basic Installation packaging check fails. What would you do first?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-JP-10

- [ ] **Code:** **Question:** A basic Upgrade channels check fails. What would you do first using the CLI?
> **Covered in:** [Customer private-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-01

- [ ] **Question:** Compare Customer-owned cloud account with Vendor-managed deployment. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Customer-owned cloud account: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Vendor-managed deployment: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-02

- [ ] **Question:** Compare Vendor-managed deployment with Customer-managed deployment. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Vendor-managed deployment: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Customer-managed deployment: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-03

- [ ] **Question:** Compare Customer-managed deployment with Cross-account access. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Customer-managed deployment: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Cross-account access: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-04

- [ ] **Configuration review:** **Question:** Compare Cross-account access with Private networking. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Cross-account access: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Private networking: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-05

- [ ] **Question:** Compare Private networking with Private registries. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Private networking: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Private registries: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-06

- [ ] **Question:** Compare Private registries with Customer KMS. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Private registries: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Customer KMS: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-07

- [ ] **Configuration review:** **Question:** Compare Customer KMS with Restricted egress. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Customer KMS: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Restricted egress: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-08

- [ ] **Question:** Compare Restricted egress with Installation packaging. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Restricted egress: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Installation packaging: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-09

- [ ] **Question:** Compare Installation packaging with Upgrade channels. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Installation packaging: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Upgrade channels: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MN-10

- [ ] **Configuration review:** **Question:** Compare Upgrade channels with Customer-owned cloud account. When would each change your design?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Upgrade channels: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Customer-owned cloud account: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Customer-owned cloud account; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-02

- [ ] **Question:** Production is degraded around Vendor-managed deployment; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Customer-managed deployment; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-04

- [ ] **Question:** Production is degraded around Cross-account access; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Private networking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-06

- [ ] **Question:** Production is degraded around Private registries; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Customer KMS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-08

- [ ] **Question:** Production is degraded around Restricted egress; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Installation packaging; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-MP-10

- [ ] **Question:** Production is degraded around Upgrade channels; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-01

- [ ] **Question:** Design a production Customer private-cloud deployment capability where Customer-owned cloud account, Cross-account access and Customer KMS are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Customer private-cloud deployment capability where Vendor-managed deployment, Private networking and Restricted egress are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-03

- [ ] **Question:** Design a production Customer private-cloud deployment capability where Customer-managed deployment, Private registries and Installation packaging are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Customer private-cloud deployment capability where Cross-account access, Customer KMS and Upgrade channels are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-05

- [ ] **Question:** Design a production Customer private-cloud deployment capability where Private networking, Restricted egress and Customer-owned cloud account are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Customer private-cloud deployment capability where Private registries, Installation packaging and Vendor-managed deployment are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-07

- [ ] **Question:** Design a production Customer private-cloud deployment capability where Customer KMS, Upgrade channels and Customer-managed deployment are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Customer private-cloud deployment capability where Restricted egress, Customer-owned cloud account and Cross-account access are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-09

- [ ] **Question:** Design a production Customer private-cloud deployment capability where Installation packaging, Vendor-managed deployment and Private networking are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Customer private-cloud deployment capability where Upgrade channels, Customer-managed deployment and Private registries are first-class requirements.
> **Covered in:** [Customer private-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Customer-owned cloud account. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Vendor-managed deployment. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Customer-managed deployment. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cross-account access. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Private networking. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Private registries. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Customer KMS. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restricted egress. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Installation packaging. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Customer private-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CUSTOMER-PRIVATE-CLOUD-DEPLOYMENT-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Upgrade channels. How do you lead it end to end?
> **Covered in:** [Customer private-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: SaaS deployment](../03-saas-deployment/README.md) · [Study note](README.md) · [Next: On-premises deployment →](../05-on-premises-deployment/README.md)

<!-- reading-navigation:end -->
