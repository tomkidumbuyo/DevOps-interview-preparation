# CircleCI — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CIRCLECI-JN-01

- [ ] **Question:** What is Config file, and why does it matter in CircleCI?

**Answer:** `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CIRCLECI-JN-02

- [ ] **Question:** What is Pipeline, and why does it matter in CircleCI?

**Answer:** one triggered config evaluation carries values and parameters into one or more workflows. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CIRCLECI-JN-03

- [ ] **Question:** What is Workflow, and why does it matter in CircleCI?

**Answer:** orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CIRCLECI-JN-04

- [ ] **Question:** What is Job, and why does it matter in CircleCI?

**Answer:** named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CIRCLECI-JN-05

- [ ] **Question:** What is Step, and why does it matter in CircleCI?

**Answer:** checkout, run, cache, workspace, artifact and reusable command operations execute in order. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CIRCLECI-JN-06

- [ ] **Question:** What is Executor/resource class, and why does it matter in CircleCI?

**Answer:** defines runtime image/VM and compute size; trust, compatibility and cost differ. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CIRCLECI-JN-07

- [ ] **Question:** What is Reusable configuration, and why does it matter in CircleCI?

**Answer:** commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CIRCLECI-JN-08

- [ ] **Code:** **Question:** What does `circleci config pack .circleci/src` help you verify for CircleCI?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security.

### CIRCLECI-JN-09

- [ ] **Code:** **Question:** What does `circleci config validate .circleci/config.yml` help you verify for CircleCI?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: protected environment variables or short-lived identity are attached to authorized workflow jobs.

### CIRCLECI-JN-10

- [ ] **Code:** **Question:** What does `circleci config process .circleci/config.yml` help you verify for CircleCI?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: setup workflow and continuation generate a reviewed bounded second-stage config.

## Junior — procedural and command questions

### CIRCLECI-JP-01

- [ ] **Code:** **Question:** A basic Config file check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci config validate .circleci/config.yml` and capture exact status/reason/request ID. `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-02

- [ ] **Question:** A basic Pipeline check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci config process .circleci/config.yml` and capture exact status/reason/request ID. one triggered config evaluation carries values and parameters into one or more workflows. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-03

- [ ] **Question:** A basic Workflow check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci local execute --job test` and capture exact status/reason/request ID. orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-04

- [ ] **Code:** **Question:** A basic Job check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci config pack .circleci/src` and capture exact status/reason/request ID. named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-05

- [ ] **Question:** A basic Step check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci config validate .circleci/config.yml` and capture exact status/reason/request ID. checkout, run, cache, workspace, artifact and reusable command operations execute in order. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-06

- [ ] **Question:** A basic Executor/resource class check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci config process .circleci/config.yml` and capture exact status/reason/request ID. defines runtime image/VM and compute size; trust, compatibility and cost differ. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-07

- [ ] **Code:** **Question:** A basic Reusable configuration check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci local execute --job test` and capture exact status/reason/request ID. commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-08

- [ ] **Question:** A basic Workspace/cache/artifact check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci config pack .circleci/src` and capture exact status/reason/request ID. workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-09

- [ ] **Question:** A basic Context and OIDC check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci config validate .circleci/config.yml` and capture exact status/reason/request ID. protected environment variables or short-lived identity are attached to authorized workflow jobs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CIRCLECI-JP-10

- [ ] **Code:** **Question:** A basic Dynamic configuration check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `circleci config process .circleci/config.yml` and capture exact status/reason/request ID. setup workflow and continuation generate a reviewed bounded second-stage config. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CIRCLECI-MN-01

- [ ] **Question:** Compare Config file with Pipeline. When would each change your design?

**Answer:** Config file: `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. Pipeline: one triggered config evaluation carries values and parameters into one or more workflows. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-02

- [ ] **Question:** Compare Pipeline with Workflow. When would each change your design?

**Answer:** Pipeline: one triggered config evaluation carries values and parameters into one or more workflows. Workflow: orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-03

- [ ] **Question:** Compare Workflow with Job. When would each change your design?

**Answer:** Workflow: orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. Job: named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-04

- [ ] **Configuration review:** **Question:** Compare Job with Step. When would each change your design?

**Answer:** Job: named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. Step: checkout, run, cache, workspace, artifact and reusable command operations execute in order. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-05

- [ ] **Question:** Compare Step with Executor/resource class. When would each change your design?

**Answer:** Step: checkout, run, cache, workspace, artifact and reusable command operations execute in order. Executor/resource class: defines runtime image/VM and compute size; trust, compatibility and cost differ. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-06

- [ ] **Question:** Compare Executor/resource class with Reusable configuration. When would each change your design?

**Answer:** Executor/resource class: defines runtime image/VM and compute size; trust, compatibility and cost differ. Reusable configuration: commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-07

- [ ] **Configuration review:** **Question:** Compare Reusable configuration with Workspace/cache/artifact. When would each change your design?

**Answer:** Reusable configuration: commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. Workspace/cache/artifact: workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-08

- [ ] **Question:** Compare Workspace/cache/artifact with Context and OIDC. When would each change your design?

**Answer:** Workspace/cache/artifact: workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security. Context and OIDC: protected environment variables or short-lived identity are attached to authorized workflow jobs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-09

- [ ] **Question:** Compare Context and OIDC with Dynamic configuration. When would each change your design?

**Answer:** Context and OIDC: protected environment variables or short-lived identity are attached to authorized workflow jobs. Dynamic configuration: setup workflow and continuation generate a reviewed bounded second-stage config. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CIRCLECI-MN-10

- [ ] **Configuration review:** **Question:** Compare Dynamic configuration with Config file. When would each change your design?

**Answer:** Dynamic configuration: setup workflow and continuation generate a reviewed bounded second-stage config. Config file: `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CIRCLECI-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Config file; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci config validate .circleci/config.yml` plus recent events/changes, then correlate the service-specific SLI. `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-02

- [ ] **Question:** Production is degraded around Pipeline; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci config process .circleci/config.yml` plus recent events/changes, then correlate the service-specific SLI. one triggered config evaluation carries values and parameters into one or more workflows. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Workflow; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci local execute --job test` plus recent events/changes, then correlate the service-specific SLI. orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-04

- [ ] **Question:** Production is degraded around Job; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci config pack .circleci/src` plus recent events/changes, then correlate the service-specific SLI. named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Step; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci config validate .circleci/config.yml` plus recent events/changes, then correlate the service-specific SLI. checkout, run, cache, workspace, artifact and reusable command operations execute in order. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-06

- [ ] **Question:** Production is degraded around Executor/resource class; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci config process .circleci/config.yml` plus recent events/changes, then correlate the service-specific SLI. defines runtime image/VM and compute size; trust, compatibility and cost differ. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Reusable configuration; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci local execute --job test` plus recent events/changes, then correlate the service-specific SLI. commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-08

- [ ] **Question:** Production is degraded around Workspace/cache/artifact; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci config pack .circleci/src` plus recent events/changes, then correlate the service-specific SLI. workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Context and OIDC; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci config validate .circleci/config.yml` plus recent events/changes, then correlate the service-specific SLI. protected environment variables or short-lived identity are attached to authorized workflow jobs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CIRCLECI-MP-10

- [ ] **Question:** Production is degraded around Dynamic configuration; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `circleci config process .circleci/config.yml` plus recent events/changes, then correlate the service-specific SLI. setup workflow and continuation generate a reviewed bounded second-stage config. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CIRCLECI-SN-01

- [ ] **Question:** Design a production CircleCI capability where Config file, Job and Reusable configuration are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production CircleCI capability where Pipeline, Step and Workspace/cache/artifact are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: one triggered config evaluation carries values and parameters into one or more workflows. checkout, run, cache, workspace, artifact and reusable command operations execute in order. workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-03

- [ ] **Question:** Design a production CircleCI capability where Workflow, Executor/resource class and Context and OIDC are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. defines runtime image/VM and compute size; trust, compatibility and cost differ. protected environment variables or short-lived identity are attached to authorized workflow jobs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production CircleCI capability where Job, Reusable configuration and Dynamic configuration are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. setup workflow and continuation generate a reviewed bounded second-stage config. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-05

- [ ] **Question:** Design a production CircleCI capability where Step, Workspace/cache/artifact and Config file are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: checkout, run, cache, workspace, artifact and reusable command operations execute in order. workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security. `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production CircleCI capability where Executor/resource class, Context and OIDC and Pipeline are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: defines runtime image/VM and compute size; trust, compatibility and cost differ. protected environment variables or short-lived identity are attached to authorized workflow jobs. one triggered config evaluation carries values and parameters into one or more workflows. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-07

- [ ] **Question:** Design a production CircleCI capability where Reusable configuration, Dynamic configuration and Workflow are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. setup workflow and continuation generate a reviewed bounded second-stage config. orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production CircleCI capability where Workspace/cache/artifact, Config file and Job are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security. `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-09

- [ ] **Question:** Design a production CircleCI capability where Context and OIDC, Pipeline and Step are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: protected environment variables or short-lived identity are attached to authorized workflow jobs. one triggered config evaluation carries values and parameters into one or more workflows. checkout, run, cache, workspace, artifact and reusable command operations execute in order. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CIRCLECI-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production CircleCI capability where Dynamic configuration, Workflow and Executor/resource class are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: setup workflow and continuation generate a reviewed bounded second-stage config. orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. defines runtime image/VM and compute size; trust, compatibility and cost differ. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CIRCLECI-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Config file. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci config validate .circleci/config.yml` as one read-only checkpoint, not the whole diagnosis. `.circleci/config.yml` version 2.1 defines parameters, orbs, executors, commands, jobs and workflows. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pipeline. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci config process .circleci/config.yml` as one read-only checkpoint, not the whole diagnosis. one triggered config evaluation carries values and parameters into one or more workflows. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workflow. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci local execute --job test` as one read-only checkpoint, not the whole diagnosis. orchestrates jobs with fan-out/fan-in, requires, filters, approvals, scheduling and serial groups. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Job. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci config pack .circleci/src` as one read-only checkpoint, not the whole diagnosis. named steps execute in Docker, machine, macOS, Windows or self-hosted runner environment. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Step. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci config validate .circleci/config.yml` as one read-only checkpoint, not the whole diagnosis. checkout, run, cache, workspace, artifact and reusable command operations execute in order. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Executor/resource class. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci config process .circleci/config.yml` as one read-only checkpoint, not the whole diagnosis. defines runtime image/VM and compute size; trust, compatibility and cost differ. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reusable configuration. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci local execute --job test` as one read-only checkpoint, not the whole diagnosis. commands/executors/jobs and parameterized orbs reduce duplication but expand supply-chain trust. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workspace/cache/artifact. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci config pack .circleci/src` as one read-only checkpoint, not the whole diagnosis. workflow file transfer, dependency acceleration and retained evidence have distinct lifecycle/security. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Context and OIDC. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci config validate .circleci/config.yml` as one read-only checkpoint, not the whole diagnosis. protected environment variables or short-lived identity are attached to authorized workflow jobs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CIRCLECI-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dynamic configuration. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `circleci config process .circleci/config.yml` as one read-only checkpoint, not the whole diagnosis. setup workflow and continuation generate a reviewed bounded second-stage config. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
