# Resilience patterns — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### RESILIENCE-PATTERNS-JN-01

- [ ] **Question:** What is Circuit breakers, and why does it matter in Resilience patterns?
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESILIENCE-PATTERNS-JN-02

- [ ] **Question:** What is Bulkheads, and why does it matter in Resilience patterns?
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESILIENCE-PATTERNS-JN-03

- [ ] **Question:** What is Rate limiting, and why does it matter in Resilience patterns?
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESILIENCE-PATTERNS-JN-04

- [ ] **Question:** What is Load shedding, and why does it matter in Resilience patterns?
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESILIENCE-PATTERNS-JN-05

- [ ] **Question:** What is Graceful degradation, and why does it matter in Resilience patterns?
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESILIENCE-PATTERNS-JN-06

- [ ] **Question:** What is Backpressure, and why does it matter in Resilience patterns?
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESILIENCE-PATTERNS-JN-07

- [ ] **Question:** What is Caching, and why does it matter in Resilience patterns?
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RESILIENCE-PATTERNS-JN-08

- [ ] **Code:** **Question:** What does `dig NAME` help you verify for Resilience patterns?
> **Covered in:** [Resilience patterns — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### RESILIENCE-PATTERNS-JN-09

- [ ] **Code:** **Question:** What does `lscpu; free -h; lsblk; ip -br addr` help you verify for Resilience patterns?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics.

### RESILIENCE-PATTERNS-JN-10

- [ ] **Code:** **Question:** What does `ss -s` help you verify for Resilience patterns?
> **Covered in:** [Resilience patterns — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### RESILIENCE-PATTERNS-JP-01

- [ ] **Code:** **Question:** A basic Circuit breakers check fails. What would you do first using the CLI?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-02

- [ ] **Question:** A basic Bulkheads check fails. What would you do first?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-03

- [ ] **Question:** A basic Rate limiting check fails. What would you do first?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-04

- [ ] **Code:** **Question:** A basic Load shedding check fails. What would you do first using the CLI?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-05

- [ ] **Question:** A basic Graceful degradation check fails. What would you do first?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-06

- [ ] **Question:** A basic Backpressure check fails. What would you do first?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-07

- [ ] **Code:** **Question:** A basic Caching check fails. What would you do first using the CLI?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-08

- [ ] **Question:** A basic Failover check fails. What would you do first?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-09

- [ ] **Question:** A basic Circuit breakers check fails. What would you do first?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RESILIENCE-PATTERNS-JP-10

- [ ] **Code:** **Question:** A basic Bulkheads check fails. What would you do first using the CLI?
> **Covered in:** [Resilience patterns — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### RESILIENCE-PATTERNS-MN-01

- [ ] **Question:** Compare Circuit breakers with Bulkheads. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Circuit breakers: stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Bulkheads: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-02

- [ ] **Question:** Compare Bulkheads with Rate limiting. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Bulkheads: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Rate limiting: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-03

- [ ] **Question:** Compare Rate limiting with Load shedding. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Rate limiting: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Load shedding: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-04

- [ ] **Configuration review:** **Question:** Compare Load shedding with Graceful degradation. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Load shedding: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Graceful degradation: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-05

- [ ] **Question:** Compare Graceful degradation with Backpressure. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Graceful degradation: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Backpressure: propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-06

- [ ] **Question:** Compare Backpressure with Caching. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Backpressure: propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. Caching: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-07

- [ ] **Configuration review:** **Question:** Compare Caching with Failover. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Caching: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Failover: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-08

- [ ] **Question:** Compare Failover with Circuit breakers. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Failover: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Circuit breakers: stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-09

- [ ] **Question:** Compare Circuit breakers with Bulkheads. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Circuit breakers: stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Bulkheads: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RESILIENCE-PATTERNS-MN-10

- [ ] **Configuration review:** **Question:** Compare Bulkheads with Circuit breakers. When would each change your design?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Bulkheads: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Circuit breakers: stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### RESILIENCE-PATTERNS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Circuit breakers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-02

- [ ] **Question:** Production is degraded around Bulkheads; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rate limiting; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-04

- [ ] **Question:** Production is degraded around Load shedding; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Graceful degradation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-06

- [ ] **Question:** Production is degraded around Backpressure; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Caching; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-08

- [ ] **Question:** Production is degraded around Failover; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Circuit breakers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RESILIENCE-PATTERNS-MP-10

- [ ] **Question:** Production is degraded around Bulkheads; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### RESILIENCE-PATTERNS-SN-01

- [ ] **Question:** Design a production Resilience patterns capability where Circuit breakers, Load shedding and Caching are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Resilience patterns capability where Bulkheads, Graceful degradation and Failover are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-03

- [ ] **Question:** Design a production Resilience patterns capability where Rate limiting, Backpressure and Circuit breakers are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Resilience patterns capability where Load shedding, Caching and Bulkheads are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-05

- [ ] **Question:** Design a production Resilience patterns capability where Graceful degradation, Failover and Circuit breakers are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Resilience patterns capability where Backpressure, Circuit breakers and Bulkheads are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-07

- [ ] **Question:** Design a production Resilience patterns capability where Caching, Bulkheads and Rate limiting are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Resilience patterns capability where Failover, Circuit breakers and Load shedding are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-09

- [ ] **Question:** Design a production Resilience patterns capability where Circuit breakers, Bulkheads and Graceful degradation are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RESILIENCE-PATTERNS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Resilience patterns capability where Bulkheads, Rate limiting and Backpressure are first-class requirements.
> **Covered in:** [Resilience patterns — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### RESILIENCE-PATTERNS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Circuit breakers. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Bulkheads. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rate limiting. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Load shedding. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Graceful degradation. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backpressure. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. propagates downstream capacity limits to producers through bounded queues, admission or rate reduction instead of unbounded buffering. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Caching. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Failover. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Circuit breakers. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. stop calls to a failing dependency after a threshold and probe recovery, preventing resource exhaustion while requiring fallback semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RESILIENCE-PATTERNS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Bulkheads. How do you lead it end to end?
> **Covered in:** [Resilience patterns — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is part of Resilience patterns; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Data consistency](../04-data-consistency/README.md) · [Study note](README.md) · [Next: API and service architecture →](../06-api-and-service-architecture/README.md)

<!-- reading-navigation:end -->
