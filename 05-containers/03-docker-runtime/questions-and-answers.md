# Docker runtime — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### DOCKER-RUNTIME-JN-01

- [ ] **Question:** What is Container lifecycle, and why does it matter in Docker runtime?
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DOCKER-RUNTIME-JN-02

- [ ] **Question:** What is Entrypoint versus command, and why does it matter in Docker runtime?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DOCKER-RUNTIME-JN-03

- [ ] **Question:** What is Environment variables, and why does it matter in Docker runtime?
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DOCKER-RUNTIME-JN-04

- [ ] **Question:** What is Signals, and why does it matter in Docker runtime?
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DOCKER-RUNTIME-JN-05

- [ ] **Question:** What is Graceful shutdown, and why does it matter in Docker runtime?
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DOCKER-RUNTIME-JN-06

- [ ] **Question:** What is Health checks, and why does it matter in Docker runtime?
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DOCKER-RUNTIME-JN-07

- [ ] **Question:** What is Restart policies, and why does it matter in Docker runtime?
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DOCKER-RUNTIME-JN-08

- [ ] **Code:** **Question:** What does `docker events --since 30m` help you verify for Docker runtime?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### DOCKER-RUNTIME-JN-09

- [ ] **Code:** **Question:** What does `docker image inspect IMAGE` help you verify for Docker runtime?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### DOCKER-RUNTIME-JN-10

- [ ] **Code:** **Question:** What does `docker inspect CONTAINER` help you verify for Docker runtime?
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference.

## Junior — procedural and command questions

### DOCKER-RUNTIME-JP-01

- [ ] **Code:** **Question:** A basic Container lifecycle check fails. What would you do first using the CLI?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-02

- [ ] **Question:** A basic Entrypoint versus command check fails. What would you do first?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-03

- [ ] **Question:** A basic Environment variables check fails. What would you do first?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker stats --no-stream` and capture exact status/reason/request ID. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-04

- [ ] **Code:** **Question:** A basic Signals check fails. What would you do first using the CLI?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker events --since 30m` and capture exact status/reason/request ID. deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-05

- [ ] **Question:** A basic Graceful shutdown check fails. What would you do first?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-06

- [ ] **Question:** A basic Health checks check fails. What would you do first?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-07

- [ ] **Code:** **Question:** A basic Restart policies check fails. What would you do first using the CLI?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker stats --no-stream` and capture exact status/reason/request ID. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-08

- [ ] **Question:** A basic Resource limits check fails. What would you do first?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker events --since 30m` and capture exact status/reason/request ID. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-09

- [ ] **Question:** A basic Container lifecycle check fails. What would you do first?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DOCKER-RUNTIME-JP-10

- [ ] **Code:** **Question:** A basic Entrypoint versus command check fails. What would you do first using the CLI?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### DOCKER-RUNTIME-MN-01

- [ ] **Question:** Compare Container lifecycle with Entrypoint versus command. When would each change your design?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Container lifecycle: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Entrypoint versus command: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-02

- [ ] **Question:** Compare Entrypoint versus command with Environment variables. When would each change your design?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Entrypoint versus command: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Environment variables: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-03

- [ ] **Question:** Compare Environment variables with Signals. When would each change your design?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Environment variables: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Signals: deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-04

- [ ] **Configuration review:** **Question:** Compare Signals with Graceful shutdown. When would each change your design?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Signals: deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. Graceful shutdown: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-05

- [ ] **Question:** Compare Graceful shutdown with Health checks. When would each change your design?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Graceful shutdown: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Health checks: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-06

- [ ] **Question:** Compare Health checks with Restart policies. When would each change your design?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Health checks: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Restart policies: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-07

- [ ] **Configuration review:** **Question:** Compare Restart policies with Resource limits. When would each change your design?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Restart policies: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Resource limits: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-08

- [ ] **Question:** Compare Resource limits with Container lifecycle. When would each change your design?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Resource limits: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Container lifecycle: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-09

- [ ] **Question:** Compare Container lifecycle with Entrypoint versus command. When would each change your design?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Container lifecycle: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Entrypoint versus command: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DOCKER-RUNTIME-MN-10

- [ ] **Configuration review:** **Question:** Compare Entrypoint versus command with Container lifecycle. When would each change your design?
> **Covered in:** [Docker runtime — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Entrypoint versus command: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Container lifecycle: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### DOCKER-RUNTIME-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Container lifecycle; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-02

- [ ] **Question:** Production is degraded around Entrypoint versus command; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Environment variables; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker stats --no-stream` plus recent events/changes, then correlate the service-specific SLI. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-04

- [ ] **Question:** Production is degraded around Signals; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker events --since 30m` plus recent events/changes, then correlate the service-specific SLI. deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Graceful shutdown; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-06

- [ ] **Question:** Production is degraded around Health checks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Restart policies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker stats --no-stream` plus recent events/changes, then correlate the service-specific SLI. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-08

- [ ] **Question:** Production is degraded around Resource limits; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker events --since 30m` plus recent events/changes, then correlate the service-specific SLI. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Container lifecycle; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DOCKER-RUNTIME-MP-10

- [ ] **Question:** Production is degraded around Entrypoint versus command; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### DOCKER-RUNTIME-SN-01

- [ ] **Question:** Design a production Docker runtime capability where Container lifecycle, Signals and Restart policies are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Docker runtime capability where Entrypoint versus command, Graceful shutdown and Resource limits are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-03

- [ ] **Question:** Design a production Docker runtime capability where Environment variables, Health checks and Container lifecycle are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Docker runtime capability where Signals, Restart policies and Entrypoint versus command are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-05

- [ ] **Question:** Design a production Docker runtime capability where Graceful shutdown, Resource limits and Container lifecycle are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Docker runtime capability where Health checks, Container lifecycle and Entrypoint versus command are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-07

- [ ] **Question:** Design a production Docker runtime capability where Restart policies, Entrypoint versus command and Environment variables are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Docker runtime capability where Resource limits, Container lifecycle and Signals are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-09

- [ ] **Question:** Design a production Docker runtime capability where Container lifecycle, Entrypoint versus command and Graceful shutdown are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DOCKER-RUNTIME-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Docker runtime capability where Entrypoint versus command, Environment variables and Health checks are first-class requirements.
> **Covered in:** [Docker runtime — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### DOCKER-RUNTIME-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container lifecycle. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Entrypoint versus command. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Environment variables. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker stats --no-stream` as one read-only checkpoint, not the whole diagnosis. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signals. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker events --since 30m` as one read-only checkpoint, not the whole diagnosis. deliver asynchronous process notifications; SIGTERM enables cleanup while SIGKILL cannot be caught and risks unfinished work. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Graceful shutdown. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Health checks. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restart policies. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker stats --no-stream` as one read-only checkpoint, not the whole diagnosis. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource limits. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker events --since 30m` as one read-only checkpoint, not the whole diagnosis. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container lifecycle. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. is part of Docker runtime; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DOCKER-RUNTIME-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Entrypoint versus command. How do you lead it end to end?
> **Covered in:** [Docker runtime — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Docker images](../02-docker-images/README.md) · [Study note](README.md) · [Next: Container networking →](../04-container-networking/README.md)

<!-- reading-navigation:end -->
