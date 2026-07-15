# Training fundamentals — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### TRAINING-FUNDAMENTALS-JN-01

- [ ] **Question:** What is Training set, and why does it matter in Training fundamentals?
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-FUNDAMENTALS-JN-02

- [ ] **Question:** What is Validation set, and why does it matter in Training fundamentals?
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-FUNDAMENTALS-JN-03

- [ ] **Question:** What is Test set, and why does it matter in Training fundamentals?
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-FUNDAMENTALS-JN-04

- [ ] **Question:** What is Epochs, and why does it matter in Training fundamentals?
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-FUNDAMENTALS-JN-05

- [ ] **Question:** What is Batch size, and why does it matter in Training fundamentals?
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-FUNDAMENTALS-JN-06

- [ ] **Question:** What is Learning rate, and why does it matter in Training fundamentals?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-FUNDAMENTALS-JN-07

- [ ] **Question:** What is Loss, and why does it matter in Training fundamentals?
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### TRAINING-FUNDAMENTALS-JN-08

- [ ] **Code:** **Question:** What does `python -m pytest -q` help you verify for Training fundamentals?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### TRAINING-FUNDAMENTALS-JN-09

- [ ] **Code:** **Question:** What does `nvidia-smi` help you verify for Training fundamentals?
> **Covered in:** [Training fundamentals — Easy mode: mental model](README.md#easy-mode-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### TRAINING-FUNDAMENTALS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pods -A -o wide` help you verify for Training fundamentals?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### TRAINING-FUNDAMENTALS-JP-01

- [ ] **Code:** **Question:** A basic Training set check fails. What would you do first using the CLI?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-02

- [ ] **Question:** A basic Validation set check fails. What would you do first?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-03

- [ ] **Question:** A basic Test set check fails. What would you do first?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-04

- [ ] **Code:** **Question:** A basic Epochs check fails. What would you do first using the CLI?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-05

- [ ] **Question:** A basic Batch size check fails. What would you do first?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-06

- [ ] **Question:** A basic Learning rate check fails. What would you do first?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-07

- [ ] **Code:** **Question:** A basic Loss check fails. What would you do first using the CLI?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-08

- [ ] **Question:** A basic Optimizers check fails. What would you do first?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest -q` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-09

- [ ] **Question:** A basic Overfitting check fails. What would you do first?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### TRAINING-FUNDAMENTALS-JP-10

- [ ] **Code:** **Question:** A basic Underfitting check fails. What would you do first using the CLI?
> **Covered in:** [Training fundamentals — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o wide` and capture exact status/reason/request ID. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### TRAINING-FUNDAMENTALS-MN-01

- [ ] **Question:** Compare Training set with Validation set. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Training set: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Validation set: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-02

- [ ] **Question:** Compare Validation set with Test set. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Validation set: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Test set: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-03

- [ ] **Question:** Compare Test set with Epochs. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Test set: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Epochs: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-04

- [ ] **Configuration review:** **Question:** Compare Epochs with Batch size. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Epochs: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Batch size: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-05

- [ ] **Question:** Compare Batch size with Learning rate. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Batch size: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Learning rate: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-06

- [ ] **Question:** Compare Learning rate with Loss. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Learning rate: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Loss: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-07

- [ ] **Configuration review:** **Question:** Compare Loss with Optimizers. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Loss: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Optimizers: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-08

- [ ] **Question:** Compare Optimizers with Overfitting. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Optimizers: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Overfitting: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-09

- [ ] **Question:** Compare Overfitting with Underfitting. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Overfitting: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Underfitting: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### TRAINING-FUNDAMENTALS-MN-10

- [ ] **Configuration review:** **Question:** Compare Underfitting with Training set. When would each change your design?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Underfitting: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Training set: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### TRAINING-FUNDAMENTALS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Training set; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-02

- [ ] **Question:** Production is degraded around Validation set; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Test set; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-04

- [ ] **Question:** Production is degraded around Epochs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Batch size; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-06

- [ ] **Question:** Production is degraded around Learning rate; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Loss; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-08

- [ ] **Question:** Production is degraded around Optimizers; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest -q` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Overfitting; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### TRAINING-FUNDAMENTALS-MP-10

- [ ] **Question:** Production is degraded around Underfitting; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o wide` plus recent events/changes, then correlate the service-specific SLI. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### TRAINING-FUNDAMENTALS-SN-01

- [ ] **Question:** Design a production Training fundamentals capability where Training set, Epochs and Loss are first-class requirements.
> **Covered in:** [Training fundamentals — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Training fundamentals capability where Validation set, Batch size and Optimizers are first-class requirements.
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-03

- [ ] **Question:** Design a production Training fundamentals capability where Test set, Learning rate and Overfitting are first-class requirements.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Training fundamentals capability where Epochs, Loss and Underfitting are first-class requirements.
> **Covered in:** [Training fundamentals — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-05

- [ ] **Question:** Design a production Training fundamentals capability where Batch size, Optimizers and Training set are first-class requirements.
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Training fundamentals capability where Learning rate, Overfitting and Validation set are first-class requirements.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-07

- [ ] **Question:** Design a production Training fundamentals capability where Loss, Underfitting and Test set are first-class requirements.
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Training fundamentals capability where Optimizers, Training set and Epochs are first-class requirements.
> **Covered in:** [Training fundamentals — Senior design checklist](README.md#senior-design-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-09

- [ ] **Question:** Design a production Training fundamentals capability where Overfitting, Validation set and Batch size are first-class requirements.
> **Covered in:** [Training fundamentals — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### TRAINING-FUNDAMENTALS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Training fundamentals capability where Underfitting, Test set and Learning rate are first-class requirements.
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### TRAINING-FUNDAMENTALS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Training set. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Validation set. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Test set. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Epochs. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Batch size. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Learning rate. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Loss. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Optimizers. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest -q` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Overfitting. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### TRAINING-FUNDAMENTALS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Underfitting. How do you lead it end to end?
> **Covered in:** [Training fundamentals — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o wide` as one read-only checkpoint, not the whole diagnosis. is part of Training fundamentals; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Model types](../02-model-types/README.md) · [Study note](README.md) · [Next: Inference fundamentals →](../04-inference-fundamentals/README.md)

<!-- reading-navigation:end -->
