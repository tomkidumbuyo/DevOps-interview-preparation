# AI observability — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AI-OBSERVABILITY-JN-01

- [ ] **Question:** What is Prompt and response metadata, and why does it matter in AI observability?
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-OBSERVABILITY-JN-02

- [ ] **Question:** What is Model/provider, and why does it matter in AI observability?
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-OBSERVABILITY-JN-03

- [ ] **Question:** What is Token counts, and why does it matter in AI observability?
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-OBSERVABILITY-JN-04

- [ ] **Question:** What is Time to first token, and why does it matter in AI observability?
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-OBSERVABILITY-JN-05

- [ ] **Question:** What is Time per output token, and why does it matter in AI observability?
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-OBSERVABILITY-JN-06

- [ ] **Question:** What is Retrieval latency, and why does it matter in AI observability?
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-OBSERVABILITY-JN-07

- [ ] **Question:** What is Retrieved-document identifiers, and why does it matter in AI observability?
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-OBSERVABILITY-JN-08

- [ ] **Code:** **Question:** What does `trivy fs .` help you verify for AI observability?
> **Covered in:** [AI observability — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### AI-OBSERVABILITY-JN-09

- [ ] **Code:** **Question:** What does `curl -s http://SERVICE/metrics` help you verify for AI observability?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### AI-OBSERVABILITY-JN-10

- [ ] **Code:** **Question:** What does `promtool check rules rules.yml` help you verify for AI observability?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### AI-OBSERVABILITY-JP-01

- [ ] **Code:** **Question:** A basic Prompt and response metadata check fails. What would you do first using the CLI?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-02

- [ ] **Question:** A basic Model/provider check fails. What would you do first?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-03

- [ ] **Question:** A basic Token counts check fails. What would you do first?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-04

- [ ] **Code:** **Question:** A basic Time to first token check fails. What would you do first using the CLI?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-05

- [ ] **Question:** A basic Time per output token check fails. What would you do first?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-06

- [ ] **Question:** A basic Retrieval latency check fails. What would you do first?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-07

- [ ] **Code:** **Question:** A basic Retrieved-document identifiers check fails. What would you do first using the CLI?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-08

- [ ] **Question:** A basic Tool-call traces check fails. What would you do first?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-09

- [ ] **Question:** A basic Evaluation scores check fails. What would you do first?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-OBSERVABILITY-JP-10

- [ ] **Code:** **Question:** A basic Cost per request check fails. What would you do first using the CLI?
> **Covered in:** [AI observability — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AI-OBSERVABILITY-MN-01

- [ ] **Question:** Compare Prompt and response metadata with Model/provider. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Prompt and response metadata: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model/provider: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-02

- [ ] **Question:** Compare Model/provider with Token counts. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model/provider: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Token counts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-03

- [ ] **Question:** Compare Token counts with Time to first token. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Token counts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Time to first token: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Time to first token with Time per output token. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Time to first token: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Time per output token: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-05

- [ ] **Question:** Compare Time per output token with Retrieval latency. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Time per output token: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Retrieval latency: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-06

- [ ] **Question:** Compare Retrieval latency with Retrieved-document identifiers. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Retrieval latency: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Retrieved-document identifiers: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Retrieved-document identifiers with Tool-call traces. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Retrieved-document identifiers: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Tool-call traces: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-08

- [ ] **Question:** Compare Tool-call traces with Evaluation scores. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Tool-call traces: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Evaluation scores: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-09

- [ ] **Question:** Compare Evaluation scores with Cost per request. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Evaluation scores: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Cost per request: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-OBSERVABILITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Cost per request with Prompt and response metadata. When would each change your design?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Cost per request: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Prompt and response metadata: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AI-OBSERVABILITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prompt and response metadata; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-02

- [ ] **Question:** Production is degraded around Model/provider; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Token counts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-04

- [ ] **Question:** Production is degraded around Time to first token; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Time per output token; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-06

- [ ] **Question:** Production is degraded around Retrieval latency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Retrieved-document identifiers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-08

- [ ] **Question:** Production is degraded around Tool-call traces; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Evaluation scores; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-OBSERVABILITY-MP-10

- [ ] **Question:** Production is degraded around Cost per request; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AI-OBSERVABILITY-SN-01

- [ ] **Question:** Design a production AI observability capability where Prompt and response metadata, Time to first token and Retrieved-document identifiers are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AI observability capability where Model/provider, Time per output token and Tool-call traces are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-03

- [ ] **Question:** Design a production AI observability capability where Token counts, Retrieval latency and Evaluation scores are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AI observability capability where Time to first token, Retrieved-document identifiers and Cost per request are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-05

- [ ] **Question:** Design a production AI observability capability where Time per output token, Tool-call traces and Prompt and response metadata are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AI observability capability where Retrieval latency, Evaluation scores and Model/provider are first-class requirements.
> **Covered in:** [AI observability — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-07

- [ ] **Question:** Design a production AI observability capability where Retrieved-document identifiers, Cost per request and Token counts are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AI observability capability where Tool-call traces, Prompt and response metadata and Time to first token are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-09

- [ ] **Question:** Design a production AI observability capability where Evaluation scores, Model/provider and Time per output token are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-OBSERVABILITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AI observability capability where Cost per request, Token counts and Retrieval latency are first-class requirements.
> **Covered in:** [AI observability — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AI-OBSERVABILITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt and response metadata. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model/provider. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Token counts. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Time to first token. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Time per output token. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retrieval latency. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retrieved-document identifiers. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tool-call traces. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Evaluation scores. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-OBSERVABILITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cost per request. How do you lead it end to end?
> **Covered in:** [AI observability — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of AI observability; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Distributed tracing](../06-distributed-tracing/README.md) · [Study note](README.md) · [Next: SRE and reliability engineering →](../../02-sre-and-reliability-engineering/README.md)

<!-- reading-navigation:end -->
