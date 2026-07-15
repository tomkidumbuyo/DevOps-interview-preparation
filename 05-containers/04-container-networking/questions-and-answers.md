# Container networking — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CONTAINER-NETWORKING-JN-01

- [ ] **Question:** What is Bridge networking, and why does it matter in Container networking?
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONTAINER-NETWORKING-JN-02

- [ ] **Question:** What is Host networking, and why does it matter in Container networking?
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONTAINER-NETWORKING-JN-03

- [ ] **Question:** What is Port mapping, and why does it matter in Container networking?
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONTAINER-NETWORKING-JN-04

- [ ] **Question:** What is DNS, and why does it matter in Container networking?
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONTAINER-NETWORKING-JN-05

- [ ] **Question:** What is Overlay networks, and why does it matter in Container networking?
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONTAINER-NETWORKING-JN-06

- [ ] **Question:** What is Network namespaces, and why does it matter in Container networking?
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONTAINER-NETWORKING-JN-07

- [ ] **Question:** What is Service-to-service communication, and why does it matter in Container networking?
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CONTAINER-NETWORKING-JN-08

- [ ] **Code:** **Question:** What does `docker events --since 30m` help you verify for Container networking?
> **Covered in:** [Container networking — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### CONTAINER-NETWORKING-JN-09

- [ ] **Code:** **Question:** What does `docker image inspect IMAGE` help you verify for Container networking?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### CONTAINER-NETWORKING-JN-10

- [ ] **Code:** **Question:** What does `docker inspect CONTAINER` help you verify for Container networking?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### CONTAINER-NETWORKING-JP-01

- [ ] **Code:** **Question:** A basic Bridge networking check fails. What would you do first using the CLI?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-02

- [ ] **Question:** A basic Host networking check fails. What would you do first?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-03

- [ ] **Question:** A basic Port mapping check fails. What would you do first?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker stats --no-stream` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-04

- [ ] **Code:** **Question:** A basic DNS check fails. What would you do first using the CLI?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker events --since 30m` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-05

- [ ] **Question:** A basic Overlay networks check fails. What would you do first?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-06

- [ ] **Question:** A basic Network namespaces check fails. What would you do first?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-07

- [ ] **Code:** **Question:** A basic Service-to-service communication check fails. What would you do first using the CLI?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker stats --no-stream` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-08

- [ ] **Question:** A basic Bridge networking check fails. What would you do first?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker events --since 30m` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-09

- [ ] **Question:** A basic Host networking check fails. What would you do first?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CONTAINER-NETWORKING-JP-10

- [ ] **Code:** **Question:** A basic Port mapping check fails. What would you do first using the CLI?
> **Covered in:** [Container networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CONTAINER-NETWORKING-MN-01

- [ ] **Question:** Compare Bridge networking with Host networking. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Bridge networking: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Host networking: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-02

- [ ] **Question:** Compare Host networking with Port mapping. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Host networking: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Port mapping: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-03

- [ ] **Question:** Compare Port mapping with DNS. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Port mapping: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. DNS: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-04

- [ ] **Configuration review:** **Question:** Compare DNS with Overlay networks. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** DNS: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Overlay networks: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-05

- [ ] **Question:** Compare Overlay networks with Network namespaces. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Overlay networks: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Network namespaces: isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-06

- [ ] **Question:** Compare Network namespaces with Service-to-service communication. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Network namespaces: isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. Service-to-service communication: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-07

- [ ] **Configuration review:** **Question:** Compare Service-to-service communication with Bridge networking. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Service-to-service communication: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Bridge networking: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-08

- [ ] **Question:** Compare Bridge networking with Host networking. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Bridge networking: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Host networking: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-09

- [ ] **Question:** Compare Host networking with Port mapping. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Host networking: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Port mapping: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CONTAINER-NETWORKING-MN-10

- [ ] **Configuration review:** **Question:** Compare Port mapping with Bridge networking. When would each change your design?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Port mapping: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Bridge networking: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CONTAINER-NETWORKING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Bridge networking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-02

- [ ] **Question:** Production is degraded around Host networking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Port mapping; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker stats --no-stream` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-04

- [ ] **Question:** Production is degraded around DNS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker events --since 30m` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Overlay networks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-06

- [ ] **Question:** Production is degraded around Network namespaces; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Service-to-service communication; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker stats --no-stream` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-08

- [ ] **Question:** Production is degraded around Bridge networking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker events --since 30m` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Host networking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CONTAINER-NETWORKING-MP-10

- [ ] **Question:** Production is degraded around Port mapping; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CONTAINER-NETWORKING-SN-01

- [ ] **Question:** Design a production Container networking capability where Bridge networking, DNS and Service-to-service communication are first-class requirements.
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Container networking capability where Host networking, Overlay networks and Bridge networking are first-class requirements.
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-03

- [ ] **Question:** Design a production Container networking capability where Port mapping, Network namespaces and Host networking are first-class requirements.
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Container networking capability where DNS, Service-to-service communication and Port mapping are first-class requirements.
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-05

- [ ] **Question:** Design a production Container networking capability where Overlay networks, Bridge networking and Bridge networking are first-class requirements.
> **Covered in:** [Container networking — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Container networking capability where Network namespaces, Host networking and Host networking are first-class requirements.
> **Covered in:** [Container networking — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-07

- [ ] **Question:** Design a production Container networking capability where Service-to-service communication, Port mapping and Port mapping are first-class requirements.
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Container networking capability where Bridge networking, Bridge networking and DNS are first-class requirements.
> **Covered in:** [Container networking — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-09

- [ ] **Question:** Design a production Container networking capability where Host networking, Host networking and Overlay networks are first-class requirements.
> **Covered in:** [Container networking — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CONTAINER-NETWORKING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Container networking capability where Port mapping, Port mapping and Network namespaces are first-class requirements.
> **Covered in:** [Container networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CONTAINER-NETWORKING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Bridge networking. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Host networking. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Port mapping. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker stats --no-stream` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNS. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker events --since 30m` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Overlay networks. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network namespaces. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. isolate interfaces, routes, firewall rules and sockets; veth/bridge or routed links connect namespaces. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service-to-service communication. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker stats --no-stream` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Bridge networking. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker events --since 30m` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Host networking. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CONTAINER-NETWORKING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Port mapping. How do you lead it end to end?
> **Covered in:** [Container networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. is part of Container networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Docker runtime](../03-docker-runtime/README.md) · [Study note](README.md) · [Next: Container storage →](../05-container-storage/README.md)

<!-- reading-navigation:end -->
