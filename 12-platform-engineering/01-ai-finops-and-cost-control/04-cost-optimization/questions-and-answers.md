# Cost optimization — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### COST-OPTIMIZATION-JN-01

- [ ] **Question:** What is Model right-sizing, and why does it matter in Cost optimization?
> **Covered in:** [Cost optimization — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-OPTIMIZATION-JN-02

- [ ] **Question:** What is Quantization, and why does it matter in Cost optimization?
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-OPTIMIZATION-JN-03

- [ ] **Question:** What is Continuous batching, and why does it matter in Cost optimization?
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-OPTIMIZATION-JN-04

- [ ] **Question:** What is Higher utilization, and why does it matter in Cost optimization?
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-OPTIMIZATION-JN-05

- [ ] **Question:** What is Model sharing, and why does it matter in Cost optimization?
> **Covered in:** [Cost optimization — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-OPTIMIZATION-JN-06

- [ ] **Question:** What is Scale-to-zero, and why does it matter in Cost optimization?
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-OPTIMIZATION-JN-07

- [ ] **Question:** What is Spot GPUs, and why does it matter in Cost optimization?
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### COST-OPTIMIZATION-JN-08

- [ ] **Code:** **Question:** What does `git diff --check` help you verify for Cost optimization?
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions.

### COST-OPTIMIZATION-JN-09

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Cost optimization?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### COST-OPTIMIZATION-JN-10

- [ ] **Code:** **Question:** What does `go test ./...` help you verify for Cost optimization?
> **Covered in:** [Cost optimization — Hands-on practice: setup → failure → verification → cleanup](README.md#hands-on-practice-setup-failure-verification-cleanup)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### COST-OPTIMIZATION-JP-01

- [ ] **Code:** **Question:** A basic Model right-sizing check fails. What would you do first using the CLI?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-02

- [ ] **Question:** A basic Quantization check fails. What would you do first?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-03

- [ ] **Question:** A basic Continuous batching check fails. What would you do first?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-04

- [ ] **Code:** **Question:** A basic Higher utilization check fails. What would you do first using the CLI?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-05

- [ ] **Question:** A basic Model sharing check fails. What would you do first?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-06

- [ ] **Question:** A basic Scale-to-zero check fails. What would you do first?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-07

- [ ] **Code:** **Question:** A basic Spot GPUs check fails. What would you do first using the CLI?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `shellcheck scripts/*.sh` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-08

- [ ] **Question:** A basic Reserved capacity check fails. What would you do first?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git diff --check` and capture exact status/reason/request ID. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-09

- [ ] **Question:** A basic Prompt caching check fails. What would you do first?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### COST-OPTIMIZATION-JP-10

- [ ] **Code:** **Question:** A basic Semantic caching check fails. What would you do first using the CLI?
> **Covered in:** [Cost optimization — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `go test ./...` and capture exact status/reason/request ID. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### COST-OPTIMIZATION-MN-01

- [ ] **Question:** Compare Model right-sizing with Quantization. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model right-sizing: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Quantization: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-02

- [ ] **Question:** Compare Quantization with Continuous batching. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Quantization: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Continuous batching: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-03

- [ ] **Question:** Compare Continuous batching with Higher utilization. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Continuous batching: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Higher utilization: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-04

- [ ] **Configuration review:** **Question:** Compare Higher utilization with Model sharing. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Higher utilization: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model sharing: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-05

- [ ] **Question:** Compare Model sharing with Scale-to-zero. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model sharing: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Scale-to-zero: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-06

- [ ] **Question:** Compare Scale-to-zero with Spot GPUs. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Scale-to-zero: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Spot GPUs: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-07

- [ ] **Configuration review:** **Question:** Compare Spot GPUs with Reserved capacity. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Spot GPUs: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Reserved capacity: must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-08

- [ ] **Question:** Compare Reserved capacity with Prompt caching. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Reserved capacity: must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Prompt caching: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-09

- [ ] **Question:** Compare Prompt caching with Semantic caching. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Prompt caching: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Semantic caching: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### COST-OPTIMIZATION-MN-10

- [ ] **Configuration review:** **Question:** Compare Semantic caching with Model right-sizing. When would each change your design?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Semantic caching: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model right-sizing: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### COST-OPTIMIZATION-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model right-sizing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-02

- [ ] **Question:** Production is degraded around Quantization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Continuous batching; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-04

- [ ] **Question:** Production is degraded around Higher utilization; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model sharing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-06

- [ ] **Question:** Production is degraded around Scale-to-zero; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Spot GPUs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `shellcheck scripts/*.sh` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-08

- [ ] **Question:** Production is degraded around Reserved capacity; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git diff --check` plus recent events/changes, then correlate the service-specific SLI. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prompt caching; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### COST-OPTIMIZATION-MP-10

- [ ] **Question:** Production is degraded around Semantic caching; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `go test ./...` plus recent events/changes, then correlate the service-specific SLI. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### COST-OPTIMIZATION-SN-01

- [ ] **Question:** Design a production Cost optimization capability where Model right-sizing, Higher utilization and Spot GPUs are first-class requirements.
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Cost optimization capability where Quantization, Model sharing and Reserved capacity are first-class requirements.
> **Covered in:** [Cost optimization — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-03

- [ ] **Question:** Design a production Cost optimization capability where Continuous batching, Scale-to-zero and Prompt caching are first-class requirements.
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Cost optimization capability where Higher utilization, Spot GPUs and Semantic caching are first-class requirements.
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-05

- [ ] **Question:** Design a production Cost optimization capability where Model sharing, Reserved capacity and Model right-sizing are first-class requirements.
> **Covered in:** [Cost optimization — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Cost optimization capability where Scale-to-zero, Prompt caching and Quantization are first-class requirements.
> **Covered in:** [Cost optimization — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-07

- [ ] **Question:** Design a production Cost optimization capability where Spot GPUs, Semantic caching and Continuous batching are first-class requirements.
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Cost optimization capability where Reserved capacity, Model right-sizing and Higher utilization are first-class requirements.
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-09

- [ ] **Question:** Design a production Cost optimization capability where Prompt caching, Quantization and Model sharing are first-class requirements.
> **Covered in:** [Cost optimization — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### COST-OPTIMIZATION-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Cost optimization capability where Semantic caching, Continuous batching and Scale-to-zero are first-class requirements.
> **Covered in:** [Cost optimization — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### COST-OPTIMIZATION-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model right-sizing. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Quantization. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Continuous batching. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Higher utilization. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model sharing. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Scale-to-zero. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Spot GPUs. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `shellcheck scripts/*.sh` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reserved capacity. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git diff --check` as one read-only checkpoint, not the whole diagnosis. must connect demand and work units to latency, errors, saturation, queueing, provisioning delay, headroom, failure domains and unit cost using measured distributions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt caching. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### COST-OPTIMIZATION-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Semantic caching. How do you lead it end to end?
> **Covered in:** [Cost optimization — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `go test ./...` as one read-only checkpoint, not the whole diagnosis. is part of Cost optimization; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Cost allocation](../03-cost-allocation/README.md) · [Study note](README.md) · [Next: Budget controls →](../05-budget-controls/README.md)

<!-- reading-navigation:end -->
