# MLOps/LLMOps platform architecture — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-01

- [ ] **Question:** What is Lifecycle state machine, and why does it matter in MLOps/LLMOps platform architecture?

**Answer:** idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-02

- [ ] **Question:** What is Control plane, and why does it matter in MLOps/LLMOps platform architecture?

**Answer:** metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-03

- [ ] **Question:** What is Data plane, and why does it matter in MLOps/LLMOps platform architecture?

**Answer:** training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-04

- [ ] **Question:** What is Release unit, and why does it matter in MLOps/LLMOps platform architecture?

**Answer:** data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-05

- [ ] **Question:** What is Metadata spine, and why does it matter in MLOps/LLMOps platform architecture?

**Answer:** stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-06

- [ ] **Question:** What is Environment promotion, and why does it matter in MLOps/LLMOps platform architecture?

**Answer:** promote immutable evidence/artifacts while configuration and credentials remain target-specific. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-07

- [ ] **Question:** What is Human decision, and why does it matter in MLOps/LLMOps platform architecture?

**Answer:** risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-08

- [ ] **Code:** **Question:** What does `curl -s http://metadata-api/health` help you verify for MLOps/LLMOps platform architecture?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: controllers compare desired release with observed deployment/index/evaluation state and retry idempotently.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-09

- [ ] **Code:** **Question:** What does `mlflow experiments search` help you verify for MLOps/LLMOps platform architecture?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JN-10

- [ ] **Code:** **Question:** What does `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` help you verify for MLOps/LLMOps platform architecture?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories.

## Junior — procedural and command questions

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-01

- [ ] **Code:** **Question:** A basic Lifecycle state machine check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow experiments search` and capture exact status/reason/request ID. idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-02

- [ ] **Question:** A basic Control plane check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` and capture exact status/reason/request ID. metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-03

- [ ] **Question:** A basic Data plane check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --all` and capture exact status/reason/request ID. training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-04

- [ ] **Code:** **Question:** A basic Release unit check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://metadata-api/health` and capture exact status/reason/request ID. data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-05

- [ ] **Question:** A basic Metadata spine check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow experiments search` and capture exact status/reason/request ID. stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-06

- [ ] **Question:** A basic Environment promotion check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` and capture exact status/reason/request ID. promote immutable evidence/artifacts while configuration and credentials remain target-specific. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-07

- [ ] **Code:** **Question:** A basic Human decision check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `git log --graph --oneline --all` and capture exact status/reason/request ID. risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-08

- [ ] **Question:** A basic Reconciliation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://metadata-api/health` and capture exact status/reason/request ID. controllers compare desired release with observed deployment/index/evaluation state and retry idempotently. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-09

- [ ] **Question:** A basic Multi-tenancy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow experiments search` and capture exact status/reason/request ID. identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-JP-10

- [ ] **Code:** **Question:** A basic Exit and retirement check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` and capture exact status/reason/request ID. revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-01

- [ ] **Question:** Compare Lifecycle state machine with Control plane. When would each change your design?

**Answer:** Lifecycle state machine: idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. Control plane: metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-02

- [ ] **Question:** Compare Control plane with Data plane. When would each change your design?

**Answer:** Control plane: metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. Data plane: training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-03

- [ ] **Question:** Compare Data plane with Release unit. When would each change your design?

**Answer:** Data plane: training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. Release unit: data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-04

- [ ] **Configuration review:** **Question:** Compare Release unit with Metadata spine. When would each change your design?

**Answer:** Release unit: data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. Metadata spine: stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-05

- [ ] **Question:** Compare Metadata spine with Environment promotion. When would each change your design?

**Answer:** Metadata spine: stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. Environment promotion: promote immutable evidence/artifacts while configuration and credentials remain target-specific. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-06

- [ ] **Question:** Compare Environment promotion with Human decision. When would each change your design?

**Answer:** Environment promotion: promote immutable evidence/artifacts while configuration and credentials remain target-specific. Human decision: risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-07

- [ ] **Configuration review:** **Question:** Compare Human decision with Reconciliation. When would each change your design?

**Answer:** Human decision: risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. Reconciliation: controllers compare desired release with observed deployment/index/evaluation state and retry idempotently. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-08

- [ ] **Question:** Compare Reconciliation with Multi-tenancy. When would each change your design?

**Answer:** Reconciliation: controllers compare desired release with observed deployment/index/evaluation state and retry idempotently. Multi-tenancy: identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-09

- [ ] **Question:** Compare Multi-tenancy with Exit and retirement. When would each change your design?

**Answer:** Multi-tenancy: identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation. Exit and retirement: revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MN-10

- [ ] **Configuration review:** **Question:** Compare Exit and retirement with Lifecycle state machine. When would each change your design?

**Answer:** Exit and retirement: revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories. Lifecycle state machine: idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Lifecycle state machine; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow experiments search` plus recent events/changes, then correlate the service-specific SLI. idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-02

- [ ] **Question:** Production is degraded around Control plane; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` plus recent events/changes, then correlate the service-specific SLI. metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Data plane; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --all` plus recent events/changes, then correlate the service-specific SLI. training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-04

- [ ] **Question:** Production is degraded around Release unit; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://metadata-api/health` plus recent events/changes, then correlate the service-specific SLI. data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Metadata spine; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow experiments search` plus recent events/changes, then correlate the service-specific SLI. stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-06

- [ ] **Question:** Production is degraded around Environment promotion; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` plus recent events/changes, then correlate the service-specific SLI. promote immutable evidence/artifacts while configuration and credentials remain target-specific. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Human decision; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `git log --graph --oneline --all` plus recent events/changes, then correlate the service-specific SLI. risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-08

- [ ] **Question:** Production is degraded around Reconciliation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://metadata-api/health` plus recent events/changes, then correlate the service-specific SLI. controllers compare desired release with observed deployment/index/evaluation state and retry idempotently. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Multi-tenancy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow experiments search` plus recent events/changes, then correlate the service-specific SLI. identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-MP-10

- [ ] **Question:** Production is degraded around Exit and retirement; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` plus recent events/changes, then correlate the service-specific SLI. revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-01

- [ ] **Question:** Design a production MLOps/LLMOps platform architecture capability where Lifecycle state machine, Release unit and Human decision are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps platform architecture capability where Control plane, Metadata spine and Reconciliation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. controllers compare desired release with observed deployment/index/evaluation state and retry idempotently. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-03

- [ ] **Question:** Design a production MLOps/LLMOps platform architecture capability where Data plane, Environment promotion and Multi-tenancy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. promote immutable evidence/artifacts while configuration and credentials remain target-specific. identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps platform architecture capability where Release unit, Human decision and Exit and retirement are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-05

- [ ] **Question:** Design a production MLOps/LLMOps platform architecture capability where Metadata spine, Reconciliation and Lifecycle state machine are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. controllers compare desired release with observed deployment/index/evaluation state and retry idempotently. idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps platform architecture capability where Environment promotion, Multi-tenancy and Control plane are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: promote immutable evidence/artifacts while configuration and credentials remain target-specific. identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation. metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-07

- [ ] **Question:** Design a production MLOps/LLMOps platform architecture capability where Human decision, Exit and retirement and Data plane are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories. training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps platform architecture capability where Reconciliation, Lifecycle state machine and Release unit are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controllers compare desired release with observed deployment/index/evaluation state and retry idempotently. idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-09

- [ ] **Question:** Design a production MLOps/LLMOps platform architecture capability where Multi-tenancy, Control plane and Metadata spine are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation. metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production MLOps/LLMOps platform architecture capability where Exit and retirement, Data plane and Environment promotion are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories. training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. promote immutable evidence/artifacts while configuration and credentials remain target-specific. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Lifecycle state machine. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow experiments search` as one read-only checkpoint, not the whole diagnosis. idea, experiment, candidate, validated, approved, deployed, monitored, deprecated and retired need explicit transitions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control plane. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` as one read-only checkpoint, not the whole diagnosis. metadata, orchestration, policy, registry, approval and reconciliation coordinate work without carrying every inference payload. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data plane. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --all` as one read-only checkpoint, not the whole diagnosis. training, batch, retrieval and serving compute move protected data and model work under tenant boundaries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Release unit. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://metadata-api/health` as one read-only checkpoint, not the whole diagnosis. data/code/config/model/runtime/evaluator/policy identity must travel together instead of calling a weights file the release. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metadata spine. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow experiments search` as one read-only checkpoint, not the whole diagnosis. stable run, dataset, model, release, deployment and request identifiers join otherwise separate systems. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Environment promotion. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` as one read-only checkpoint, not the whole diagnosis. promote immutable evidence/artifacts while configuration and credentials remain target-specific. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Human decision. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `git log --graph --oneline --all` as one read-only checkpoint, not the whole diagnosis. risk-based approvals and exceptions retain actor, evidence, reason, expiry and rollback authority. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reconciliation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://metadata-api/health` as one read-only checkpoint, not the whole diagnosis. controllers compare desired release with observed deployment/index/evaluation state and retry idempotently. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Multi-tenancy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow experiments search` as one read-only checkpoint, not the whole diagnosis. identity, quota, compute, metadata, artifacts, networks and cost allocation require explicit isolation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### MLOPS-LLMOPS-PLATFORM-ARCHITECTURE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Exit and retirement. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get workflows,pipelines,trainingjobs,inferenceservices -A` as one read-only checkpoint, not the whole diagnosis. revoke endpoints/credentials, preserve required evidence, delete protected data/artifacts and update inventories. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
