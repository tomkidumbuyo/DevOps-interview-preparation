# Troubleshooting scenarios — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-01

- [ ] **Question:** What is GPU unavailable, and why does it matter in Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-02

- [ ] **Question:** What is GPU node cannot join, and why does it matter in Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-03

- [ ] **Question:** What is CUDA-driver mismatch, and why does it matter in Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-04

- [ ] **Question:** What is GPU Operator failure, and why does it matter in Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-05

- [ ] **Question:** What is Model will not load, and why does it matter in Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-06

- [ ] **Question:** What is GPU out-of-memory, and why does it matter in Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-07

- [ ] **Question:** What is Inference latency spike, and why does it matter in Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-08

- [ ] **Code:** **Question:** What does `git log --since='2 hours ago' --oneline` help you verify for Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-09

- [ ] **Code:** **Question:** What does `date -u; whoami; hostname` help you verify for Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get events -A --sort-by=.lastTimestamp` help you verify for Troubleshooting scenarios?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-01

- [ ] **Code:** **Question:** A basic GPU unavailable check fails. What would you do first using the CLI?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `date -u; whoami; hostname` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-02

- [ ] **Question:** A basic GPU node cannot join check fails. What would you do first?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-03

- [ ] **Question:** A basic CUDA-driver mismatch check fails. What would you do first?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-04

- [ ] **Code:** **Question:** A basic GPU Operator failure check fails. What would you do first using the CLI?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='2 hours ago' --oneline` and capture exact status/reason/request ID. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-05

- [ ] **Question:** A basic Model will not load check fails. What would you do first?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `date -u; whoami; hostname` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-06

- [ ] **Question:** A basic GPU out-of-memory check fails. What would you do first?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-07

- [ ] **Code:** **Question:** A basic Inference latency spike check fails. What would you do first using the CLI?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `terraform plan` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-08

- [ ] **Question:** A basic Time-to-first-token regression check fails. What would you do first?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --since='2 hours ago' --oneline` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-09

- [ ] **Question:** A basic Token throughput collapse check fails. What would you do first?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `date -u; whoami; hostname` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-TROUBLESHOOTING-SCENARIOS-JP-10

- [ ] **Code:** **Question:** A basic vLLM worker crash check fails. What would you do first using the CLI?
> **Covered in:** [Troubleshooting scenarios — Command and configuration lab](README.md#command-and-configuration-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --sort-by=.lastTimestamp` and capture exact status/reason/request ID. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-01

- [ ] **Question:** Compare GPU unavailable with GPU node cannot join. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** GPU unavailable: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. GPU node cannot join: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-02

- [ ] **Question:** Compare GPU node cannot join with CUDA-driver mismatch. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** GPU node cannot join: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. CUDA-driver mismatch: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-03

- [ ] **Question:** Compare CUDA-driver mismatch with GPU Operator failure. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** CUDA-driver mismatch: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. GPU Operator failure: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-04

- [ ] **Configuration review:** **Question:** Compare GPU Operator failure with Model will not load. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** GPU Operator failure: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Model will not load: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-05

- [ ] **Question:** Compare Model will not load with GPU out-of-memory. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Model will not load: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. GPU out-of-memory: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-06

- [ ] **Question:** Compare GPU out-of-memory with Inference latency spike. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** GPU out-of-memory: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Inference latency spike: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-07

- [ ] **Configuration review:** **Question:** Compare Inference latency spike with Time-to-first-token regression. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Inference latency spike: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Time-to-first-token regression: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-08

- [ ] **Question:** Compare Time-to-first-token regression with Token throughput collapse. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Time-to-first-token regression: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Token throughput collapse: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-09

- [ ] **Question:** Compare Token throughput collapse with vLLM worker crash. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Token throughput collapse: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. vLLM worker crash: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MN-10

- [ ] **Configuration review:** **Question:** Compare vLLM worker crash with GPU unavailable. When would each change your design?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** vLLM worker crash: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. GPU unavailable: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around GPU unavailable; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `date -u; whoami; hostname` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-02

- [ ] **Question:** Production is degraded around GPU node cannot join; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around CUDA-driver mismatch; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-04

- [ ] **Question:** Production is degraded around GPU Operator failure; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='2 hours ago' --oneline` plus recent events/changes, then correlate the service-specific SLI. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model will not load; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `date -u; whoami; hostname` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-06

- [ ] **Question:** Production is degraded around GPU out-of-memory; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inference latency spike; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `terraform plan` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-08

- [ ] **Question:** Production is degraded around Time-to-first-token regression; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --since='2 hours ago' --oneline` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Token throughput collapse; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `date -u; whoami; hostname` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-TROUBLESHOOTING-SCENARIOS-MP-10

- [ ] **Question:** Production is degraded around vLLM worker crash; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --sort-by=.lastTimestamp` plus recent events/changes, then correlate the service-specific SLI. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-01

- [ ] **Question:** Design a production Troubleshooting scenarios capability where GPU unavailable, GPU Operator failure and Inference latency spike are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Troubleshooting scenarios capability where GPU node cannot join, Model will not load and Time-to-first-token regression are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-03

- [ ] **Question:** Design a production Troubleshooting scenarios capability where CUDA-driver mismatch, GPU out-of-memory and Token throughput collapse are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Troubleshooting scenarios capability where GPU Operator failure, Inference latency spike and vLLM worker crash are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-05

- [ ] **Question:** Design a production Troubleshooting scenarios capability where Model will not load, Time-to-first-token regression and GPU unavailable are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Troubleshooting scenarios capability where GPU out-of-memory, Token throughput collapse and GPU node cannot join are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-07

- [ ] **Question:** Design a production Troubleshooting scenarios capability where Inference latency spike, vLLM worker crash and CUDA-driver mismatch are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Troubleshooting scenarios capability where Time-to-first-token regression, GPU unavailable and GPU Operator failure are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-09

- [ ] **Question:** Design a production Troubleshooting scenarios capability where Token throughput collapse, GPU node cannot join and Model will not load are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Troubleshooting scenarios capability where vLLM worker crash, CUDA-driver mismatch and GPU out-of-memory are first-class requirements.
> **Covered in:** [Troubleshooting scenarios — Complete curriculum checklist](README.md#complete-curriculum-checklist)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU unavailable. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `date -u; whoami; hostname` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU node cannot join. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CUDA-driver mismatch. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU Operator failure. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='2 hours ago' --oneline` as one read-only checkpoint, not the whole diagnosis. requires a layer-by-layer, evidence-first path from user impact and recent change through identity, configuration, runtime, dependency and resource saturation, followed by reversible mitigation and verified repair. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model will not load. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `date -u; whoami; hostname` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU out-of-memory. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inference latency spike. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `terraform plan` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Time-to-first-token regression. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --since='2 hours ago' --oneline` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Token throughput collapse. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `date -u; whoami; hostname` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-TROUBLESHOOTING-SCENARIOS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving vLLM worker crash. How do you lead it end to end?
> **Covered in:** [Troubleshooting scenarios — Beginner → mid-level → senior learning path](README.md#beginner-mid-level-senior-learning-path)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --sort-by=.lastTimestamp` as one read-only checkpoint, not the whole diagnosis. is part of Troubleshooting scenarios; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Architecture exercises](../01-architecture-exercises/README.md) · [Study note](README.md) · [Next: Migration scenarios →](../03-migration-scenarios/README.md)

<!-- reading-navigation:end -->
