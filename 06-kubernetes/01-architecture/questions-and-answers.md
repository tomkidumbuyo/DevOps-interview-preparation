# Architecture — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-ARCHITECTURE-JN-01

- [ ] **Question:** What is API groups/versions, and why does it matter in Architecture?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** resource kinds evolve through served/storage versions and conversion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ARCHITECTURE-JN-02

- [ ] **Question:** What is Request path, and why does it matter in Architecture?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ARCHITECTURE-JN-03

- [ ] **Question:** What is Controller loop, and why does it matter in Architecture?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** watches desired/observed state and performs level-based idempotent reconciliation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ARCHITECTURE-JN-04

- [ ] **Question:** What is Scheduler queue, and why does it matter in Architecture?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** unscheduled Pods progress through filtering/scoring/backoff before binding. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ARCHITECTURE-JN-05

- [ ] **Question:** What is API groups/versions, and why does it matter in Architecture?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** resource kinds evolve through served/storage versions and conversion. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ARCHITECTURE-JN-06

- [ ] **Question:** What is Request path, and why does it matter in Architecture?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ARCHITECTURE-JN-07

- [ ] **Question:** What is Controller loop, and why does it matter in Architecture?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** watches desired/observed state and performs level-based idempotent reconciliation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-ARCHITECTURE-JN-08

- [ ] **Code:** **Question:** What does `kubectl get events -A --field-selector=reason=FailedScheduling` help you verify for Architecture?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: unscheduled Pods progress through filtering/scoring/backoff before binding.

### BRANCH-ARCHITECTURE-JN-09

- [ ] **Code:** **Question:** What does `kubectl get --raw '/readyz?verbose'` help you verify for Architecture?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: resource kinds evolve through served/storage versions and conversion.

### BRANCH-ARCHITECTURE-JN-10

- [ ] **Code:** **Question:** What does `kubectl get events -A --field-selector=reason=FailedScheduling` help you verify for Architecture?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence.

## Junior — procedural and command questions

### BRANCH-ARCHITECTURE-JP-01

- [ ] **Code:** **Question:** A basic API groups/versions check fails. What would you do first using the CLI?
> **Covered in:** [Kubernetes API server and etcd — Command lab](01-api-server-etcd/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. resource kinds evolve through served/storage versions and conversion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-02

- [ ] **Question:** A basic Request path check fails. What would you do first?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-03

- [ ] **Question:** A basic Controller loop check fails. What would you do first?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. watches desired/observed state and performs level-based idempotent reconciliation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-04

- [ ] **Code:** **Question:** A basic Scheduler queue check fails. What would you do first using the CLI?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. unscheduled Pods progress through filtering/scoring/backoff before binding. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-05

- [ ] **Question:** A basic API groups/versions check fails. What would you do first?
> **Covered in:** [Kubernetes API server and etcd — Command lab](01-api-server-etcd/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. resource kinds evolve through served/storage versions and conversion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-06

- [ ] **Question:** A basic Request path check fails. What would you do first?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-07

- [ ] **Code:** **Question:** A basic Controller loop check fails. What would you do first using the CLI?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. watches desired/observed state and performs level-based idempotent reconciliation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-08

- [ ] **Question:** A basic Scheduler queue check fails. What would you do first?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. unscheduled Pods progress through filtering/scoring/backoff before binding. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-09

- [ ] **Question:** A basic API groups/versions check fails. What would you do first?
> **Covered in:** [Kubernetes API server and etcd — Command lab](01-api-server-etcd/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get --raw '/readyz?verbose'` and capture exact status/reason/request ID. resource kinds evolve through served/storage versions and conversion. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-ARCHITECTURE-JP-10

- [ ] **Code:** **Question:** A basic Request path check fails. What would you do first using the CLI?
> **Covered in:** [Architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-ARCHITECTURE-MN-01

- [ ] **Question:** Compare API groups/versions with Request path. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API groups/versions: resource kinds evolve through served/storage versions and conversion. Request path: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-02

- [ ] **Question:** Compare Request path with Controller loop. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Request path: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Controller loop: watches desired/observed state and performs level-based idempotent reconciliation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-03

- [ ] **Question:** Compare Controller loop with Scheduler queue. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Controller loop: watches desired/observed state and performs level-based idempotent reconciliation. Scheduler queue: unscheduled Pods progress through filtering/scoring/backoff before binding. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-04

- [ ] **Configuration review:** **Question:** Compare Scheduler queue with API groups/versions. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Scheduler queue: unscheduled Pods progress through filtering/scoring/backoff before binding. API groups/versions: resource kinds evolve through served/storage versions and conversion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-05

- [ ] **Question:** Compare API groups/versions with Request path. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API groups/versions: resource kinds evolve through served/storage versions and conversion. Request path: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-06

- [ ] **Question:** Compare Request path with Controller loop. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Request path: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Controller loop: watches desired/observed state and performs level-based idempotent reconciliation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-07

- [ ] **Configuration review:** **Question:** Compare Controller loop with Scheduler queue. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Controller loop: watches desired/observed state and performs level-based idempotent reconciliation. Scheduler queue: unscheduled Pods progress through filtering/scoring/backoff before binding. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-08

- [ ] **Question:** Compare Scheduler queue with API groups/versions. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Scheduler queue: unscheduled Pods progress through filtering/scoring/backoff before binding. API groups/versions: resource kinds evolve through served/storage versions and conversion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-09

- [ ] **Question:** Compare API groups/versions with Request path. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API groups/versions: resource kinds evolve through served/storage versions and conversion. Request path: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-ARCHITECTURE-MN-10

- [ ] **Configuration review:** **Question:** Compare Request path with API groups/versions. When would each change your design?
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Request path: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. API groups/versions: resource kinds evolve through served/storage versions and conversion. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-ARCHITECTURE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around API groups/versions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. resource kinds evolve through served/storage versions and conversion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-02

- [ ] **Question:** Production is degraded around Request path; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Controller loop; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. watches desired/observed state and performs level-based idempotent reconciliation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-04

- [ ] **Question:** Production is degraded around Scheduler queue; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. unscheduled Pods progress through filtering/scoring/backoff before binding. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around API groups/versions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. resource kinds evolve through served/storage versions and conversion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-06

- [ ] **Question:** Production is degraded around Request path; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Controller loop; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. watches desired/observed state and performs level-based idempotent reconciliation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-08

- [ ] **Question:** Production is degraded around Scheduler queue; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. unscheduled Pods progress through filtering/scoring/backoff before binding. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around API groups/versions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get --raw '/readyz?verbose'` plus recent events/changes, then correlate the service-specific SLI. resource kinds evolve through served/storage versions and conversion. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-ARCHITECTURE-MP-10

- [ ] **Question:** Production is degraded around Request path; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-ARCHITECTURE-SN-01

- [ ] **Question:** Design a production Architecture capability where API groups/versions, Scheduler queue and Controller loop are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resource kinds evolve through served/storage versions and conversion. unscheduled Pods progress through filtering/scoring/backoff before binding. watches desired/observed state and performs level-based idempotent reconciliation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Architecture capability where Request path, API groups/versions and Scheduler queue are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. resource kinds evolve through served/storage versions and conversion. unscheduled Pods progress through filtering/scoring/backoff before binding. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-03

- [ ] **Question:** Design a production Architecture capability where Controller loop, Request path and API groups/versions are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: watches desired/observed state and performs level-based idempotent reconciliation. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. resource kinds evolve through served/storage versions and conversion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Architecture capability where Scheduler queue, Controller loop and Request path are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: unscheduled Pods progress through filtering/scoring/backoff before binding. watches desired/observed state and performs level-based idempotent reconciliation. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-05

- [ ] **Question:** Design a production Architecture capability where API groups/versions, Scheduler queue and API groups/versions are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resource kinds evolve through served/storage versions and conversion. unscheduled Pods progress through filtering/scoring/backoff before binding. resource kinds evolve through served/storage versions and conversion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Architecture capability where Request path, API groups/versions and Request path are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. resource kinds evolve through served/storage versions and conversion. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-07

- [ ] **Question:** Design a production Architecture capability where Controller loop, Request path and Controller loop are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: watches desired/observed state and performs level-based idempotent reconciliation. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. watches desired/observed state and performs level-based idempotent reconciliation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Architecture capability where Scheduler queue, API groups/versions and Scheduler queue are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: unscheduled Pods progress through filtering/scoring/backoff before binding. resource kinds evolve through served/storage versions and conversion. unscheduled Pods progress through filtering/scoring/backoff before binding. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-09

- [ ] **Question:** Design a production Architecture capability where API groups/versions, Request path and API groups/versions are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: resource kinds evolve through served/storage versions and conversion. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. resource kinds evolve through served/storage versions and conversion. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-ARCHITECTURE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Architecture capability where Request path, Controller loop and Request path are first-class requirements.
> **Covered in:** [Architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. watches desired/observed state and performs level-based idempotent reconciliation. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-ARCHITECTURE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API groups/versions. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. resource kinds evolve through served/storage versions and conversion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Request path. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Controller loop. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. watches desired/observed state and performs level-based idempotent reconciliation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scheduler queue. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. unscheduled Pods progress through filtering/scoring/backoff before binding. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API groups/versions. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. resource kinds evolve through served/storage versions and conversion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Request path. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Controller loop. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. watches desired/observed state and performs level-based idempotent reconciliation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scheduler queue. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. unscheduled Pods progress through filtering/scoring/backoff before binding. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving API groups/versions. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get --raw '/readyz?verbose'` as one read-only checkpoint, not the whole diagnosis. resource kinds evolve through served/storage versions and conversion. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-ARCHITECTURE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Request path. How do you lead it end to end?
> **Covered in:** [Architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. authentication, authorization, mutating admission, schema/defaulting, validating admission and persistence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Kubernetes core platform](../README.md) · [Study note](README.md) · [Next: Kubernetes API server and etcd →](01-api-server-etcd/README.md)

<!-- reading-navigation:end -->
