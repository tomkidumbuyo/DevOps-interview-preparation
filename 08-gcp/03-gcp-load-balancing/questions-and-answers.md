# GCP load balancing — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-GCP-LOAD-BALANCING-JN-01

- [ ] **Question:** What is Global external Application Load Balancer, and why does it matter in GCP load balancing?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-LOAD-BALANCING-JN-02

- [ ] **Question:** What is Regional external Application Load Balancer, and why does it matter in GCP load balancing?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-LOAD-BALANCING-JN-03

- [ ] **Question:** What is Internal Application Load Balancer, and why does it matter in GCP load balancing?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-LOAD-BALANCING-JN-04

- [ ] **Question:** What is External proxy Network Load Balancer, and why does it matter in GCP load balancing?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-LOAD-BALANCING-JN-05

- [ ] **Question:** What is Passthrough Network Load Balancer, and why does it matter in GCP load balancing?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-LOAD-BALANCING-JN-06

- [ ] **Question:** What is Internal passthrough Network Load Balancer, and why does it matter in GCP load balancing?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-LOAD-BALANCING-JN-07

- [ ] **Question:** What is Backend services, and why does it matter in GCP load balancing?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-LOAD-BALANCING-JN-08

- [ ] **Code:** **Question:** What does `gcloud logging read 'severity>=ERROR' --limit=20` help you verify for GCP load balancing?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-LOAD-BALANCING-JN-09

- [ ] **Code:** **Question:** What does `gcloud auth list` help you verify for GCP load balancing?
> **Covered in:** [GCP load balancing — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-LOAD-BALANCING-JN-10

- [ ] **Code:** **Question:** What does `gcloud config list` help you verify for GCP load balancing?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-GCP-LOAD-BALANCING-JP-01

- [ ] **Code:** **Question:** A basic Global external Application Load Balancer check fails. What would you do first using the CLI?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-02

- [ ] **Question:** A basic Regional external Application Load Balancer check fails. What would you do first?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-03

- [ ] **Question:** A basic Internal Application Load Balancer check fails. What would you do first?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-04

- [ ] **Code:** **Question:** A basic External proxy Network Load Balancer check fails. What would you do first using the CLI?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-05

- [ ] **Question:** A basic Passthrough Network Load Balancer check fails. What would you do first?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-06

- [ ] **Question:** A basic Internal passthrough Network Load Balancer check fails. What would you do first?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-07

- [ ] **Code:** **Question:** A basic Backend services check fails. What would you do first using the CLI?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-08

- [ ] **Question:** A basic URL maps check fails. What would you do first?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-09

- [ ] **Question:** A basic Health checks check fails. What would you do first?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-LOAD-BALANCING-JP-10

- [ ] **Code:** **Question:** A basic Managed certificates check fails. What would you do first using the CLI?
> **Covered in:** [GCP load balancing — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-GCP-LOAD-BALANCING-MN-01

- [ ] **Question:** Compare Global external Application Load Balancer with Regional external Application Load Balancer. When would each change your design?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Global external Application Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Regional external Application Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-02

- [ ] **Question:** Compare Regional external Application Load Balancer with Internal Application Load Balancer. When would each change your design?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Regional external Application Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Internal Application Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-03

- [ ] **Question:** Compare Internal Application Load Balancer with External proxy Network Load Balancer. When would each change your design?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Internal Application Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. External proxy Network Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-04

- [ ] **Configuration review:** **Question:** Compare External proxy Network Load Balancer with Passthrough Network Load Balancer. When would each change your design?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** External proxy Network Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Passthrough Network Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-05

- [ ] **Question:** Compare Passthrough Network Load Balancer with Internal passthrough Network Load Balancer. When would each change your design?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Passthrough Network Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Internal passthrough Network Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-06

- [ ] **Question:** Compare Internal passthrough Network Load Balancer with Backend services. When would each change your design?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Internal passthrough Network Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Backend services: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-07

- [ ] **Configuration review:** **Question:** Compare Backend services with URL maps. When would each change your design?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Backend services: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. URL maps: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-08

- [ ] **Question:** Compare URL maps with Health checks. When would each change your design?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** URL maps: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Health checks: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-09

- [ ] **Question:** Compare Health checks with Managed certificates. When would each change your design?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Health checks: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Managed certificates: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-LOAD-BALANCING-MN-10

- [ ] **Configuration review:** **Question:** Compare Managed certificates with Global external Application Load Balancer. When would each change your design?
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Managed certificates: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Global external Application Load Balancer: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-GCP-LOAD-BALANCING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Global external Application Load Balancer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-02

- [ ] **Question:** Production is degraded around Regional external Application Load Balancer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Internal Application Load Balancer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-04

- [ ] **Question:** Production is degraded around External proxy Network Load Balancer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Passthrough Network Load Balancer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-06

- [ ] **Question:** Production is degraded around Internal passthrough Network Load Balancer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backend services; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-08

- [ ] **Question:** Production is degraded around URL maps; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Health checks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-LOAD-BALANCING-MP-10

- [ ] **Question:** Production is degraded around Managed certificates; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-GCP-LOAD-BALANCING-SN-01

- [ ] **Question:** Design a production GCP load balancing capability where Global external Application Load Balancer, External proxy Network Load Balancer and Backend services are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GCP load balancing capability where Regional external Application Load Balancer, Passthrough Network Load Balancer and URL maps are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-03

- [ ] **Question:** Design a production GCP load balancing capability where Internal Application Load Balancer, Internal passthrough Network Load Balancer and Health checks are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GCP load balancing capability where External proxy Network Load Balancer, Backend services and Managed certificates are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-05

- [ ] **Question:** Design a production GCP load balancing capability where Passthrough Network Load Balancer, URL maps and Global external Application Load Balancer are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GCP load balancing capability where Internal passthrough Network Load Balancer, Health checks and Regional external Application Load Balancer are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-07

- [ ] **Question:** Design a production GCP load balancing capability where Backend services, Managed certificates and Internal Application Load Balancer are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GCP load balancing capability where URL maps, Global external Application Load Balancer and External proxy Network Load Balancer are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-09

- [ ] **Question:** Design a production GCP load balancing capability where Health checks, Regional external Application Load Balancer and Passthrough Network Load Balancer are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-LOAD-BALANCING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GCP load balancing capability where Managed certificates, Internal Application Load Balancer and Internal passthrough Network Load Balancer are first-class requirements.
> **Covered in:** [GCP load balancing — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-GCP-LOAD-BALANCING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Global external Application Load Balancer. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Regional external Application Load Balancer. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Internal Application Load Balancer. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving External proxy Network Load Balancer. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Passthrough Network Load Balancer. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Internal passthrough Network Load Balancer. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backend services. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving URL maps. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Health checks. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-LOAD-BALANCING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed certificates. How do you lead it end to end?
> **Covered in:** [GCP load balancing — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP load balancing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: GCP networking](../02-gcp-networking/README.md) · [Study note](README.md) · [Next: GCP compute and containers →](../04-gcp-compute-and-containers/README.md)

<!-- reading-navigation:end -->
