# Taking ownership of an existing platform — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-01

- [ ] **Question:** What is First 30, 60 and 90 days, and why does it matter in Taking ownership of an existing platform?

**Answer:** is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-02

- [ ] **Question:** What is Platform and dependency inventory, and why does it matter in Taking ownership of an existing platform?

**Answer:** is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-03

- [ ] **Question:** What is Identifying undocumented infrastructure, and why does it matter in Taking ownership of an existing platform?

**Answer:** is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-04

- [ ] **Question:** What is Detecting configuration drift, and why does it matter in Taking ownership of an existing platform?

**Answer:** is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-05

- [ ] **Question:** What is Establishing service ownership, and why does it matter in Taking ownership of an existing platform?

**Answer:** is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-06

- [ ] **Question:** What is Assessing production risks, and why does it matter in Taking ownership of an existing platform?

**Answer:** is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-07

- [ ] **Question:** What is Creating a platform backlog, and why does it matter in Taking ownership of an existing platform?

**Answer:** is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-08

- [ ] **Code:** **Question:** What does `git shortlog -sn` help you verify for Taking ownership of an existing platform?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-09

- [ ] **Code:** **Question:** What does `git log --since='30 days ago' --stat` help you verify for Taking ownership of an existing platform?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JN-10

- [ ] **Code:** **Question:** What does `kubectl get events -A --sort-by=.lastTimestamp` help you verify for Taking ownership of an existing platform?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-01

- [ ] **Code:** **Question:** A basic First 30, 60 and 90 days check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-02

- [ ] **Question:** A basic Platform and dependency inventory check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-03

- [ ] **Question:** A basic Identifying undocumented infrastructure check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-04

- [ ] **Code:** **Question:** A basic Detecting configuration drift check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git shortlog -sn` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-05

- [ ] **Question:** A basic Establishing service ownership check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-06

- [ ] **Question:** A basic Assessing production risks check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-07

- [ ] **Code:** **Question:** A basic Creating a platform backlog check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-08

- [ ] **Question:** A basic Identifying immediate safety improvements check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git shortlog -sn` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-09

- [ ] **Question:** A basic First 30, 60 and 90 days check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='30 days ago' --stat` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-JP-10

- [ ] **Code:** **Question:** A basic Platform and dependency inventory check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-01

- [ ] **Question:** Compare First 30, 60 and 90 days with Platform and dependency inventory. When would each change your design?

**Answer:** First 30, 60 and 90 days: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Platform and dependency inventory: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-02

- [ ] **Question:** Compare Platform and dependency inventory with Identifying undocumented infrastructure. When would each change your design?

**Answer:** Platform and dependency inventory: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Identifying undocumented infrastructure: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-03

- [ ] **Question:** Compare Identifying undocumented infrastructure with Detecting configuration drift. When would each change your design?

**Answer:** Identifying undocumented infrastructure: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Detecting configuration drift: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-04

- [ ] **Configuration review:** **Question:** Compare Detecting configuration drift with Establishing service ownership. When would each change your design?

**Answer:** Detecting configuration drift: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Establishing service ownership: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-05

- [ ] **Question:** Compare Establishing service ownership with Assessing production risks. When would each change your design?

**Answer:** Establishing service ownership: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Assessing production risks: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-06

- [ ] **Question:** Compare Assessing production risks with Creating a platform backlog. When would each change your design?

**Answer:** Assessing production risks: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Creating a platform backlog: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-07

- [ ] **Configuration review:** **Question:** Compare Creating a platform backlog with Identifying immediate safety improvements. When would each change your design?

**Answer:** Creating a platform backlog: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Identifying immediate safety improvements: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-08

- [ ] **Question:** Compare Identifying immediate safety improvements with First 30, 60 and 90 days. When would each change your design?

**Answer:** Identifying immediate safety improvements: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. First 30, 60 and 90 days: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-09

- [ ] **Question:** Compare First 30, 60 and 90 days with Platform and dependency inventory. When would each change your design?

**Answer:** First 30, 60 and 90 days: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Platform and dependency inventory: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MN-10

- [ ] **Configuration review:** **Question:** Compare Platform and dependency inventory with First 30, 60 and 90 days. When would each change your design?

**Answer:** Platform and dependency inventory: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. First 30, 60 and 90 days: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around First 30, 60 and 90 days; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-02

- [ ] **Question:** Production is degraded around Platform and dependency inventory; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Identifying undocumented infrastructure; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-04

- [ ] **Question:** Production is degraded around Detecting configuration drift; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git shortlog -sn` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Establishing service ownership; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-06

- [ ] **Question:** Production is degraded around Assessing production risks; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Creating a platform backlog; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-08

- [ ] **Question:** Production is degraded around Identifying immediate safety improvements; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git shortlog -sn` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around First 30, 60 and 90 days; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='30 days ago' --stat` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-MP-10

- [ ] **Question:** Production is degraded around Platform and dependency inventory; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-01

- [ ] **Question:** Design a production Taking ownership of an existing platform capability where First 30, 60 and 90 days, Detecting configuration drift and Creating a platform backlog are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Taking ownership of an existing platform capability where Platform and dependency inventory, Establishing service ownership and Identifying immediate safety improvements are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-03

- [ ] **Question:** Design a production Taking ownership of an existing platform capability where Identifying undocumented infrastructure, Assessing production risks and First 30, 60 and 90 days are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Taking ownership of an existing platform capability where Detecting configuration drift, Creating a platform backlog and Platform and dependency inventory are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-05

- [ ] **Question:** Design a production Taking ownership of an existing platform capability where Establishing service ownership, Identifying immediate safety improvements and First 30, 60 and 90 days are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Taking ownership of an existing platform capability where Assessing production risks, First 30, 60 and 90 days and Platform and dependency inventory are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-07

- [ ] **Question:** Design a production Taking ownership of an existing platform capability where Creating a platform backlog, Platform and dependency inventory and Identifying undocumented infrastructure are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Taking ownership of an existing platform capability where Identifying immediate safety improvements, First 30, 60 and 90 days and Detecting configuration drift are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-09

- [ ] **Question:** Design a production Taking ownership of an existing platform capability where First 30, 60 and 90 days, Platform and dependency inventory and Establishing service ownership are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Taking ownership of an existing platform capability where Platform and dependency inventory, Identifying undocumented infrastructure and Assessing production risks are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving First 30, 60 and 90 days. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Platform and dependency inventory. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Identifying undocumented infrastructure. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Detecting configuration drift. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git shortlog -sn` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Establishing service ownership. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Assessing production risks. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Creating a platform backlog. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Identifying immediate safety improvements. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git shortlog -sn` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving First 30, 60 and 90 days. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='30 days ago' --stat` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TAKING-OWNERSHIP-OF-AN-EXISTING-PLATFORM-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Platform and dependency inventory. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Taking ownership of an existing platform; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
