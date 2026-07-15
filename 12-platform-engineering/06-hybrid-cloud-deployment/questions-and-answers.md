# Hybrid-cloud deployment — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-01

- [ ] **Question:** What is Cloud control plane with on-prem data plane, and why does it matter in Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-02

- [ ] **Question:** What is On-prem control plane with cloud bursting, and why does it matter in Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-03

- [ ] **Question:** What is Hybrid identity, and why does it matter in Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-04

- [ ] **Question:** What is Hybrid networking, and why does it matter in Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-05

- [ ] **Question:** What is VPN and private connectivity, and why does it matter in Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-06

- [ ] **Question:** What is Artifact synchronization, and why does it matter in Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-07

- [ ] **Question:** What is Data synchronization, and why does it matter in Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JN-10

- [ ] **Code:** **Question:** What does `go test ./...` help you verify for Hybrid-cloud deployment?
> **Covered in:** [Hybrid-cloud deployment — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery.

## Junior — procedural and command questions

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-01

- [ ] **Code:** **Question:** A basic Cloud control plane with on-prem data plane check fails. What would you do first using the CLI?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-02

- [ ] **Question:** A basic On-prem control plane with cloud bursting check fails. What would you do first?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-03

- [ ] **Question:** A basic Hybrid identity check fails. What would you do first?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-04

- [ ] **Code:** **Question:** A basic Hybrid networking check fails. What would you do first using the CLI?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-05

- [ ] **Question:** A basic VPN and private connectivity check fails. What would you do first?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-06

- [ ] **Question:** A basic Artifact synchronization check fails. What would you do first?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-07

- [ ] **Code:** **Question:** A basic Data synchronization check fails. What would you do first using the CLI?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-08

- [ ] **Question:** A basic Model synchronization check fails. What would you do first?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-09

- [ ] **Question:** A basic Central governance check fails. What would you do first?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-JP-10

- [ ] **Code:** **Question:** A basic Local policy enforcement check fails. What would you do first using the CLI?
> **Covered in:** [Hybrid-cloud deployment — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-01

- [ ] **Question:** Compare Cloud control plane with on-prem data plane with On-prem control plane with cloud bursting. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Cloud control plane with on-prem data plane: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. On-prem control plane with cloud bursting: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-02

- [ ] **Question:** Compare On-prem control plane with cloud bursting with Hybrid identity. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** On-prem control plane with cloud bursting: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Hybrid identity: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-03

- [ ] **Question:** Compare Hybrid identity with Hybrid networking. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Hybrid identity: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Hybrid networking: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-04

- [ ] **Configuration review:** **Question:** Compare Hybrid networking with VPN and private connectivity. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Hybrid networking: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. VPN and private connectivity: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-05

- [ ] **Question:** Compare VPN and private connectivity with Artifact synchronization. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** VPN and private connectivity: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Artifact synchronization: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-06

- [ ] **Question:** Compare Artifact synchronization with Data synchronization. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Artifact synchronization: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Data synchronization: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-07

- [ ] **Configuration review:** **Question:** Compare Data synchronization with Model synchronization. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Data synchronization: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model synchronization: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-08

- [ ] **Question:** Compare Model synchronization with Central governance. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model synchronization: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Central governance: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-09

- [ ] **Question:** Compare Central governance with Local policy enforcement. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Central governance: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Local policy enforcement: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MN-10

- [ ] **Configuration review:** **Question:** Compare Local policy enforcement with Cloud control plane with on-prem data plane. When would each change your design?
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Local policy enforcement: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Cloud control plane with on-prem data plane: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cloud control plane with on-prem data plane; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-02

- [ ] **Question:** Production is degraded around On-prem control plane with cloud bursting; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Hybrid identity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-04

- [ ] **Question:** Production is degraded around Hybrid networking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPN and private connectivity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-06

- [ ] **Question:** Production is degraded around Artifact synchronization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Data synchronization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-08

- [ ] **Question:** Production is degraded around Model synchronization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Central governance; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-MP-10

- [ ] **Question:** Production is degraded around Local policy enforcement; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-01

- [ ] **Question:** Design a production Hybrid-cloud deployment capability where Cloud control plane with on-prem data plane, Hybrid networking and Data synchronization are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Hybrid-cloud deployment capability where On-prem control plane with cloud bursting, VPN and private connectivity and Model synchronization are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-03

- [ ] **Question:** Design a production Hybrid-cloud deployment capability where Hybrid identity, Artifact synchronization and Central governance are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Hybrid-cloud deployment capability where Hybrid networking, Data synchronization and Local policy enforcement are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-05

- [ ] **Question:** Design a production Hybrid-cloud deployment capability where VPN and private connectivity, Model synchronization and Cloud control plane with on-prem data plane are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Hybrid-cloud deployment capability where Artifact synchronization, Central governance and On-prem control plane with cloud bursting are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-07

- [ ] **Question:** Design a production Hybrid-cloud deployment capability where Data synchronization, Local policy enforcement and Hybrid identity are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Hybrid-cloud deployment capability where Model synchronization, Cloud control plane with on-prem data plane and Hybrid networking are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-09

- [ ] **Question:** Design a production Hybrid-cloud deployment capability where Central governance, On-prem control plane with cloud bursting and VPN and private connectivity are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Hybrid-cloud deployment capability where Local policy enforcement, Hybrid identity and Artifact synchronization are first-class requirements.
> **Covered in:** [Hybrid-cloud deployment — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cloud control plane with on-prem data plane. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving On-prem control plane with cloud bursting. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hybrid identity. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hybrid networking. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPN and private connectivity. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Artifact synchronization. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data synchronization. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model synchronization. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Central governance. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Hybrid-cloud deployment; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-HYBRID-CLOUD-DEPLOYMENT-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Local policy enforcement. How do you lead it end to end?
> **Covered in:** [Hybrid-cloud deployment — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: On-premises deployment](../05-on-premises-deployment/README.md) · [Study note](README.md) · [Next: Air-gapped and restricted environments →](../07-air-gapped-and-restricted-environments/README.md)

<!-- reading-navigation:end -->
