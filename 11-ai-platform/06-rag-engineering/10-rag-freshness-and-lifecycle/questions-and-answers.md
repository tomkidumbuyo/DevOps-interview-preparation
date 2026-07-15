# RAG freshness and lifecycle — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### RAG-FRESHNESS-AND-LIFECYCLE-JN-01

- [ ] **Question:** What is Incremental updates, and why does it matter in RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-02

- [ ] **Question:** What is Re-indexing, and why does it matter in RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-03

- [ ] **Question:** What is Deletions, and why does it matter in RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-04

- [ ] **Question:** What is Right-to-erasure, and why does it matter in RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-05

- [ ] **Question:** What is Expiration, and why does it matter in RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-06

- [ ] **Question:** What is Source-of-truth tracking, and why does it matter in RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-07

- [ ] **Question:** What is Index-version migration, and why does it matter in RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-08

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-09

- [ ] **Code:** **Question:** What does `nvidia-smi` help you verify for RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### RAG-FRESHNESS-AND-LIFECYCLE-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pods -A -o wide` help you verify for RAG freshness and lifecycle?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### RAG-FRESHNESS-AND-LIFECYCLE-JP-01

- [ ] **Code:** **Question:** A basic Incremental updates check fails. What would you do first using the CLI?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-02

- [ ] **Question:** A basic Re-indexing check fails. What would you do first?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-03

- [ ] **Question:** A basic Deletions check fails. What would you do first?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-04

- [ ] **Code:** **Question:** A basic Right-to-erasure check fails. What would you do first using the CLI?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-05

- [ ] **Question:** A basic Expiration check fails. What would you do first?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-06

- [ ] **Question:** A basic Source-of-truth tracking check fails. What would you do first?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-07

- [ ] **Code:** **Question:** A basic Index-version migration check fails. What would you do first using the CLI?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-08

- [ ] **Question:** A basic Embedding-version migration check fails. What would you do first?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-09

- [ ] **Question:** A basic Incremental updates check fails. What would you do first?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RAG-FRESHNESS-AND-LIFECYCLE-JP-10

- [ ] **Code:** **Question:** A basic Re-indexing check fails. What would you do first using the CLI?
> **Covered in:** [RAG freshness and lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### RAG-FRESHNESS-AND-LIFECYCLE-MN-01

- [ ] **Question:** Compare Incremental updates with Re-indexing. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Incremental updates: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Re-indexing: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-02

- [ ] **Question:** Compare Re-indexing with Deletions. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Re-indexing: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Deletions: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-03

- [ ] **Question:** Compare Deletions with Right-to-erasure. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Deletions: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Right-to-erasure: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-04

- [ ] **Configuration review:** **Question:** Compare Right-to-erasure with Expiration. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Right-to-erasure: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Expiration: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-05

- [ ] **Question:** Compare Expiration with Source-of-truth tracking. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Expiration: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Source-of-truth tracking: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-06

- [ ] **Question:** Compare Source-of-truth tracking with Index-version migration. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Source-of-truth tracking: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Index-version migration: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-07

- [ ] **Configuration review:** **Question:** Compare Index-version migration with Embedding-version migration. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Index-version migration: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Embedding-version migration: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-08

- [ ] **Question:** Compare Embedding-version migration with Incremental updates. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Embedding-version migration: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Incremental updates: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-09

- [ ] **Question:** Compare Incremental updates with Re-indexing. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Incremental updates: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Re-indexing: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RAG-FRESHNESS-AND-LIFECYCLE-MN-10

- [ ] **Configuration review:** **Question:** Compare Re-indexing with Incremental updates. When would each change your design?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Re-indexing: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Incremental updates: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### RAG-FRESHNESS-AND-LIFECYCLE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Incremental updates; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-02

- [ ] **Question:** Production is degraded around Re-indexing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Deletions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-04

- [ ] **Question:** Production is degraded around Right-to-erasure; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Expiration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-06

- [ ] **Question:** Production is degraded around Source-of-truth tracking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Index-version migration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-08

- [ ] **Question:** Production is degraded around Embedding-version migration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Incremental updates; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RAG-FRESHNESS-AND-LIFECYCLE-MP-10

- [ ] **Question:** Production is degraded around Re-indexing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### RAG-FRESHNESS-AND-LIFECYCLE-SN-01

- [ ] **Question:** Design a production RAG freshness and lifecycle capability where Incremental updates, Right-to-erasure and Index-version migration are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production RAG freshness and lifecycle capability where Re-indexing, Expiration and Embedding-version migration are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-03

- [ ] **Question:** Design a production RAG freshness and lifecycle capability where Deletions, Source-of-truth tracking and Incremental updates are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production RAG freshness and lifecycle capability where Right-to-erasure, Index-version migration and Re-indexing are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-05

- [ ] **Question:** Design a production RAG freshness and lifecycle capability where Expiration, Embedding-version migration and Incremental updates are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production RAG freshness and lifecycle capability where Source-of-truth tracking, Incremental updates and Re-indexing are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-07

- [ ] **Question:** Design a production RAG freshness and lifecycle capability where Index-version migration, Re-indexing and Deletions are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production RAG freshness and lifecycle capability where Embedding-version migration, Incremental updates and Right-to-erasure are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-09

- [ ] **Question:** Design a production RAG freshness and lifecycle capability where Incremental updates, Re-indexing and Expiration are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RAG-FRESHNESS-AND-LIFECYCLE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production RAG freshness and lifecycle capability where Re-indexing, Deletions and Source-of-truth tracking are first-class requirements.
> **Covered in:** [RAG freshness and lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### RAG-FRESHNESS-AND-LIFECYCLE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Incremental updates. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Re-indexing. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Deletions. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Right-to-erasure. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Expiration. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Source-of-truth tracking. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Index-version migration. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Embedding-version migration. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is a controlled state transition requiring inventory, compatibility, protected state, rehearsal, rollback/abort criteria, integrity checks and measured user-facing RPO/RTO or completion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Incremental updates. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RAG-FRESHNESS-AND-LIFECYCLE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Re-indexing. How do you lead it end to end?
> **Covered in:** [RAG freshness and lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of RAG freshness and lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Context construction](../09-context-construction/README.md) · [Study note](README.md) · [Next: RAG multi-tenancy →](../11-rag-multi-tenancy/README.md)

<!-- reading-navigation:end -->
