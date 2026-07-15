# Experiment tracking and comparison — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-01

- [ ] **Question:** What is Experiment, and why does it matter in Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** groups runs around one owned objective while avoiding an endless unstructured namespace. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-02

- [ ] **Question:** What is Run, and why does it matter in Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-03

- [ ] **Question:** What is Parameter, and why does it matter in Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** intended input/configuration is logged before execution and is distinct from observed metric. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-04

- [ ] **Question:** What is Metric, and why does it matter in Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** value plus step/time/dataset/slice semantics prevents misleading comparison. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-05

- [ ] **Question:** What is Artifact, and why does it matter in Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-06

- [ ] **Question:** What is Nested runs, and why does it matter in Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** organize trials/folds/stages without losing independent failure/evidence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-07

- [ ] **Question:** What is Tags, and why does it matter in Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-08

- [ ] **Code:** **Question:** What does `mlflow server --host 127.0.0.1 --port 5000` help you verify for Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: confidence intervals, repeated seeds and slice results matter beyond the best scalar score.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-09

- [ ] **Code:** **Question:** What does `mlflow experiments search` help you verify for Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: authentication, artifact credentials, database availability, backup and tenancy are production concerns.

### EXPERIMENT-TRACKING-AND-COMPARISON-JN-10

- [ ] **Code:** **Question:** What does `mlflow runs list --experiment-id EXPERIMENT_ID` help you verify for Experiment tracking and comparison?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: promotion creates a reviewed lineage record rather than treating a dashboard click as deployment.

## Junior — procedural and command questions

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-01

- [ ] **Code:** **Question:** A basic Experiment check fails. What would you do first using the CLI?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow experiments search` and capture exact status/reason/request ID. groups runs around one owned objective while avoiding an endless unstructured namespace. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-02

- [ ] **Question:** A basic Run check fails. What would you do first?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow runs list --experiment-id EXPERIMENT_ID` and capture exact status/reason/request ID. one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-03

- [ ] **Question:** A basic Parameter check fails. What would you do first?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow artifacts list --run-id RUN_ID` and capture exact status/reason/request ID. intended input/configuration is logged before execution and is distinct from observed metric. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-04

- [ ] **Code:** **Question:** A basic Metric check fails. What would you do first using the CLI?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow server --host 127.0.0.1 --port 5000` and capture exact status/reason/request ID. value plus step/time/dataset/slice semantics prevents misleading comparison. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-05

- [ ] **Question:** A basic Artifact check fails. What would you do first?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow experiments search` and capture exact status/reason/request ID. model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-06

- [ ] **Question:** A basic Nested runs check fails. What would you do first?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow runs list --experiment-id EXPERIMENT_ID` and capture exact status/reason/request ID. organize trials/folds/stages without losing independent failure/evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-07

- [ ] **Code:** **Question:** A basic Tags check fails. What would you do first using the CLI?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow artifacts list --run-id RUN_ID` and capture exact status/reason/request ID. owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-08

- [ ] **Question:** A basic Comparison check fails. What would you do first?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow server --host 127.0.0.1 --port 5000` and capture exact status/reason/request ID. confidence intervals, repeated seeds and slice results matter beyond the best scalar score. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-09

- [ ] **Question:** A basic Tracking server check fails. What would you do first?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow experiments search` and capture exact status/reason/request ID. authentication, artifact credentials, database availability, backup and tenancy are production concerns. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### EXPERIMENT-TRACKING-AND-COMPARISON-JP-10

- [ ] **Code:** **Question:** A basic Candidate selection check fails. What would you do first using the CLI?
> **Covered in:** [Experiment tracking and comparison — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow runs list --experiment-id EXPERIMENT_ID` and capture exact status/reason/request ID. promotion creates a reviewed lineage record rather than treating a dashboard click as deployment. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-01

- [ ] **Question:** Compare Experiment with Run. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Experiment: groups runs around one owned objective while avoiding an endless unstructured namespace. Run: one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-02

- [ ] **Question:** Compare Run with Parameter. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Run: one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. Parameter: intended input/configuration is logged before execution and is distinct from observed metric. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-03

- [ ] **Question:** Compare Parameter with Metric. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Parameter: intended input/configuration is logged before execution and is distinct from observed metric. Metric: value plus step/time/dataset/slice semantics prevents misleading comparison. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-04

- [ ] **Configuration review:** **Question:** Compare Metric with Artifact. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Metric: value plus step/time/dataset/slice semantics prevents misleading comparison. Artifact: model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-05

- [ ] **Question:** Compare Artifact with Nested runs. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Artifact: model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. Nested runs: organize trials/folds/stages without losing independent failure/evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-06

- [ ] **Question:** Compare Nested runs with Tags. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Nested runs: organize trials/folds/stages without losing independent failure/evidence. Tags: owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-07

- [ ] **Configuration review:** **Question:** Compare Tags with Comparison. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Tags: owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. Comparison: confidence intervals, repeated seeds and slice results matter beyond the best scalar score. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-08

- [ ] **Question:** Compare Comparison with Tracking server. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Comparison: confidence intervals, repeated seeds and slice results matter beyond the best scalar score. Tracking server: authentication, artifact credentials, database availability, backup and tenancy are production concerns. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-09

- [ ] **Question:** Compare Tracking server with Candidate selection. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Tracking server: authentication, artifact credentials, database availability, backup and tenancy are production concerns. Candidate selection: promotion creates a reviewed lineage record rather than treating a dashboard click as deployment. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### EXPERIMENT-TRACKING-AND-COMPARISON-MN-10

- [ ] **Configuration review:** **Question:** Compare Candidate selection with Experiment. When would each change your design?
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Candidate selection: promotion creates a reviewed lineage record rather than treating a dashboard click as deployment. Experiment: groups runs around one owned objective while avoiding an endless unstructured namespace. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Experiment; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow experiments search` plus recent events/changes, then correlate the service-specific SLI. groups runs around one owned objective while avoiding an endless unstructured namespace. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-02

- [ ] **Question:** Production is degraded around Run; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow runs list --experiment-id EXPERIMENT_ID` plus recent events/changes, then correlate the service-specific SLI. one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Parameter; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow artifacts list --run-id RUN_ID` plus recent events/changes, then correlate the service-specific SLI. intended input/configuration is logged before execution and is distinct from observed metric. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-04

- [ ] **Question:** Production is degraded around Metric; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow server --host 127.0.0.1 --port 5000` plus recent events/changes, then correlate the service-specific SLI. value plus step/time/dataset/slice semantics prevents misleading comparison. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Artifact; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow experiments search` plus recent events/changes, then correlate the service-specific SLI. model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-06

- [ ] **Question:** Production is degraded around Nested runs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow runs list --experiment-id EXPERIMENT_ID` plus recent events/changes, then correlate the service-specific SLI. organize trials/folds/stages without losing independent failure/evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Tags; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow artifacts list --run-id RUN_ID` plus recent events/changes, then correlate the service-specific SLI. owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-08

- [ ] **Question:** Production is degraded around Comparison; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow server --host 127.0.0.1 --port 5000` plus recent events/changes, then correlate the service-specific SLI. confidence intervals, repeated seeds and slice results matter beyond the best scalar score. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Tracking server; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow experiments search` plus recent events/changes, then correlate the service-specific SLI. authentication, artifact credentials, database availability, backup and tenancy are production concerns. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### EXPERIMENT-TRACKING-AND-COMPARISON-MP-10

- [ ] **Question:** Production is degraded around Candidate selection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Experiment tracking and comparison — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow runs list --experiment-id EXPERIMENT_ID` plus recent events/changes, then correlate the service-specific SLI. promotion creates a reviewed lineage record rather than treating a dashboard click as deployment. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-01

- [ ] **Question:** Design a production Experiment tracking and comparison capability where Experiment, Metric and Tags are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: groups runs around one owned objective while avoiding an endless unstructured namespace. value plus step/time/dataset/slice semantics prevents misleading comparison. owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Experiment tracking and comparison capability where Run, Artifact and Comparison are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. confidence intervals, repeated seeds and slice results matter beyond the best scalar score. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-03

- [ ] **Question:** Design a production Experiment tracking and comparison capability where Parameter, Nested runs and Tracking server are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: intended input/configuration is logged before execution and is distinct from observed metric. organize trials/folds/stages without losing independent failure/evidence. authentication, artifact credentials, database availability, backup and tenancy are production concerns. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Experiment tracking and comparison capability where Metric, Tags and Candidate selection are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: value plus step/time/dataset/slice semantics prevents misleading comparison. owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. promotion creates a reviewed lineage record rather than treating a dashboard click as deployment. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-05

- [ ] **Question:** Design a production Experiment tracking and comparison capability where Artifact, Comparison and Experiment are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. confidence intervals, repeated seeds and slice results matter beyond the best scalar score. groups runs around one owned objective while avoiding an endless unstructured namespace. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Experiment tracking and comparison capability where Nested runs, Tracking server and Run are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: organize trials/folds/stages without losing independent failure/evidence. authentication, artifact credentials, database availability, backup and tenancy are production concerns. one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-07

- [ ] **Question:** Design a production Experiment tracking and comparison capability where Tags, Candidate selection and Parameter are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. promotion creates a reviewed lineage record rather than treating a dashboard click as deployment. intended input/configuration is logged before execution and is distinct from observed metric. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Experiment tracking and comparison capability where Comparison, Experiment and Metric are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: confidence intervals, repeated seeds and slice results matter beyond the best scalar score. groups runs around one owned objective while avoiding an endless unstructured namespace. value plus step/time/dataset/slice semantics prevents misleading comparison. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-09

- [ ] **Question:** Design a production Experiment tracking and comparison capability where Tracking server, Run and Artifact are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authentication, artifact credentials, database availability, backup and tenancy are production concerns. one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### EXPERIMENT-TRACKING-AND-COMPARISON-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Experiment tracking and comparison capability where Candidate selection, Parameter and Nested runs are first-class requirements.
> **Covered in:** [Experiment tracking and comparison — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: promotion creates a reviewed lineage record rather than treating a dashboard click as deployment. intended input/configuration is logged before execution and is distinct from observed metric. organize trials/folds/stages without losing independent failure/evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Experiment. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow experiments search` as one read-only checkpoint, not the whole diagnosis. groups runs around one owned objective while avoiding an endless unstructured namespace. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Run. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow runs list --experiment-id EXPERIMENT_ID` as one read-only checkpoint, not the whole diagnosis. one execution records code revision, parameters, environment, data identity, metrics, artifacts, status and actor. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parameter. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow artifacts list --run-id RUN_ID` as one read-only checkpoint, not the whole diagnosis. intended input/configuration is logged before execution and is distinct from observed metric. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metric. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow server --host 127.0.0.1 --port 5000` as one read-only checkpoint, not the whole diagnosis. value plus step/time/dataset/slice semantics prevents misleading comparison. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Artifact. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow experiments search` as one read-only checkpoint, not the whole diagnosis. model/checkpoint/plot/log/evaluation output needs digest, media type, size and storage policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Nested runs. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow runs list --experiment-id EXPERIMENT_ID` as one read-only checkpoint, not the whole diagnosis. organize trials/folds/stages without losing independent failure/evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tags. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow artifacts list --run-id RUN_ID` as one read-only checkpoint, not the whole diagnosis. owner, purpose, tenant/data class, hardware and ticket improve search/governance without encoding secrets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Comparison. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow server --host 127.0.0.1 --port 5000` as one read-only checkpoint, not the whole diagnosis. confidence intervals, repeated seeds and slice results matter beyond the best scalar score. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tracking server. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow experiments search` as one read-only checkpoint, not the whole diagnosis. authentication, artifact credentials, database availability, backup and tenancy are production concerns. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### EXPERIMENT-TRACKING-AND-COMPARISON-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Candidate selection. How do you lead it end to end?
> **Covered in:** [Experiment tracking and comparison — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow runs list --experiment-id EXPERIMENT_ID` as one read-only checkpoint, not the whole diagnosis. promotion creates a reviewed lineage record rather than treating a dashboard click as deployment. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: MLOps/LLMOps platform architecture](../01-lifecycle-platform-architecture/README.md) · [Study note](README.md) · [Next: Data versioning, quality and lineage →](../03-data-versioning-quality-lineage/README.md)

<!-- reading-navigation:end -->
