# Prompt governance — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### PROMPT-GOVERNANCE-JN-01

- [ ] **Question:** What is Prompt registry, and why does it matter in Prompt governance?
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPT-GOVERNANCE-JN-02

- [ ] **Question:** What is Prompt ownership, and why does it matter in Prompt governance?
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPT-GOVERNANCE-JN-03

- [ ] **Question:** What is Versioning, and why does it matter in Prompt governance?
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPT-GOVERNANCE-JN-04

- [ ] **Question:** What is Approval, and why does it matter in Prompt governance?
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPT-GOVERNANCE-JN-05

- [ ] **Question:** What is Testing, and why does it matter in Prompt governance?
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPT-GOVERNANCE-JN-06

- [ ] **Question:** What is Rollback, and why does it matter in Prompt governance?
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPT-GOVERNANCE-JN-07

- [ ] **Question:** What is Sensitive instructions, and why does it matter in Prompt governance?
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### PROMPT-GOVERNANCE-JN-08

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Prompt governance?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### PROMPT-GOVERNANCE-JN-09

- [ ] **Code:** **Question:** What does `nvidia-smi` help you verify for Prompt governance?
> **Covered in:** [Prompt governance — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### PROMPT-GOVERNANCE-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pods -A -o wide` help you verify for Prompt governance?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### PROMPT-GOVERNANCE-JP-01

- [ ] **Code:** **Question:** A basic Prompt registry check fails. What would you do first using the CLI?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-02

- [ ] **Question:** A basic Prompt ownership check fails. What would you do first?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-03

- [ ] **Question:** A basic Versioning check fails. What would you do first?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-04

- [ ] **Code:** **Question:** A basic Approval check fails. What would you do first using the CLI?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-05

- [ ] **Question:** A basic Testing check fails. What would you do first?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-06

- [ ] **Question:** A basic Rollback check fails. What would you do first?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-07

- [ ] **Code:** **Question:** A basic Sensitive instructions check fails. What would you do first using the CLI?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-08

- [ ] **Question:** A basic Change history check fails. What would you do first?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-09

- [ ] **Question:** A basic Prompt registry check fails. What would you do first?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### PROMPT-GOVERNANCE-JP-10

- [ ] **Code:** **Question:** A basic Prompt ownership check fails. What would you do first using the CLI?
> **Covered in:** [Prompt governance — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### PROMPT-GOVERNANCE-MN-01

- [ ] **Question:** Compare Prompt registry with Prompt ownership. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Prompt registry: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Prompt ownership: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-02

- [ ] **Question:** Compare Prompt ownership with Versioning. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Prompt ownership: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Versioning: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-03

- [ ] **Question:** Compare Versioning with Approval. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Versioning: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Approval: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-04

- [ ] **Configuration review:** **Question:** Compare Approval with Testing. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Approval: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Testing: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-05

- [ ] **Question:** Compare Testing with Rollback. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Testing: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Rollback: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-06

- [ ] **Question:** Compare Rollback with Sensitive instructions. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Rollback: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Sensitive instructions: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-07

- [ ] **Configuration review:** **Question:** Compare Sensitive instructions with Change history. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Sensitive instructions: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Change history: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-08

- [ ] **Question:** Compare Change history with Prompt registry. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Change history: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Prompt registry: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-09

- [ ] **Question:** Compare Prompt registry with Prompt ownership. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Prompt registry: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Prompt ownership: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### PROMPT-GOVERNANCE-MN-10

- [ ] **Configuration review:** **Question:** Compare Prompt ownership with Prompt registry. When would each change your design?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Prompt ownership: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Prompt registry: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### PROMPT-GOVERNANCE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prompt registry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-02

- [ ] **Question:** Production is degraded around Prompt ownership; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Versioning; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-04

- [ ] **Question:** Production is degraded around Approval; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Testing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-06

- [ ] **Question:** Production is degraded around Rollback; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Sensitive instructions; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-08

- [ ] **Question:** Production is degraded around Change history; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prompt registry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### PROMPT-GOVERNANCE-MP-10

- [ ] **Question:** Production is degraded around Prompt ownership; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### PROMPT-GOVERNANCE-SN-01

- [ ] **Question:** Design a production Prompt governance capability where Prompt registry, Approval and Sensitive instructions are first-class requirements.
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Prompt governance capability where Prompt ownership, Testing and Change history are first-class requirements.
> **Covered in:** [Prompt governance — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-03

- [ ] **Question:** Design a production Prompt governance capability where Versioning, Rollback and Prompt registry are first-class requirements.
> **Covered in:** [Prompt governance — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Prompt governance capability where Approval, Sensitive instructions and Prompt ownership are first-class requirements.
> **Covered in:** [Prompt governance — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-05

- [ ] **Question:** Design a production Prompt governance capability where Testing, Change history and Prompt registry are first-class requirements.
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Prompt governance capability where Rollback, Prompt registry and Prompt ownership are first-class requirements.
> **Covered in:** [Prompt governance — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-07

- [ ] **Question:** Design a production Prompt governance capability where Sensitive instructions, Prompt ownership and Versioning are first-class requirements.
> **Covered in:** [Prompt governance — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Prompt governance capability where Change history, Prompt registry and Approval are first-class requirements.
> **Covered in:** [Prompt governance — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-09

- [ ] **Question:** Design a production Prompt governance capability where Prompt registry, Prompt ownership and Testing are first-class requirements.
> **Covered in:** [Prompt governance — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### PROMPT-GOVERNANCE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Prompt governance capability where Prompt ownership, Versioning and Rollback are first-class requirements.
> **Covered in:** [Prompt governance — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### PROMPT-GOVERNANCE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt registry. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt ownership. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Versioning. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Approval. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Testing. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sensitive instructions. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Change history. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt registry. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### PROMPT-GOVERNANCE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt ownership. How do you lead it end to end?
> **Covered in:** [Prompt governance — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Prompt governance; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Data governance](../03-data-governance/README.md) · [Study note](README.md) · [Next: Policy enforcement →](../05-policy-enforcement/README.md)

<!-- reading-navigation:end -->
