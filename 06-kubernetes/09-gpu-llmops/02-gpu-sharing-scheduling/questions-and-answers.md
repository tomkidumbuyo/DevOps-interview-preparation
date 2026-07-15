# GPU sharing, scheduling and queueing — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-01

- [ ] **Question:** What is Whole GPU, and why does it matter in GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** simple exclusive allocation offers strongest default isolation at fragmentation cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-02

- [ ] **Question:** What is MIG, and why does it matter in GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** supported GPUs partition hardware memory/fault domains into fixed profiles. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-03

- [ ] **Question:** What is Time-slicing, and why does it matter in GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** oversubscribes compute without memory/fault isolation and weakens attribution. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-04

- [ ] **Question:** What is CUDA MPS, and why does it matter in GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** coordinates compatible processes for concurrency with separate operational/isolation constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-05

- [ ] **Question:** What is GPU fragmentation, and why does it matter in GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** free devices/profiles spread across nodes may not fit multi-GPU Pods. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-06

- [ ] **Question:** What is Gang scheduling, and why does it matter in GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-07

- [ ] **Question:** What is Fair sharing, and why does it matter in GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-08

- [ ] **Code:** **Question:** What does `nvidia-smi topo -m` help you verify for GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-09

- [ ] **Code:** **Question:** What does `nvidia-smi mig -lgi` help you verify for GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: scarce urgent workloads need policy, checkpoint/drain and starvation protection.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JN-10

- [ ] **Code:** **Question:** What does `kubectl get workload,localqueue,clusterqueue -A` help you verify for GPU sharing, scheduling and queueing?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: tenant GPU/profile/time/token budgets need admission and usage measurement.

## Junior — procedural and command questions

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-01

- [ ] **Code:** **Question:** A basic Whole GPU check fails. What would you do first using the CLI?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node GPU_NODE` and capture exact status/reason/request ID. simple exclusive allocation offers strongest default isolation at fragmentation cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-02

- [ ] **Question:** A basic MIG check fails. What would you do first?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. supported GPUs partition hardware memory/fault domains into fixed profiles. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-03

- [ ] **Question:** A basic Time-slicing check fails. What would you do first?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. oversubscribes compute without memory/fault isolation and weakens attribution. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-04

- [ ] **Code:** **Question:** A basic CUDA MPS check fails. What would you do first using the CLI?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi mig -lgi` and capture exact status/reason/request ID. coordinates compatible processes for concurrency with separate operational/isolation constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-05

- [ ] **Question:** A basic GPU fragmentation check fails. What would you do first?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get workload,localqueue,clusterqueue -A` and capture exact status/reason/request ID. free devices/profiles spread across nodes may not fit multi-GPU Pods. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-06

- [ ] **Question:** A basic Gang scheduling check fails. What would you do first?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe node GPU_NODE` and capture exact status/reason/request ID. admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-07

- [ ] **Code:** **Question:** A basic Fair sharing check fails. What would you do first using the CLI?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get events -A --field-selector=reason=FailedScheduling` and capture exact status/reason/request ID. queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-08

- [ ] **Question:** A basic Topology check fails. What would you do first?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-09

- [ ] **Question:** A basic Priority/preemption check fails. What would you do first?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi mig -lgi` and capture exact status/reason/request ID. scarce urgent workloads need policy, checkpoint/drain and starvation protection. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-JP-10

- [ ] **Code:** **Question:** A basic Quota/accounting check fails. What would you do first using the CLI?
> **Covered in:** [GPU sharing, scheduling and queueing — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get workload,localqueue,clusterqueue -A` and capture exact status/reason/request ID. tenant GPU/profile/time/token budgets need admission and usage measurement. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-01

- [ ] **Question:** Compare Whole GPU with MIG. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Whole GPU: simple exclusive allocation offers strongest default isolation at fragmentation cost. MIG: supported GPUs partition hardware memory/fault domains into fixed profiles. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-02

- [ ] **Question:** Compare MIG with Time-slicing. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** MIG: supported GPUs partition hardware memory/fault domains into fixed profiles. Time-slicing: oversubscribes compute without memory/fault isolation and weakens attribution. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-03

- [ ] **Question:** Compare Time-slicing with CUDA MPS. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Time-slicing: oversubscribes compute without memory/fault isolation and weakens attribution. CUDA MPS: coordinates compatible processes for concurrency with separate operational/isolation constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-04

- [ ] **Configuration review:** **Question:** Compare CUDA MPS with GPU fragmentation. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CUDA MPS: coordinates compatible processes for concurrency with separate operational/isolation constraints. GPU fragmentation: free devices/profiles spread across nodes may not fit multi-GPU Pods. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-05

- [ ] **Question:** Compare GPU fragmentation with Gang scheduling. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** GPU fragmentation: free devices/profiles spread across nodes may not fit multi-GPU Pods. Gang scheduling: admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-06

- [ ] **Question:** Compare Gang scheduling with Fair sharing. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Gang scheduling: admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. Fair sharing: queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-07

- [ ] **Configuration review:** **Question:** Compare Fair sharing with Topology. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Fair sharing: queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. Topology: NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-08

- [ ] **Question:** Compare Topology with Priority/preemption. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Topology: NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance. Priority/preemption: scarce urgent workloads need policy, checkpoint/drain and starvation protection. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-09

- [ ] **Question:** Compare Priority/preemption with Quota/accounting. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Priority/preemption: scarce urgent workloads need policy, checkpoint/drain and starvation protection. Quota/accounting: tenant GPU/profile/time/token budgets need admission and usage measurement. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MN-10

- [ ] **Configuration review:** **Question:** Compare Quota/accounting with Whole GPU. When would each change your design?
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Quota/accounting: tenant GPU/profile/time/token budgets need admission and usage measurement. Whole GPU: simple exclusive allocation offers strongest default isolation at fragmentation cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Whole GPU; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node GPU_NODE` plus recent events/changes, then correlate the service-specific SLI. simple exclusive allocation offers strongest default isolation at fragmentation cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-02

- [ ] **Question:** Production is degraded around MIG; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. supported GPUs partition hardware memory/fault domains into fixed profiles. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Time-slicing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. oversubscribes compute without memory/fault isolation and weakens attribution. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-04

- [ ] **Question:** Production is degraded around CUDA MPS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi mig -lgi` plus recent events/changes, then correlate the service-specific SLI. coordinates compatible processes for concurrency with separate operational/isolation constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around GPU fragmentation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get workload,localqueue,clusterqueue -A` plus recent events/changes, then correlate the service-specific SLI. free devices/profiles spread across nodes may not fit multi-GPU Pods. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-06

- [ ] **Question:** Production is degraded around Gang scheduling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe node GPU_NODE` plus recent events/changes, then correlate the service-specific SLI. admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Fair sharing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get events -A --field-selector=reason=FailedScheduling` plus recent events/changes, then correlate the service-specific SLI. queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-08

- [ ] **Question:** Production is degraded around Topology; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Priority/preemption; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi mig -lgi` plus recent events/changes, then correlate the service-specific SLI. scarce urgent workloads need policy, checkpoint/drain and starvation protection. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-MP-10

- [ ] **Question:** Production is degraded around Quota/accounting; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get workload,localqueue,clusterqueue -A` plus recent events/changes, then correlate the service-specific SLI. tenant GPU/profile/time/token budgets need admission and usage measurement. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-01

- [ ] **Question:** Design a production GPU sharing, scheduling and queueing capability where Whole GPU, CUDA MPS and Fair sharing are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: simple exclusive allocation offers strongest default isolation at fragmentation cost. coordinates compatible processes for concurrency with separate operational/isolation constraints. queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GPU sharing, scheduling and queueing capability where MIG, GPU fragmentation and Topology are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported GPUs partition hardware memory/fault domains into fixed profiles. free devices/profiles spread across nodes may not fit multi-GPU Pods. NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-03

- [ ] **Question:** Design a production GPU sharing, scheduling and queueing capability where Time-slicing, Gang scheduling and Priority/preemption are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: oversubscribes compute without memory/fault isolation and weakens attribution. admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. scarce urgent workloads need policy, checkpoint/drain and starvation protection. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GPU sharing, scheduling and queueing capability where CUDA MPS, Fair sharing and Quota/accounting are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: coordinates compatible processes for concurrency with separate operational/isolation constraints. queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. tenant GPU/profile/time/token budgets need admission and usage measurement. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-05

- [ ] **Question:** Design a production GPU sharing, scheduling and queueing capability where GPU fragmentation, Topology and Whole GPU are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: free devices/profiles spread across nodes may not fit multi-GPU Pods. NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance. simple exclusive allocation offers strongest default isolation at fragmentation cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GPU sharing, scheduling and queueing capability where Gang scheduling, Priority/preemption and MIG are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. scarce urgent workloads need policy, checkpoint/drain and starvation protection. supported GPUs partition hardware memory/fault domains into fixed profiles. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-07

- [ ] **Question:** Design a production GPU sharing, scheduling and queueing capability where Fair sharing, Quota/accounting and Time-slicing are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. tenant GPU/profile/time/token budgets need admission and usage measurement. oversubscribes compute without memory/fault isolation and weakens attribution. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GPU sharing, scheduling and queueing capability where Topology, Whole GPU and CUDA MPS are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance. simple exclusive allocation offers strongest default isolation at fragmentation cost. coordinates compatible processes for concurrency with separate operational/isolation constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-09

- [ ] **Question:** Design a production GPU sharing, scheduling and queueing capability where Priority/preemption, MIG and GPU fragmentation are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scarce urgent workloads need policy, checkpoint/drain and starvation protection. supported GPUs partition hardware memory/fault domains into fixed profiles. free devices/profiles spread across nodes may not fit multi-GPU Pods. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GPU sharing, scheduling and queueing capability where Quota/accounting, Time-slicing and Gang scheduling are first-class requirements.
> **Covered in:** [GPU sharing, scheduling and queueing — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tenant GPU/profile/time/token budgets need admission and usage measurement. oversubscribes compute without memory/fault isolation and weakens attribution. admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Whole GPU. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node GPU_NODE` as one read-only checkpoint, not the whole diagnosis. simple exclusive allocation offers strongest default isolation at fragmentation cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving MIG. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. supported GPUs partition hardware memory/fault domains into fixed profiles. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Time-slicing. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. oversubscribes compute without memory/fault isolation and weakens attribution. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CUDA MPS. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi mig -lgi` as one read-only checkpoint, not the whole diagnosis. coordinates compatible processes for concurrency with separate operational/isolation constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU fragmentation. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get workload,localqueue,clusterqueue -A` as one read-only checkpoint, not the whole diagnosis. free devices/profiles spread across nodes may not fit multi-GPU Pods. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Gang scheduling. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe node GPU_NODE` as one read-only checkpoint, not the whole diagnosis. admits all workers/resources together so distributed jobs do not deadlock holding partial capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fair sharing. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get events -A --field-selector=reason=FailedScheduling` as one read-only checkpoint, not the whole diagnosis. queues/cohorts borrow quota while preventing one tenant from monopolizing GPUs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Topology. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. NUMA/PCIe/NVLink/NVSwitch/NIC placement determines collective/serving performance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Priority/preemption. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi mig -lgi` as one read-only checkpoint, not the whole diagnosis. scarce urgent workloads need policy, checkpoint/drain and starvation protection. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GPU-SHARING-SCHEDULING-AND-QUEUEING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Quota/accounting. How do you lead it end to end?
> **Covered in:** [GPU sharing, scheduling and queueing — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get workload,localqueue,clusterqueue -A` as one read-only checkpoint, not the whole diagnosis. tenant GPU/profile/time/token budgets need admission and usage measurement. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: GPU Operator, device plugins and DRA](../01-gpu-operator-dra/README.md) · [Study note](README.md) · [Next: KServe, vLLM and Triton on Kubernetes →](../03-model-serving/README.md)

<!-- reading-navigation:end -->
