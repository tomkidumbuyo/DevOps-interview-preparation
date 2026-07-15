# Developer experience — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### DEVELOPER-EXPERIENCE-JN-01

- [ ] **Question:** What is Documentation, and why does it matter in Developer experience?
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEVELOPER-EXPERIENCE-JN-02

- [ ] **Question:** What is Examples, and why does it matter in Developer experience?
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEVELOPER-EXPERIENCE-JN-03

- [ ] **Question:** What is Quickstarts, and why does it matter in Developer experience?
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEVELOPER-EXPERIENCE-JN-04

- [ ] **Question:** What is Local development, and why does it matter in Developer experience?
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEVELOPER-EXPERIENCE-JN-05

- [ ] **Question:** What is Preview environments, and why does it matter in Developer experience?
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEVELOPER-EXPERIENCE-JN-06

- [ ] **Question:** What is Meaningful errors, and why does it matter in Developer experience?
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEVELOPER-EXPERIENCE-JN-07

- [ ] **Question:** What is Self-service troubleshooting, and why does it matter in Developer experience?
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DEVELOPER-EXPERIENCE-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Developer experience?
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### DEVELOPER-EXPERIENCE-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Developer experience?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### DEVELOPER-EXPERIENCE-JN-10

- [ ] **Code:** **Question:** What does `go test ./...` help you verify for Developer experience?
> **Covered in:** [Developer experience — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### DEVELOPER-EXPERIENCE-JP-01

- [ ] **Code:** **Question:** A basic Documentation check fails. What would you do first using the CLI?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-02

- [ ] **Question:** A basic Examples check fails. What would you do first?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-03

- [ ] **Question:** A basic Quickstarts check fails. What would you do first?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-04

- [ ] **Code:** **Question:** A basic Local development check fails. What would you do first using the CLI?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-05

- [ ] **Question:** A basic Preview environments check fails. What would you do first?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-06

- [ ] **Question:** A basic Meaningful errors check fails. What would you do first?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-07

- [ ] **Code:** **Question:** A basic Self-service troubleshooting check fails. What would you do first using the CLI?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-08

- [ ] **Question:** A basic Support channels check fails. What would you do first?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-09

- [ ] **Question:** A basic Documentation check fails. What would you do first?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DEVELOPER-EXPERIENCE-JP-10

- [ ] **Code:** **Question:** A basic Examples check fails. What would you do first using the CLI?
> **Covered in:** [Developer experience — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### DEVELOPER-EXPERIENCE-MN-01

- [ ] **Question:** Compare Documentation with Examples. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Documentation: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Examples: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-02

- [ ] **Question:** Compare Examples with Quickstarts. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Examples: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Quickstarts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-03

- [ ] **Question:** Compare Quickstarts with Local development. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Quickstarts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Local development: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-04

- [ ] **Configuration review:** **Question:** Compare Local development with Preview environments. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Local development: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Preview environments: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-05

- [ ] **Question:** Compare Preview environments with Meaningful errors. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Preview environments: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Meaningful errors: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-06

- [ ] **Question:** Compare Meaningful errors with Self-service troubleshooting. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Meaningful errors: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Self-service troubleshooting: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-07

- [ ] **Configuration review:** **Question:** Compare Self-service troubleshooting with Support channels. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Self-service troubleshooting: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Support channels: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-08

- [ ] **Question:** Compare Support channels with Documentation. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Support channels: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Documentation: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-09

- [ ] **Question:** Compare Documentation with Examples. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Documentation: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Examples: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DEVELOPER-EXPERIENCE-MN-10

- [ ] **Configuration review:** **Question:** Compare Examples with Documentation. When would each change your design?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Examples: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Documentation: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### DEVELOPER-EXPERIENCE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Documentation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-02

- [ ] **Question:** Production is degraded around Examples; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Quickstarts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-04

- [ ] **Question:** Production is degraded around Local development; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Preview environments; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-06

- [ ] **Question:** Production is degraded around Meaningful errors; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Self-service troubleshooting; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-08

- [ ] **Question:** Production is degraded around Support channels; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Documentation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DEVELOPER-EXPERIENCE-MP-10

- [ ] **Question:** Production is degraded around Examples; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### DEVELOPER-EXPERIENCE-SN-01

- [ ] **Question:** Design a production Developer experience capability where Documentation, Local development and Self-service troubleshooting are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Developer experience capability where Examples, Preview environments and Support channels are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-03

- [ ] **Question:** Design a production Developer experience capability where Quickstarts, Meaningful errors and Documentation are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Developer experience capability where Local development, Self-service troubleshooting and Examples are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-05

- [ ] **Question:** Design a production Developer experience capability where Preview environments, Support channels and Documentation are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Developer experience capability where Meaningful errors, Documentation and Examples are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-07

- [ ] **Question:** Design a production Developer experience capability where Self-service troubleshooting, Examples and Quickstarts are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Developer experience capability where Support channels, Documentation and Local development are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-09

- [ ] **Question:** Design a production Developer experience capability where Documentation, Examples and Preview environments are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DEVELOPER-EXPERIENCE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Developer experience capability where Examples, Quickstarts and Meaningful errors are first-class requirements.
> **Covered in:** [Developer experience — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### DEVELOPER-EXPERIENCE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Documentation. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Examples. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Quickstarts. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Local development. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Preview environments. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Meaningful errors. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Self-service troubleshooting. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Support channels. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Documentation. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DEVELOPER-EXPERIENCE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Examples. How do you lead it end to end?
> **Covered in:** [Developer experience — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Developer experience; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Platform reconciliation](../05-platform-reconciliation/README.md) · [Study note](README.md) · [Next: Platform product management →](../07-platform-product-management/README.md)

<!-- reading-navigation:end -->
