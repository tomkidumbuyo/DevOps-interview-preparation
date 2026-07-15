# Distributed training and checkpoint recovery — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-01

- [ ] **Question:** What is Data parallel, and why does it matter in Distributed training and checkpoint recovery?

**Answer:** replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-02

- [ ] **Question:** What is DDP, and why does it matter in Distributed training and checkpoint recovery?

**Answer:** one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-03

- [ ] **Question:** What is FSDP/ZeRO, and why does it matter in Distributed training and checkpoint recovery?

**Answer:** shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-04

- [ ] **Question:** What is Tensor parallel, and why does it matter in Distributed training and checkpoint recovery?

**Answer:** partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-05

- [ ] **Question:** What is Pipeline parallel, and why does it matter in Distributed training and checkpoint recovery?

**Answer:** partitions layers into stages with microbatches, bubbles and failure coordination. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-06

- [ ] **Question:** What is NCCL collectives, and why does it matter in Distributed training and checkpoint recovery?

**Answer:** ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-07

- [ ] **Question:** What is Elasticity, and why does it matter in Distributed training and checkpoint recovery?

**Answer:** worker loss/restart changes membership only when algorithm/checkpoint semantics support it. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-08

- [ ] **Code:** **Question:** What does `kubectl logs -n NS -l job-name=TRAINING_JOB --prefix` help you verify for Distributed training and checkpoint recovery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: sharded state needs a committed manifest and compatible reshard/load procedure.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-09

- [ ] **Code:** **Question:** What does `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` help you verify for Distributed training and checkpoint recovery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JN-10

- [ ] **Code:** **Question:** What does `nvidia-smi topo -m` help you verify for Distributed training and checkpoint recovery?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences.

## Junior — procedural and command questions

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-01

- [ ] **Code:** **Question:** A basic Data parallel check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` and capture exact status/reason/request ID. replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-02

- [ ] **Question:** A basic DDP check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-03

- [ ] **Question:** A basic FSDP/ZeRO check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `NCCL_DEBUG=INFO torchrun --nproc-per-node=2 diagnose.py` and capture exact status/reason/request ID. shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-04

- [ ] **Code:** **Question:** A basic Tensor parallel check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n NS -l job-name=TRAINING_JOB --prefix` and capture exact status/reason/request ID. partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-05

- [ ] **Question:** A basic Pipeline parallel check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` and capture exact status/reason/request ID. partitions layers into stages with microbatches, bubbles and failure coordination. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-06

- [ ] **Question:** A basic NCCL collectives check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-07

- [ ] **Code:** **Question:** A basic Elasticity check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `NCCL_DEBUG=INFO torchrun --nproc-per-node=2 diagnose.py` and capture exact status/reason/request ID. worker loss/restart changes membership only when algorithm/checkpoint semantics support it. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-08

- [ ] **Question:** A basic Distributed checkpoint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n NS -l job-name=TRAINING_JOB --prefix` and capture exact status/reason/request ID. sharded state needs a committed manifest and compatible reshard/load procedure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-09

- [ ] **Question:** A basic Straggler check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` and capture exact status/reason/request ID. one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-JP-10

- [ ] **Code:** **Question:** A basic Reproducibility check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi topo -m` and capture exact status/reason/request ID. seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-01

- [ ] **Question:** Compare Data parallel with DDP. When would each change your design?

**Answer:** Data parallel: replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. DDP: one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-02

- [ ] **Question:** Compare DDP with FSDP/ZeRO. When would each change your design?

**Answer:** DDP: one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. FSDP/ZeRO: shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-03

- [ ] **Question:** Compare FSDP/ZeRO with Tensor parallel. When would each change your design?

**Answer:** FSDP/ZeRO: shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. Tensor parallel: partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-04

- [ ] **Configuration review:** **Question:** Compare Tensor parallel with Pipeline parallel. When would each change your design?

**Answer:** Tensor parallel: partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. Pipeline parallel: partitions layers into stages with microbatches, bubbles and failure coordination. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-05

- [ ] **Question:** Compare Pipeline parallel with NCCL collectives. When would each change your design?

**Answer:** Pipeline parallel: partitions layers into stages with microbatches, bubbles and failure coordination. NCCL collectives: ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-06

- [ ] **Question:** Compare NCCL collectives with Elasticity. When would each change your design?

**Answer:** NCCL collectives: ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. Elasticity: worker loss/restart changes membership only when algorithm/checkpoint semantics support it. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-07

- [ ] **Configuration review:** **Question:** Compare Elasticity with Distributed checkpoint. When would each change your design?

**Answer:** Elasticity: worker loss/restart changes membership only when algorithm/checkpoint semantics support it. Distributed checkpoint: sharded state needs a committed manifest and compatible reshard/load procedure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-08

- [ ] **Question:** Compare Distributed checkpoint with Straggler. When would each change your design?

**Answer:** Distributed checkpoint: sharded state needs a committed manifest and compatible reshard/load procedure. Straggler: one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-09

- [ ] **Question:** Compare Straggler with Reproducibility. When would each change your design?

**Answer:** Straggler: one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. Reproducibility: seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MN-10

- [ ] **Configuration review:** **Question:** Compare Reproducibility with Data parallel. When would each change your design?

**Answer:** Reproducibility: seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. Data parallel: replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Data parallel; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` plus recent events/changes, then correlate the service-specific SLI. replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-02

- [ ] **Question:** Production is degraded around DDP; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around FSDP/ZeRO; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `NCCL_DEBUG=INFO torchrun --nproc-per-node=2 diagnose.py` plus recent events/changes, then correlate the service-specific SLI. shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-04

- [ ] **Question:** Production is degraded around Tensor parallel; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n NS -l job-name=TRAINING_JOB --prefix` plus recent events/changes, then correlate the service-specific SLI. partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pipeline parallel; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` plus recent events/changes, then correlate the service-specific SLI. partitions layers into stages with microbatches, bubbles and failure coordination. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-06

- [ ] **Question:** Production is degraded around NCCL collectives; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Elasticity; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `NCCL_DEBUG=INFO torchrun --nproc-per-node=2 diagnose.py` plus recent events/changes, then correlate the service-specific SLI. worker loss/restart changes membership only when algorithm/checkpoint semantics support it. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-08

- [ ] **Question:** Production is degraded around Distributed checkpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n NS -l job-name=TRAINING_JOB --prefix` plus recent events/changes, then correlate the service-specific SLI. sharded state needs a committed manifest and compatible reshard/load procedure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Straggler; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` plus recent events/changes, then correlate the service-specific SLI. one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-MP-10

- [ ] **Question:** Production is degraded around Reproducibility; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi topo -m` plus recent events/changes, then correlate the service-specific SLI. seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-01

- [ ] **Question:** Design a production Distributed training and checkpoint recovery capability where Data parallel, Tensor parallel and Elasticity are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. worker loss/restart changes membership only when algorithm/checkpoint semantics support it. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed training and checkpoint recovery capability where DDP, Pipeline parallel and Distributed checkpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. partitions layers into stages with microbatches, bubbles and failure coordination. sharded state needs a committed manifest and compatible reshard/load procedure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-03

- [ ] **Question:** Design a production Distributed training and checkpoint recovery capability where FSDP/ZeRO, NCCL collectives and Straggler are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed training and checkpoint recovery capability where Tensor parallel, Elasticity and Reproducibility are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. worker loss/restart changes membership only when algorithm/checkpoint semantics support it. seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-05

- [ ] **Question:** Design a production Distributed training and checkpoint recovery capability where Pipeline parallel, Distributed checkpoint and Data parallel are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: partitions layers into stages with microbatches, bubbles and failure coordination. sharded state needs a committed manifest and compatible reshard/load procedure. replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed training and checkpoint recovery capability where NCCL collectives, Straggler and DDP are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-07

- [ ] **Question:** Design a production Distributed training and checkpoint recovery capability where Elasticity, Reproducibility and FSDP/ZeRO are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: worker loss/restart changes membership only when algorithm/checkpoint semantics support it. seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed training and checkpoint recovery capability where Distributed checkpoint, Data parallel and Tensor parallel are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: sharded state needs a committed manifest and compatible reshard/load procedure. replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-09

- [ ] **Question:** Design a production Distributed training and checkpoint recovery capability where Straggler, DDP and Pipeline parallel are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. partitions layers into stages with microbatches, bubbles and failure coordination. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Distributed training and checkpoint recovery capability where Reproducibility, FSDP/ZeRO and NCCL collectives are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data parallel. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` as one read-only checkpoint, not the whole diagnosis. replicas process different batches and synchronize gradients; global batch and optimizer behavior change with world size. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DDP. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. one process per GPU and collective gradient reduction require rank/world/rendezvous correctness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving FSDP/ZeRO. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `NCCL_DEBUG=INFO torchrun --nproc-per-node=2 diagnose.py` as one read-only checkpoint, not the whole diagnosis. shard parameters, gradients and optimizer state to trade communication/complexity for memory scale. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tensor parallel. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n NS -l job-name=TRAINING_JOB --prefix` as one read-only checkpoint, not the whole diagnosis. partitions matrix operations within a layer and benefits from high-bandwidth low-latency topology. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pipeline parallel. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` as one read-only checkpoint, not the whole diagnosis. partitions layers into stages with microbatches, bubbles and failure coordination. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NCCL collectives. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. ring/tree algorithms depend on rank, interface, RDMA/EFA, topology and version compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Elasticity. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `NCCL_DEBUG=INFO torchrun --nproc-per-node=2 diagnose.py` as one read-only checkpoint, not the whole diagnosis. worker loss/restart changes membership only when algorithm/checkpoint semantics support it. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Distributed checkpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n NS -l job-name=TRAINING_JOB --prefix` as one read-only checkpoint, not the whole diagnosis. sharded state needs a committed manifest and compatible reshard/load procedure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Straggler. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `torchrun --standalone --nproc-per-node=2 train.py --smoke-test` as one read-only checkpoint, not the whole diagnosis. one slow GPU/network/data worker holds synchronous progress and can hide behind average utilization. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### DISTRIBUTED-TRAINING-AND-CHECKPOINT-RECOVERY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reproducibility. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi topo -m` as one read-only checkpoint, not the whole diagnosis. seeds alone do not eliminate nondeterministic kernels, asynchronous order or topology differences. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
