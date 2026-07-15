# Senior engineering expectations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### SENIOR-ENGINEERING-EXPECTATIONS-JN-01

- [ ] **Question:** What is Requirement discovery, and why does it matter in Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-02

- [ ] **Question:** What is Assumption identification, and why does it matter in Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-03

- [ ] **Question:** What is Architecture decision records, and why does it matter in Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-04

- [ ] **Question:** What is Build-versus-buy decisions, and why does it matter in Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-05

- [ ] **Question:** What is Technical strategy, and why does it matter in Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-06

- [ ] **Question:** What is Roadmap creation, and why does it matter in Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-07

- [ ] **Question:** What is Prioritizing reliability, security, speed and cost, and why does it matter in Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-08

- [ ] **Code:** **Question:** What does `git shortlog -sn` help you verify for Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-09

- [ ] **Code:** **Question:** What does `git log --since='30 days ago' --stat` help you verify for Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### SENIOR-ENGINEERING-EXPECTATIONS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get events -A --sort-by=.lastTimestamp` help you verify for Senior engineering expectations?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### SENIOR-ENGINEERING-EXPECTATIONS-JP-01

- [ ] **Code:** **Question:** A basic Requirement discovery check fails. What would you do first using the CLI?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-02

- [ ] **Question:** A basic Assumption identification check fails. What would you do first?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-03

- [ ] **Question:** A basic Architecture decision records check fails. What would you do first?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-04

- [ ] **Code:** **Question:** A basic Build-versus-buy decisions check fails. What would you do first using the CLI?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git shortlog -sn` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-05

- [ ] **Question:** A basic Technical strategy check fails. What would you do first?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-06

- [ ] **Question:** A basic Roadmap creation check fails. What would you do first?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-07

- [ ] **Code:** **Question:** A basic Prioritizing reliability, security, speed and cost check fails. What would you do first using the CLI?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-08

- [ ] **Question:** A basic Managing technical debt check fails. What would you do first?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git shortlog -sn` and capture exact status/reason/request ID. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-09

- [ ] **Question:** A basic Creating operational standards and guardrails check fails. What would you do first?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SENIOR-ENGINEERING-EXPECTATIONS-JP-10

- [ ] **Code:** **Question:** A basic Requirement discovery check fails. What would you do first using the CLI?
> **Covered in:** [Senior engineering expectations — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### SENIOR-ENGINEERING-EXPECTATIONS-MN-01

- [ ] **Question:** Compare Requirement discovery with Assumption identification. When would each change your design?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Requirement discovery: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Assumption identification: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-02

- [ ] **Question:** Compare Assumption identification with Architecture decision records. When would each change your design?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Assumption identification: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Architecture decision records: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-03

- [ ] **Question:** Compare Architecture decision records with Build-versus-buy decisions. When would each change your design?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Architecture decision records: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Build-versus-buy decisions: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Build-versus-buy decisions with Technical strategy. When would each change your design?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Build-versus-buy decisions: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Technical strategy: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-05

- [ ] **Question:** Compare Technical strategy with Roadmap creation. When would each change your design?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Technical strategy: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Roadmap creation: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-06

- [ ] **Question:** Compare Roadmap creation with Prioritizing reliability, security, speed and cost. When would each change your design?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Roadmap creation: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Prioritizing reliability, security, speed and cost: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Prioritizing reliability, security, speed and cost with Managing technical debt. When would each change your design?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Prioritizing reliability, security, speed and cost: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Managing technical debt: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-08

- [ ] **Question:** Compare Managing technical debt with Creating operational standards and guardrails. When would each change your design?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Managing technical debt: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Creating operational standards and guardrails: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-09

- [ ] **Question:** Compare Creating operational standards and guardrails with Requirement discovery. When would each change your design?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Creating operational standards and guardrails: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Requirement discovery: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SENIOR-ENGINEERING-EXPECTATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Requirement discovery with Requirement discovery. When would each change your design?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Requirement discovery: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Requirement discovery: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### SENIOR-ENGINEERING-EXPECTATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Requirement discovery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-02

- [ ] **Question:** Production is degraded around Assumption identification; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Architecture decision records; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-04

- [ ] **Question:** Production is degraded around Build-versus-buy decisions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git shortlog -sn` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Technical strategy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-06

- [ ] **Question:** Production is degraded around Roadmap creation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prioritizing reliability, security, speed and cost; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-08

- [ ] **Question:** Production is degraded around Managing technical debt; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git shortlog -sn` plus recent events/changes, then correlate the service-specific SLI. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Creating operational standards and guardrails; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SENIOR-ENGINEERING-EXPECTATIONS-MP-10

- [ ] **Question:** Production is degraded around Requirement discovery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### SENIOR-ENGINEERING-EXPECTATIONS-SN-01

- [ ] **Question:** Design a production Senior engineering expectations capability where Requirement discovery, Build-versus-buy decisions and Prioritizing reliability, security, speed and cost are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Senior engineering expectations capability where Assumption identification, Technical strategy and Managing technical debt are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-03

- [ ] **Question:** Design a production Senior engineering expectations capability where Architecture decision records, Roadmap creation and Creating operational standards and guardrails are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Senior engineering expectations capability where Build-versus-buy decisions, Prioritizing reliability, security, speed and cost and Requirement discovery are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-05

- [ ] **Question:** Design a production Senior engineering expectations capability where Technical strategy, Managing technical debt and Requirement discovery are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Senior engineering expectations capability where Roadmap creation, Creating operational standards and guardrails and Assumption identification are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-07

- [ ] **Question:** Design a production Senior engineering expectations capability where Prioritizing reliability, security, speed and cost, Requirement discovery and Architecture decision records are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Senior engineering expectations capability where Managing technical debt, Requirement discovery and Build-versus-buy decisions are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-09

- [ ] **Question:** Design a production Senior engineering expectations capability where Creating operational standards and guardrails, Assumption identification and Technical strategy are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SENIOR-ENGINEERING-EXPECTATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Senior engineering expectations capability where Requirement discovery, Architecture decision records and Roadmap creation are first-class requirements.
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### SENIOR-ENGINEERING-EXPECTATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Requirement discovery. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Assumption identification. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Architecture decision records. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Build-versus-buy decisions. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git shortlog -sn` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Technical strategy. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Roadmap creation. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prioritizing reliability, security, speed and cost. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managing technical debt. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git shortlog -sn` as one read-only checkpoint, not the whole diagnosis. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Creating operational standards and guardrails. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SENIOR-ENGINEERING-EXPECTATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Requirement discovery. How do you lead it end to end?
> **Covered in:** [Senior engineering expectations — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Senior engineering expectations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Understanding the role](../01-understanding-the-role/README.md) · [Study note](README.md) · [Next: Taking ownership of an existing platform →](../03-taking-ownership-of-an-existing-platform/README.md)

<!-- reading-navigation:end -->
