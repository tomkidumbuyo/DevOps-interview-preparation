# Change integration — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### CHANGE-INTEGRATION-JN-01

- [ ] **Question:** What is Merge, and why does it matter in Change integration?

**Answer:** combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CHANGE-INTEGRATION-JN-02

- [ ] **Question:** What is Rebase, and why does it matter in Change integration?

**Answer:** replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CHANGE-INTEGRATION-JN-03

- [ ] **Question:** What is Cherry-pick, and why does it matter in Change integration?

**Answer:** is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CHANGE-INTEGRATION-JN-04

- [ ] **Question:** What is Revert, and why does it matter in Change integration?

**Answer:** is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CHANGE-INTEGRATION-JN-05

- [ ] **Question:** What is Reset, and why does it matter in Change integration?

**Answer:** is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CHANGE-INTEGRATION-JN-06

- [ ] **Question:** What is Merge, and why does it matter in Change integration?

**Answer:** combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CHANGE-INTEGRATION-JN-07

- [ ] **Question:** What is Rebase, and why does it matter in Change integration?

**Answer:** replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### CHANGE-INTEGRATION-JN-08

- [ ] **Code:** **Question:** What does `git verify-commit HEAD` help you verify for Change integration?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### CHANGE-INTEGRATION-JN-09

- [ ] **Code:** **Question:** What does `git cat-file -p HEAD` help you verify for Change integration?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### CHANGE-INTEGRATION-JN-10

- [ ] **Code:** **Question:** What does `git log --graph --oneline --decorate --all` help you verify for Change integration?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### CHANGE-INTEGRATION-JP-01

- [ ] **Code:** **Question:** A basic Merge check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git cat-file -p HEAD` and capture exact status/reason/request ID. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-02

- [ ] **Question:** A basic Rebase check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --decorate --all` and capture exact status/reason/request ID. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-03

- [ ] **Question:** A basic Cherry-pick check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-04

- [ ] **Code:** **Question:** A basic Revert check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git verify-commit HEAD` and capture exact status/reason/request ID. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-05

- [ ] **Question:** A basic Reset check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git cat-file -p HEAD` and capture exact status/reason/request ID. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-06

- [ ] **Question:** A basic Merge check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --decorate --all` and capture exact status/reason/request ID. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-07

- [ ] **Code:** **Question:** A basic Rebase check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-08

- [ ] **Question:** A basic Cherry-pick check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git verify-commit HEAD` and capture exact status/reason/request ID. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-09

- [ ] **Question:** A basic Revert check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git cat-file -p HEAD` and capture exact status/reason/request ID. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### CHANGE-INTEGRATION-JP-10

- [ ] **Code:** **Question:** A basic Reset check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --decorate --all` and capture exact status/reason/request ID. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### CHANGE-INTEGRATION-MN-01

- [ ] **Question:** Compare Merge with Rebase. When would each change your design?

**Answer:** Merge: combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Rebase: replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-02

- [ ] **Question:** Compare Rebase with Cherry-pick. When would each change your design?

**Answer:** Rebase: replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Cherry-pick: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-03

- [ ] **Question:** Compare Cherry-pick with Revert. When would each change your design?

**Answer:** Cherry-pick: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Revert: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-04

- [ ] **Configuration review:** **Question:** Compare Revert with Reset. When would each change your design?

**Answer:** Revert: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Reset: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-05

- [ ] **Question:** Compare Reset with Merge. When would each change your design?

**Answer:** Reset: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Merge: combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-06

- [ ] **Question:** Compare Merge with Rebase. When would each change your design?

**Answer:** Merge: combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Rebase: replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-07

- [ ] **Configuration review:** **Question:** Compare Rebase with Cherry-pick. When would each change your design?

**Answer:** Rebase: replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Cherry-pick: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-08

- [ ] **Question:** Compare Cherry-pick with Revert. When would each change your design?

**Answer:** Cherry-pick: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Revert: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-09

- [ ] **Question:** Compare Revert with Reset. When would each change your design?

**Answer:** Revert: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Reset: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### CHANGE-INTEGRATION-MN-10

- [ ] **Configuration review:** **Question:** Compare Reset with Merge. When would each change your design?

**Answer:** Reset: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Merge: combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### CHANGE-INTEGRATION-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Merge; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git cat-file -p HEAD` plus recent events/changes, then correlate the service-specific SLI. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-02

- [ ] **Question:** Production is degraded around Rebase; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --decorate --all` plus recent events/changes, then correlate the service-specific SLI. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cherry-pick; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-04

- [ ] **Question:** Production is degraded around Revert; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git verify-commit HEAD` plus recent events/changes, then correlate the service-specific SLI. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Reset; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git cat-file -p HEAD` plus recent events/changes, then correlate the service-specific SLI. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-06

- [ ] **Question:** Production is degraded around Merge; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --decorate --all` plus recent events/changes, then correlate the service-specific SLI. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rebase; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-08

- [ ] **Question:** Production is degraded around Cherry-pick; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git verify-commit HEAD` plus recent events/changes, then correlate the service-specific SLI. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Revert; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git cat-file -p HEAD` plus recent events/changes, then correlate the service-specific SLI. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### CHANGE-INTEGRATION-MP-10

- [ ] **Question:** Production is degraded around Reset; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --decorate --all` plus recent events/changes, then correlate the service-specific SLI. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### CHANGE-INTEGRATION-SN-01

- [ ] **Question:** Design a production Change integration capability where Merge, Revert and Rebase are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Change integration capability where Rebase, Reset and Cherry-pick are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-03

- [ ] **Question:** Design a production Change integration capability where Cherry-pick, Merge and Revert are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Change integration capability where Revert, Rebase and Reset are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-05

- [ ] **Question:** Design a production Change integration capability where Reset, Cherry-pick and Merge are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Change integration capability where Merge, Revert and Rebase are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-07

- [ ] **Question:** Design a production Change integration capability where Rebase, Reset and Cherry-pick are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Change integration capability where Cherry-pick, Merge and Revert are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-09

- [ ] **Question:** Design a production Change integration capability where Revert, Rebase and Reset are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### CHANGE-INTEGRATION-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Change integration capability where Reset, Cherry-pick and Merge are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### CHANGE-INTEGRATION-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Merge. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git cat-file -p HEAD` as one read-only checkpoint, not the whole diagnosis. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rebase. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --decorate --all` as one read-only checkpoint, not the whole diagnosis. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cherry-pick. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Revert. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git verify-commit HEAD` as one read-only checkpoint, not the whole diagnosis. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reset. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git cat-file -p HEAD` as one read-only checkpoint, not the whole diagnosis. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Merge. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --decorate --all` as one read-only checkpoint, not the whole diagnosis. combines histories with fast-forward or a merge commit, preserving ancestry and requiring semantic conflict resolution. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rebase. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. replays commits onto another base and creates new commit IDs; avoid rewriting history others depend on without coordination. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cherry-pick. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git verify-commit HEAD` as one read-only checkpoint, not the whole diagnosis. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Revert. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git cat-file -p HEAD` as one read-only checkpoint, not the whole diagnosis. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### CHANGE-INTEGRATION-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reset. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --decorate --all` as one read-only checkpoint, not the whole diagnosis. is part of Change integration; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
