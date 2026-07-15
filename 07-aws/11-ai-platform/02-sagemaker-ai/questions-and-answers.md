# Amazon SageMaker AI — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-SAGEMAKER-AI-JN-01

- [ ] **Question:** What is Training job, and why does it matter in Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** immutable container/data/hyperparameter/instance run writes model artifacts/metrics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SAGEMAKER-AI-JN-02

- [ ] **Question:** What is Processing job, and why does it matter in Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** managed batch preprocessing/evaluation under reproducible container and data inputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SAGEMAKER-AI-JN-03

- [ ] **Question:** What is Pipeline, and why does it matter in Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DAG connects parameterized steps, cache and conditions with lineage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SAGEMAKER-AI-JN-04

- [ ] **Question:** What is Model Registry, and why does it matter in Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** model packages/versions/approval status bind artifact/container/evidence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SAGEMAKER-AI-JN-05

- [ ] **Question:** What is Real-time endpoint, and why does it matter in Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** provisioned variants serve synchronous low-latency predictions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SAGEMAKER-AI-JN-06

- [ ] **Question:** What is Async/serverless/batch, and why does it matter in Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** queued, intermittent or offline modes trade latency/capacity/features. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SAGEMAKER-AI-JN-07

- [ ] **Question:** What is Multi-model endpoint, and why does it matter in Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** shares fleet and dynamically loads models with cache/isolation/cold-start risk. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-SAGEMAKER-AI-JN-08

- [ ] **Code:** **Question:** What does `aws sagemaker-runtime invoke-endpoint --endpoint-name ENDPOINT --body fileb://request.json output.json` help you verify for Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: weighted/shadow traffic supports controlled release under metric/eval gates.

### AMAZON-SAGEMAKER-AI-JN-09

- [ ] **Code:** **Question:** What does `aws sagemaker list-training-jobs` help you verify for Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: invocation/concurrency/backlog metrics must account for model load and downstream.

### AMAZON-SAGEMAKER-AI-JN-10

- [ ] **Code:** **Question:** What does `aws sagemaker list-model-packages --model-package-group-name GROUP` help you verify for Amazon SageMaker AI?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: managed monitoring/explainability/bias features need task-specific thresholds and ownership.

## Junior — procedural and command questions

### AMAZON-SAGEMAKER-AI-JP-01

- [ ] **Code:** **Question:** A basic Training job check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-training-jobs` and capture exact status/reason/request ID. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-02

- [ ] **Question:** A basic Processing job check fails. What would you do first?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-model-packages --model-package-group-name GROUP` and capture exact status/reason/request ID. managed batch preprocessing/evaluation under reproducible container and data inputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-03

- [ ] **Question:** A basic Pipeline check fails. What would you do first?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker describe-endpoint --endpoint-name ENDPOINT` and capture exact status/reason/request ID. DAG connects parameterized steps, cache and conditions with lineage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-04

- [ ] **Code:** **Question:** A basic Model Registry check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SageMaker AI — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker-runtime invoke-endpoint --endpoint-name ENDPOINT --body fileb://request.json output.json` and capture exact status/reason/request ID. model packages/versions/approval status bind artifact/container/evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-05

- [ ] **Question:** A basic Real-time endpoint check fails. What would you do first?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-training-jobs` and capture exact status/reason/request ID. provisioned variants serve synchronous low-latency predictions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-06

- [ ] **Question:** A basic Async/serverless/batch check fails. What would you do first?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-model-packages --model-package-group-name GROUP` and capture exact status/reason/request ID. queued, intermittent or offline modes trade latency/capacity/features. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-07

- [ ] **Code:** **Question:** A basic Multi-model endpoint check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker describe-endpoint --endpoint-name ENDPOINT` and capture exact status/reason/request ID. shares fleet and dynamically loads models with cache/isolation/cold-start risk. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-08

- [ ] **Question:** A basic Production variant check fails. What would you do first?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker-runtime invoke-endpoint --endpoint-name ENDPOINT --body fileb://request.json output.json` and capture exact status/reason/request ID. weighted/shadow traffic supports controlled release under metric/eval gates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-09

- [ ] **Question:** A basic Endpoint autoscaling check fails. What would you do first?
> **Covered in:** [Amazon SageMaker AI — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-training-jobs` and capture exact status/reason/request ID. invocation/concurrency/backlog metrics must account for model load and downstream. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-SAGEMAKER-AI-JP-10

- [ ] **Code:** **Question:** A basic Model Monitor/Clarify check fails. What would you do first using the CLI?
> **Covered in:** [Amazon SageMaker AI — Security model](README.md#security-model)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sagemaker list-model-packages --model-package-group-name GROUP` and capture exact status/reason/request ID. managed monitoring/explainability/bias features need task-specific thresholds and ownership. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-SAGEMAKER-AI-MN-01

- [ ] **Question:** Compare Training job with Processing job. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Training job: immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Processing job: managed batch preprocessing/evaluation under reproducible container and data inputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-02

- [ ] **Question:** Compare Processing job with Pipeline. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Processing job: managed batch preprocessing/evaluation under reproducible container and data inputs. Pipeline: DAG connects parameterized steps, cache and conditions with lineage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-03

- [ ] **Question:** Compare Pipeline with Model Registry. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pipeline: DAG connects parameterized steps, cache and conditions with lineage. Model Registry: model packages/versions/approval status bind artifact/container/evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-04

- [ ] **Configuration review:** **Question:** Compare Model Registry with Real-time endpoint. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Model Registry: model packages/versions/approval status bind artifact/container/evidence. Real-time endpoint: provisioned variants serve synchronous low-latency predictions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-05

- [ ] **Question:** Compare Real-time endpoint with Async/serverless/batch. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Real-time endpoint: provisioned variants serve synchronous low-latency predictions. Async/serverless/batch: queued, intermittent or offline modes trade latency/capacity/features. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-06

- [ ] **Question:** Compare Async/serverless/batch with Multi-model endpoint. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Async/serverless/batch: queued, intermittent or offline modes trade latency/capacity/features. Multi-model endpoint: shares fleet and dynamically loads models with cache/isolation/cold-start risk. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-07

- [ ] **Configuration review:** **Question:** Compare Multi-model endpoint with Production variant. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Multi-model endpoint: shares fleet and dynamically loads models with cache/isolation/cold-start risk. Production variant: weighted/shadow traffic supports controlled release under metric/eval gates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-08

- [ ] **Question:** Compare Production variant with Endpoint autoscaling. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Production variant: weighted/shadow traffic supports controlled release under metric/eval gates. Endpoint autoscaling: invocation/concurrency/backlog metrics must account for model load and downstream. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-09

- [ ] **Question:** Compare Endpoint autoscaling with Model Monitor/Clarify. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Endpoint autoscaling: invocation/concurrency/backlog metrics must account for model load and downstream. Model Monitor/Clarify: managed monitoring/explainability/bias features need task-specific thresholds and ownership. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-SAGEMAKER-AI-MN-10

- [ ] **Configuration review:** **Question:** Compare Model Monitor/Clarify with Training job. When would each change your design?
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Model Monitor/Clarify: managed monitoring/explainability/bias features need task-specific thresholds and ownership. Training job: immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-SAGEMAKER-AI-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Training job; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-training-jobs` plus recent events/changes, then correlate the service-specific SLI. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-02

- [ ] **Question:** Production is degraded around Processing job; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-model-packages --model-package-group-name GROUP` plus recent events/changes, then correlate the service-specific SLI. managed batch preprocessing/evaluation under reproducible container and data inputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pipeline; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker describe-endpoint --endpoint-name ENDPOINT` plus recent events/changes, then correlate the service-specific SLI. DAG connects parameterized steps, cache and conditions with lineage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-04

- [ ] **Question:** Production is degraded around Model Registry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker-runtime invoke-endpoint --endpoint-name ENDPOINT --body fileb://request.json output.json` plus recent events/changes, then correlate the service-specific SLI. model packages/versions/approval status bind artifact/container/evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Real-time endpoint; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-training-jobs` plus recent events/changes, then correlate the service-specific SLI. provisioned variants serve synchronous low-latency predictions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-06

- [ ] **Question:** Production is degraded around Async/serverless/batch; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-model-packages --model-package-group-name GROUP` plus recent events/changes, then correlate the service-specific SLI. queued, intermittent or offline modes trade latency/capacity/features. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Multi-model endpoint; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker describe-endpoint --endpoint-name ENDPOINT` plus recent events/changes, then correlate the service-specific SLI. shares fleet and dynamically loads models with cache/isolation/cold-start risk. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-08

- [ ] **Question:** Production is degraded around Production variant; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker-runtime invoke-endpoint --endpoint-name ENDPOINT --body fileb://request.json output.json` plus recent events/changes, then correlate the service-specific SLI. weighted/shadow traffic supports controlled release under metric/eval gates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Endpoint autoscaling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-training-jobs` plus recent events/changes, then correlate the service-specific SLI. invocation/concurrency/backlog metrics must account for model load and downstream. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-SAGEMAKER-AI-MP-10

- [ ] **Question:** Production is degraded around Model Monitor/Clarify; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sagemaker list-model-packages --model-package-group-name GROUP` plus recent events/changes, then correlate the service-specific SLI. managed monitoring/explainability/bias features need task-specific thresholds and ownership. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-SAGEMAKER-AI-SN-01

- [ ] **Question:** Design a production Amazon SageMaker AI capability where Training job, Model Registry and Multi-model endpoint are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: immutable container/data/hyperparameter/instance run writes model artifacts/metrics. model packages/versions/approval status bind artifact/container/evidence. shares fleet and dynamically loads models with cache/isolation/cold-start risk. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SageMaker AI capability where Processing job, Real-time endpoint and Production variant are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed batch preprocessing/evaluation under reproducible container and data inputs. provisioned variants serve synchronous low-latency predictions. weighted/shadow traffic supports controlled release under metric/eval gates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-03

- [ ] **Question:** Design a production Amazon SageMaker AI capability where Pipeline, Async/serverless/batch and Endpoint autoscaling are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: DAG connects parameterized steps, cache and conditions with lineage. queued, intermittent or offline modes trade latency/capacity/features. invocation/concurrency/backlog metrics must account for model load and downstream. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SageMaker AI capability where Model Registry, Multi-model endpoint and Model Monitor/Clarify are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model packages/versions/approval status bind artifact/container/evidence. shares fleet and dynamically loads models with cache/isolation/cold-start risk. managed monitoring/explainability/bias features need task-specific thresholds and ownership. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-05

- [ ] **Question:** Design a production Amazon SageMaker AI capability where Real-time endpoint, Production variant and Training job are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provisioned variants serve synchronous low-latency predictions. weighted/shadow traffic supports controlled release under metric/eval gates. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SageMaker AI capability where Async/serverless/batch, Endpoint autoscaling and Processing job are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: queued, intermittent or offline modes trade latency/capacity/features. invocation/concurrency/backlog metrics must account for model load and downstream. managed batch preprocessing/evaluation under reproducible container and data inputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-07

- [ ] **Question:** Design a production Amazon SageMaker AI capability where Multi-model endpoint, Model Monitor/Clarify and Pipeline are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shares fleet and dynamically loads models with cache/isolation/cold-start risk. managed monitoring/explainability/bias features need task-specific thresholds and ownership. DAG connects parameterized steps, cache and conditions with lineage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SageMaker AI capability where Production variant, Training job and Model Registry are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: weighted/shadow traffic supports controlled release under metric/eval gates. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. model packages/versions/approval status bind artifact/container/evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-09

- [ ] **Question:** Design a production Amazon SageMaker AI capability where Endpoint autoscaling, Processing job and Real-time endpoint are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: invocation/concurrency/backlog metrics must account for model load and downstream. managed batch preprocessing/evaluation under reproducible container and data inputs. provisioned variants serve synchronous low-latency predictions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-SAGEMAKER-AI-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon SageMaker AI capability where Model Monitor/Clarify, Pipeline and Async/serverless/batch are first-class requirements.
> **Covered in:** [Amazon SageMaker AI — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed monitoring/explainability/bias features need task-specific thresholds and ownership. DAG connects parameterized steps, cache and conditions with lineage. queued, intermittent or offline modes trade latency/capacity/features. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-SAGEMAKER-AI-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Training job. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-training-jobs` as one read-only checkpoint, not the whole diagnosis. immutable container/data/hyperparameter/instance run writes model artifacts/metrics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Processing job. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-model-packages --model-package-group-name GROUP` as one read-only checkpoint, not the whole diagnosis. managed batch preprocessing/evaluation under reproducible container and data inputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pipeline. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker describe-endpoint --endpoint-name ENDPOINT` as one read-only checkpoint, not the whole diagnosis. DAG connects parameterized steps, cache and conditions with lineage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model Registry. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker-runtime invoke-endpoint --endpoint-name ENDPOINT --body fileb://request.json output.json` as one read-only checkpoint, not the whole diagnosis. model packages/versions/approval status bind artifact/container/evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Real-time endpoint. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-training-jobs` as one read-only checkpoint, not the whole diagnosis. provisioned variants serve synchronous low-latency predictions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Async/serverless/batch. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-model-packages --model-package-group-name GROUP` as one read-only checkpoint, not the whole diagnosis. queued, intermittent or offline modes trade latency/capacity/features. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multi-model endpoint. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker describe-endpoint --endpoint-name ENDPOINT` as one read-only checkpoint, not the whole diagnosis. shares fleet and dynamically loads models with cache/isolation/cold-start risk. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Production variant. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker-runtime invoke-endpoint --endpoint-name ENDPOINT --body fileb://request.json output.json` as one read-only checkpoint, not the whole diagnosis. weighted/shadow traffic supports controlled release under metric/eval gates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Endpoint autoscaling. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-training-jobs` as one read-only checkpoint, not the whole diagnosis. invocation/concurrency/backlog metrics must account for model load and downstream. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-SAGEMAKER-AI-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model Monitor/Clarify. How do you lead it end to end?
> **Covered in:** [Amazon SageMaker AI — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sagemaker list-model-packages --model-package-group-name GROUP` as one read-only checkpoint, not the whole diagnosis. managed monitoring/explainability/bias features need task-specific thresholds and ownership. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon Bedrock](../01-bedrock/README.md) · [Study note](README.md) · [Next: AI/ML workloads on Amazon EKS →](../03-eks-ai-inference/README.md)

<!-- reading-navigation:end -->
