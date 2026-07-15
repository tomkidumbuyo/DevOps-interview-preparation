# On-premises deployment — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-01

- [ ] **Question:** What is Bare-metal Kubernetes, and why does it matter in On-premises deployment?
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-02

- [ ] **Question:** What is Virtualized Kubernetes, and why does it matter in On-premises deployment?
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-03

- [ ] **Question:** What is Air-gapped installation, and why does it matter in On-premises deployment?
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-04

- [ ] **Question:** What is Private image registries, and why does it matter in On-premises deployment?
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-05

- [ ] **Question:** What is Offline artifact bundles, and why does it matter in On-premises deployment?
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-06

- [ ] **Question:** What is GPU driver management, and why does it matter in On-premises deployment?
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-07

- [ ] **Question:** What is Hardware compatibility, and why does it matter in On-premises deployment?
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for On-premises deployment?
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for On-premises deployment?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-ON-PREMISES-DEPLOYMENT-JN-10

- [ ] **Code:** **Question:** What does `go test ./...` help you verify for On-premises deployment?
> **Covered in:** [On-premises deployment — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-01

- [ ] **Code:** **Question:** A basic Bare-metal Kubernetes check fails. What would you do first using the CLI?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-02

- [ ] **Question:** A basic Virtualized Kubernetes check fails. What would you do first?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-03

- [ ] **Question:** A basic Air-gapped installation check fails. What would you do first?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-04

- [ ] **Code:** **Question:** A basic Private image registries check fails. What would you do first using the CLI?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-05

- [ ] **Question:** A basic Offline artifact bundles check fails. What would you do first?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-06

- [ ] **Question:** A basic GPU driver management check fails. What would you do first?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-07

- [ ] **Code:** **Question:** A basic Hardware compatibility check fails. What would you do first using the CLI?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-08

- [ ] **Question:** A basic Storage integration check fails. What would you do first?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-09

- [ ] **Question:** A basic Network integration check fails. What would you do first?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ON-PREMISES-DEPLOYMENT-JP-10

- [ ] **Code:** **Question:** A basic Load-balancer integration check fails. What would you do first using the CLI?
> **Covered in:** [On-premises deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-01

- [ ] **Question:** Compare Bare-metal Kubernetes with Virtualized Kubernetes. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Bare-metal Kubernetes: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Virtualized Kubernetes: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-02

- [ ] **Question:** Compare Virtualized Kubernetes with Air-gapped installation. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Virtualized Kubernetes: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Air-gapped installation: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-03

- [ ] **Question:** Compare Air-gapped installation with Private image registries. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Air-gapped installation: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Private image registries: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-04

- [ ] **Configuration review:** **Question:** Compare Private image registries with Offline artifact bundles. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Private image registries: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Offline artifact bundles: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-05

- [ ] **Question:** Compare Offline artifact bundles with GPU driver management. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Offline artifact bundles: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. GPU driver management: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-06

- [ ] **Question:** Compare GPU driver management with Hardware compatibility. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** GPU driver management: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Hardware compatibility: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-07

- [ ] **Configuration review:** **Question:** Compare Hardware compatibility with Storage integration. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Hardware compatibility: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Storage integration: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-08

- [ ] **Question:** Compare Storage integration with Network integration. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Storage integration: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Network integration: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-09

- [ ] **Question:** Compare Network integration with Load-balancer integration. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Network integration: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Load-balancer integration: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ON-PREMISES-DEPLOYMENT-MN-10

- [ ] **Configuration review:** **Question:** Compare Load-balancer integration with Bare-metal Kubernetes. When would each change your design?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Load-balancer integration: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Bare-metal Kubernetes: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Bare-metal Kubernetes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-02

- [ ] **Question:** Production is degraded around Virtualized Kubernetes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Air-gapped installation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-04

- [ ] **Question:** Production is degraded around Private image registries; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Offline artifact bundles; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-06

- [ ] **Question:** Production is degraded around GPU driver management; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Hardware compatibility; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-08

- [ ] **Question:** Production is degraded around Storage integration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Network integration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ON-PREMISES-DEPLOYMENT-MP-10

- [ ] **Question:** Production is degraded around Load-balancer integration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-01

- [ ] **Question:** Design a production On-premises deployment capability where Bare-metal Kubernetes, Private image registries and Hardware compatibility are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production On-premises deployment capability where Virtualized Kubernetes, Offline artifact bundles and Storage integration are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-03

- [ ] **Question:** Design a production On-premises deployment capability where Air-gapped installation, GPU driver management and Network integration are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production On-premises deployment capability where Private image registries, Hardware compatibility and Load-balancer integration are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-05

- [ ] **Question:** Design a production On-premises deployment capability where Offline artifact bundles, Storage integration and Bare-metal Kubernetes are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production On-premises deployment capability where GPU driver management, Network integration and Virtualized Kubernetes are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-07

- [ ] **Question:** Design a production On-premises deployment capability where Hardware compatibility, Load-balancer integration and Air-gapped installation are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production On-premises deployment capability where Storage integration, Bare-metal Kubernetes and Private image registries are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-09

- [ ] **Question:** Design a production On-premises deployment capability where Network integration, Virtualized Kubernetes and Offline artifact bundles are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ON-PREMISES-DEPLOYMENT-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production On-premises deployment capability where Load-balancer integration, Air-gapped installation and GPU driver management are first-class requirements.
> **Covered in:** [On-premises deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Bare-metal Kubernetes. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Virtualized Kubernetes. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Air-gapped installation. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Private image registries. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Offline artifact bundles. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU driver management. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hardware compatibility. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Storage integration. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network integration. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ON-PREMISES-DEPLOYMENT-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Load-balancer integration. How do you lead it end to end?
> **Covered in:** [On-premises deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of On-premises deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Customer private-cloud deployment](../04-customer-private-cloud-deployment/README.md) · [Study note](README.md) · [Next: Hybrid-cloud deployment →](../06-hybrid-cloud-deployment/README.md)

<!-- reading-navigation:end -->
