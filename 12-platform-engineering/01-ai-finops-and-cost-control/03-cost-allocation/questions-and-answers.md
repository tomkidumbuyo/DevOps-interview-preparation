# Cost allocation — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### COST-ALLOCATION-JN-01

- [ ] **Question:** What is Tags, and why does it matter in Cost allocation?
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-ALLOCATION-JN-02

- [ ] **Question:** What is Labels, and why does it matter in Cost allocation?
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-ALLOCATION-JN-03

- [ ] **Question:** What is Tenant IDs, and why does it matter in Cost allocation?
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-ALLOCATION-JN-04

- [ ] **Question:** What is Project IDs, and why does it matter in Cost allocation?
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-ALLOCATION-JN-05

- [ ] **Question:** What is Model IDs, and why does it matter in Cost allocation?
> **Covered in:** [Cost allocation — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-ALLOCATION-JN-06

- [ ] **Question:** What is Gateway metering, and why does it matter in Cost allocation?
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-ALLOCATION-JN-07

- [ ] **Question:** What is Chargeback, and why does it matter in Cost allocation?
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-ALLOCATION-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Cost allocation?
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### COST-ALLOCATION-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Cost allocation?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### COST-ALLOCATION-JN-10

- [ ] **Code:** **Question:** What does `go test ./...` help you verify for Cost allocation?
> **Covered in:** [Cost allocation — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### COST-ALLOCATION-JP-01

- [ ] **Code:** **Question:** A basic Tags check fails. What would you do first using the CLI?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-02

- [ ] **Question:** A basic Labels check fails. What would you do first?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-03

- [ ] **Question:** A basic Tenant IDs check fails. What would you do first?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-04

- [ ] **Code:** **Question:** A basic Project IDs check fails. What would you do first using the CLI?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-05

- [ ] **Question:** A basic Model IDs check fails. What would you do first?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-06

- [ ] **Question:** A basic Gateway metering check fails. What would you do first?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-07

- [ ] **Code:** **Question:** A basic Chargeback check fails. What would you do first using the CLI?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-08

- [ ] **Question:** A basic Showback check fails. What would you do first?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-09

- [ ] **Question:** A basic Tags check fails. What would you do first?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-ALLOCATION-JP-10

- [ ] **Code:** **Question:** A basic Labels check fails. What would you do first using the CLI?
> **Covered in:** [Cost allocation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### COST-ALLOCATION-MN-01

- [ ] **Question:** Compare Tags with Labels. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Tags: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Labels: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-02

- [ ] **Question:** Compare Labels with Tenant IDs. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Labels: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Tenant IDs: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-03

- [ ] **Question:** Compare Tenant IDs with Project IDs. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Tenant IDs: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Project IDs: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-04

- [ ] **Configuration review:** **Question:** Compare Project IDs with Model IDs. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Project IDs: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model IDs: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-05

- [ ] **Question:** Compare Model IDs with Gateway metering. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model IDs: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Gateway metering: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-06

- [ ] **Question:** Compare Gateway metering with Chargeback. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Gateway metering: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Chargeback: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-07

- [ ] **Configuration review:** **Question:** Compare Chargeback with Showback. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Chargeback: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Showback: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-08

- [ ] **Question:** Compare Showback with Tags. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Showback: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Tags: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-09

- [ ] **Question:** Compare Tags with Labels. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Tags: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Labels: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-ALLOCATION-MN-10

- [ ] **Configuration review:** **Question:** Compare Labels with Tags. When would each change your design?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Labels: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Tags: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### COST-ALLOCATION-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Tags; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-02

- [ ] **Question:** Production is degraded around Labels; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Tenant IDs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-04

- [ ] **Question:** Production is degraded around Project IDs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model IDs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-06

- [ ] **Question:** Production is degraded around Gateway metering; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Chargeback; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-08

- [ ] **Question:** Production is degraded around Showback; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Tags; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-ALLOCATION-MP-10

- [ ] **Question:** Production is degraded around Labels; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### COST-ALLOCATION-SN-01

- [ ] **Question:** Design a production Cost allocation capability where Tags, Project IDs and Chargeback are first-class requirements.
> **Covered in:** [Cost allocation — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Cost allocation capability where Labels, Model IDs and Showback are first-class requirements.
> **Covered in:** [Cost allocation — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-03

- [ ] **Question:** Design a production Cost allocation capability where Tenant IDs, Gateway metering and Tags are first-class requirements.
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Cost allocation capability where Project IDs, Chargeback and Labels are first-class requirements.
> **Covered in:** [Cost allocation — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-05

- [ ] **Question:** Design a production Cost allocation capability where Model IDs, Showback and Tags are first-class requirements.
> **Covered in:** [Cost allocation — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Cost allocation capability where Gateway metering, Tags and Labels are first-class requirements.
> **Covered in:** [Cost allocation — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-07

- [ ] **Question:** Design a production Cost allocation capability where Chargeback, Labels and Tenant IDs are first-class requirements.
> **Covered in:** [Cost allocation — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Cost allocation capability where Showback, Tags and Project IDs are first-class requirements.
> **Covered in:** [Cost allocation — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-09

- [ ] **Question:** Design a production Cost allocation capability where Tags, Labels and Model IDs are first-class requirements.
> **Covered in:** [Cost allocation — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-ALLOCATION-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Cost allocation capability where Labels, Tenant IDs and Gateway metering are first-class requirements.
> **Covered in:** [Cost allocation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### COST-ALLOCATION-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tags. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Labels. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tenant IDs. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Project IDs. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model IDs. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Gateway metering. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Chargeback. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Showback. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tags. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-ALLOCATION-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Labels. How do you lead it end to end?
> **Covered in:** [Cost allocation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Cost allocation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Inference unit economics](../02-inference-unit-economics/README.md) · [Study note](README.md) · [Next: Cost optimization →](../04-cost-optimization/README.md)

<!-- reading-navigation:end -->
