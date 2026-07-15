# Service indicators and objectives — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-01

- [ ] **Question:** What is SLIs, and why does it matter in Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-02

- [ ] **Question:** What is SLOs, and why does it matter in Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-03

- [ ] **Question:** What is SLAs, and why does it matter in Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-04

- [ ] **Question:** What is Error budgets, and why does it matter in Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-05

- [ ] **Question:** What is Burn rates, and why does it matter in Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-06

- [ ] **Question:** What is Multi-window alerts, and why does it matter in Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-07

- [ ] **Question:** What is User-facing indicators, and why does it matter in Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-08

- [ ] **Code:** **Question:** What does `trivy fs .` help you verify for Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-09

- [ ] **Code:** **Question:** What does `curl -s http://SERVICE/metrics` help you verify for Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### SERVICE-INDICATORS-AND-OBJECTIVES-JN-10

- [ ] **Code:** **Question:** What does `promtool check rules rules.yml` help you verify for Service indicators and objectives?
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-01

- [ ] **Code:** **Question:** A basic SLIs check fails. What would you do first using the CLI?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-02

- [ ] **Question:** A basic SLOs check fails. What would you do first?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-03

- [ ] **Question:** A basic SLAs check fails. What would you do first?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-04

- [ ] **Code:** **Question:** A basic Error budgets check fails. What would you do first using the CLI?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-05

- [ ] **Question:** A basic Burn rates check fails. What would you do first?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-06

- [ ] **Question:** A basic Multi-window alerts check fails. What would you do first?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-07

- [ ] **Code:** **Question:** A basic User-facing indicators check fails. What would you do first using the CLI?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-08

- [ ] **Question:** A basic AI-quality SLOs check fails. What would you do first?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-09

- [ ] **Question:** A basic SLIs check fails. What would you do first?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SERVICE-INDICATORS-AND-OBJECTIVES-JP-10

- [ ] **Code:** **Question:** A basic SLOs check fails. What would you do first using the CLI?
> **Covered in:** [Service indicators and objectives — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-01

- [ ] **Question:** Compare SLIs with SLOs. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** SLIs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. SLOs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-02

- [ ] **Question:** Compare SLOs with SLAs. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** SLOs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. SLAs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-03

- [ ] **Question:** Compare SLAs with Error budgets. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** SLAs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Error budgets: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-04

- [ ] **Configuration review:** **Question:** Compare Error budgets with Burn rates. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Error budgets: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Burn rates: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-05

- [ ] **Question:** Compare Burn rates with Multi-window alerts. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Burn rates: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Multi-window alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-06

- [ ] **Question:** Compare Multi-window alerts with User-facing indicators. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Multi-window alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. User-facing indicators: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-07

- [ ] **Configuration review:** **Question:** Compare User-facing indicators with AI-quality SLOs. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** User-facing indicators: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. AI-quality SLOs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-08

- [ ] **Question:** Compare AI-quality SLOs with SLIs. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** AI-quality SLOs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. SLIs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-09

- [ ] **Question:** Compare SLIs with SLOs. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** SLIs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. SLOs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SERVICE-INDICATORS-AND-OBJECTIVES-MN-10

- [ ] **Configuration review:** **Question:** Compare SLOs with SLIs. When would each change your design?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** SLOs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. SLIs: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around SLIs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-02

- [ ] **Question:** Production is degraded around SLOs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around SLAs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-04

- [ ] **Question:** Production is degraded around Error budgets; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Burn rates; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-06

- [ ] **Question:** Production is degraded around Multi-window alerts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around User-facing indicators; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-08

- [ ] **Question:** Production is degraded around AI-quality SLOs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around SLIs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SERVICE-INDICATORS-AND-OBJECTIVES-MP-10

- [ ] **Question:** Production is degraded around SLOs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-01

- [ ] **Question:** Design a production Service indicators and objectives capability where SLIs, Error budgets and User-facing indicators are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Service indicators and objectives capability where SLOs, Burn rates and AI-quality SLOs are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-03

- [ ] **Question:** Design a production Service indicators and objectives capability where SLAs, Multi-window alerts and SLIs are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Service indicators and objectives capability where Error budgets, User-facing indicators and SLOs are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-05

- [ ] **Question:** Design a production Service indicators and objectives capability where Burn rates, AI-quality SLOs and SLIs are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Service indicators and objectives capability where Multi-window alerts, SLIs and SLOs are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-07

- [ ] **Question:** Design a production Service indicators and objectives capability where User-facing indicators, SLOs and SLAs are first-class requirements.
> **Covered in:** [Service indicators and objectives — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Service indicators and objectives capability where AI-quality SLOs, SLIs and Error budgets are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-09

- [ ] **Question:** Design a production Service indicators and objectives capability where SLIs, SLOs and Burn rates are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SERVICE-INDICATORS-AND-OBJECTIVES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Service indicators and objectives capability where SLOs, SLAs and Multi-window alerts are first-class requirements.
> **Covered in:** [Service indicators and objectives — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SLIs. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SLOs. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SLAs. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Error budgets. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Burn rates. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multi-window alerts. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving User-facing indicators. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AI-quality SLOs. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SLIs. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SERVICE-INDICATORS-AND-OBJECTIVES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SLOs. How do you lead it end to end?
> **Covered in:** [Service indicators and objectives — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of Service indicators and objectives; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Reliability concepts](../01-reliability-concepts/README.md) · [Study note](README.md) · [Next: Alerting →](../03-alerting/README.md)

<!-- reading-navigation:end -->
