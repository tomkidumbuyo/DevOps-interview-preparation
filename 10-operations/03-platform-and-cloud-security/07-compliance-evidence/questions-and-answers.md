# Compliance evidence — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### COMPLIANCE-EVIDENCE-JN-01

- [ ] **Question:** What is Access logs, and why does it matter in Compliance evidence?
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COMPLIANCE-EVIDENCE-JN-02

- [ ] **Question:** What is Change logs, and why does it matter in Compliance evidence?
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COMPLIANCE-EVIDENCE-JN-03

- [ ] **Question:** What is IaC history, and why does it matter in Compliance evidence?
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COMPLIANCE-EVIDENCE-JN-04

- [ ] **Question:** What is Approval records, and why does it matter in Compliance evidence?
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COMPLIANCE-EVIDENCE-JN-05

- [ ] **Question:** What is Vulnerability reports, and why does it matter in Compliance evidence?
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COMPLIANCE-EVIDENCE-JN-06

- [ ] **Question:** What is Backup tests, and why does it matter in Compliance evidence?
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COMPLIANCE-EVIDENCE-JN-07

- [ ] **Question:** What is Restore tests, and why does it matter in Compliance evidence?
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COMPLIANCE-EVIDENCE-JN-08

- [ ] **Code:** **Question:** What does `trivy fs .` help you verify for Compliance evidence?
> **Covered in:** [Compliance evidence — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair.

### COMPLIANCE-EVIDENCE-JN-09

- [ ] **Code:** **Question:** What does `curl -s http://SERVICE/metrics` help you verify for Compliance evidence?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery.

### COMPLIANCE-EVIDENCE-JN-10

- [ ] **Code:** **Question:** What does `promtool check rules rules.yml` help you verify for Compliance evidence?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses.

## Junior — procedural and command questions

### COMPLIANCE-EVIDENCE-JP-01

- [ ] **Code:** **Question:** A basic Access logs check fails. What would you do first using the CLI?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-02

- [ ] **Question:** A basic Change logs check fails. What would you do first?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-03

- [ ] **Question:** A basic IaC history check fails. What would you do first?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-04

- [ ] **Code:** **Question:** A basic Approval records check fails. What would you do first using the CLI?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-05

- [ ] **Question:** A basic Vulnerability reports check fails. What would you do first?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-06

- [ ] **Question:** A basic Backup tests check fails. What would you do first?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-07

- [ ] **Code:** **Question:** A basic Restore tests check fails. What would you do first using the CLI?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-08

- [ ] **Question:** A basic Incident records check fails. What would you do first?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-09

- [ ] **Question:** A basic Policy reports check fails. What would you do first?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COMPLIANCE-EVIDENCE-JP-10

- [ ] **Code:** **Question:** A basic Access logs check fails. What would you do first using the CLI?
> **Covered in:** [Compliance evidence — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### COMPLIANCE-EVIDENCE-MN-01

- [ ] **Question:** Compare Access logs with Change logs. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Access logs: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Change logs: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-02

- [ ] **Question:** Compare Change logs with IaC history. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Change logs: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. IaC history: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-03

- [ ] **Question:** Compare IaC history with Approval records. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** IaC history: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Approval records: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-04

- [ ] **Configuration review:** **Question:** Compare Approval records with Vulnerability reports. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Approval records: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Vulnerability reports: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-05

- [ ] **Question:** Compare Vulnerability reports with Backup tests. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Vulnerability reports: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Backup tests: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-06

- [ ] **Question:** Compare Backup tests with Restore tests. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Backup tests: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Restore tests: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-07

- [ ] **Configuration review:** **Question:** Compare Restore tests with Incident records. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Restore tests: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Incident records: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-08

- [ ] **Question:** Compare Incident records with Policy reports. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Incident records: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Policy reports: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-09

- [ ] **Question:** Compare Policy reports with Access logs. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Policy reports: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Access logs: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COMPLIANCE-EVIDENCE-MN-10

- [ ] **Configuration review:** **Question:** Compare Access logs with Access logs. When would each change your design?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Access logs: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Access logs: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### COMPLIANCE-EVIDENCE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Access logs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-02

- [ ] **Question:** Production is degraded around Change logs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around IaC history; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-04

- [ ] **Question:** Production is degraded around Approval records; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Vulnerability reports; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-06

- [ ] **Question:** Production is degraded around Backup tests; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Restore tests; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-08

- [ ] **Question:** Production is degraded around Incident records; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Policy reports; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COMPLIANCE-EVIDENCE-MP-10

- [ ] **Question:** Production is degraded around Access logs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### COMPLIANCE-EVIDENCE-SN-01

- [ ] **Question:** Design a production Compliance evidence capability where Access logs, Approval records and Restore tests are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Compliance evidence capability where Change logs, Vulnerability reports and Incident records are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-03

- [ ] **Question:** Design a production Compliance evidence capability where IaC history, Backup tests and Policy reports are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Compliance evidence capability where Approval records, Restore tests and Access logs are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-05

- [ ] **Question:** Design a production Compliance evidence capability where Vulnerability reports, Incident records and Access logs are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Compliance evidence capability where Backup tests, Policy reports and Change logs are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-07

- [ ] **Question:** Design a production Compliance evidence capability where Restore tests, Access logs and IaC history are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Compliance evidence capability where Incident records, Access logs and Approval records are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-09

- [ ] **Question:** Design a production Compliance evidence capability where Policy reports, Change logs and Vulnerability reports are first-class requirements.
> **Covered in:** [Compliance evidence — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COMPLIANCE-EVIDENCE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Compliance evidence capability where Access logs, IaC history and Backup tests are first-class requirements.
> **Covered in:** [Compliance evidence — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### COMPLIANCE-EVIDENCE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access logs. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Change logs. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IaC history. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Approval records. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Vulnerability reports. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Compliance evidence; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backup tests. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restore tests. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Incident records. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Policy reports. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. defines a trust/control boundary: identify actor, protected asset, decision/enforcement point, least privilege, bypass path, audit evidence, rotation/revocation and recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COMPLIANCE-EVIDENCE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access logs. How do you lead it end to end?
> **Covered in:** [Compliance evidence — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Vulnerability management](../06-vulnerability-management/README.md) · [Study note](README.md) · [Next: AI/ML platform, LLMOps, security and governance →](../../../11-ai-platform/README.md)

<!-- reading-navigation:end -->
