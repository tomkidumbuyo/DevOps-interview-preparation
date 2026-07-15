# Container fundamentals — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-CONTAINER-FUNDAMENTALS-JN-01

- [ ] **Question:** What is Namespaces, and why does it matter in Container fundamentals?
> **Covered in:** [Container fundamentals — Easy mode: the mental model](README.md#easy-mode-the-mental-model)

**Answer:** isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-02

- [ ] **Question:** What is Control groups, and why does it matter in Container fundamentals?
> **Covered in:** [Container internals — Complete curriculum checklist](01-container-internals/README.md#complete-curriculum-checklist)

**Answer:** is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-03

- [ ] **Question:** What is Capabilities, and why does it matter in Container fundamentals?
> **Covered in:** [Container fundamentals — Easy mode: the mental model](README.md#easy-mode-the-mental-model)

**Answer:** is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-04

- [ ] **Question:** What is Seccomp, and why does it matter in Container fundamentals?
> **Covered in:** [Container fundamentals — Easy mode: the mental model](README.md#easy-mode-the-mental-model)

**Answer:** filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-05

- [ ] **Question:** What is Union filesystems, and why does it matter in Container fundamentals?
> **Covered in:** [Container internals — Complete curriculum checklist](01-container-internals/README.md#complete-curriculum-checklist)

**Answer:** is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-06

- [ ] **Question:** What is OverlayFS, and why does it matter in Container fundamentals?
> **Covered in:** [Container fundamentals — Easy mode: the mental model](README.md#easy-mode-the-mental-model)

**Answer:** presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-07

- [ ] **Question:** What is Container runtimes, and why does it matter in Container fundamentals?
> **Covered in:** [Container fundamentals — Easy mode: the mental model](README.md#easy-mode-the-mental-model)

**Answer:** is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-08

- [ ] **Code:** **Question:** What does `docker events --since 30m` help you verify for Container fundamentals?
> **Covered in:** [Docker runtime — Command and configuration lab](03-docker-runtime/README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-09

- [ ] **Code:** **Question:** What does `docker image inspect IMAGE` help you verify for Container fundamentals?
> **Covered in:** [Container fundamentals — Image construction: easy to production](README.md#image-construction-easy-to-production)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-CONTAINER-FUNDAMENTALS-JN-10

- [ ] **Code:** **Question:** What does `docker inspect CONTAINER` help you verify for Container fundamentals?
> **Covered in:** [Container fundamentals — Easy mode: the mental model](README.md#easy-mode-the-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-CONTAINER-FUNDAMENTALS-JP-01

- [ ] **Code:** **Question:** A basic Namespaces check fails. What would you do first using the CLI?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-02

- [ ] **Question:** A basic Control groups check fails. What would you do first?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-03

- [ ] **Question:** A basic Capabilities check fails. What would you do first?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker stats --no-stream` and capture exact status/reason/request ID. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-04

- [ ] **Code:** **Question:** A basic Seccomp check fails. What would you do first using the CLI?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker events --since 30m` and capture exact status/reason/request ID. filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-05

- [ ] **Question:** A basic Union filesystems check fails. What would you do first?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-06

- [ ] **Question:** A basic OverlayFS check fails. What would you do first?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-07

- [ ] **Code:** **Question:** A basic Container runtimes check fails. What would you do first using the CLI?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker stats --no-stream` and capture exact status/reason/request ID. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-08

- [ ] **Question:** A basic OCI specifications check fails. What would you do first?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker events --since 30m` and capture exact status/reason/request ID. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-09

- [ ] **Question:** A basic Image layers check fails. What would you do first?
> **Covered in:** [Docker images — Command and configuration lab](02-docker-images/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker image inspect IMAGE` and capture exact status/reason/request ID. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-CONTAINER-FUNDAMENTALS-JP-10

- [ ] **Code:** **Question:** A basic Dockerfiles check fails. What would you do first using the CLI?
> **Covered in:** [Container internals — Command and configuration lab](01-container-internals/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `docker inspect CONTAINER` and capture exact status/reason/request ID. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-CONTAINER-FUNDAMENTALS-MN-01

- [ ] **Question:** Compare Namespaces with Control groups. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Namespaces: isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. Control groups: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-02

- [ ] **Question:** Compare Control groups with Capabilities. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Control groups: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Capabilities: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-03

- [ ] **Question:** Compare Capabilities with Seccomp. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Capabilities: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Seccomp: filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-04

- [ ] **Configuration review:** **Question:** Compare Seccomp with Union filesystems. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Seccomp: filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. Union filesystems: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-05

- [ ] **Question:** Compare Union filesystems with OverlayFS. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Union filesystems: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. OverlayFS: presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-06

- [ ] **Question:** Compare OverlayFS with Container runtimes. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** OverlayFS: presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Container runtimes: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-07

- [ ] **Configuration review:** **Question:** Compare Container runtimes with OCI specifications. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Container runtimes: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. OCI specifications: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-08

- [ ] **Question:** Compare OCI specifications with Image layers. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** OCI specifications: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Image layers: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-09

- [ ] **Question:** Compare Image layers with Dockerfiles. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Image layers: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dockerfiles: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-CONTAINER-FUNDAMENTALS-MN-10

- [ ] **Configuration review:** **Question:** Compare Dockerfiles with Namespaces. When would each change your design?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Dockerfiles: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Namespaces: isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-CONTAINER-FUNDAMENTALS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Namespaces; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-02

- [ ] **Question:** Production is degraded around Control groups; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Capabilities; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker stats --no-stream` plus recent events/changes, then correlate the service-specific SLI. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-04

- [ ] **Question:** Production is degraded around Seccomp; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker events --since 30m` plus recent events/changes, then correlate the service-specific SLI. filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Union filesystems; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-06

- [ ] **Question:** Production is degraded around OverlayFS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Container runtimes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker stats --no-stream` plus recent events/changes, then correlate the service-specific SLI. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-08

- [ ] **Question:** Production is degraded around OCI specifications; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker events --since 30m` plus recent events/changes, then correlate the service-specific SLI. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Image layers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container fundamentals — Image construction: easy to production](README.md#image-construction-easy-to-production)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker image inspect IMAGE` plus recent events/changes, then correlate the service-specific SLI. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-CONTAINER-FUNDAMENTALS-MP-10

- [ ] **Question:** Production is degraded around Dockerfiles; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `docker inspect CONTAINER` plus recent events/changes, then correlate the service-specific SLI. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-CONTAINER-FUNDAMENTALS-SN-01

- [ ] **Question:** Design a production Container fundamentals capability where Namespaces, Seccomp and Container runtimes are first-class requirements.
> **Covered in:** [Container internals — Senior design checklist](01-container-internals/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Container fundamentals capability where Control groups, Union filesystems and OCI specifications are first-class requirements.
> **Covered in:** [Container internals — Complete curriculum checklist](01-container-internals/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-03

- [ ] **Question:** Design a production Container fundamentals capability where Capabilities, OverlayFS and Image layers are first-class requirements.
> **Covered in:** [Container fundamentals — Image construction: easy to production](README.md#image-construction-easy-to-production)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Container fundamentals capability where Seccomp, Container runtimes and Dockerfiles are first-class requirements.
> **Covered in:** [Container internals — Senior design checklist](01-container-internals/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-05

- [ ] **Question:** Design a production Container fundamentals capability where Union filesystems, OCI specifications and Namespaces are first-class requirements.
> **Covered in:** [Container internals — Complete curriculum checklist](01-container-internals/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Container fundamentals capability where OverlayFS, Image layers and Control groups are first-class requirements.
> **Covered in:** [Container internals — Complete curriculum checklist](01-container-internals/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-07

- [ ] **Question:** Design a production Container fundamentals capability where Container runtimes, Dockerfiles and Capabilities are first-class requirements.
> **Covered in:** [Container internals — Senior design checklist](01-container-internals/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Container fundamentals capability where OCI specifications, Namespaces and Seccomp are first-class requirements.
> **Covered in:** [Container internals — Complete curriculum checklist](01-container-internals/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-09

- [ ] **Question:** Design a production Container fundamentals capability where Image layers, Control groups and Union filesystems are first-class requirements.
> **Covered in:** [Container internals — Complete curriculum checklist](01-container-internals/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-CONTAINER-FUNDAMENTALS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Container fundamentals capability where Dockerfiles, Capabilities and OverlayFS are first-class requirements.
> **Covered in:** [Container internals — Senior design checklist](01-container-internals/README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-CONTAINER-FUNDAMENTALS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Namespaces. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. isolate process-visible kernel resources such as PID, mount, network, IPC, UTS and user IDs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control groups. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Capabilities. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker stats --no-stream` as one read-only checkpoint, not the whole diagnosis. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Seccomp. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker events --since 30m` as one read-only checkpoint, not the whole diagnosis. filters allowed system calls to reduce kernel attack surface; profiles must match workload behavior and architecture. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Union filesystems. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OverlayFS. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. presents lower image layers plus an upper writable layer; copy-up and inode/storage behavior affect container performance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container runtimes. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker stats --no-stream` as one read-only checkpoint, not the whole diagnosis. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving OCI specifications. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker events --since 30m` as one read-only checkpoint, not the whole diagnosis. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Image layers. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker image inspect IMAGE` as one read-only checkpoint, not the whole diagnosis. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-CONTAINER-FUNDAMENTALS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dockerfiles. How do you lead it end to end?
> **Covered in:** [Container internals — Beginner → mid-level → senior learning path](01-container-internals/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `docker inspect CONTAINER` as one read-only checkpoint, not the whole diagnosis. is part of Container fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Git security](../04-git-delivery/06-git-security/README.md) · [Study note](README.md) · [Next: Container internals →](01-container-internals/README.md)

<!-- reading-navigation:end -->
