# AI/ML workloads on Amazon EKS — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-01

- [ ] **Question:** What is GPU node pool, and why does it matter in AI/ML workloads on Amazon EKS?

**Answer:** hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-02

- [ ] **Question:** What is Karpenter GPU provisioning, and why does it matter in AI/ML workloads on Amazon EKS?

**Answer:** pending resource/label/topology constraints select compatible EC2 capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-03

- [ ] **Question:** What is GPU Operator/device plugin, and why does it matter in AI/ML workloads on Amazon EKS?

**Answer:** reconciles/advertises devices and telemetry but does not fix application compatibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-04

- [ ] **Question:** What is KServe/vLLM/Triton, and why does it matter in AI/ML workloads on Amazon EKS?

**Answer:** control plane and runtimes trade portability, performance and operations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-05

- [ ] **Question:** What is Model cache, and why does it matter in AI/ML workloads on Amazon EKS?

**Answer:** S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-06

- [ ] **Question:** What is Queue-based scaling, and why does it matter in AI/ML workloads on Amazon EKS?

**Answer:** token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-07

- [ ] **Question:** What is EFA/NCCL, and why does it matter in AI/ML workloads on Amazon EKS?

**Answer:** distributed workloads need topology, drivers, placement and network qualification. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-08

- [ ] **Code:** **Question:** What does `kubectl exec -n inference POD -- nvidia-smi` help you verify for AI/ML workloads on Amazon EKS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: interruptions and scarce types require diversity, checkpoint/fallback and reservations.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-09

- [ ] **Code:** **Question:** What does `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` help you verify for AI/ML workloads on Amazon EKS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pods -A --field-selector=status.phase=Pending` help you verify for AI/ML workloads on Amazon EKS?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: independently qualify node image, driver, runtime, model and prompt/evaluator changes.

## Junior — procedural and command questions

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-01

- [ ] **Code:** **Question:** A basic GPU node pool check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` and capture exact status/reason/request ID. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-02

- [ ] **Question:** A basic Karpenter GPU provisioning check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. pending resource/label/topology constraints select compatible EC2 capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-03

- [ ] **Question:** A basic GPU Operator/device plugin check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/karpenter --since=30m` and capture exact status/reason/request ID. reconciles/advertises devices and telemetry but does not fix application compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-04

- [ ] **Code:** **Question:** A basic KServe/vLLM/Triton check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl exec -n inference POD -- nvidia-smi` and capture exact status/reason/request ID. control plane and runtimes trade portability, performance and operations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-05

- [ ] **Question:** A basic Model cache check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` and capture exact status/reason/request ID. S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-06

- [ ] **Question:** A basic Queue-based scaling check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-07

- [ ] **Code:** **Question:** A basic EFA/NCCL check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n kube-system deploy/karpenter --since=30m` and capture exact status/reason/request ID. distributed workloads need topology, drivers, placement and network qualification. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-08

- [ ] **Question:** A basic Spot/capacity check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl exec -n inference POD -- nvidia-smi` and capture exact status/reason/request ID. interruptions and scarce types require diversity, checkpoint/fallback and reservations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-09

- [ ] **Question:** A basic Inference telemetry check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` and capture exact status/reason/request ID. queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-JP-10

- [ ] **Code:** **Question:** A basic Canary lifecycle check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A --field-selector=status.phase=Pending` and capture exact status/reason/request ID. independently qualify node image, driver, runtime, model and prompt/evaluator changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-01

- [ ] **Question:** Compare GPU node pool with Karpenter GPU provisioning. When would each change your design?

**Answer:** GPU node pool: hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Karpenter GPU provisioning: pending resource/label/topology constraints select compatible EC2 capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-02

- [ ] **Question:** Compare Karpenter GPU provisioning with GPU Operator/device plugin. When would each change your design?

**Answer:** Karpenter GPU provisioning: pending resource/label/topology constraints select compatible EC2 capacity. GPU Operator/device plugin: reconciles/advertises devices and telemetry but does not fix application compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-03

- [ ] **Question:** Compare GPU Operator/device plugin with KServe/vLLM/Triton. When would each change your design?

**Answer:** GPU Operator/device plugin: reconciles/advertises devices and telemetry but does not fix application compatibility. KServe/vLLM/Triton: control plane and runtimes trade portability, performance and operations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-04

- [ ] **Configuration review:** **Question:** Compare KServe/vLLM/Triton with Model cache. When would each change your design?

**Answer:** KServe/vLLM/Triton: control plane and runtimes trade portability, performance and operations. Model cache: S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-05

- [ ] **Question:** Compare Model cache with Queue-based scaling. When would each change your design?

**Answer:** Model cache: S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. Queue-based scaling: token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-06

- [ ] **Question:** Compare Queue-based scaling with EFA/NCCL. When would each change your design?

**Answer:** Queue-based scaling: token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. EFA/NCCL: distributed workloads need topology, drivers, placement and network qualification. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-07

- [ ] **Configuration review:** **Question:** Compare EFA/NCCL with Spot/capacity. When would each change your design?

**Answer:** EFA/NCCL: distributed workloads need topology, drivers, placement and network qualification. Spot/capacity: interruptions and scarce types require diversity, checkpoint/fallback and reservations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-08

- [ ] **Question:** Compare Spot/capacity with Inference telemetry. When would each change your design?

**Answer:** Spot/capacity: interruptions and scarce types require diversity, checkpoint/fallback and reservations. Inference telemetry: queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-09

- [ ] **Question:** Compare Inference telemetry with Canary lifecycle. When would each change your design?

**Answer:** Inference telemetry: queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput. Canary lifecycle: independently qualify node image, driver, runtime, model and prompt/evaluator changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MN-10

- [ ] **Configuration review:** **Question:** Compare Canary lifecycle with GPU node pool. When would each change your design?

**Answer:** Canary lifecycle: independently qualify node image, driver, runtime, model and prompt/evaluator changes. GPU node pool: hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around GPU node pool; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` plus recent events/changes, then correlate the service-specific SLI. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-02

- [ ] **Question:** Production is degraded around Karpenter GPU provisioning; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. pending resource/label/topology constraints select compatible EC2 capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around GPU Operator/device plugin; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/karpenter --since=30m` plus recent events/changes, then correlate the service-specific SLI. reconciles/advertises devices and telemetry but does not fix application compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-04

- [ ] **Question:** Production is degraded around KServe/vLLM/Triton; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl exec -n inference POD -- nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. control plane and runtimes trade portability, performance and operations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Model cache; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` plus recent events/changes, then correlate the service-specific SLI. S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-06

- [ ] **Question:** Production is degraded around Queue-based scaling; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around EFA/NCCL; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n kube-system deploy/karpenter --since=30m` plus recent events/changes, then correlate the service-specific SLI. distributed workloads need topology, drivers, placement and network qualification. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-08

- [ ] **Question:** Production is degraded around Spot/capacity; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl exec -n inference POD -- nvidia-smi` plus recent events/changes, then correlate the service-specific SLI. interruptions and scarce types require diversity, checkpoint/fallback and reservations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Inference telemetry; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` plus recent events/changes, then correlate the service-specific SLI. queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-MP-10

- [ ] **Question:** Production is degraded around Canary lifecycle; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A --field-selector=status.phase=Pending` plus recent events/changes, then correlate the service-specific SLI. independently qualify node image, driver, runtime, model and prompt/evaluator changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-01

- [ ] **Question:** Design a production AI/ML workloads on Amazon EKS capability where GPU node pool, KServe/vLLM/Triton and EFA/NCCL are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. control plane and runtimes trade portability, performance and operations. distributed workloads need topology, drivers, placement and network qualification. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AI/ML workloads on Amazon EKS capability where Karpenter GPU provisioning, Model cache and Spot/capacity are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pending resource/label/topology constraints select compatible EC2 capacity. S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. interruptions and scarce types require diversity, checkpoint/fallback and reservations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-03

- [ ] **Question:** Design a production AI/ML workloads on Amazon EKS capability where GPU Operator/device plugin, Queue-based scaling and Inference telemetry are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reconciles/advertises devices and telemetry but does not fix application compatibility. token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AI/ML workloads on Amazon EKS capability where KServe/vLLM/Triton, EFA/NCCL and Canary lifecycle are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: control plane and runtimes trade portability, performance and operations. distributed workloads need topology, drivers, placement and network qualification. independently qualify node image, driver, runtime, model and prompt/evaluator changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-05

- [ ] **Question:** Design a production AI/ML workloads on Amazon EKS capability where Model cache, Spot/capacity and GPU node pool are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. interruptions and scarce types require diversity, checkpoint/fallback and reservations. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AI/ML workloads on Amazon EKS capability where Queue-based scaling, Inference telemetry and Karpenter GPU provisioning are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput. pending resource/label/topology constraints select compatible EC2 capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-07

- [ ] **Question:** Design a production AI/ML workloads on Amazon EKS capability where EFA/NCCL, Canary lifecycle and GPU Operator/device plugin are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: distributed workloads need topology, drivers, placement and network qualification. independently qualify node image, driver, runtime, model and prompt/evaluator changes. reconciles/advertises devices and telemetry but does not fix application compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AI/ML workloads on Amazon EKS capability where Spot/capacity, GPU node pool and KServe/vLLM/Triton are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: interruptions and scarce types require diversity, checkpoint/fallback and reservations. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. control plane and runtimes trade portability, performance and operations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-09

- [ ] **Question:** Design a production AI/ML workloads on Amazon EKS capability where Inference telemetry, Karpenter GPU provisioning and Model cache are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput. pending resource/label/topology constraints select compatible EC2 capacity. S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AI/ML workloads on Amazon EKS capability where Canary lifecycle, GPU Operator/device plugin and Queue-based scaling are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: independently qualify node image, driver, runtime, model and prompt/evaluator changes. reconciles/advertises devices and telemetry but does not fix application compatibility. token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU node pool. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` as one read-only checkpoint, not the whole diagnosis. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Karpenter GPU provisioning. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. pending resource/label/topology constraints select compatible EC2 capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU Operator/device plugin. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/karpenter --since=30m` as one read-only checkpoint, not the whole diagnosis. reconciles/advertises devices and telemetry but does not fix application compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving KServe/vLLM/Triton. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl exec -n inference POD -- nvidia-smi` as one read-only checkpoint, not the whole diagnosis. control plane and runtimes trade portability, performance and operations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model cache. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` as one read-only checkpoint, not the whole diagnosis. S3/shared/local NVMe distribution controls cold start, integrity and disk pressure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Queue-based scaling. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. token queue drives replicas; pending Pods drive nodes after long provisioning/warmup. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving EFA/NCCL. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n kube-system deploy/karpenter --since=30m` as one read-only checkpoint, not the whole diagnosis. distributed workloads need topology, drivers, placement and network qualification. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Spot/capacity. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl exec -n inference POD -- nvidia-smi` as one read-only checkpoint, not the whole diagnosis. interruptions and scarce types require diversity, checkpoint/fallback and reservations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Inference telemetry. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` as one read-only checkpoint, not the whole diagnosis. queue, TTFT, inter-token, tokens/s, KV, GPU and quality/cost define goodput. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AI-ML-WORKLOADS-ON-AMAZON-EKS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Canary lifecycle. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A --field-selector=status.phase=Pending` as one read-only checkpoint, not the whole diagnosis. independently qualify node image, driver, runtime, model and prompt/evaluator changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
