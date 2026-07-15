# Reliability concepts — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### RELIABILITY-CONCEPTS-JN-01

- [ ] **Question:** What is Availability, and why does it matter in Reliability concepts?
> **Covered in:** [Reliability concepts — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RELIABILITY-CONCEPTS-JN-02

- [ ] **Question:** What is Durability, and why does it matter in Reliability concepts?
> **Covered in:** [Reliability concepts — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RELIABILITY-CONCEPTS-JN-03

- [ ] **Question:** What is Reliability, and why does it matter in Reliability concepts?
> **Covered in:** [Reliability concepts — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RELIABILITY-CONCEPTS-JN-04

- [ ] **Question:** What is Latency, and why does it matter in Reliability concepts?
> **Covered in:** [Reliability concepts — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RELIABILITY-CONCEPTS-JN-05

- [ ] **Question:** What is Throughput, and why does it matter in Reliability concepts?
> **Covered in:** [Reliability concepts — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RELIABILITY-CONCEPTS-JN-06

- [ ] **Question:** What is Correctness, and why does it matter in Reliability concepts?
> **Covered in:** [Reliability concepts — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RELIABILITY-CONCEPTS-JN-07

- [ ] **Question:** What is Freshness, and why does it matter in Reliability concepts?
> **Covered in:** [Reliability concepts — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RELIABILITY-CONCEPTS-JN-08

- [ ] **Code:** **Question:** What does `trivy fs .` help you verify for Reliability concepts?
> **Covered in:** [Reliability concepts — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### RELIABILITY-CONCEPTS-JN-09

- [ ] **Code:** **Question:** What does `curl -s http://SERVICE/metrics` help you verify for Reliability concepts?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### RELIABILITY-CONCEPTS-JN-10

- [ ] **Code:** **Question:** What does `promtool check rules rules.yml` help you verify for Reliability concepts?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### RELIABILITY-CONCEPTS-JP-01

- [ ] **Code:** **Question:** A basic Availability check fails. What would you do first using the CLI?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-02

- [ ] **Question:** A basic Durability check fails. What would you do first?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-03

- [ ] **Question:** A basic Reliability check fails. What would you do first?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-04

- [ ] **Code:** **Question:** A basic Latency check fails. What would you do first using the CLI?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-05

- [ ] **Question:** A basic Throughput check fails. What would you do first?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-06

- [ ] **Question:** A basic Correctness check fails. What would you do first?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-07

- [ ] **Code:** **Question:** A basic Freshness check fails. What would you do first using the CLI?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-08

- [ ] **Question:** A basic Quality check fails. What would you do first?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `trivy fs .` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-09

- [ ] **Question:** A basic Availability check fails. What would you do first?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://SERVICE/metrics` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RELIABILITY-CONCEPTS-JP-10

- [ ] **Code:** **Question:** A basic Durability check fails. What would you do first using the CLI?
> **Covered in:** [Reliability concepts — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `promtool check rules rules.yml` and capture exact status/reason/request ID. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### RELIABILITY-CONCEPTS-MN-01

- [ ] **Question:** Compare Availability with Durability. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Availability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Durability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-02

- [ ] **Question:** Compare Durability with Reliability. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Durability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Reliability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-03

- [ ] **Question:** Compare Reliability with Latency. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Reliability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Latency: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-04

- [ ] **Configuration review:** **Question:** Compare Latency with Throughput. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Latency: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Throughput: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-05

- [ ] **Question:** Compare Throughput with Correctness. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Throughput: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Correctness: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-06

- [ ] **Question:** Compare Correctness with Freshness. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Correctness: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Freshness: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-07

- [ ] **Configuration review:** **Question:** Compare Freshness with Quality. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Freshness: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Quality: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-08

- [ ] **Question:** Compare Quality with Availability. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Quality: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Availability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-09

- [ ] **Question:** Compare Availability with Durability. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Availability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Durability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RELIABILITY-CONCEPTS-MN-10

- [ ] **Configuration review:** **Question:** Compare Durability with Availability. When would each change your design?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Durability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Availability: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### RELIABILITY-CONCEPTS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Availability; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-02

- [ ] **Question:** Production is degraded around Durability; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Reliability; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-04

- [ ] **Question:** Production is degraded around Latency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Throughput; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-06

- [ ] **Question:** Production is degraded around Correctness; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Freshness; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-08

- [ ] **Question:** Production is degraded around Quality; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `trivy fs .` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Availability; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://SERVICE/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RELIABILITY-CONCEPTS-MP-10

- [ ] **Question:** Production is degraded around Durability; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `promtool check rules rules.yml` plus recent events/changes, then correlate the service-specific SLI. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### RELIABILITY-CONCEPTS-SN-01

- [ ] **Question:** Design a production Reliability concepts capability where Availability, Latency and Freshness are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Reliability concepts capability where Durability, Throughput and Quality are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-03

- [ ] **Question:** Design a production Reliability concepts capability where Reliability, Correctness and Availability are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Reliability concepts capability where Latency, Freshness and Durability are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-05

- [ ] **Question:** Design a production Reliability concepts capability where Throughput, Quality and Availability are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Reliability concepts capability where Correctness, Availability and Durability are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-07

- [ ] **Question:** Design a production Reliability concepts capability where Freshness, Durability and Reliability are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Reliability concepts capability where Quality, Availability and Latency are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-09

- [ ] **Question:** Design a production Reliability concepts capability where Availability, Durability and Throughput are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RELIABILITY-CONCEPTS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Reliability concepts capability where Durability, Reliability and Correctness are first-class requirements.
> **Covered in:** [Reliability concepts — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### RELIABILITY-CONCEPTS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Availability. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Durability. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reliability. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Latency. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Throughput. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Correctness. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Freshness. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Quality. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `trivy fs .` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Availability. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://SERVICE/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RELIABILITY-CONCEPTS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Durability. How do you lead it end to end?
> **Covered in:** [Reliability concepts — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `promtool check rules rules.yml` as one read-only checkpoint, not the whole diagnosis. is part of Reliability concepts; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: SRE and reliability engineering](../README.md) · [Study note](README.md) · [Next: Service indicators and objectives →](../02-service-indicators-and-objectives/README.md)

<!-- reading-navigation:end -->
