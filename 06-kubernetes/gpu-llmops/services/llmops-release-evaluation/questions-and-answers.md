# LLMOps release and evaluation on Kubernetes — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-01

- [ ] **Question:** What is Release manifest, and why does it matter in LLMOps release and evaluation on Kubernetes?

**Answer:** exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-02

- [ ] **Question:** What is Golden dataset, and why does it matter in LLMOps release and evaluation on Kubernetes?

**Answer:** versioned owned task examples and edge/adversarial cases. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-03

- [ ] **Question:** What is Offline evaluation, and why does it matter in LLMOps release and evaluation on Kubernetes?

**Answer:** compares quality/safety/latency/cost before production under reproducible inputs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-04

- [ ] **Question:** What is Model-as-judge, and why does it matter in LLMOps release and evaluation on Kubernetes?

**Answer:** scalable evaluator with bias/non-determinism/calibration and version risk. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-05

- [ ] **Question:** What is Shadow evaluation, and why does it matter in LLMOps release and evaluation on Kubernetes?

**Answer:** production input copy provides realism under privacy/side-effect/cost controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-06

- [ ] **Question:** What is Canary, and why does it matter in LLMOps release and evaluation on Kubernetes?

**Answer:** small user/tenant traffic with automated infrastructure and quality rollback gates. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-07

- [ ] **Question:** What is Champion/challenger, and why does it matter in LLMOps release and evaluation on Kubernetes?

**Answer:** compares incumbent/candidate while retaining explicit promotion authority. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-08

- [ ] **Code:** **Question:** What does `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` help you verify for LLMOps release and evaluation on Kubernetes?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: prompt or retrieval changes are model-release changes and need lineage/eval.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-09

- [ ] **Code:** **Question:** What does `kubectl get deployment,inferenceservice -n inference -o yaml` help you verify for LLMOps release and evaluation on Kubernetes?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: retains prior artifacts/config/index and handles in-flight/cache/schema compatibility.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JN-10

- [ ] **Code:** **Question:** What does `kubectl rollout history deployment/NAME -n inference` help you verify for LLMOps release and evaluation on Kubernetes?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: approval links dataset/evaluator/results/exception/actor to deployed revision.

## Junior — procedural and command questions

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-01

- [ ] **Code:** **Question:** A basic Release manifest check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get deployment,inferenceservice -n inference -o yaml` and capture exact status/reason/request ID. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-02

- [ ] **Question:** A basic Golden dataset check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/NAME -n inference` and capture exact status/reason/request ID. versioned owned task examples and edge/adversarial cases. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-03

- [ ] **Question:** A basic Offline evaluation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app history APP` and capture exact status/reason/request ID. compares quality/safety/latency/cost before production under reproducible inputs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-04

- [ ] **Code:** **Question:** A basic Model-as-judge check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` and capture exact status/reason/request ID. scalable evaluator with bias/non-determinism/calibration and version risk. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-05

- [ ] **Question:** A basic Shadow evaluation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get deployment,inferenceservice -n inference -o yaml` and capture exact status/reason/request ID. production input copy provides realism under privacy/side-effect/cost controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-06

- [ ] **Question:** A basic Canary check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/NAME -n inference` and capture exact status/reason/request ID. small user/tenant traffic with automated infrastructure and quality rollback gates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-07

- [ ] **Code:** **Question:** A basic Champion/challenger check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argocd app history APP` and capture exact status/reason/request ID. compares incumbent/candidate while retaining explicit promotion authority. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-08

- [ ] **Question:** A basic Prompt/index drift check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` and capture exact status/reason/request ID. prompt or retrieval changes are model-release changes and need lineage/eval. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-09

- [ ] **Question:** A basic Rollback check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get deployment,inferenceservice -n inference -o yaml` and capture exact status/reason/request ID. retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-JP-10

- [ ] **Code:** **Question:** A basic Audit check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl rollout history deployment/NAME -n inference` and capture exact status/reason/request ID. approval links dataset/evaluator/results/exception/actor to deployed revision. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-01

- [ ] **Question:** Compare Release manifest with Golden dataset. When would each change your design?

**Answer:** Release manifest: exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Golden dataset: versioned owned task examples and edge/adversarial cases. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-02

- [ ] **Question:** Compare Golden dataset with Offline evaluation. When would each change your design?

**Answer:** Golden dataset: versioned owned task examples and edge/adversarial cases. Offline evaluation: compares quality/safety/latency/cost before production under reproducible inputs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-03

- [ ] **Question:** Compare Offline evaluation with Model-as-judge. When would each change your design?

**Answer:** Offline evaluation: compares quality/safety/latency/cost before production under reproducible inputs. Model-as-judge: scalable evaluator with bias/non-determinism/calibration and version risk. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-04

- [ ] **Configuration review:** **Question:** Compare Model-as-judge with Shadow evaluation. When would each change your design?

**Answer:** Model-as-judge: scalable evaluator with bias/non-determinism/calibration and version risk. Shadow evaluation: production input copy provides realism under privacy/side-effect/cost controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-05

- [ ] **Question:** Compare Shadow evaluation with Canary. When would each change your design?

**Answer:** Shadow evaluation: production input copy provides realism under privacy/side-effect/cost controls. Canary: small user/tenant traffic with automated infrastructure and quality rollback gates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-06

- [ ] **Question:** Compare Canary with Champion/challenger. When would each change your design?

**Answer:** Canary: small user/tenant traffic with automated infrastructure and quality rollback gates. Champion/challenger: compares incumbent/candidate while retaining explicit promotion authority. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-07

- [ ] **Configuration review:** **Question:** Compare Champion/challenger with Prompt/index drift. When would each change your design?

**Answer:** Champion/challenger: compares incumbent/candidate while retaining explicit promotion authority. Prompt/index drift: prompt or retrieval changes are model-release changes and need lineage/eval. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-08

- [ ] **Question:** Compare Prompt/index drift with Rollback. When would each change your design?

**Answer:** Prompt/index drift: prompt or retrieval changes are model-release changes and need lineage/eval. Rollback: retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-09

- [ ] **Question:** Compare Rollback with Audit. When would each change your design?

**Answer:** Rollback: retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. Audit: approval links dataset/evaluator/results/exception/actor to deployed revision. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MN-10

- [ ] **Configuration review:** **Question:** Compare Audit with Release manifest. When would each change your design?

**Answer:** Audit: approval links dataset/evaluator/results/exception/actor to deployed revision. Release manifest: exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Release manifest; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get deployment,inferenceservice -n inference -o yaml` plus recent events/changes, then correlate the service-specific SLI. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-02

- [ ] **Question:** Production is degraded around Golden dataset; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/NAME -n inference` plus recent events/changes, then correlate the service-specific SLI. versioned owned task examples and edge/adversarial cases. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Offline evaluation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app history APP` plus recent events/changes, then correlate the service-specific SLI. compares quality/safety/latency/cost before production under reproducible inputs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-04

- [ ] **Question:** Production is degraded around Model-as-judge; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` plus recent events/changes, then correlate the service-specific SLI. scalable evaluator with bias/non-determinism/calibration and version risk. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Shadow evaluation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get deployment,inferenceservice -n inference -o yaml` plus recent events/changes, then correlate the service-specific SLI. production input copy provides realism under privacy/side-effect/cost controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-06

- [ ] **Question:** Production is degraded around Canary; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/NAME -n inference` plus recent events/changes, then correlate the service-specific SLI. small user/tenant traffic with automated infrastructure and quality rollback gates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Champion/challenger; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argocd app history APP` plus recent events/changes, then correlate the service-specific SLI. compares incumbent/candidate while retaining explicit promotion authority. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-08

- [ ] **Question:** Production is degraded around Prompt/index drift; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` plus recent events/changes, then correlate the service-specific SLI. prompt or retrieval changes are model-release changes and need lineage/eval. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Rollback; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get deployment,inferenceservice -n inference -o yaml` plus recent events/changes, then correlate the service-specific SLI. retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-MP-10

- [ ] **Question:** Production is degraded around Audit; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl rollout history deployment/NAME -n inference` plus recent events/changes, then correlate the service-specific SLI. approval links dataset/evaluator/results/exception/actor to deployed revision. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-01

- [ ] **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Release manifest, Model-as-judge and Champion/challenger are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. scalable evaluator with bias/non-determinism/calibration and version risk. compares incumbent/candidate while retaining explicit promotion authority. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Golden dataset, Shadow evaluation and Prompt/index drift are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: versioned owned task examples and edge/adversarial cases. production input copy provides realism under privacy/side-effect/cost controls. prompt or retrieval changes are model-release changes and need lineage/eval. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-03

- [ ] **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Offline evaluation, Canary and Rollback are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: compares quality/safety/latency/cost before production under reproducible inputs. small user/tenant traffic with automated infrastructure and quality rollback gates. retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Model-as-judge, Champion/challenger and Audit are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scalable evaluator with bias/non-determinism/calibration and version risk. compares incumbent/candidate while retaining explicit promotion authority. approval links dataset/evaluator/results/exception/actor to deployed revision. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-05

- [ ] **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Shadow evaluation, Prompt/index drift and Release manifest are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: production input copy provides realism under privacy/side-effect/cost controls. prompt or retrieval changes are model-release changes and need lineage/eval. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Canary, Rollback and Golden dataset are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: small user/tenant traffic with automated infrastructure and quality rollback gates. retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. versioned owned task examples and edge/adversarial cases. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-07

- [ ] **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Champion/challenger, Audit and Offline evaluation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: compares incumbent/candidate while retaining explicit promotion authority. approval links dataset/evaluator/results/exception/actor to deployed revision. compares quality/safety/latency/cost before production under reproducible inputs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Prompt/index drift, Release manifest and Model-as-judge are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: prompt or retrieval changes are model-release changes and need lineage/eval. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. scalable evaluator with bias/non-determinism/calibration and version risk. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-09

- [ ] **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Rollback, Golden dataset and Shadow evaluation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. versioned owned task examples and edge/adversarial cases. production input copy provides realism under privacy/side-effect/cost controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production LLMOps release and evaluation on Kubernetes capability where Audit, Offline evaluation and Canary are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: approval links dataset/evaluator/results/exception/actor to deployed revision. compares quality/safety/latency/cost before production under reproducible inputs. small user/tenant traffic with automated infrastructure and quality rollback gates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Release manifest. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get deployment,inferenceservice -n inference -o yaml` as one read-only checkpoint, not the whole diagnosis. exact model/tokenizer/template/adapter/runtime/image/flags/hardware/index/evaluator identity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Golden dataset. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/NAME -n inference` as one read-only checkpoint, not the whole diagnosis. versioned owned task examples and edge/adversarial cases. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Offline evaluation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app history APP` as one read-only checkpoint, not the whole diagnosis. compares quality/safety/latency/cost before production under reproducible inputs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Model-as-judge. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` as one read-only checkpoint, not the whole diagnosis. scalable evaluator with bias/non-determinism/calibration and version risk. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Shadow evaluation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get deployment,inferenceservice -n inference -o yaml` as one read-only checkpoint, not the whole diagnosis. production input copy provides realism under privacy/side-effect/cost controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Canary. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/NAME -n inference` as one read-only checkpoint, not the whole diagnosis. small user/tenant traffic with automated infrastructure and quality rollback gates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Champion/challenger. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argocd app history APP` as one read-only checkpoint, not the whole diagnosis. compares incumbent/candidate while retaining explicit promotion authority. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prompt/index drift. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest release.yaml --dataset golden-v12.jsonl` as one read-only checkpoint, not the whole diagnosis. prompt or retrieval changes are model-release changes and need lineage/eval. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rollback. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get deployment,inferenceservice -n inference -o yaml` as one read-only checkpoint, not the whole diagnosis. retains prior artifacts/config/index and handles in-flight/cache/schema compatibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### LLMOPS-RELEASE-AND-EVALUATION-ON-KUBERNETES-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Audit. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl rollout history deployment/NAME -n inference` as one read-only checkpoint, not the whole diagnosis. approval links dataset/evaluator/results/exception/actor to deployed revision. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
