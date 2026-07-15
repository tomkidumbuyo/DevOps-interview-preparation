# Distributed systems — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### DISTRIBUTED-SYSTEMS-JN-01

- [ ] **Question:** What is Partial failure, and why does it matter in Distributed systems?
> **Covered in:** [Distributed systems — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-SYSTEMS-JN-02

- [ ] **Question:** What is Network partitions, and why does it matter in Distributed systems?
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-SYSTEMS-JN-03

- [ ] **Question:** What is Timeouts, and why does it matter in Distributed systems?
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-SYSTEMS-JN-04

- [ ] **Question:** What is Retries, and why does it matter in Distributed systems?
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-SYSTEMS-JN-05

- [ ] **Question:** What is Backoff and jitter, and why does it matter in Distributed systems?
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-SYSTEMS-JN-06

- [ ] **Question:** What is Idempotency, and why does it matter in Distributed systems?
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-SYSTEMS-JN-07

- [ ] **Question:** What is Deduplication, and why does it matter in Distributed systems?
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-SYSTEMS-JN-08

- [ ] **Code:** **Question:** What does `dig NAME` help you verify for Distributed systems?
> **Covered in:** [Distributed systems — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering.

### DISTRIBUTED-SYSTEMS-JN-09

- [ ] **Code:** **Question:** What does `lscpu; free -h; lsblk; ip -br addr` help you verify for Distributed systems?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### DISTRIBUTED-SYSTEMS-JN-10

- [ ] **Code:** **Question:** What does `ss -s` help you verify for Distributed systems?
> **Covered in:** [Distributed systems — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### DISTRIBUTED-SYSTEMS-JP-01

- [ ] **Code:** **Question:** A basic Partial failure check fails. What would you do first using the CLI?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-02

- [ ] **Question:** A basic Network partitions check fails. What would you do first?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-03

- [ ] **Question:** A basic Timeouts check fails. What would you do first?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-04

- [ ] **Code:** **Question:** A basic Retries check fails. What would you do first using the CLI?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-05

- [ ] **Question:** A basic Backoff and jitter check fails. What would you do first?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-06

- [ ] **Question:** A basic Idempotency check fails. What would you do first?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-07

- [ ] **Code:** **Question:** A basic Deduplication check fails. What would you do first using the CLI?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -v URL` and capture exact status/reason/request ID. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-08

- [ ] **Question:** A basic At-least-once delivery check fails. What would you do first?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig NAME` and capture exact status/reason/request ID. may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-09

- [ ] **Question:** A basic At-most-once delivery check fails. What would you do first?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `lscpu; free -h; lsblk; ip -br addr` and capture exact status/reason/request ID. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-SYSTEMS-JP-10

- [ ] **Code:** **Question:** A basic Exactly-once claims check fails. What would you do first using the CLI?
> **Covered in:** [Distributed systems — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `ss -s` and capture exact status/reason/request ID. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### DISTRIBUTED-SYSTEMS-MN-01

- [ ] **Question:** Compare Partial failure with Network partitions. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Partial failure: means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Network partitions: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-02

- [ ] **Question:** Compare Network partitions with Timeouts. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Network partitions: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Timeouts: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-03

- [ ] **Question:** Compare Timeouts with Retries. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Timeouts: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Retries: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-04

- [ ] **Configuration review:** **Question:** Compare Retries with Backoff and jitter. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Retries: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Backoff and jitter: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-05

- [ ] **Question:** Compare Backoff and jitter with Idempotency. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Backoff and jitter: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Idempotency: makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-06

- [ ] **Question:** Compare Idempotency with Deduplication. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Idempotency: makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Deduplication: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-07

- [ ] **Configuration review:** **Question:** Compare Deduplication with At-least-once delivery. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Deduplication: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. At-least-once delivery: may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-08

- [ ] **Question:** Compare At-least-once delivery with At-most-once delivery. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** At-least-once delivery: may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering. At-most-once delivery: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-09

- [ ] **Question:** Compare At-most-once delivery with Exactly-once claims. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** At-most-once delivery: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Exactly-once claims: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-SYSTEMS-MN-10

- [ ] **Configuration review:** **Question:** Compare Exactly-once claims with Partial failure. When would each change your design?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Exactly-once claims: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Partial failure: means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### DISTRIBUTED-SYSTEMS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Partial failure; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-02

- [ ] **Question:** Production is degraded around Network partitions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Timeouts; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-04

- [ ] **Question:** Production is degraded around Retries; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backoff and jitter; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-06

- [ ] **Question:** Production is degraded around Idempotency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Deduplication; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -v URL` plus recent events/changes, then correlate the service-specific SLI. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-08

- [ ] **Question:** Production is degraded around At-least-once delivery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig NAME` plus recent events/changes, then correlate the service-specific SLI. may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around At-most-once delivery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `lscpu; free -h; lsblk; ip -br addr` plus recent events/changes, then correlate the service-specific SLI. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-SYSTEMS-MP-10

- [ ] **Question:** Production is degraded around Exactly-once claims; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `ss -s` plus recent events/changes, then correlate the service-specific SLI. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### DISTRIBUTED-SYSTEMS-SN-01

- [ ] **Question:** Design a production Distributed systems capability where Partial failure, Retries and Deduplication are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed systems capability where Network partitions, Backoff and jitter and At-least-once delivery are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-03

- [ ] **Question:** Design a production Distributed systems capability where Timeouts, Idempotency and At-most-once delivery are first-class requirements.
> **Covered in:** [Distributed systems — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed systems capability where Retries, Deduplication and Exactly-once claims are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-05

- [ ] **Question:** Design a production Distributed systems capability where Backoff and jitter, At-least-once delivery and Partial failure are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed systems capability where Idempotency, At-most-once delivery and Network partitions are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-07

- [ ] **Question:** Design a production Distributed systems capability where Deduplication, Exactly-once claims and Timeouts are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed systems capability where At-least-once delivery, Partial failure and Retries are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-09

- [ ] **Question:** Design a production Distributed systems capability where At-most-once delivery, Network partitions and Backoff and jitter are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-SYSTEMS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed systems capability where Exactly-once claims, Timeouts and Idempotency are first-class requirements.
> **Covered in:** [Distributed systems — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### DISTRIBUTED-SYSTEMS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Partial failure. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network partitions. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Timeouts. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retries. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backoff and jitter. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Idempotency. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deduplication. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -v URL` as one read-only checkpoint, not the whole diagnosis. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving At-least-once delivery. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig NAME` as one read-only checkpoint, not the whole diagnosis. may redeliver and therefore requires idempotent consumers, deduplication and safe acknowledgement ordering. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving At-most-once delivery. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `lscpu; free -h; lsblk; ip -br addr` as one read-only checkpoint, not the whole diagnosis. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-SYSTEMS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Exactly-once claims. How do you lead it end to end?
> **Covered in:** [Distributed systems — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `ss -s` as one read-only checkpoint, not the whole diagnosis. is part of Distributed systems; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Concurrency](../02-concurrency/README.md) · [Study note](README.md) · [Next: Data consistency →](../04-data-consistency/README.md)

<!-- reading-navigation:end -->
