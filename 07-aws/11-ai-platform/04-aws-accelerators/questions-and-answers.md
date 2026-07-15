# AWS GPUs, Inferentia and Trainium — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-01

- [ ] **Question:** What is G-family GPU, and why does it matter in AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-02

- [ ] **Question:** What is P-family GPU, and why does it matter in AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-03

- [ ] **Question:** What is Inferentia, and why does it matter in AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** AWS inference accelerator programmed through Neuron SDK and compiled model support. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-04

- [ ] **Question:** What is Trainium, and why does it matter in AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** AWS training accelerator with Neuron distributed stack and operation compatibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-05

- [ ] **Question:** What is Neuron SDK, and why does it matter in AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** compiler/runtime/framework integration is a qualification and portability dependency. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-06

- [ ] **Question:** What is Accelerator memory, and why does it matter in AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-07

- [ ] **Question:** What is EFA, and why does it matter in AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** OS-bypass networking improves supported collectives only with compatible topology/software. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-08

- [ ] **Code:** **Question:** What does `nvidia-smi topo -m` help you verify for AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: commits specific capacity/time and differs from discount-only commitments.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` help you verify for AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: fault-tolerant jobs need checkpoint/restart and diversified capacity.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-capacity-reservations` help you verify for AWS GPUs, Inferentia and Trainium?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: target model/precision/batch/context/goodput/quality and total cost decide hardware.

## Junior — procedural and command questions

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-01

- [ ] **Code:** **Question:** A basic G-family GPU check fails. What would you do first using the CLI?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` and capture exact status/reason/request ID. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-02

- [ ] **Question:** A basic P-family GPU check fails. What would you do first?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-capacity-reservations` and capture exact status/reason/request ID. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-03

- [ ] **Question:** A basic Inferentia check fails. What would you do first?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `neuron-ls` and capture exact status/reason/request ID. AWS inference accelerator programmed through Neuron SDK and compiled model support. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-04

- [ ] **Code:** **Question:** A basic Trainium check fails. What would you do first using the CLI?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. AWS training accelerator with Neuron distributed stack and operation compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-05

- [ ] **Question:** A basic Neuron SDK check fails. What would you do first?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` and capture exact status/reason/request ID. compiler/runtime/framework integration is a qualification and portability dependency. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-06

- [ ] **Question:** A basic Accelerator memory check fails. What would you do first?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-capacity-reservations` and capture exact status/reason/request ID. weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-07

- [ ] **Code:** **Question:** A basic EFA check fails. What would you do first using the CLI?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `neuron-ls` and capture exact status/reason/request ID. OS-bypass networking improves supported collectives only with compatible topology/software. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-08

- [ ] **Question:** A basic Capacity reservation/block check fails. What would you do first?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. commits specific capacity/time and differs from discount-only commitments. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-09

- [ ] **Question:** A basic Spot check fails. What would you do first?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` and capture exact status/reason/request ID. fault-tolerant jobs need checkpoint/restart and diversified capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-JP-10

- [ ] **Code:** **Question:** A basic Benchmark check fails. What would you do first using the CLI?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-capacity-reservations` and capture exact status/reason/request ID. target model/precision/batch/context/goodput/quality and total cost decide hardware. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-01

- [ ] **Question:** Compare G-family GPU with P-family GPU. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** G-family GPU: graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. P-family GPU: high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-02

- [ ] **Question:** Compare P-family GPU with Inferentia. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** P-family GPU: high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Inferentia: AWS inference accelerator programmed through Neuron SDK and compiled model support. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-03

- [ ] **Question:** Compare Inferentia with Trainium. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** Inferentia: AWS inference accelerator programmed through Neuron SDK and compiled model support. Trainium: AWS training accelerator with Neuron distributed stack and operation compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-04

- [ ] **Configuration review:** **Question:** Compare Trainium with Neuron SDK. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Trainium: AWS training accelerator with Neuron distributed stack and operation compatibility. Neuron SDK: compiler/runtime/framework integration is a qualification and portability dependency. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-05

- [ ] **Question:** Compare Neuron SDK with Accelerator memory. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Neuron SDK: compiler/runtime/framework integration is a qualification and portability dependency. Accelerator memory: weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-06

- [ ] **Question:** Compare Accelerator memory with EFA. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Accelerator memory: weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. EFA: OS-bypass networking improves supported collectives only with compatible topology/software. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-07

- [ ] **Configuration review:** **Question:** Compare EFA with Capacity reservation/block. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** EFA: OS-bypass networking improves supported collectives only with compatible topology/software. Capacity reservation/block: commits specific capacity/time and differs from discount-only commitments. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-08

- [ ] **Question:** Compare Capacity reservation/block with Spot. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Capacity reservation/block: commits specific capacity/time and differs from discount-only commitments. Spot: fault-tolerant jobs need checkpoint/restart and diversified capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-09

- [ ] **Question:** Compare Spot with Benchmark. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Spot: fault-tolerant jobs need checkpoint/restart and diversified capacity. Benchmark: target model/precision/batch/context/goodput/quality and total cost decide hardware. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MN-10

- [ ] **Configuration review:** **Question:** Compare Benchmark with G-family GPU. When would each change your design?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Benchmark: target model/precision/batch/context/goodput/quality and total cost decide hardware. G-family GPU: graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around G-family GPU; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` plus recent events/changes, then correlate the service-specific SLI. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-02

- [ ] **Question:** Production is degraded around P-family GPU; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-capacity-reservations` plus recent events/changes, then correlate the service-specific SLI. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inferentia; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `neuron-ls` plus recent events/changes, then correlate the service-specific SLI. AWS inference accelerator programmed through Neuron SDK and compiled model support. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-04

- [ ] **Question:** Production is degraded around Trainium; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. AWS training accelerator with Neuron distributed stack and operation compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Neuron SDK; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` plus recent events/changes, then correlate the service-specific SLI. compiler/runtime/framework integration is a qualification and portability dependency. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-06

- [ ] **Question:** Production is degraded around Accelerator memory; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-capacity-reservations` plus recent events/changes, then correlate the service-specific SLI. weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around EFA; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `neuron-ls` plus recent events/changes, then correlate the service-specific SLI. OS-bypass networking improves supported collectives only with compatible topology/software. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-08

- [ ] **Question:** Production is degraded around Capacity reservation/block; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. commits specific capacity/time and differs from discount-only commitments. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Spot; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` plus recent events/changes, then correlate the service-specific SLI. fault-tolerant jobs need checkpoint/restart and diversified capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-MP-10

- [ ] **Question:** Production is degraded around Benchmark; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-capacity-reservations` plus recent events/changes, then correlate the service-specific SLI. target model/precision/batch/context/goodput/quality and total cost decide hardware. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-01

- [ ] **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where G-family GPU, Trainium and EFA are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. AWS training accelerator with Neuron distributed stack and operation compatibility. OS-bypass networking improves supported collectives only with compatible topology/software. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where P-family GPU, Neuron SDK and Capacity reservation/block are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. compiler/runtime/framework integration is a qualification and portability dependency. commits specific capacity/time and differs from discount-only commitments. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-03

- [ ] **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where Inferentia, Accelerator memory and Spot are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AWS inference accelerator programmed through Neuron SDK and compiled model support. weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. fault-tolerant jobs need checkpoint/restart and diversified capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where Trainium, EFA and Benchmark are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AWS training accelerator with Neuron distributed stack and operation compatibility. OS-bypass networking improves supported collectives only with compatible topology/software. target model/precision/batch/context/goodput/quality and total cost decide hardware. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-05

- [ ] **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where Neuron SDK, Capacity reservation/block and G-family GPU are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: compiler/runtime/framework integration is a qualification and portability dependency. commits specific capacity/time and differs from discount-only commitments. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where Accelerator memory, Spot and P-family GPU are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. fault-tolerant jobs need checkpoint/restart and diversified capacity. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-07

- [ ] **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where EFA, Benchmark and Inferentia are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: OS-bypass networking improves supported collectives only with compatible topology/software. target model/precision/batch/context/goodput/quality and total cost decide hardware. AWS inference accelerator programmed through Neuron SDK and compiled model support. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where Capacity reservation/block, G-family GPU and Trainium are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: commits specific capacity/time and differs from discount-only commitments. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. AWS training accelerator with Neuron distributed stack and operation compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-09

- [ ] **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where Spot, P-family GPU and Neuron SDK are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: fault-tolerant jobs need checkpoint/restart and diversified capacity. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. compiler/runtime/framework integration is a qualification and portability dependency. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS GPUs, Inferentia and Trainium capability where Benchmark, Inferentia and Accelerator memory are first-class requirements.
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: target model/precision/batch/context/goodput/quality and total cost decide hardware. AWS inference accelerator programmed through Neuron SDK and compiled model support. weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving G-family GPU. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` as one read-only checkpoint, not the whole diagnosis. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving P-family GPU. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-capacity-reservations` as one read-only checkpoint, not the whole diagnosis. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inferentia. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `neuron-ls` as one read-only checkpoint, not the whole diagnosis. AWS inference accelerator programmed through Neuron SDK and compiled model support. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Trainium. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. AWS training accelerator with Neuron distributed stack and operation compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Neuron SDK. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` as one read-only checkpoint, not the whole diagnosis. compiler/runtime/framework integration is a qualification and portability dependency. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Accelerator memory. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-capacity-reservations` as one read-only checkpoint, not the whole diagnosis. weights, KV/activations/workspace/fragmentation determine fit beyond parameter count. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving EFA. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `neuron-ls` as one read-only checkpoint, not the whole diagnosis. OS-bypass networking improves supported collectives only with compatible topology/software. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Capacity reservation/block. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. commits specific capacity/time and differs from discount-only commitments. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Spot. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` as one read-only checkpoint, not the whole diagnosis. fault-tolerant jobs need checkpoint/restart and diversified capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-GPUS-INFERENTIA-AND-TRAINIUM-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Benchmark. How do you lead it end to end?
> **Covered in:** [AWS GPUs, Inferentia and Trainium — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-capacity-reservations` as one read-only checkpoint, not the whole diagnosis. target model/precision/batch/context/goodput/quality and total cost decide hardware. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AI/ML workloads on Amazon EKS](../03-eks-ai-inference/README.md) · [Study note](README.md) · [Next: Google Cloud Platform →](../../../08-gcp/README.md)

<!-- reading-navigation:end -->
