# MLOps/LLMOps FinOps and capacity — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-01

- [ ] **Question:** What is Cost taxonomy, and why does it matter in MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-02

- [ ] **Question:** What is Allocation, and why does it matter in MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-03

- [ ] **Question:** What is Unit economics, and why does it matter in MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-04

- [ ] **Question:** What is Goodput, and why does it matter in MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-05

- [ ] **Question:** What is Training efficiency, and why does it matter in MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-06

- [ ] **Question:** What is Serving efficiency, and why does it matter in MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-07

- [ ] **Question:** What is Provider reconciliation, and why does it matter in MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** gateway estimates compare with provider usage/invoice and flag routing/metering drift. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-08

- [ ] **Code:** **Question:** What does `python scripts/reconcile_usage.py --provider PROVIDER --month YYYY-MM` help you verify for MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-09

- [ ] **Code:** **Question:** What does `python scripts/cost_per_release.py --release RELEASE_ID` help you verify for MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JN-10

- [ ] **Code:** **Question:** What does `kubectl top pod -A --containers` help you verify for MLOps/LLMOps FinOps and capacity?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold.

## Junior — procedural and command questions

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-01

- [ ] **Code:** **Question:** A basic Cost taxonomy check fails. What would you do first using the CLI?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/cost_per_release.py --release RELEASE_ID` and capture exact status/reason/request ID. training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-02

- [ ] **Question:** A basic Allocation check fails. What would you do first?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -A --containers` and capture exact status/reason/request ID. tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-03

- [ ] **Question:** A basic Unit economics check fails. What would you do first?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi dmon -s pucvmet` and capture exact status/reason/request ID. cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-04

- [ ] **Code:** **Question:** A basic Goodput check fails. What would you do first using the CLI?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/reconcile_usage.py --provider PROVIDER --month YYYY-MM` and capture exact status/reason/request ID. paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-05

- [ ] **Question:** A basic Training efficiency check fails. What would you do first?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/cost_per_release.py --release RELEASE_ID` and capture exact status/reason/request ID. samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-06

- [ ] **Question:** A basic Serving efficiency check fails. What would you do first?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -A --containers` and capture exact status/reason/request ID. batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-07

- [ ] **Code:** **Question:** A basic Provider reconciliation check fails. What would you do first using the CLI?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `nvidia-smi dmon -s pucvmet` and capture exact status/reason/request ID. gateway estimates compare with provider usage/invoice and flag routing/metering drift. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-08

- [ ] **Question:** A basic Budget control check fails. What would you do first?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/reconcile_usage.py --provider PROVIDER --month YYYY-MM` and capture exact status/reason/request ID. forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-09

- [ ] **Question:** A basic Commitment check fails. What would you do first?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/cost_per_release.py --release RELEASE_ID` and capture exact status/reason/request ID. reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-JP-10

- [ ] **Code:** **Question:** A basic Optimization gate check fails. What would you do first using the CLI?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl top pod -A --containers` and capture exact status/reason/request ID. every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-01

- [ ] **Question:** Compare Cost taxonomy with Allocation. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cost taxonomy: training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. Allocation: tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-02

- [ ] **Question:** Compare Allocation with Unit economics. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Allocation: tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. Unit economics: cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-03

- [ ] **Question:** Compare Unit economics with Goodput. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Unit economics: cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. Goodput: paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Goodput with Training efficiency. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Goodput: paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. Training efficiency: samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-05

- [ ] **Question:** Compare Training efficiency with Serving efficiency. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Training efficiency: samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. Serving efficiency: batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-06

- [ ] **Question:** Compare Serving efficiency with Provider reconciliation. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Serving efficiency: batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. Provider reconciliation: gateway estimates compare with provider usage/invoice and flag routing/metering drift. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Provider reconciliation with Budget control. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Provider reconciliation: gateway estimates compare with provider usage/invoice and flag routing/metering drift. Budget control: forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-08

- [ ] **Question:** Compare Budget control with Commitment. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Budget control: forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely. Commitment: reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-09

- [ ] **Question:** Compare Commitment with Optimization gate. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Commitment: reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance. Optimization gate: every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Optimization gate with Cost taxonomy. When would each change your design?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Optimization gate: every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold. Cost taxonomy: training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cost taxonomy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/cost_per_release.py --release RELEASE_ID` plus recent events/changes, then correlate the service-specific SLI. training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-02

- [ ] **Question:** Production is degraded around Allocation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Unit economics; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi dmon -s pucvmet` plus recent events/changes, then correlate the service-specific SLI. cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-04

- [ ] **Question:** Production is degraded around Goodput; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/reconcile_usage.py --provider PROVIDER --month YYYY-MM` plus recent events/changes, then correlate the service-specific SLI. paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Training efficiency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/cost_per_release.py --release RELEASE_ID` plus recent events/changes, then correlate the service-specific SLI. samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-06

- [ ] **Question:** Production is degraded around Serving efficiency; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Provider reconciliation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `nvidia-smi dmon -s pucvmet` plus recent events/changes, then correlate the service-specific SLI. gateway estimates compare with provider usage/invoice and flag routing/metering drift. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-08

- [ ] **Question:** Production is degraded around Budget control; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/reconcile_usage.py --provider PROVIDER --month YYYY-MM` plus recent events/changes, then correlate the service-specific SLI. forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Commitment; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/cost_per_release.py --release RELEASE_ID` plus recent events/changes, then correlate the service-specific SLI. reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-MP-10

- [ ] **Question:** Production is degraded around Optimization gate; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl top pod -A --containers` plus recent events/changes, then correlate the service-specific SLI. every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-01

- [ ] **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Cost taxonomy, Goodput and Provider reconciliation are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. gateway estimates compare with provider usage/invoice and flag routing/metering drift. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Allocation, Training efficiency and Budget control are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-03

- [ ] **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Unit economics, Serving efficiency and Commitment are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Goodput, Provider reconciliation and Optimization gate are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. gateway estimates compare with provider usage/invoice and flag routing/metering drift. every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-05

- [ ] **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Training efficiency, Budget control and Cost taxonomy are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely. training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Serving efficiency, Commitment and Allocation are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance. tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-07

- [ ] **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Provider reconciliation, Optimization gate and Unit economics are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: gateway estimates compare with provider usage/invoice and flag routing/metering drift. every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold. cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Budget control, Cost taxonomy and Goodput are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely. training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-09

- [ ] **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Commitment, Allocation and Training efficiency are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance. tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps FinOps and capacity capability where Optimization gate, Unit economics and Serving efficiency are first-class requirements.
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold. cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cost taxonomy. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/cost_per_release.py --release RELEASE_ID` as one read-only checkpoint, not the whole diagnosis. training GPU, serving capacity/provider tokens, storage, vector/search, network and telemetry are separated. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Allocation. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. tenant/project/model/release/environment/owner identifiers join billing without high-cardinality metric abuse. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Unit economics. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi dmon -s pucvmet` as one read-only checkpoint, not the whole diagnosis. cost per trained candidate, evaluated case, indexed document and successful quality-controlled request guide decisions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Goodput. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/reconcile_usage.py --provider PROVIDER --month YYYY-MM` as one read-only checkpoint, not the whole diagnosis. paid work meeting latency/quality/safety is distinguished from raw tokens, requests or GPU utilization. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Training efficiency. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/cost_per_release.py --release RELEASE_ID` as one read-only checkpoint, not the whole diagnosis. samples/tokens to target quality, GPU goodput, checkpoint waste and experiment pruning control spend. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Serving efficiency. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. batching, KV/cache, quantization, routing, autoscaling and warm capacity trade cost against SLO/quality. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Provider reconciliation. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `nvidia-smi dmon -s pucvmet` as one read-only checkpoint, not the whole diagnosis. gateway estimates compare with provider usage/invoice and flag routing/metering drift. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Budget control. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/reconcile_usage.py --provider PROVIDER --month YYYY-MM` as one read-only checkpoint, not the whole diagnosis. forecast, quota, alert, admission and approval stop runaway experiments/agents/evaluations safely. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Commitment. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/cost_per_release.py --release RELEASE_ID` as one read-only checkpoint, not the whole diagnosis. reservations/savings plans/capacity contracts match stable floor while burst/interruption strategies cover variance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-FINOPS-AND-CAPACITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Optimization gate. How do you lead it end to end?
> **Covered in:** [MLOps/LLMOps FinOps and capacity — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl top pod -A --containers` as one read-only checkpoint, not the whole diagnosis. every saving proposal states expected amount, SLO/quality/security risk, experiment and rollback threshold. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AI supply chain, signing and provenance](../25-ai-supply-chain/README.md) · [Study note](README.md) · [Next: Agents and tool-using AI →](../../09-agents-and-tool-using-ai/README.md)

<!-- reading-navigation:end -->
