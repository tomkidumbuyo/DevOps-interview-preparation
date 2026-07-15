# Platform reconciliation — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### PLATFORM-RECONCILIATION-JN-01

- [ ] **Question:** What is Desired state, and why does it matter in Platform reconciliation?
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PLATFORM-RECONCILIATION-JN-02

- [ ] **Question:** What is Controllers, and why does it matter in Platform reconciliation?
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PLATFORM-RECONCILIATION-JN-03

- [ ] **Question:** What is Idempotency, and why does it matter in Platform reconciliation?
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PLATFORM-RECONCILIATION-JN-04

- [ ] **Question:** What is Retries, and why does it matter in Platform reconciliation?
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PLATFORM-RECONCILIATION-JN-05

- [ ] **Question:** What is Status conditions, and why does it matter in Platform reconciliation?
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PLATFORM-RECONCILIATION-JN-06

- [ ] **Question:** What is Long-running operations, and why does it matter in Platform reconciliation?
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PLATFORM-RECONCILIATION-JN-07

- [ ] **Question:** What is Partial failure, and why does it matter in Platform reconciliation?
> **Covered in:** [Platform reconciliation — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PLATFORM-RECONCILIATION-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Platform reconciliation?
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### PLATFORM-RECONCILIATION-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Platform reconciliation?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### PLATFORM-RECONCILIATION-JN-10

- [ ] **Code:** **Question:** What does `go test ./...` help you verify for Platform reconciliation?
> **Covered in:** [Platform reconciliation — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### PLATFORM-RECONCILIATION-JP-01

- [ ] **Code:** **Question:** A basic Desired state check fails. What would you do first using the CLI?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-02

- [ ] **Question:** A basic Controllers check fails. What would you do first?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-03

- [ ] **Question:** A basic Idempotency check fails. What would you do first?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-04

- [ ] **Code:** **Question:** A basic Retries check fails. What would you do first using the CLI?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-05

- [ ] **Question:** A basic Status conditions check fails. What would you do first?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-06

- [ ] **Question:** A basic Long-running operations check fails. What would you do first?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-07

- [ ] **Code:** **Question:** A basic Partial failure check fails. What would you do first using the CLI?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-08

- [ ] **Question:** A basic Rollback check fails. What would you do first?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-09

- [ ] **Question:** A basic Resource cleanup check fails. What would you do first?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PLATFORM-RECONCILIATION-JP-10

- [ ] **Code:** **Question:** A basic Desired state check fails. What would you do first using the CLI?
> **Covered in:** [Platform reconciliation — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### PLATFORM-RECONCILIATION-MN-01

- [ ] **Question:** Compare Desired state with Controllers. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Desired state: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Controllers: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-02

- [ ] **Question:** Compare Controllers with Idempotency. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Controllers: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Idempotency: makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-03

- [ ] **Question:** Compare Idempotency with Retries. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Idempotency: makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Retries: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-04

- [ ] **Configuration review:** **Question:** Compare Retries with Status conditions. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Retries: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Status conditions: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-05

- [ ] **Question:** Compare Status conditions with Long-running operations. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Status conditions: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Long-running operations: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-06

- [ ] **Question:** Compare Long-running operations with Partial failure. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Long-running operations: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Partial failure: means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-07

- [ ] **Configuration review:** **Question:** Compare Partial failure with Rollback. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Partial failure: means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Rollback: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-08

- [ ] **Question:** Compare Rollback with Resource cleanup. When would each change your design?
> **Covered in:** [Platform reconciliation — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** Rollback: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Resource cleanup: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-09

- [ ] **Question:** Compare Resource cleanup with Desired state. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Resource cleanup: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Desired state: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PLATFORM-RECONCILIATION-MN-10

- [ ] **Configuration review:** **Question:** Compare Desired state with Desired state. When would each change your design?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Desired state: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Desired state: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### PLATFORM-RECONCILIATION-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Desired state; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-02

- [ ] **Question:** Production is degraded around Controllers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Idempotency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-04

- [ ] **Question:** Production is degraded around Retries; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Status conditions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-06

- [ ] **Question:** Production is degraded around Long-running operations; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Partial failure; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-08

- [ ] **Question:** Production is degraded around Rollback; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Resource cleanup; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PLATFORM-RECONCILIATION-MP-10

- [ ] **Question:** Production is degraded around Desired state; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### PLATFORM-RECONCILIATION-SN-01

- [ ] **Question:** Design a production Platform reconciliation capability where Desired state, Retries and Partial failure are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Platform reconciliation capability where Controllers, Status conditions and Rollback are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-03

- [ ] **Question:** Design a production Platform reconciliation capability where Idempotency, Long-running operations and Resource cleanup are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Platform reconciliation capability where Retries, Partial failure and Desired state are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-05

- [ ] **Question:** Design a production Platform reconciliation capability where Status conditions, Rollback and Desired state are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Platform reconciliation capability where Long-running operations, Resource cleanup and Controllers are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-07

- [ ] **Question:** Design a production Platform reconciliation capability where Partial failure, Desired state and Idempotency are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Platform reconciliation capability where Rollback, Desired state and Retries are first-class requirements.
> **Covered in:** [Platform reconciliation — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-09

- [ ] **Question:** Design a production Platform reconciliation capability where Resource cleanup, Controllers and Status conditions are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PLATFORM-RECONCILIATION-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Platform reconciliation capability where Desired state, Idempotency and Long-running operations are first-class requirements.
> **Covered in:** [Platform reconciliation — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### PLATFORM-RECONCILIATION-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Desired state. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Controllers. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Idempotency. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. makes repeating the same logical operation converge on one intended effect, commonly through stable request keys and atomic deduplication records. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retries. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. repeat attempts for transient faults but require bounded budgets, deadlines, idempotency and jitter to avoid duplicate effects and retry storms. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Status conditions. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Long-running operations. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Partial failure. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. means one component or message can fail while others continue, so a timeout cannot prove whether a remote side effect occurred. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource cleanup. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PLATFORM-RECONCILIATION-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Desired state. How do you lead it end to end?
> **Covered in:** [Platform reconciliation — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Platform reconciliation; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Platform APIs](../04-platform-apis/README.md) · [Study note](README.md) · [Next: Developer experience →](../06-developer-experience/README.md)

<!-- reading-navigation:end -->
