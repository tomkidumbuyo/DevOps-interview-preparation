# 10 Operations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-10-OPERATIONS-JN-01

- [ ] **Question:** What is OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16, and why does it matter in 10 Operations?
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-10-OPERATIONS-JN-02

- [ ] **Question:** What is Metrics, and why does it matter in 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-10-OPERATIONS-JN-03

- [ ] **Question:** What is Logs, and why does it matter in 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-10-OPERATIONS-JN-04

- [ ] **Question:** What is Traces, and why does it matter in 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-10-OPERATIONS-JN-05

- [ ] **Question:** What is Events, and why does it matter in 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-10-OPERATIONS-JN-06

- [ ] **Question:** What is Profiles, and why does it matter in 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-10-OPERATIONS-JN-07

- [ ] **Question:** What is Correlation, and why does it matter in 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-10-OPERATIONS-JN-08

- [ ] **Code:** **Question:** What does `trivy fs .` help you verify for 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-10-OPERATIONS-JN-09

- [ ] **Code:** **Question:** What does `curl -s http://SERVICE/metrics` help you verify for 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-10-OPERATIONS-JN-10

- [ ] **Code:** **Question:** What does `promtool check rules rules.yml` help you verify for 10 Operations?
> **Covered in:** [Operations, observability, reliability and security — Integrated operations mental model](README.md#integrated-operations-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-10-OPERATIONS-JP-01

- [ ] **Code:** **Question:** A basic OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16 check fails. What would you do first using the CLI?
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-02

- [ ] **Question:** A basic Metrics check fails. What would you do first?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-03

- [ ] **Question:** A basic Logs check fails. What would you do first?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-04

- [ ] **Code:** **Question:** A basic Traces check fails. What would you do first using the CLI?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-05

- [ ] **Question:** A basic Events check fails. What would you do first?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-06

- [ ] **Question:** A basic Profiles check fails. What would you do first?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-07

- [ ] **Code:** **Question:** A basic Correlation check fails. What would you do first using the CLI?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-08

- [ ] **Question:** A basic Context propagation check fails. What would you do first?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-09

- [ ] **Question:** A basic Structured telemetry check fails. What would you do first?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-10-OPERATIONS-JP-10

- [ ] **Code:** **Question:** A basic Counters check fails. What would you do first using the CLI?
> **Covered in:** [Observability — Command and configuration lab](01-observability/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-10-OPERATIONS-MN-01

- [ ] **Question:** Compare OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16 with Metrics. When would each change your design?
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Metrics: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-02

- [ ] **Question:** Compare Metrics with Logs. When would each change your design?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Metrics: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Logs: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-03

- [ ] **Question:** Compare Logs with Traces. When would each change your design?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Logs: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Traces: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Traces with Events. When would each change your design?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Traces: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Events: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-05

- [ ] **Question:** Compare Events with Profiles. When would each change your design?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Events: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Profiles: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-06

- [ ] **Question:** Compare Profiles with Correlation. When would each change your design?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Profiles: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Correlation: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Correlation with Context propagation. When would each change your design?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Correlation: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Context propagation: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-08

- [ ] **Question:** Compare Context propagation with Structured telemetry. When would each change your design?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Context propagation: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Structured telemetry: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-09

- [ ] **Question:** Compare Structured telemetry with Counters. When would each change your design?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Structured telemetry: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Counters: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-10-OPERATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Counters with OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16. When would each change your design?
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Counters: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-10-OPERATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-02

- [ ] **Question:** Production is degraded around Metrics; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Logs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform and cloud security — Complete curriculum checklist](03-platform-and-cloud-security/README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-04

- [ ] **Question:** Production is degraded around Traces; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Events; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-06

- [ ] **Question:** Production is degraded around Profiles; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Correlation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-08

- [ ] **Question:** Production is degraded around Context propagation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Structured telemetry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-10-OPERATIONS-MP-10

- [ ] **Question:** Production is degraded around Counters; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-10-OPERATIONS-SN-01

- [ ] **Question:** Design a production 10 Operations capability where OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16, Traces and Correlation are first-class requirements.
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production 10 Operations capability where Metrics, Events and Context propagation are first-class requirements.
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-03

- [ ] **Question:** Design a production 10 Operations capability where Logs, Profiles and Structured telemetry are first-class requirements.
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production 10 Operations capability where Traces, Correlation and Counters are first-class requirements.
> **Covered in:** [Observability — Senior design checklist](01-observability/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-05

- [ ] **Question:** Design a production 10 Operations capability where Events, Context propagation and OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16 are first-class requirements.
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production 10 Operations capability where Profiles, Structured telemetry and Metrics are first-class requirements.
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-07

- [ ] **Question:** Design a production 10 Operations capability where Correlation, Counters and Logs are first-class requirements.
> **Covered in:** [Observability — Senior design checklist](01-observability/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production 10 Operations capability where Context propagation, OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16 and Traces are first-class requirements.
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-09

- [ ] **Question:** Design a production 10 Operations capability where Structured telemetry, Metrics and Events are first-class requirements.
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-10-OPERATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production 10 Operations capability where Counters, Logs and Profiles are first-class requirements.
> **Covered in:** [Observability — Senior design checklist](01-observability/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-10-OPERATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OpenTelemetry provides common conventions for traces, metrics and logs, including GenAI-specific attributes for operations, models, token usage, evaluaturn660468search16. How do you lead it end to end?
> **Covered in:** [Observability — Complete curriculum checklist](01-observability/README.md#complete-curriculum-checklist)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metrics. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Logs. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. turns runtime state into evidence; define signal semantics, labels/context, retention/privacy/cost, healthy baseline, actionable threshold and a query that distinguishes competing hypotheses. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Traces. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Events. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Profiles. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Correlation. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Context propagation. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Structured telemetry. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-10-OPERATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Counters. How do you lead it end to end?
> **Covered in:** [Observability — Beginner → mid-level → senior learning path](01-observability/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of 10 Operations; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: CircleCI](../09-iac-delivery/03-ci-cd/09-circleci/README.md) · [Study note](README.md) · [Next: Observability →](01-observability/README.md)

<!-- reading-navigation:end -->
