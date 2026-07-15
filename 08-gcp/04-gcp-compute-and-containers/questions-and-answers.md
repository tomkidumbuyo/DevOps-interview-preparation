# GCP compute and containers — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-01

- [ ] **Question:** What is Compute Engine, and why does it matter in GCP compute and containers?
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-02

- [ ] **Question:** What is Machine families, and why does it matter in GCP compute and containers?
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-03

- [ ] **Question:** What is Managed Instance Groups, and why does it matter in GCP compute and containers?
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-04

- [ ] **Question:** What is Instance templates, and why does it matter in GCP compute and containers?
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-05

- [ ] **Question:** What is Autoscaling, and why does it matter in GCP compute and containers?
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-06

- [ ] **Question:** What is Spot VMs, and why does it matter in GCP compute and containers?
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-07

- [ ] **Question:** What is Reservations, and why does it matter in GCP compute and containers?
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-08

- [ ] **Code:** **Question:** What does `gcloud logging read 'severity>=ERROR' --limit=20` help you verify for GCP compute and containers?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-09

- [ ] **Code:** **Question:** What does `gcloud auth list` help you verify for GCP compute and containers?
> **Covered in:** [GCP compute and containers — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JN-10

- [ ] **Code:** **Question:** What does `gcloud config list` help you verify for GCP compute and containers?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-01

- [ ] **Code:** **Question:** A basic Compute Engine check fails. What would you do first using the CLI?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-02

- [ ] **Question:** A basic Machine families check fails. What would you do first?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-03

- [ ] **Question:** A basic Managed Instance Groups check fails. What would you do first?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-04

- [ ] **Code:** **Question:** A basic Instance templates check fails. What would you do first using the CLI?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-05

- [ ] **Question:** A basic Autoscaling check fails. What would you do first?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-06

- [ ] **Question:** A basic Spot VMs check fails. What would you do first?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-07

- [ ] **Code:** **Question:** A basic Reservations check fails. What would you do first using the CLI?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-08

- [ ] **Question:** A basic GPU VMs check fails. What would you do first?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-09

- [ ] **Question:** A basic Local SSD check fails. What would you do first?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-JP-10

- [ ] **Code:** **Question:** A basic GKE Standard check fails. What would you do first using the CLI?
> **Covered in:** [GCP compute and containers — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-01

- [ ] **Question:** Compare Compute Engine with Machine families. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Compute Engine: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Machine families: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-02

- [ ] **Question:** Compare Machine families with Managed Instance Groups. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Machine families: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Managed Instance Groups: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-03

- [ ] **Question:** Compare Managed Instance Groups with Instance templates. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Managed Instance Groups: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Instance templates: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-04

- [ ] **Configuration review:** **Question:** Compare Instance templates with Autoscaling. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Instance templates: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Autoscaling: must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-05

- [ ] **Question:** Compare Autoscaling with Spot VMs. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Autoscaling: must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Spot VMs: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-06

- [ ] **Question:** Compare Spot VMs with Reservations. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Spot VMs: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Reservations: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-07

- [ ] **Configuration review:** **Question:** Compare Reservations with GPU VMs. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Reservations: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. GPU VMs: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-08

- [ ] **Question:** Compare GPU VMs with Local SSD. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** GPU VMs: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Local SSD: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-09

- [ ] **Question:** Compare Local SSD with GKE Standard. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Local SSD: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. GKE Standard: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MN-10

- [ ] **Configuration review:** **Question:** Compare GKE Standard with Compute Engine. When would each change your design?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** GKE Standard: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compute Engine: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Compute Engine; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-02

- [ ] **Question:** Production is degraded around Machine families; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Managed Instance Groups; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-04

- [ ] **Question:** Production is degraded around Instance templates; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Autoscaling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-06

- [ ] **Question:** Production is degraded around Spot VMs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Reservations; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-08

- [ ] **Question:** Production is degraded around GPU VMs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Local SSD; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-MP-10

- [ ] **Question:** Production is degraded around GKE Standard; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-01

- [ ] **Question:** Design a production GCP compute and containers capability where Compute Engine, Instance templates and Reservations are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GCP compute and containers capability where Machine families, Autoscaling and GPU VMs are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-03

- [ ] **Question:** Design a production GCP compute and containers capability where Managed Instance Groups, Spot VMs and Local SSD are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GCP compute and containers capability where Instance templates, Reservations and GKE Standard are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-05

- [ ] **Question:** Design a production GCP compute and containers capability where Autoscaling, GPU VMs and Compute Engine are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GCP compute and containers capability where Spot VMs, Local SSD and Machine families are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-07

- [ ] **Question:** Design a production GCP compute and containers capability where Reservations, GKE Standard and Managed Instance Groups are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GCP compute and containers capability where GPU VMs, Compute Engine and Instance templates are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-09

- [ ] **Question:** Design a production GCP compute and containers capability where Local SSD, Machine families and Autoscaling are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GCP compute and containers capability where GKE Standard, Managed Instance Groups and Spot VMs are first-class requirements.
> **Covered in:** [GCP compute and containers — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Compute Engine. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Machine families. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Managed Instance Groups. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Instance templates. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Autoscaling. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Spot VMs. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reservations. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU VMs. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Local SSD. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-COMPUTE-AND-CONTAINERS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GKE Standard. How do you lead it end to end?
> **Covered in:** [GCP compute and containers — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP compute and containers; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: GCP load balancing](../03-gcp-load-balancing/README.md) · [Study note](README.md) · [Next: GCP storage and databases →](../05-gcp-storage-and-databases/README.md)

<!-- reading-navigation:end -->
