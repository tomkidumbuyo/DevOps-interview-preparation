# ML pipeline orchestration — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### ML-PIPELINE-ORCHESTRATION-JN-01

- [ ] **Question:** What is Component contract, and why does it matter in ML pipeline orchestration?

**Answer:** container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-PIPELINE-ORCHESTRATION-JN-02

- [ ] **Question:** What is DAG, and why does it matter in ML pipeline orchestration?

**Answer:** data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-PIPELINE-ORCHESTRATION-JN-03

- [ ] **Question:** What is Artifact passing, and why does it matter in ML pipeline orchestration?

**Answer:** object references/digests scale better than large values and preserve lineage. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-PIPELINE-ORCHESTRATION-JN-04

- [ ] **Question:** What is Caching, and why does it matter in ML pipeline orchestration?

**Answer:** cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-PIPELINE-ORCHESTRATION-JN-05

- [ ] **Question:** What is Retry, and why does it matter in ML pipeline orchestration?

**Answer:** only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-PIPELINE-ORCHESTRATION-JN-06

- [ ] **Question:** What is Conditional gate, and why does it matter in ML pipeline orchestration?

**Answer:** evaluation/policy decision consumes explicit evidence and records why a branch executed. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-PIPELINE-ORCHESTRATION-JN-07

- [ ] **Question:** What is Backfill, and why does it matter in ML pipeline orchestration?

**Answer:** bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-PIPELINE-ORCHESTRATION-JN-08

- [ ] **Code:** **Question:** What does `kubectl describe workflow RUN -n NS` help you verify for ML pipeline orchestration?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: each component receives short-lived least-privileged identity instead of pipeline-wide static keys.

### ML-PIPELINE-ORCHESTRATION-JN-09

- [ ] **Code:** **Question:** What does `kfp dsl compile --py pipeline.py --output pipeline.yaml` help you verify for ML pipeline orchestration?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release.

### ML-PIPELINE-ORCHESTRATION-JN-10

- [ ] **Code:** **Question:** What does `argo lint workflow.yaml` help you verify for ML pipeline orchestration?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: pipeline SDK, compiled spec, orchestrator and component images require compatibility testing.

## Junior — procedural and command questions

### ML-PIPELINE-ORCHESTRATION-JP-01

- [ ] **Code:** **Question:** A basic Component contract check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kfp dsl compile --py pipeline.py --output pipeline.yaml` and capture exact status/reason/request ID. container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-02

- [ ] **Question:** A basic DAG check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argo lint workflow.yaml` and capture exact status/reason/request ID. data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-03

- [ ] **Question:** A basic Artifact passing check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get workflows -A` and capture exact status/reason/request ID. object references/digests scale better than large values and preserve lineage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-04

- [ ] **Code:** **Question:** A basic Caching check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe workflow RUN -n NS` and capture exact status/reason/request ID. cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-05

- [ ] **Question:** A basic Retry check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kfp dsl compile --py pipeline.py --output pipeline.yaml` and capture exact status/reason/request ID. only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-06

- [ ] **Question:** A basic Conditional gate check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argo lint workflow.yaml` and capture exact status/reason/request ID. evaluation/policy decision consumes explicit evidence and records why a branch executed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-07

- [ ] **Code:** **Question:** A basic Backfill check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get workflows -A` and capture exact status/reason/request ID. bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-08

- [ ] **Question:** A basic Secrets/identity check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe workflow RUN -n NS` and capture exact status/reason/request ID. each component receives short-lived least-privileged identity instead of pipeline-wide static keys. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-09

- [ ] **Question:** A basic Observability check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kfp dsl compile --py pipeline.py --output pipeline.yaml` and capture exact status/reason/request ID. pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-PIPELINE-ORCHESTRATION-JP-10

- [ ] **Code:** **Question:** A basic Compiler/version skew check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `argo lint workflow.yaml` and capture exact status/reason/request ID. pipeline SDK, compiled spec, orchestrator and component images require compatibility testing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### ML-PIPELINE-ORCHESTRATION-MN-01

- [ ] **Question:** Compare Component contract with DAG. When would each change your design?

**Answer:** Component contract: container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. DAG: data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-02

- [ ] **Question:** Compare DAG with Artifact passing. When would each change your design?

**Answer:** DAG: data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. Artifact passing: object references/digests scale better than large values and preserve lineage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-03

- [ ] **Question:** Compare Artifact passing with Caching. When would each change your design?

**Answer:** Artifact passing: object references/digests scale better than large values and preserve lineage. Caching: cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-04

- [ ] **Configuration review:** **Question:** Compare Caching with Retry. When would each change your design?

**Answer:** Caching: cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. Retry: only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-05

- [ ] **Question:** Compare Retry with Conditional gate. When would each change your design?

**Answer:** Retry: only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. Conditional gate: evaluation/policy decision consumes explicit evidence and records why a branch executed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-06

- [ ] **Question:** Compare Conditional gate with Backfill. When would each change your design?

**Answer:** Conditional gate: evaluation/policy decision consumes explicit evidence and records why a branch executed. Backfill: bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-07

- [ ] **Configuration review:** **Question:** Compare Backfill with Secrets/identity. When would each change your design?

**Answer:** Backfill: bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. Secrets/identity: each component receives short-lived least-privileged identity instead of pipeline-wide static keys. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-08

- [ ] **Question:** Compare Secrets/identity with Observability. When would each change your design?

**Answer:** Secrets/identity: each component receives short-lived least-privileged identity instead of pipeline-wide static keys. Observability: pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-09

- [ ] **Question:** Compare Observability with Compiler/version skew. When would each change your design?

**Answer:** Observability: pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release. Compiler/version skew: pipeline SDK, compiled spec, orchestrator and component images require compatibility testing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-PIPELINE-ORCHESTRATION-MN-10

- [ ] **Configuration review:** **Question:** Compare Compiler/version skew with Component contract. When would each change your design?

**Answer:** Compiler/version skew: pipeline SDK, compiled spec, orchestrator and component images require compatibility testing. Component contract: container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### ML-PIPELINE-ORCHESTRATION-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Component contract; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kfp dsl compile --py pipeline.py --output pipeline.yaml` plus recent events/changes, then correlate the service-specific SLI. container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-02

- [ ] **Question:** Production is degraded around DAG; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argo lint workflow.yaml` plus recent events/changes, then correlate the service-specific SLI. data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Artifact passing; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get workflows -A` plus recent events/changes, then correlate the service-specific SLI. object references/digests scale better than large values and preserve lineage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-04

- [ ] **Question:** Production is degraded around Caching; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe workflow RUN -n NS` plus recent events/changes, then correlate the service-specific SLI. cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Retry; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kfp dsl compile --py pipeline.py --output pipeline.yaml` plus recent events/changes, then correlate the service-specific SLI. only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-06

- [ ] **Question:** Production is degraded around Conditional gate; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argo lint workflow.yaml` plus recent events/changes, then correlate the service-specific SLI. evaluation/policy decision consumes explicit evidence and records why a branch executed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backfill; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get workflows -A` plus recent events/changes, then correlate the service-specific SLI. bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-08

- [ ] **Question:** Production is degraded around Secrets/identity; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe workflow RUN -n NS` plus recent events/changes, then correlate the service-specific SLI. each component receives short-lived least-privileged identity instead of pipeline-wide static keys. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Observability; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kfp dsl compile --py pipeline.py --output pipeline.yaml` plus recent events/changes, then correlate the service-specific SLI. pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-PIPELINE-ORCHESTRATION-MP-10

- [ ] **Question:** Production is degraded around Compiler/version skew; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `argo lint workflow.yaml` plus recent events/changes, then correlate the service-specific SLI. pipeline SDK, compiled spec, orchestrator and component images require compatibility testing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### ML-PIPELINE-ORCHESTRATION-SN-01

- [ ] **Question:** Design a production ML pipeline orchestration capability where Component contract, Caching and Backfill are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production ML pipeline orchestration capability where DAG, Retry and Secrets/identity are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. each component receives short-lived least-privileged identity instead of pipeline-wide static keys. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-03

- [ ] **Question:** Design a production ML pipeline orchestration capability where Artifact passing, Conditional gate and Observability are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: object references/digests scale better than large values and preserve lineage. evaluation/policy decision consumes explicit evidence and records why a branch executed. pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production ML pipeline orchestration capability where Caching, Backfill and Compiler/version skew are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. pipeline SDK, compiled spec, orchestrator and component images require compatibility testing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-05

- [ ] **Question:** Design a production ML pipeline orchestration capability where Retry, Secrets/identity and Component contract are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. each component receives short-lived least-privileged identity instead of pipeline-wide static keys. container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production ML pipeline orchestration capability where Conditional gate, Observability and DAG are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: evaluation/policy decision consumes explicit evidence and records why a branch executed. pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release. data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-07

- [ ] **Question:** Design a production ML pipeline orchestration capability where Backfill, Compiler/version skew and Artifact passing are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. pipeline SDK, compiled spec, orchestrator and component images require compatibility testing. object references/digests scale better than large values and preserve lineage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production ML pipeline orchestration capability where Secrets/identity, Component contract and Caching are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: each component receives short-lived least-privileged identity instead of pipeline-wide static keys. container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-09

- [ ] **Question:** Design a production ML pipeline orchestration capability where Observability, DAG and Retry are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release. data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-PIPELINE-ORCHESTRATION-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production ML pipeline orchestration capability where Compiler/version skew, Artifact passing and Conditional gate are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pipeline SDK, compiled spec, orchestrator and component images require compatibility testing. object references/digests scale better than large values and preserve lineage. evaluation/policy decision consumes explicit evidence and records why a branch executed. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### ML-PIPELINE-ORCHESTRATION-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Component contract. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kfp dsl compile --py pipeline.py --output pipeline.yaml` as one read-only checkpoint, not the whole diagnosis. container/code, typed parameters, artifact inputs/outputs, resources and retry behavior are versioned. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DAG. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argo lint workflow.yaml` as one read-only checkpoint, not the whole diagnosis. data/control dependencies define concurrency and critical path; hidden external state breaks reproducibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Artifact passing. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get workflows -A` as one read-only checkpoint, not the whole diagnosis. object references/digests scale better than large values and preserve lineage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Caching. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe workflow RUN -n NS` as one read-only checkpoint, not the whole diagnosis. cache key includes all semantic inputs and environment; unsafe caching can promote stale artifacts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Retry. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kfp dsl compile --py pipeline.py --output pipeline.yaml` as one read-only checkpoint, not the whole diagnosis. only transient idempotent stages retry automatically; remote side effects need operation keys/reconciliation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Conditional gate. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argo lint workflow.yaml` as one read-only checkpoint, not the whole diagnosis. evaluation/policy decision consumes explicit evidence and records why a branch executed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backfill. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get workflows -A` as one read-only checkpoint, not the whole diagnosis. bounded partition ranges, concurrency and checkpoints prevent normal workloads from being overwhelmed. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secrets/identity. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe workflow RUN -n NS` as one read-only checkpoint, not the whole diagnosis. each component receives short-lived least-privileged identity instead of pipeline-wide static keys. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Observability. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kfp dsl compile --py pipeline.py --output pipeline.yaml` as one read-only checkpoint, not the whole diagnosis. pipeline/run/task/artifact IDs correlate status, logs, resource use, cost and downstream release. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-PIPELINE-ORCHESTRATION-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Compiler/version skew. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `argo lint workflow.yaml` as one read-only checkpoint, not the whole diagnosis. pipeline SDK, compiled spec, orchestrator and component images require compatibility testing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
