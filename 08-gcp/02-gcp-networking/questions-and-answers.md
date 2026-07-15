# GCP networking — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-GCP-NETWORKING-JN-01

- [ ] **Question:** What is Global VPCs, and why does it matter in GCP networking?
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-NETWORKING-JN-02

- [ ] **Question:** What is Subnets, and why does it matter in GCP networking?
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-NETWORKING-JN-03

- [ ] **Question:** What is Routes, and why does it matter in GCP networking?
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-NETWORKING-JN-04

- [ ] **Question:** What is Firewall rules, and why does it matter in GCP networking?
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-NETWORKING-JN-05

- [ ] **Question:** What is Hierarchical firewall policies, and why does it matter in GCP networking?
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-NETWORKING-JN-06

- [ ] **Question:** What is Cloud NAT, and why does it matter in GCP networking?
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-NETWORKING-JN-07

- [ ] **Question:** What is Private Google Access, and why does it matter in GCP networking?
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-NETWORKING-JN-08

- [ ] **Code:** **Question:** What does `gcloud logging read 'severity>=ERROR' --limit=20` help you verify for GCP networking?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-NETWORKING-JN-09

- [ ] **Code:** **Question:** What does `gcloud auth list` help you verify for GCP networking?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-NETWORKING-JN-10

- [ ] **Code:** **Question:** What does `gcloud config list` help you verify for GCP networking?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-GCP-NETWORKING-JP-01

- [ ] **Code:** **Question:** A basic Global VPCs check fails. What would you do first using the CLI?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-02

- [ ] **Question:** A basic Subnets check fails. What would you do first?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-03

- [ ] **Question:** A basic Routes check fails. What would you do first?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-04

- [ ] **Code:** **Question:** A basic Firewall rules check fails. What would you do first using the CLI?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-05

- [ ] **Question:** A basic Hierarchical firewall policies check fails. What would you do first?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-06

- [ ] **Question:** A basic Cloud NAT check fails. What would you do first?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-07

- [ ] **Code:** **Question:** A basic Private Google Access check fails. What would you do first using the CLI?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-08

- [ ] **Question:** A basic Private Service Connect check fails. What would you do first?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-09

- [ ] **Question:** A basic VPC peering check fails. What would you do first?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-NETWORKING-JP-10

- [ ] **Code:** **Question:** A basic Network Connectivity Center check fails. What would you do first using the CLI?
> **Covered in:** [GCP networking — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-GCP-NETWORKING-MN-01

- [ ] **Question:** Compare Global VPCs with Subnets. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Global VPCs: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Subnets: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-02

- [ ] **Question:** Compare Subnets with Routes. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Subnets: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Routes: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-03

- [ ] **Question:** Compare Routes with Firewall rules. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Routes: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Firewall rules: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-04

- [ ] **Configuration review:** **Question:** Compare Firewall rules with Hierarchical firewall policies. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Firewall rules: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Hierarchical firewall policies: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-05

- [ ] **Question:** Compare Hierarchical firewall policies with Cloud NAT. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Hierarchical firewall policies: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Cloud NAT: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-06

- [ ] **Question:** Compare Cloud NAT with Private Google Access. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Cloud NAT: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Private Google Access: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-07

- [ ] **Configuration review:** **Question:** Compare Private Google Access with Private Service Connect. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Private Google Access: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Private Service Connect: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-08

- [ ] **Question:** Compare Private Service Connect with VPC peering. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Private Service Connect: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. VPC peering: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-09

- [ ] **Question:** Compare VPC peering with Network Connectivity Center. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** VPC peering: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Network Connectivity Center: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-NETWORKING-MN-10

- [ ] **Configuration review:** **Question:** Compare Network Connectivity Center with Global VPCs. When would each change your design?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Network Connectivity Center: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Global VPCs: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-GCP-NETWORKING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Global VPCs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-02

- [ ] **Question:** Production is degraded around Subnets; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Routes; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-04

- [ ] **Question:** Production is degraded around Firewall rules; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Hierarchical firewall policies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-06

- [ ] **Question:** Production is degraded around Cloud NAT; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Private Google Access; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-08

- [ ] **Question:** Production is degraded around Private Service Connect; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC peering; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-NETWORKING-MP-10

- [ ] **Question:** Production is degraded around Network Connectivity Center; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-GCP-NETWORKING-SN-01

- [ ] **Question:** Design a production GCP networking capability where Global VPCs, Firewall rules and Private Google Access are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GCP networking capability where Subnets, Hierarchical firewall policies and Private Service Connect are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-03

- [ ] **Question:** Design a production GCP networking capability where Routes, Cloud NAT and VPC peering are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GCP networking capability where Firewall rules, Private Google Access and Network Connectivity Center are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-05

- [ ] **Question:** Design a production GCP networking capability where Hierarchical firewall policies, Private Service Connect and Global VPCs are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GCP networking capability where Cloud NAT, VPC peering and Subnets are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-07

- [ ] **Question:** Design a production GCP networking capability where Private Google Access, Network Connectivity Center and Routes are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GCP networking capability where Private Service Connect, Global VPCs and Firewall rules are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-09

- [ ] **Question:** Design a production GCP networking capability where VPC peering, Subnets and Hierarchical firewall policies are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-NETWORKING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GCP networking capability where Network Connectivity Center, Routes and Cloud NAT are first-class requirements.
> **Covered in:** [GCP networking — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-GCP-NETWORKING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Global VPCs. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Subnets. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Routes. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Firewall rules. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hierarchical firewall policies. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cloud NAT. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Private Google Access. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Private Service Connect. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC peering. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-NETWORKING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Network Connectivity Center. How do you lead it end to end?
> **Covered in:** [GCP networking — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP networking; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: GCP foundations and governance](../01-gcp-foundations-and-governance/README.md) · [Study note](README.md) · [Next: GCP load balancing →](../03-gcp-load-balancing/README.md)

<!-- reading-navigation:end -->
