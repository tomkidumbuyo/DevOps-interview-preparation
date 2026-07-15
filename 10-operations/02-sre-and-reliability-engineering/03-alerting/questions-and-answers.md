# Alerting — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### ALERTING-JN-01

- [ ] **Question:** What is Symptom-based alerts, and why does it matter in Alerting?
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ALERTING-JN-02

- [ ] **Question:** What is Cause-based alerts, and why does it matter in Alerting?
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ALERTING-JN-03

- [ ] **Question:** What is Actionable alerts, and why does it matter in Alerting?
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ALERTING-JN-04

- [ ] **Question:** What is Alert fatigue, and why does it matter in Alerting?
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ALERTING-JN-05

- [ ] **Question:** What is Escalation, and why does it matter in Alerting?
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ALERTING-JN-06

- [ ] **Question:** What is Paging policies, and why does it matter in Alerting?
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ALERTING-JN-07

- [ ] **Question:** What is Runbook links, and why does it matter in Alerting?
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ALERTING-JN-08

- [ ] **Code:** **Question:** What does `trivy fs .` help you verify for Alerting?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses.

### ALERTING-JN-09

- [ ] **Code:** **Question:** What does `curl -s http://SERVICE/metrics` help you verify for Alerting?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses.

### ALERTING-JN-10

- [ ] **Code:** **Question:** What does `promtool check rules rules.yml` help you verify for Alerting?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses.

## Junior — procedural and command questions

### ALERTING-JP-01

- [ ] **Code:** **Question:** A basic Symptom-based alerts check fails. What would you do first using the CLI?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-02

- [ ] **Question:** A basic Cause-based alerts check fails. What would you do first?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-03

- [ ] **Question:** A basic Actionable alerts check fails. What would you do first?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-04

- [ ] **Code:** **Question:** A basic Alert fatigue check fails. What would you do first using the CLI?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-05

- [ ] **Question:** A basic Escalation check fails. What would you do first?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-06

- [ ] **Question:** A basic Paging policies check fails. What would you do first?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-07

- [ ] **Code:** **Question:** A basic Runbook links check fails. What would you do first using the CLI?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-08

- [ ] **Question:** A basic Symptom-based alerts check fails. What would you do first?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-09

- [ ] **Question:** A basic Cause-based alerts check fails. What would you do first?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ALERTING-JP-10

- [ ] **Code:** **Question:** A basic Actionable alerts check fails. What would you do first using the CLI?
> **Covered in:** [Alerting — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### ALERTING-MN-01

- [ ] **Question:** Compare Symptom-based alerts with Cause-based alerts. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Symptom-based alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Cause-based alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-02

- [ ] **Question:** Compare Cause-based alerts with Actionable alerts. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Cause-based alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Actionable alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-03

- [ ] **Question:** Compare Actionable alerts with Alert fatigue. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Actionable alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Alert fatigue: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-04

- [ ] **Configuration review:** **Question:** Compare Alert fatigue with Escalation. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Alert fatigue: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Escalation: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-05

- [ ] **Question:** Compare Escalation with Paging policies. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Escalation: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Paging policies: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-06

- [ ] **Question:** Compare Paging policies with Runbook links. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Paging policies: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Runbook links: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-07

- [ ] **Configuration review:** **Question:** Compare Runbook links with Symptom-based alerts. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Runbook links: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Symptom-based alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-08

- [ ] **Question:** Compare Symptom-based alerts with Cause-based alerts. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Symptom-based alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Cause-based alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-09

- [ ] **Question:** Compare Cause-based alerts with Actionable alerts. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Cause-based alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Actionable alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ALERTING-MN-10

- [ ] **Configuration review:** **Question:** Compare Actionable alerts with Symptom-based alerts. When would each change your design?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Actionable alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Symptom-based alerts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### ALERTING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Symptom-based alerts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-02

- [ ] **Question:** Production is degraded around Cause-based alerts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Actionable alerts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-04

- [ ] **Question:** Production is degraded around Alert fatigue; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Escalation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-06

- [ ] **Question:** Production is degraded around Paging policies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Runbook links; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-08

- [ ] **Question:** Production is degraded around Symptom-based alerts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cause-based alerts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ALERTING-MP-10

- [ ] **Question:** Production is degraded around Actionable alerts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### ALERTING-SN-01

- [ ] **Question:** Design a production Alerting capability where Symptom-based alerts, Alert fatigue and Runbook links are first-class requirements.
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Alerting capability where Cause-based alerts, Escalation and Symptom-based alerts are first-class requirements.
> **Covered in:** [Alerting — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-03

- [ ] **Question:** Design a production Alerting capability where Actionable alerts, Paging policies and Cause-based alerts are first-class requirements.
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Alerting capability where Alert fatigue, Runbook links and Actionable alerts are first-class requirements.
> **Covered in:** [Alerting — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-05

- [ ] **Question:** Design a production Alerting capability where Escalation, Symptom-based alerts and Symptom-based alerts are first-class requirements.
> **Covered in:** [Alerting — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Alerting capability where Paging policies, Cause-based alerts and Cause-based alerts are first-class requirements.
> **Covered in:** [Alerting — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-07

- [ ] **Question:** Design a production Alerting capability where Runbook links, Actionable alerts and Actionable alerts are first-class requirements.
> **Covered in:** [Alerting — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Alerting capability where Symptom-based alerts, Symptom-based alerts and Alert fatigue are first-class requirements.
> **Covered in:** [Alerting — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-09

- [ ] **Question:** Design a production Alerting capability where Cause-based alerts, Cause-based alerts and Escalation are first-class requirements.
> **Covered in:** [Alerting — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ALERTING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Alerting capability where Actionable alerts, Actionable alerts and Paging policies are first-class requirements.
> **Covered in:** [Alerting — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### ALERTING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Symptom-based alerts. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cause-based alerts. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Actionable alerts. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Alert fatigue. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Escalation. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Paging policies. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Runbook links. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Alerting; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Symptom-based alerts. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cause-based alerts. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ALERTING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Actionable alerts. How do you lead it end to end?
> **Covered in:** [Alerting — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Service indicators and objectives](../02-service-indicators-and-objectives/README.md) · [Study note](README.md) · [Next: Capacity planning →](../04-capacity-planning/README.md)

<!-- reading-navigation:end -->
