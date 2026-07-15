# Git security — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### GIT-SECURITY-JN-01

- [ ] **Question:** What is Signed commits, and why does it matter in Git security?
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GIT-SECURITY-JN-02

- [ ] **Question:** What is Signed tags, and why does it matter in Git security?
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GIT-SECURITY-JN-03

- [ ] **Question:** What is Secret detection, and why does it matter in Git security?
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GIT-SECURITY-JN-04

- [ ] **Question:** What is Repository permissions, and why does it matter in Git security?
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GIT-SECURITY-JN-05

- [ ] **Question:** What is Dependency updates, and why does it matter in Git security?
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GIT-SECURITY-JN-06

- [ ] **Question:** What is Signed commits, and why does it matter in Git security?
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GIT-SECURITY-JN-07

- [ ] **Question:** What is Signed tags, and why does it matter in Git security?
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GIT-SECURITY-JN-08

- [ ] **Code:** **Question:** What does `git verify-commit HEAD` help you verify for Git security?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### GIT-SECURITY-JN-09

- [ ] **Code:** **Question:** What does `git cat-file -p HEAD` help you verify for Git security?
> **Covered in:** [Git security — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### GIT-SECURITY-JN-10

- [ ] **Code:** **Question:** What does `git log --graph --oneline --decorate --all` help you verify for Git security?
> **Covered in:** [Git security — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### GIT-SECURITY-JP-01

- [ ] **Code:** **Question:** A basic Signed commits check fails. What would you do first using the CLI?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git cat-file -p HEAD` and capture exact status/reason/request ID. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-02

- [ ] **Question:** A basic Signed tags check fails. What would you do first?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --decorate --all` and capture exact status/reason/request ID. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-03

- [ ] **Question:** A basic Secret detection check fails. What would you do first?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-04

- [ ] **Code:** **Question:** A basic Repository permissions check fails. What would you do first using the CLI?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git verify-commit HEAD` and capture exact status/reason/request ID. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-05

- [ ] **Question:** A basic Dependency updates check fails. What would you do first?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git cat-file -p HEAD` and capture exact status/reason/request ID. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-06

- [ ] **Question:** A basic Signed commits check fails. What would you do first?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --decorate --all` and capture exact status/reason/request ID. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-07

- [ ] **Code:** **Question:** A basic Signed tags check fails. What would you do first using the CLI?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-08

- [ ] **Question:** A basic Secret detection check fails. What would you do first?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git verify-commit HEAD` and capture exact status/reason/request ID. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-09

- [ ] **Question:** A basic Repository permissions check fails. What would you do first?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git cat-file -p HEAD` and capture exact status/reason/request ID. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GIT-SECURITY-JP-10

- [ ] **Code:** **Question:** A basic Dependency updates check fails. What would you do first using the CLI?
> **Covered in:** [Git security — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --decorate --all` and capture exact status/reason/request ID. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### GIT-SECURITY-MN-01

- [ ] **Question:** Compare Signed commits with Signed tags. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Signed commits: bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Signed tags: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-02

- [ ] **Question:** Compare Signed tags with Secret detection. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Signed tags: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Secret detection: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-03

- [ ] **Question:** Compare Secret detection with Repository permissions. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Secret detection: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Repository permissions: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Repository permissions with Dependency updates. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Repository permissions: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dependency updates: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-05

- [ ] **Question:** Compare Dependency updates with Signed commits. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Dependency updates: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Signed commits: bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-06

- [ ] **Question:** Compare Signed commits with Signed tags. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Signed commits: bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Signed tags: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Signed tags with Secret detection. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Signed tags: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Secret detection: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-08

- [ ] **Question:** Compare Secret detection with Repository permissions. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Secret detection: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Repository permissions: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-09

- [ ] **Question:** Compare Repository permissions with Dependency updates. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Repository permissions: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dependency updates: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GIT-SECURITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Dependency updates with Signed commits. When would each change your design?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Dependency updates: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Signed commits: bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### GIT-SECURITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Signed commits; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git cat-file -p HEAD` plus recent events/changes, then correlate the service-specific SLI. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-02

- [ ] **Question:** Production is degraded around Signed tags; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --decorate --all` plus recent events/changes, then correlate the service-specific SLI. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Secret detection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-04

- [ ] **Question:** Production is degraded around Repository permissions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git verify-commit HEAD` plus recent events/changes, then correlate the service-specific SLI. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Dependency updates; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git cat-file -p HEAD` plus recent events/changes, then correlate the service-specific SLI. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-06

- [ ] **Question:** Production is degraded around Signed commits; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --decorate --all` plus recent events/changes, then correlate the service-specific SLI. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Signed tags; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-08

- [ ] **Question:** Production is degraded around Secret detection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git verify-commit HEAD` plus recent events/changes, then correlate the service-specific SLI. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Repository permissions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git cat-file -p HEAD` plus recent events/changes, then correlate the service-specific SLI. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GIT-SECURITY-MP-10

- [ ] **Question:** Production is degraded around Dependency updates; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --decorate --all` plus recent events/changes, then correlate the service-specific SLI. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### GIT-SECURITY-SN-01

- [ ] **Question:** Design a production Git security capability where Signed commits, Repository permissions and Signed tags are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Git security capability where Signed tags, Dependency updates and Secret detection are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-03

- [ ] **Question:** Design a production Git security capability where Secret detection, Signed commits and Repository permissions are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Git security capability where Repository permissions, Signed tags and Dependency updates are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-05

- [ ] **Question:** Design a production Git security capability where Dependency updates, Secret detection and Signed commits are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Git security capability where Signed commits, Repository permissions and Signed tags are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-07

- [ ] **Question:** Design a production Git security capability where Signed tags, Dependency updates and Secret detection are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Git security capability where Secret detection, Signed commits and Repository permissions are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-09

- [ ] **Question:** Design a production Git security capability where Repository permissions, Signed tags and Dependency updates are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GIT-SECURITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Git security capability where Dependency updates, Secret detection and Signed commits are first-class requirements.
> **Covered in:** [Git security — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### GIT-SECURITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signed commits. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git cat-file -p HEAD` as one read-only checkpoint, not the whole diagnosis. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signed tags. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --decorate --all` as one read-only checkpoint, not the whole diagnosis. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret detection. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Repository permissions. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git verify-commit HEAD` as one read-only checkpoint, not the whole diagnosis. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dependency updates. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git cat-file -p HEAD` as one read-only checkpoint, not the whole diagnosis. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signed commits. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --decorate --all` as one read-only checkpoint, not the whole diagnosis. bind a commit object to a verified signing identity but do not prove code safety or reviewer authorization by themselves. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Signed tags. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret detection. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git verify-commit HEAD` as one read-only checkpoint, not the whole diagnosis. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Repository permissions. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git cat-file -p HEAD` as one read-only checkpoint, not the whole diagnosis. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GIT-SECURITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dependency updates. How do you lead it end to end?
> **Covered in:** [Git security — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --decorate --all` as one read-only checkpoint, not the whole diagnosis. is part of Git security; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Release management](../05-release-management/README.md) · [Study note](README.md) · [Next: Container fundamentals →](../../05-containers/README.md)

<!-- reading-navigation:end -->
