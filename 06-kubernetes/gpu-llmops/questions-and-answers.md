# Gpu Llmops — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-GPU-LLMOPS-JN-01

- [ ] **Question:** What is Driver, and why does it matter in Gpu Llmops?

**Answer:** host kernel module/firmware is the foundation and must match hardware/kernel/runtime. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GPU-LLMOPS-JN-02

- [ ] **Question:** What is Container toolkit, and why does it matter in Gpu Llmops?

**Answer:** injects device/library/runtime configuration into GPU containers. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GPU-LLMOPS-JN-03

- [ ] **Question:** What is Whole GPU, and why does it matter in Gpu Llmops?

**Answer:** simple exclusive allocation offers strongest default isolation at fragmentation cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GPU-LLMOPS-JN-04

- [ ] **Question:** What is MIG, and why does it matter in Gpu Llmops?

**Answer:** supported GPUs partition hardware memory/fault domains into fixed profiles. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GPU-LLMOPS-JN-05

- [ ] **Question:** What is InferenceService, and why does it matter in Gpu Llmops?

**Answer:** KServe resource declares predictor/runtime/storage/traffic under deployment mode. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GPU-LLMOPS-JN-06

- [ ] **Question:** What is ServingRuntime, and why does it matter in Gpu Llmops?

**Answer:** reusable supported model format/container/protocol contract. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GPU-LLMOPS-JN-07

- [ ] **Question:** What is Queue depth/age, and why does it matter in Gpu Llmops?

**Answer:** leading overload signal when arrival work exceeds serving goodput. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GPU-LLMOPS-JN-08

- [ ] **Code:** **Question:** What does `kubectl describe node GPU_NODE` help you verify for Gpu Llmops?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: input/output length estimate better reflects heterogeneous request cost.

### BRANCH-GPU-LLMOPS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get inferenceservice,servingruntime -A` help you verify for Gpu Llmops?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity.

### BRANCH-GPU-LLMOPS-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe hpa NAME -n NS` help you verify for Gpu Llmops?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: versioned owned task examples and edge/adversarial cases.

## Junior — procedural and command questions

### BRANCH-GPU-LLMOPS-JP-01

- [ ] **Code:** **Question:** A basic Driver check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -n gpu-operator -o wide` and capture exact status/reason/request ID. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-02

- [ ] **Question:** A basic Container toolkit check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node GPU_NODE` and capture exact status/reason/request ID. injects device/library/runtime configuration into GPU containers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-03

- [ ] **Question:** A basic Whole GPU check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice,servingruntime -A` and capture exact status/reason/request ID. simple exclusive allocation offers strongest default isolation at fragmentation cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-04

- [ ] **Code:** **Question:** A basic MIG check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe hpa NAME -n NS` and capture exact status/reason/request ID. supported GPUs partition hardware memory/fault domains into fixed profiles. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-05

- [ ] **Question:** A basic InferenceService check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get deployment,inferenceservice -n inference -o yaml` and capture exact status/reason/request ID. KServe resource declares predictor/runtime/storage/traffic under deployment mode. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-06

- [ ] **Question:** A basic ServingRuntime check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get gateway,httproute,networkpolicy -A` and capture exact status/reason/request ID. reusable supported model format/container/protocol contract. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-07

- [ ] **Code:** **Question:** A basic Queue depth/age check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -n gpu-operator -o wide` and capture exact status/reason/request ID. leading overload signal when arrival work exceeds serving goodput. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-08

- [ ] **Question:** A basic Predicted token work check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node GPU_NODE` and capture exact status/reason/request ID. input/output length estimate better reflects heterogeneous request cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-09

- [ ] **Question:** A basic Release manifest check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get inferenceservice,servingruntime -A` and capture exact status/reason/request ID. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GPU-LLMOPS-JP-10

- [ ] **Code:** **Question:** A basic Golden dataset check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe hpa NAME -n NS` and capture exact status/reason/request ID. versioned owned task examples and edge/adversarial cases. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-GPU-LLMOPS-MN-01

- [ ] **Question:** Compare Driver with Container toolkit. When would each change your design?

**Answer:** Driver: host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Container toolkit: injects device/library/runtime configuration into GPU containers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-02

- [ ] **Question:** Compare Container toolkit with Whole GPU. When would each change your design?

**Answer:** Container toolkit: injects device/library/runtime configuration into GPU containers. Whole GPU: simple exclusive allocation offers strongest default isolation at fragmentation cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-03

- [ ] **Question:** Compare Whole GPU with MIG. When would each change your design?

**Answer:** Whole GPU: simple exclusive allocation offers strongest default isolation at fragmentation cost. MIG: supported GPUs partition hardware memory/fault domains into fixed profiles. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-04

- [ ] **Configuration review:** **Question:** Compare MIG with InferenceService. When would each change your design?

**Answer:** MIG: supported GPUs partition hardware memory/fault domains into fixed profiles. InferenceService: KServe resource declares predictor/runtime/storage/traffic under deployment mode. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-05

- [ ] **Question:** Compare InferenceService with ServingRuntime. When would each change your design?

**Answer:** InferenceService: KServe resource declares predictor/runtime/storage/traffic under deployment mode. ServingRuntime: reusable supported model format/container/protocol contract. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-06

- [ ] **Question:** Compare ServingRuntime with Queue depth/age. When would each change your design?

**Answer:** ServingRuntime: reusable supported model format/container/protocol contract. Queue depth/age: leading overload signal when arrival work exceeds serving goodput. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-07

- [ ] **Configuration review:** **Question:** Compare Queue depth/age with Predicted token work. When would each change your design?

**Answer:** Queue depth/age: leading overload signal when arrival work exceeds serving goodput. Predicted token work: input/output length estimate better reflects heterogeneous request cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-08

- [ ] **Question:** Compare Predicted token work with Release manifest. When would each change your design?

**Answer:** Predicted token work: input/output length estimate better reflects heterogeneous request cost. Release manifest: exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-09

- [ ] **Question:** Compare Release manifest with Golden dataset. When would each change your design?

**Answer:** Release manifest: exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Golden dataset: versioned owned task examples and edge/adversarial cases. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GPU-LLMOPS-MN-10

- [ ] **Configuration review:** **Question:** Compare Golden dataset with Driver. When would each change your design?

**Answer:** Golden dataset: versioned owned task examples and edge/adversarial cases. Driver: host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-GPU-LLMOPS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Driver; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -n gpu-operator -o wide` plus recent events/changes, then correlate the service-specific SLI. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-02

- [ ] **Question:** Production is degraded around Container toolkit; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node GPU_NODE` plus recent events/changes, then correlate the service-specific SLI. injects device/library/runtime configuration into GPU containers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Whole GPU; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice,servingruntime -A` plus recent events/changes, then correlate the service-specific SLI. simple exclusive allocation offers strongest default isolation at fragmentation cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-04

- [ ] **Question:** Production is degraded around MIG; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe hpa NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. supported GPUs partition hardware memory/fault domains into fixed profiles. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around InferenceService; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get deployment,inferenceservice -n inference -o yaml` plus recent events/changes, then correlate the service-specific SLI. KServe resource declares predictor/runtime/storage/traffic under deployment mode. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-06

- [ ] **Question:** Production is degraded around ServingRuntime; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get gateway,httproute,networkpolicy -A` plus recent events/changes, then correlate the service-specific SLI. reusable supported model format/container/protocol contract. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Queue depth/age; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -n gpu-operator -o wide` plus recent events/changes, then correlate the service-specific SLI. leading overload signal when arrival work exceeds serving goodput. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-08

- [ ] **Question:** Production is degraded around Predicted token work; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node GPU_NODE` plus recent events/changes, then correlate the service-specific SLI. input/output length estimate better reflects heterogeneous request cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Release manifest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get inferenceservice,servingruntime -A` plus recent events/changes, then correlate the service-specific SLI. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GPU-LLMOPS-MP-10

- [ ] **Question:** Production is degraded around Golden dataset; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe hpa NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. versioned owned task examples and edge/adversarial cases. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-GPU-LLMOPS-SN-01

- [ ] **Question:** Design a production Gpu Llmops capability where Driver, MIG and Queue depth/age are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: host kernel module/firmware is the foundation and must match hardware/kernel/runtime. supported GPUs partition hardware memory/fault domains into fixed profiles. leading overload signal when arrival work exceeds serving goodput. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Gpu Llmops capability where Container toolkit, InferenceService and Predicted token work are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: injects device/library/runtime configuration into GPU containers. KServe resource declares predictor/runtime/storage/traffic under deployment mode. input/output length estimate better reflects heterogeneous request cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-03

- [ ] **Question:** Design a production Gpu Llmops capability where Whole GPU, ServingRuntime and Release manifest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: simple exclusive allocation offers strongest default isolation at fragmentation cost. reusable supported model format/container/protocol contract. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Gpu Llmops capability where MIG, Queue depth/age and Golden dataset are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported GPUs partition hardware memory/fault domains into fixed profiles. leading overload signal when arrival work exceeds serving goodput. versioned owned task examples and edge/adversarial cases. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-05

- [ ] **Question:** Design a production Gpu Llmops capability where InferenceService, Predicted token work and Driver are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: KServe resource declares predictor/runtime/storage/traffic under deployment mode. input/output length estimate better reflects heterogeneous request cost. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Gpu Llmops capability where ServingRuntime, Release manifest and Container toolkit are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reusable supported model format/container/protocol contract. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. injects device/library/runtime configuration into GPU containers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-07

- [ ] **Question:** Design a production Gpu Llmops capability where Queue depth/age, Golden dataset and Whole GPU are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: leading overload signal when arrival work exceeds serving goodput. versioned owned task examples and edge/adversarial cases. simple exclusive allocation offers strongest default isolation at fragmentation cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Gpu Llmops capability where Predicted token work, Driver and MIG are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: input/output length estimate better reflects heterogeneous request cost. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. supported GPUs partition hardware memory/fault domains into fixed profiles. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-09

- [ ] **Question:** Design a production Gpu Llmops capability where Release manifest, Container toolkit and InferenceService are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. injects device/library/runtime configuration into GPU containers. KServe resource declares predictor/runtime/storage/traffic under deployment mode. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GPU-LLMOPS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Gpu Llmops capability where Golden dataset, Whole GPU and ServingRuntime are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned owned task examples and edge/adversarial cases. simple exclusive allocation offers strongest default isolation at fragmentation cost. reusable supported model format/container/protocol contract. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-GPU-LLMOPS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Driver. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -n gpu-operator -o wide` as one read-only checkpoint, not the whole diagnosis. host kernel module/firmware is the foundation and must match hardware/kernel/runtime. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container toolkit. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node GPU_NODE` as one read-only checkpoint, not the whole diagnosis. injects device/library/runtime configuration into GPU containers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Whole GPU. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice,servingruntime -A` as one read-only checkpoint, not the whole diagnosis. simple exclusive allocation offers strongest default isolation at fragmentation cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving MIG. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe hpa NAME -n NS` as one read-only checkpoint, not the whole diagnosis. supported GPUs partition hardware memory/fault domains into fixed profiles. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving InferenceService. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get deployment,inferenceservice -n inference -o yaml` as one read-only checkpoint, not the whole diagnosis. KServe resource declares predictor/runtime/storage/traffic under deployment mode. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ServingRuntime. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get gateway,httproute,networkpolicy -A` as one read-only checkpoint, not the whole diagnosis. reusable supported model format/container/protocol contract. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Queue depth/age. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -n gpu-operator -o wide` as one read-only checkpoint, not the whole diagnosis. leading overload signal when arrival work exceeds serving goodput. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Predicted token work. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node GPU_NODE` as one read-only checkpoint, not the whole diagnosis. input/output length estimate better reflects heterogeneous request cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Release manifest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get inferenceservice,servingruntime -A` as one read-only checkpoint, not the whole diagnosis. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GPU-LLMOPS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Golden dataset. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe hpa NAME -n NS` as one read-only checkpoint, not the whole diagnosis. versioned owned task examples and edge/adversarial cases. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
