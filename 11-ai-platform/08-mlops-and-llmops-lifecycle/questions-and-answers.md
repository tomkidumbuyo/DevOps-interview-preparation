# MLOps and LLMOps lifecycle — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-01

- [ ] **Question:** What is Experiment tracking, and why does it matter in MLOps and LLMOps lifecycle?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](02-experiment-tracking/README.md#architecture-and-lifecycle)

**Answer:** is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-02

- [ ] **Question:** What is Dataset versioning, and why does it matter in MLOps and LLMOps lifecycle?
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](03-data-versioning-quality-lineage/README.md#architecture-and-lifecycle)

**Answer:** is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-03

- [ ] **Question:** What is Prompt versioning, and why does it matter in MLOps and LLMOps lifecycle?
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](16-promptops/README.md#architecture-and-lifecycle)

**Answer:** is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-04

- [ ] **Question:** What is Model versioning, and why does it matter in MLOps and LLMOps lifecycle?
> **Covered in:** [MLOps and LLMOps lifecycle — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-05

- [ ] **Question:** What is Feature and embedding versioning, and why does it matter in MLOps and LLMOps lifecycle?
> **Covered in:** [MLOps and LLMOps lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-06

- [ ] **Question:** What is Model registry, and why does it matter in MLOps and LLMOps lifecycle?
> **Covered in:** [MLOps and LLMOps lifecycle — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-07

- [ ] **Question:** What is Artifact registry, and why does it matter in MLOps and LLMOps lifecycle?
> **Covered in:** [Model registry, artifacts and lineage — Architecture and lifecycle](10-model-registry-artifact-lineage/README.md#architecture-and-lifecycle)

**Answer:** is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-08

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for MLOps and LLMOps lifecycle?
> **Covered in:** [Model validation and release gates — Command lab](12-model-validation-release-gates/README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-09

- [ ] **Code:** **Question:** What does `nvidia-smi` help you verify for MLOps and LLMOps lifecycle?
> **Covered in:** [MLOps/LLMOps platform architecture — Architecture and lifecycle](01-lifecycle-platform-architecture/README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pods -A -o wide` help you verify for MLOps and LLMOps lifecycle?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-01

- [ ] **Code:** **Question:** A basic Experiment tracking check fails. What would you do first using the CLI?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-02

- [ ] **Question:** A basic Dataset versioning check fails. What would you do first?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-03

- [ ] **Question:** A basic Prompt versioning check fails. What would you do first?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-04

- [ ] **Code:** **Question:** A basic Model versioning check fails. What would you do first using the CLI?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-05

- [ ] **Question:** A basic Feature and embedding versioning check fails. What would you do first?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-06

- [ ] **Question:** A basic Model registry check fails. What would you do first?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-07

- [ ] **Code:** **Question:** A basic Artifact registry check fails. What would you do first using the CLI?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-08

- [ ] **Question:** A basic Lineage check fails. What would you do first?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-09

- [ ] **Question:** A basic Reproducibility check fails. What would you do first?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-JP-10

- [ ] **Code:** **Question:** A basic Training pipelines check fails. What would you do first using the CLI?
> **Covered in:** [MLOps and LLMOps lifecycle — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-01

- [ ] **Question:** Compare Experiment tracking with Dataset versioning. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Experiment tracking: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dataset versioning: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-02

- [ ] **Question:** Compare Dataset versioning with Prompt versioning. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Dataset versioning: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Prompt versioning: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-03

- [ ] **Question:** Compare Prompt versioning with Model versioning. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Prompt versioning: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model versioning: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-04

- [ ] **Configuration review:** **Question:** Compare Model versioning with Feature and embedding versioning. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model versioning: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Feature and embedding versioning: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-05

- [ ] **Question:** Compare Feature and embedding versioning with Model registry. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Feature and embedding versioning: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Model registry: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-06

- [ ] **Question:** Compare Model registry with Artifact registry. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Model registry: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Artifact registry: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-07

- [ ] **Configuration review:** **Question:** Compare Artifact registry with Lineage. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Artifact registry: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Lineage: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-08

- [ ] **Question:** Compare Lineage with Reproducibility. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Lineage: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Reproducibility: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-09

- [ ] **Question:** Compare Reproducibility with Training pipelines. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Reproducibility: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Training pipelines: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MN-10

- [ ] **Configuration review:** **Question:** Compare Training pipelines with Experiment tracking. When would each change your design?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Training pipelines: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Experiment tracking: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Experiment tracking; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-02

- [ ] **Question:** Production is degraded around Dataset versioning; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prompt versioning; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-04

- [ ] **Question:** Production is degraded around Model versioning; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Feature and embedding versioning; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-06

- [ ] **Question:** Production is degraded around Model registry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Artifact registry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-08

- [ ] **Question:** Production is degraded around Lineage; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Reproducibility; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-MP-10

- [ ] **Question:** Production is degraded around Training pipelines; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-01

- [ ] **Question:** Design a production MLOps and LLMOps lifecycle capability where Experiment tracking, Model versioning and Artifact registry are first-class requirements.
> **Covered in:** [MLOps and LLMOps lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps and LLMOps lifecycle capability where Dataset versioning, Feature and embedding versioning and Lineage are first-class requirements.
> **Covered in:** [Data versioning, quality and lineage — Architecture and lifecycle](03-data-versioning-quality-lineage/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-03

- [ ] **Question:** Design a production MLOps and LLMOps lifecycle capability where Prompt versioning, Model registry and Reproducibility are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](16-promptops/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps and LLMOps lifecycle capability where Model versioning, Artifact registry and Training pipelines are first-class requirements.
> **Covered in:** [MLOps and LLMOps lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-05

- [ ] **Question:** Design a production MLOps and LLMOps lifecycle capability where Feature and embedding versioning, Lineage and Experiment tracking are first-class requirements.
> **Covered in:** [MLOps and LLMOps lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps and LLMOps lifecycle capability where Model registry, Reproducibility and Dataset versioning are first-class requirements.
> **Covered in:** [PromptOps: prompt, template and policy lifecycle — Architecture and lifecycle](16-promptops/README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-07

- [ ] **Question:** Design a production MLOps and LLMOps lifecycle capability where Artifact registry, Training pipelines and Prompt versioning are first-class requirements.
> **Covered in:** [MLOps and LLMOps lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps and LLMOps lifecycle capability where Lineage, Experiment tracking and Model versioning are first-class requirements.
> **Covered in:** [MLOps and LLMOps lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-09

- [ ] **Question:** Design a production MLOps and LLMOps lifecycle capability where Reproducibility, Dataset versioning and Feature and embedding versioning are first-class requirements.
> **Covered in:** [MLOps and LLMOps lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps and LLMOps lifecycle capability where Training pipelines, Prompt versioning and Model registry are first-class requirements.
> **Covered in:** [MLOps and LLMOps lifecycle — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Experiment tracking. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dataset versioning. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt versioning. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model versioning. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Feature and embedding versioning. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model registry. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Artifact registry. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lineage. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reproducibility. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-MLOPS-AND-LLMOPS-LIFECYCLE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Training pipelines. How do you lead it end to end?
> **Covered in:** [MLOps and LLMOps lifecycle — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of MLOps and LLMOps lifecycle; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Evaluation reliability](../07-ai-evaluation-infrastructure/10-evaluation-reliability/README.md) · [Study note](README.md) · [Next: MLOps/LLMOps platform architecture →](01-lifecycle-platform-architecture/README.md)

<!-- reading-navigation:end -->
