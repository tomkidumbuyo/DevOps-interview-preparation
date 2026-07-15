# Interview and role-ownership framework — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-01

- [ ] **Question:** What is AI Platform Engineer versus DevOps Engineer, and why does it matter in Interview and role-ownership framework?
> **Covered in:** [Interview and role-ownership framework — Role mental model](README.md#role-mental-model)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-02

- [ ] **Question:** What is AI Platform Engineer versus MLOps Engineer, and why does it matter in Interview and role-ownership framework?
> **Covered in:** [Interview and role-ownership framework — Role mental model](README.md#role-mental-model)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-03

- [ ] **Question:** What is Platform ownership versus project delivery, and why does it matter in Interview and role-ownership framework?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-04

- [ ] **Question:** What is Control plane versus data plane, and why does it matter in Interview and role-ownership framework?
> **Covered in:** [Interview and role-ownership framework — Interview answer patterns](README.md#interview-answer-patterns)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-05

- [ ] **Question:** What is Product platform versus customer deployment, and why does it matter in Interview and role-ownership framework?
> **Covered in:** [Interview and role-ownership framework — Role mental model](README.md#role-mental-model)

**Answer:** is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-06

- [ ] **Question:** What is Removing operational load from engineering leadership, and why does it matter in Interview and role-ownership framework?
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-07

- [ ] **Question:** What is Enabling developer self-service, and why does it matter in Interview and role-ownership framework?
> **Covered in:** [Interview and role-ownership framework — Interview answer patterns](README.md#interview-answer-patterns)

**Answer:** is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-08

- [ ] **Code:** **Question:** What does `git shortlog -sn` help you verify for Interview and role-ownership framework?
> **Covered in:** [Interview and role-ownership framework — Interview answer patterns](README.md#interview-answer-patterns)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-09

- [ ] **Code:** **Question:** What does `git log --since='30 days ago' --stat` help you verify for Interview and role-ownership framework?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JN-10

- [ ] **Code:** **Question:** What does `kubectl get events -A --sort-by=.lastTimestamp` help you verify for Interview and role-ownership framework?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-01

- [ ] **Code:** **Question:** A basic AI Platform Engineer versus DevOps Engineer check fails. What would you do first using the CLI?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-02

- [ ] **Question:** A basic AI Platform Engineer versus MLOps Engineer check fails. What would you do first?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-03

- [ ] **Question:** A basic Platform ownership versus project delivery check fails. What would you do first?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-04

- [ ] **Code:** **Question:** A basic Control plane versus data plane check fails. What would you do first using the CLI?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git shortlog -sn` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-05

- [ ] **Question:** A basic Product platform versus customer deployment check fails. What would you do first?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-06

- [ ] **Question:** A basic Removing operational load from engineering leadership check fails. What would you do first?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-07

- [ ] **Code:** **Question:** A basic Enabling developer self-service check fails. What would you do first using the CLI?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-08

- [ ] **Question:** A basic Requirement discovery check fails. What would you do first?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git shortlog -sn` and capture exact status/reason/request ID. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-09

- [ ] **Question:** A basic Assumption identification check fails. What would you do first?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-JP-10

- [ ] **Code:** **Question:** A basic Architecture decision records check fails. What would you do first using the CLI?
> **Covered in:** [Understanding the role — Command and configuration lab](01-understanding-the-role/README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-01

- [ ] **Question:** Compare AI Platform Engineer versus DevOps Engineer with AI Platform Engineer versus MLOps Engineer. When would each change your design?
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** AI Platform Engineer versus DevOps Engineer: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. AI Platform Engineer versus MLOps Engineer: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-02

- [ ] **Question:** Compare AI Platform Engineer versus MLOps Engineer with Platform ownership versus project delivery. When would each change your design?
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** AI Platform Engineer versus MLOps Engineer: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Platform ownership versus project delivery: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-03

- [ ] **Question:** Compare Platform ownership versus project delivery with Control plane versus data plane. When would each change your design?
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Platform ownership versus project delivery: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Control plane versus data plane: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-04

- [ ] **Configuration review:** **Question:** Compare Control plane versus data plane with Product platform versus customer deployment. When would each change your design?
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Control plane versus data plane: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Product platform versus customer deployment: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-05

- [ ] **Question:** Compare Product platform versus customer deployment with Removing operational load from engineering leadership. When would each change your design?
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Product platform versus customer deployment: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Removing operational load from engineering leadership: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-06

- [ ] **Question:** Compare Removing operational load from engineering leadership with Enabling developer self-service. When would each change your design?
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Removing operational load from engineering leadership: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Enabling developer self-service: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-07

- [ ] **Configuration review:** **Question:** Compare Enabling developer self-service with Requirement discovery. When would each change your design?
> **Covered in:** [Understanding the role — Beginner → mid-level → senior learning path](01-understanding-the-role/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Enabling developer self-service: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Requirement discovery: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-08

- [ ] **Question:** Compare Requirement discovery with Assumption identification. When would each change your design?
> **Covered in:** [Understanding the role — Beginner → mid-level → senior learning path](01-understanding-the-role/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Requirement discovery: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Assumption identification: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-09

- [ ] **Question:** Compare Assumption identification with Architecture decision records. When would each change your design?
> **Covered in:** [Senior engineering expectations — Complete curriculum checklist](02-senior-engineering-expectations/README.md#complete-curriculum-checklist)

**Answer:** Assumption identification: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Architecture decision records: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MN-10

- [ ] **Configuration review:** **Question:** Compare Architecture decision records with AI Platform Engineer versus DevOps Engineer. When would each change your design?
> **Covered in:** [Understanding the role — Beginner → mid-level → senior learning path](01-understanding-the-role/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Architecture decision records: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. AI Platform Engineer versus DevOps Engineer: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around AI Platform Engineer versus DevOps Engineer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Interview and role-ownership framework — Role mental model](README.md#role-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-02

- [ ] **Question:** Production is degraded around AI Platform Engineer versus MLOps Engineer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Interview and role-ownership framework — Role mental model](README.md#role-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Platform ownership versus project delivery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Understanding the role — Beginner → mid-level → senior learning path](01-understanding-the-role/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-04

- [ ] **Question:** Production is degraded around Control plane versus data plane; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Understanding the role — Beginner → mid-level → senior learning path](01-understanding-the-role/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git shortlog -sn` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Product platform versus customer deployment; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Interview and role-ownership framework — Role mental model](README.md#role-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-06

- [ ] **Question:** Production is degraded around Removing operational load from engineering leadership; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Enabling developer self-service; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Understanding the role — Beginner → mid-level → senior learning path](01-understanding-the-role/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-08

- [ ] **Question:** Production is degraded around Requirement discovery; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Understanding the role — Beginner → mid-level → senior learning path](01-understanding-the-role/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git shortlog -sn` plus recent events/changes, then correlate the service-specific SLI. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Assumption identification; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Understanding the role — Beginner → mid-level → senior learning path](01-understanding-the-role/README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-MP-10

- [ ] **Question:** Production is degraded around Architecture decision records; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Understanding the role — Easy mode: mental model](01-understanding-the-role/README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-01

- [ ] **Question:** Design a production Interview and role-ownership framework capability where AI Platform Engineer versus DevOps Engineer, Control plane versus data plane and Enabling developer self-service are first-class requirements.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Interview and role-ownership framework capability where AI Platform Engineer versus MLOps Engineer, Product platform versus customer deployment and Requirement discovery are first-class requirements.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-03

- [ ] **Question:** Design a production Interview and role-ownership framework capability where Platform ownership versus project delivery, Removing operational load from engineering leadership and Assumption identification are first-class requirements.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Interview and role-ownership framework capability where Control plane versus data plane, Enabling developer self-service and Architecture decision records are first-class requirements.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-05

- [ ] **Question:** Design a production Interview and role-ownership framework capability where Product platform versus customer deployment, Requirement discovery and AI Platform Engineer versus DevOps Engineer are first-class requirements.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Interview and role-ownership framework capability where Removing operational load from engineering leadership, Assumption identification and AI Platform Engineer versus MLOps Engineer are first-class requirements.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-07

- [ ] **Question:** Design a production Interview and role-ownership framework capability where Enabling developer self-service, Architecture decision records and Platform ownership versus project delivery are first-class requirements.
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Interview and role-ownership framework capability where Requirement discovery, AI Platform Engineer versus DevOps Engineer and Control plane versus data plane are first-class requirements.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-09

- [ ] **Question:** Design a production Interview and role-ownership framework capability where Assumption identification, AI Platform Engineer versus MLOps Engineer and Product platform versus customer deployment are first-class requirements.
> **Covered in:** [Understanding the role — Complete curriculum checklist](01-understanding-the-role/README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Interview and role-ownership framework capability where Architecture decision records, Platform ownership versus project delivery and Removing operational load from engineering leadership are first-class requirements.
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AI Platform Engineer versus DevOps Engineer. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AI Platform Engineer versus MLOps Engineer. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Platform ownership versus project delivery. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control plane versus data plane. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git shortlog -sn` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Product platform versus customer deployment. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is a design comparison: define both sides, contrast mechanism and guarantees, then select using workload, failure, security, ownership and cost evidence rather than preference. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Removing operational load from engineering leadership. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Enabling developer self-service. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Requirement discovery. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git shortlog -sn` as one read-only checkpoint, not the whole diagnosis. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Assumption identification. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-INTERVIEW-AND-ROLE-OWNERSHIP-FRAMEWORK-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Architecture decision records. How do you lead it end to end?
> **Covered in:** [Interview and role-ownership framework — Senior ownership expectations](README.md#senior-ownership-expectations)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Interview and role-ownership framework; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Contents](../README.md) · [Study note](README.md) · [Next: Understanding the role →](01-understanding-the-role/README.md)

<!-- reading-navigation:end -->
