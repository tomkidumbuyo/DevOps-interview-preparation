# Ai Platform — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-AI-PLATFORM-JN-01

- [ ] **Question:** What is Foundation model access, and why does it matter in Ai Platform?

**Answer:** model/provider/Region/API capability and terms must be approved. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AI-PLATFORM-JN-02

- [ ] **Question:** What is Converse/Invoke API, and why does it matter in Ai Platform?

**Answer:** normalized/model APIs differ in streaming, tools and request schema. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AI-PLATFORM-JN-03

- [ ] **Question:** What is Training job, and why does it matter in Ai Platform?

**Answer:** immutable container/data/hyperparameter/instance run writes model artifacts/metrics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AI-PLATFORM-JN-04

- [ ] **Question:** What is Processing job, and why does it matter in Ai Platform?

**Answer:** managed batch preprocessing/evaluation under reproducible container and data inputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AI-PLATFORM-JN-05

- [ ] **Question:** What is GPU node pool, and why does it matter in Ai Platform?

**Answer:** hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AI-PLATFORM-JN-06

- [ ] **Question:** What is Karpenter GPU provisioning, and why does it matter in Ai Platform?

**Answer:** pending resource/label/topology constraints select compatible EC2 capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AI-PLATFORM-JN-07

- [ ] **Question:** What is G-family GPU, and why does it matter in Ai Platform?

**Answer:** graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-AI-PLATFORM-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` help you verify for Ai Platform?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation.

### BRANCH-AI-PLATFORM-JN-09

- [ ] **Code:** **Question:** What does `aws bedrock list-foundation-models` help you verify for Ai Platform?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: model/provider/Region/API capability and terms must be approved.

### BRANCH-AI-PLATFORM-JN-10

- [ ] **Code:** **Question:** What does `aws sagemaker list-training-jobs` help you verify for Ai Platform?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: normalized/model APIs differ in streaming, tools and request schema.

## Junior — procedural and command questions

### BRANCH-AI-PLATFORM-JP-01

- [ ] **Code:** **Question:** A basic Foundation model access check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-foundation-models` and capture exact status/reason/request ID. model/provider/Region/API capability and terms must be approved. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-02

- [ ] **Question:** A basic Converse/Invoke API check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-training-jobs` and capture exact status/reason/request ID. normalized/model APIs differ in streaming, tools and request schema. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-03

- [ ] **Question:** A basic Training job check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` and capture exact status/reason/request ID. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-04

- [ ] **Code:** **Question:** A basic Processing job check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` and capture exact status/reason/request ID. managed batch preprocessing/evaluation under reproducible container and data inputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-05

- [ ] **Question:** A basic GPU node pool check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-foundation-models` and capture exact status/reason/request ID. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-06

- [ ] **Question:** A basic Karpenter GPU provisioning check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-training-jobs` and capture exact status/reason/request ID. pending resource/label/topology constraints select compatible EC2 capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-07

- [ ] **Code:** **Question:** A basic G-family GPU check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` and capture exact status/reason/request ID. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-08

- [ ] **Question:** A basic P-family GPU check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` and capture exact status/reason/request ID. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-09

- [ ] **Question:** A basic Foundation model access check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws bedrock list-foundation-models` and capture exact status/reason/request ID. model/provider/Region/API capability and terms must be approved. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-AI-PLATFORM-JP-10

- [ ] **Code:** **Question:** A basic Converse/Invoke API check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-training-jobs` and capture exact status/reason/request ID. normalized/model APIs differ in streaming, tools and request schema. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-AI-PLATFORM-MN-01

- [ ] **Question:** Compare Foundation model access with Converse/Invoke API. When would each change your design?

**Answer:** Foundation model access: model/provider/Region/API capability and terms must be approved. Converse/Invoke API: normalized/model APIs differ in streaming, tools and request schema. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-02

- [ ] **Question:** Compare Converse/Invoke API with Training job. When would each change your design?

**Answer:** Converse/Invoke API: normalized/model APIs differ in streaming, tools and request schema. Training job: immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-03

- [ ] **Question:** Compare Training job with Processing job. When would each change your design?

**Answer:** Training job: immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Processing job: managed batch preprocessing/evaluation under reproducible container and data inputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-04

- [ ] **Configuration review:** **Question:** Compare Processing job with GPU node pool. When would each change your design?

**Answer:** Processing job: managed batch preprocessing/evaluation under reproducible container and data inputs. GPU node pool: hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-05

- [ ] **Question:** Compare GPU node pool with Karpenter GPU provisioning. When would each change your design?

**Answer:** GPU node pool: hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Karpenter GPU provisioning: pending resource/label/topology constraints select compatible EC2 capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-06

- [ ] **Question:** Compare Karpenter GPU provisioning with G-family GPU. When would each change your design?

**Answer:** Karpenter GPU provisioning: pending resource/label/topology constraints select compatible EC2 capacity. G-family GPU: graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-07

- [ ] **Configuration review:** **Question:** Compare G-family GPU with P-family GPU. When would each change your design?

**Answer:** G-family GPU: graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. P-family GPU: high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-08

- [ ] **Question:** Compare P-family GPU with Foundation model access. When would each change your design?

**Answer:** P-family GPU: high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Foundation model access: model/provider/Region/API capability and terms must be approved. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-09

- [ ] **Question:** Compare Foundation model access with Converse/Invoke API. When would each change your design?

**Answer:** Foundation model access: model/provider/Region/API capability and terms must be approved. Converse/Invoke API: normalized/model APIs differ in streaming, tools and request schema. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-AI-PLATFORM-MN-10

- [ ] **Configuration review:** **Question:** Compare Converse/Invoke API with Foundation model access. When would each change your design?

**Answer:** Converse/Invoke API: normalized/model APIs differ in streaming, tools and request schema. Foundation model access: model/provider/Region/API capability and terms must be approved. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-AI-PLATFORM-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Foundation model access; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-foundation-models` plus recent events/changes, then correlate the service-specific SLI. model/provider/Region/API capability and terms must be approved. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-02

- [ ] **Question:** Production is degraded around Converse/Invoke API; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-training-jobs` plus recent events/changes, then correlate the service-specific SLI. normalized/model APIs differ in streaming, tools and request schema. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Training job; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` plus recent events/changes, then correlate the service-specific SLI. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-04

- [ ] **Question:** Production is degraded around Processing job; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` plus recent events/changes, then correlate the service-specific SLI. managed batch preprocessing/evaluation under reproducible container and data inputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around GPU node pool; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-foundation-models` plus recent events/changes, then correlate the service-specific SLI. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-06

- [ ] **Question:** Production is degraded around Karpenter GPU provisioning; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-training-jobs` plus recent events/changes, then correlate the service-specific SLI. pending resource/label/topology constraints select compatible EC2 capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around G-family GPU; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` plus recent events/changes, then correlate the service-specific SLI. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-08

- [ ] **Question:** Production is degraded around P-family GPU; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` plus recent events/changes, then correlate the service-specific SLI. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Foundation model access; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws bedrock list-foundation-models` plus recent events/changes, then correlate the service-specific SLI. model/provider/Region/API capability and terms must be approved. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-AI-PLATFORM-MP-10

- [ ] **Question:** Production is degraded around Converse/Invoke API; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-training-jobs` plus recent events/changes, then correlate the service-specific SLI. normalized/model APIs differ in streaming, tools and request schema. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-AI-PLATFORM-SN-01

- [ ] **Question:** Design a production Ai Platform capability where Foundation model access, Processing job and G-family GPU are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model/provider/Region/API capability and terms must be approved. managed batch preprocessing/evaluation under reproducible container and data inputs. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Ai Platform capability where Converse/Invoke API, GPU node pool and P-family GPU are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: normalized/model APIs differ in streaming, tools and request schema. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-03

- [ ] **Question:** Design a production Ai Platform capability where Training job, Karpenter GPU provisioning and Foundation model access are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable container/data/hyperparameter/instance run writes model artifacts/metrics. pending resource/label/topology constraints select compatible EC2 capacity. model/provider/Region/API capability and terms must be approved. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Ai Platform capability where Processing job, G-family GPU and Converse/Invoke API are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed batch preprocessing/evaluation under reproducible container and data inputs. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. normalized/model APIs differ in streaming, tools and request schema. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-05

- [ ] **Question:** Design a production Ai Platform capability where GPU node pool, P-family GPU and Foundation model access are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. model/provider/Region/API capability and terms must be approved. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Ai Platform capability where Karpenter GPU provisioning, Foundation model access and Converse/Invoke API are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pending resource/label/topology constraints select compatible EC2 capacity. model/provider/Region/API capability and terms must be approved. normalized/model APIs differ in streaming, tools and request schema. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-07

- [ ] **Question:** Design a production Ai Platform capability where G-family GPU, Converse/Invoke API and Training job are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. normalized/model APIs differ in streaming, tools and request schema. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Ai Platform capability where P-family GPU, Foundation model access and Processing job are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. model/provider/Region/API capability and terms must be approved. managed batch preprocessing/evaluation under reproducible container and data inputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-09

- [ ] **Question:** Design a production Ai Platform capability where Foundation model access, Converse/Invoke API and GPU node pool are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model/provider/Region/API capability and terms must be approved. normalized/model APIs differ in streaming, tools and request schema. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-AI-PLATFORM-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Ai Platform capability where Converse/Invoke API, Training job and Karpenter GPU provisioning are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: normalized/model APIs differ in streaming, tools and request schema. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. pending resource/label/topology constraints select compatible EC2 capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-AI-PLATFORM-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Foundation model access. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-foundation-models` as one read-only checkpoint, not the whole diagnosis. model/provider/Region/API capability and terms must be approved. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Converse/Invoke API. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-training-jobs` as one read-only checkpoint, not the whole diagnosis. normalized/model APIs differ in streaming, tools and request schema. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Training job. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` as one read-only checkpoint, not the whole diagnosis. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Processing job. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` as one read-only checkpoint, not the whole diagnosis. managed batch preprocessing/evaluation under reproducible container and data inputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GPU node pool. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-foundation-models` as one read-only checkpoint, not the whole diagnosis. hardware/AMI/driver/toolkit/plugin compatibility and taints isolate accelerators. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Karpenter GPU provisioning. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-training-jobs` as one read-only checkpoint, not the whole diagnosis. pending resource/label/topology constraints select compatible EC2 capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving G-family GPU. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get nodes -L karpenter.k8s.aws/instance-gpu-name` as one read-only checkpoint, not the whole diagnosis. graphics/inference-oriented NVIDIA instances with generation-specific GPU/memory/network. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving P-family GPU. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-instance-types --filters Name=instance-type,Values='g*','p*','inf*','trn*'` as one read-only checkpoint, not the whole diagnosis. high-end training/HPC and large inference with NVLink/EFA/UltraCluster features by generation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Foundation model access. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws bedrock list-foundation-models` as one read-only checkpoint, not the whole diagnosis. model/provider/Region/API capability and terms must be approved. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-AI-PLATFORM-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Converse/Invoke API. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-training-jobs` as one read-only checkpoint, not the whole diagnosis. normalized/model APIs differ in streaming, tools and request schema. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
