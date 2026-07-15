# Air-gapped and restricted environments — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-01

- [ ] **Question:** What is Offline installation media, and why does it matter in Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-02

- [ ] **Question:** What is Dependency mirroring, and why does it matter in Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-03

- [ ] **Question:** What is OCI registry mirroring, and why does it matter in Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-04

- [ ] **Question:** What is Package repositories, and why does it matter in Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-05

- [ ] **Question:** What is Model repositories, and why does it matter in Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-06

- [ ] **Question:** What is Vulnerability-database updates, and why does it matter in Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-07

- [ ] **Question:** What is License validation, and why does it matter in Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JN-10

- [ ] **Code:** **Question:** What does `go test ./...` help you verify for Air-gapped and restricted environments?
> **Covered in:** [Air-gapped and restricted environments — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion.

## Junior — procedural and command questions

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-01

- [ ] **Code:** **Question:** A basic Offline installation media check fails. What would you do first using the CLI?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-02

- [ ] **Question:** A basic Dependency mirroring check fails. What would you do first?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-03

- [ ] **Question:** A basic OCI registry mirroring check fails. What would you do first?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-04

- [ ] **Code:** **Question:** A basic Package repositories check fails. What would you do first using the CLI?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-05

- [ ] **Question:** A basic Model repositories check fails. What would you do first?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-06

- [ ] **Question:** A basic Vulnerability-database updates check fails. What would you do first?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-07

- [ ] **Code:** **Question:** A basic License validation check fails. What would you do first using the CLI?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-08

- [ ] **Question:** A basic Certificate rotation check fails. What would you do first?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-09

- [ ] **Question:** A basic Secret rotation check fails. What would you do first?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-JP-10

- [ ] **Code:** **Question:** A basic Offline upgrades check fails. What would you do first using the CLI?
> **Covered in:** [Air-gapped and restricted environments — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-01

- [ ] **Question:** Compare Offline installation media with Dependency mirroring. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Offline installation media: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dependency mirroring: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-02

- [ ] **Question:** Compare Dependency mirroring with OCI registry mirroring. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Dependency mirroring: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. OCI registry mirroring: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-03

- [ ] **Question:** Compare OCI registry mirroring with Package repositories. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** OCI registry mirroring: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Package repositories: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-04

- [ ] **Configuration review:** **Question:** Compare Package repositories with Model repositories. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Package repositories: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model repositories: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-05

- [ ] **Question:** Compare Model repositories with Vulnerability-database updates. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model repositories: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Vulnerability-database updates: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-06

- [ ] **Question:** Compare Vulnerability-database updates with License validation. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Vulnerability-database updates: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. License validation: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-07

- [ ] **Configuration review:** **Question:** Compare License validation with Certificate rotation. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** License validation: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Certificate rotation: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-08

- [ ] **Question:** Compare Certificate rotation with Secret rotation. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Certificate rotation: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Secret rotation: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-09

- [ ] **Question:** Compare Secret rotation with Offline upgrades. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Secret rotation: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Offline upgrades: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MN-10

- [ ] **Configuration review:** **Question:** Compare Offline upgrades with Offline installation media. When would each change your design?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Offline upgrades: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Offline installation media: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Offline installation media; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-02

- [ ] **Question:** Production is degraded around Dependency mirroring; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around OCI registry mirroring; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-04

- [ ] **Question:** Production is degraded around Package repositories; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model repositories; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-06

- [ ] **Question:** Production is degraded around Vulnerability-database updates; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around License validation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-08

- [ ] **Question:** Production is degraded around Certificate rotation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Secret rotation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-MP-10

- [ ] **Question:** Production is degraded around Offline upgrades; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-01

- [ ] **Question:** Design a production Air-gapped and restricted environments capability where Offline installation media, Package repositories and License validation are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Air-gapped and restricted environments capability where Dependency mirroring, Model repositories and Certificate rotation are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-03

- [ ] **Question:** Design a production Air-gapped and restricted environments capability where OCI registry mirroring, Vulnerability-database updates and Secret rotation are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Air-gapped and restricted environments capability where Package repositories, License validation and Offline upgrades are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-05

- [ ] **Question:** Design a production Air-gapped and restricted environments capability where Model repositories, Certificate rotation and Offline installation media are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Air-gapped and restricted environments capability where Vulnerability-database updates, Secret rotation and Dependency mirroring are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-07

- [ ] **Question:** Design a production Air-gapped and restricted environments capability where License validation, Offline upgrades and OCI registry mirroring are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Air-gapped and restricted environments capability where Certificate rotation, Offline installation media and Package repositories are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-09

- [ ] **Question:** Design a production Air-gapped and restricted environments capability where Secret rotation, Dependency mirroring and Model repositories are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Air-gapped and restricted environments capability where Offline upgrades, OCI registry mirroring and Vulnerability-database updates are first-class requirements.
> **Covered in:** [Air-gapped and restricted environments — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Offline installation media. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dependency mirroring. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OCI registry mirroring. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Package repositories. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model repositories. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Vulnerability-database updates. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving License validation. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Certificate rotation. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret rotation. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Air-gapped and restricted environments; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AIR-GAPPED-AND-RESTRICTED-ENVIRONMENTS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Offline upgrades. How do you lead it end to end?
> **Covered in:** [Air-gapped and restricted environments — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Hybrid-cloud deployment](../06-hybrid-cloud-deployment/README.md) · [Study note](README.md) · [Next: Internal developer platform for AI →](../08-internal-developer-platform-for-ai/README.md)

<!-- reading-navigation:end -->
