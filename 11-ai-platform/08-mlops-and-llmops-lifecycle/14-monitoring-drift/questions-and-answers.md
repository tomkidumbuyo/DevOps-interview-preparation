# ML monitoring, drift and data quality — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-01

- [ ] **Question:** What is Input quality, and why does it matter in ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-02

- [ ] **Question:** What is Covariate drift, and why does it matter in ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** production input distribution differs from reference but does not alone prove quality degradation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-03

- [ ] **Question:** What is Prediction drift, and why does it matter in ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** output distribution changes and can arise from traffic, model, policy or upstream shifts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-04

- [ ] **Question:** What is Concept drift, and why does it matter in ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** relationship between input and desired output changes and requires trustworthy delayed labels. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-05

- [ ] **Question:** What is Label delay, and why does it matter in ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-06

- [ ] **Question:** What is Slice monitoring, and why does it matter in ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** aggregate stability can hide one tenant/language/segment regression. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-07

- [ ] **Question:** What is Threshold, and why does it matter in ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-08

- [ ] **Code:** **Question:** What does `python -m pytest tests/drift -q` help you verify for ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: identify which source/transform/model deployments explain an observed change.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-09

- [ ] **Code:** **Question:** What does `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` help you verify for ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: model decisions can alter future data and create selection or self-reinforcement bias.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JN-10

- [ ] **Code:** **Question:** What does `curl -s http://MODEL/metrics` help you verify for ML monitoring, drift and data quality?
> **Covered in:** [ML monitoring, drift and data quality — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric.

## Junior — procedural and command questions

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-01

- [ ] **Code:** **Question:** A basic Input quality check fails. What would you do first using the CLI?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` and capture exact status/reason/request ID. schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-02

- [ ] **Question:** A basic Covariate drift check fails. What would you do first?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. production input distribution differs from reference but does not alone prove quality degradation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-03

- [ ] **Question:** A basic Prediction drift check fails. What would you do first?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n inference deploy/MODEL --since=30m` and capture exact status/reason/request ID. output distribution changes and can arise from traffic, model, policy or upstream shifts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-04

- [ ] **Code:** **Question:** A basic Concept drift check fails. What would you do first using the CLI?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/drift -q` and capture exact status/reason/request ID. relationship between input and desired output changes and requires trustworthy delayed labels. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-05

- [ ] **Question:** A basic Label delay check fails. What would you do first?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` and capture exact status/reason/request ID. monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-06

- [ ] **Question:** A basic Slice monitoring check fails. What would you do first?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. aggregate stability can hide one tenant/language/segment regression. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-07

- [ ] **Code:** **Question:** A basic Threshold check fails. What would you do first using the CLI?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl logs -n inference deploy/MODEL --since=30m` and capture exact status/reason/request ID. expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-08

- [ ] **Question:** A basic Data lineage check fails. What would you do first?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m pytest tests/drift -q` and capture exact status/reason/request ID. identify which source/transform/model deployments explain an observed change. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-09

- [ ] **Question:** A basic Feedback loop check fails. What would you do first?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` and capture exact status/reason/request ID. model decisions can alter future data and create selection or self-reinforcement bias. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-JP-10

- [ ] **Code:** **Question:** A basic Response check fails. What would you do first using the CLI?
> **Covered in:** [ML monitoring, drift and data quality — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -s http://MODEL/metrics` and capture exact status/reason/request ID. investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-01

- [ ] **Question:** Compare Input quality with Covariate drift. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Input quality: schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. Covariate drift: production input distribution differs from reference but does not alone prove quality degradation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-02

- [ ] **Question:** Compare Covariate drift with Prediction drift. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Covariate drift: production input distribution differs from reference but does not alone prove quality degradation. Prediction drift: output distribution changes and can arise from traffic, model, policy or upstream shifts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-03

- [ ] **Question:** Compare Prediction drift with Concept drift. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Prediction drift: output distribution changes and can arise from traffic, model, policy or upstream shifts. Concept drift: relationship between input and desired output changes and requires trustworthy delayed labels. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-04

- [ ] **Configuration review:** **Question:** Compare Concept drift with Label delay. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Concept drift: relationship between input and desired output changes and requires trustworthy delayed labels. Label delay: monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-05

- [ ] **Question:** Compare Label delay with Slice monitoring. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Label delay: monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. Slice monitoring: aggregate stability can hide one tenant/language/segment regression. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-06

- [ ] **Question:** Compare Slice monitoring with Threshold. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Slice monitoring: aggregate stability can hide one tenant/language/segment regression. Threshold: expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-07

- [ ] **Configuration review:** **Question:** Compare Threshold with Data lineage. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Threshold: expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. Data lineage: identify which source/transform/model deployments explain an observed change. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-08

- [ ] **Question:** Compare Data lineage with Feedback loop. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Data lineage: identify which source/transform/model deployments explain an observed change. Feedback loop: model decisions can alter future data and create selection or self-reinforcement bias. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-09

- [ ] **Question:** Compare Feedback loop with Response. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Feedback loop: model decisions can alter future data and create selection or self-reinforcement bias. Response: investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MN-10

- [ ] **Configuration review:** **Question:** Compare Response with Input quality. When would each change your design?
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Response: investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric. Input quality: schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Input quality; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` plus recent events/changes, then correlate the service-specific SLI. schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-02

- [ ] **Question:** Production is degraded around Covariate drift; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. production input distribution differs from reference but does not alone prove quality degradation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Prediction drift; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n inference deploy/MODEL --since=30m` plus recent events/changes, then correlate the service-specific SLI. output distribution changes and can arise from traffic, model, policy or upstream shifts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-04

- [ ] **Question:** Production is degraded around Concept drift; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/drift -q` plus recent events/changes, then correlate the service-specific SLI. relationship between input and desired output changes and requires trustworthy delayed labels. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Label delay; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` plus recent events/changes, then correlate the service-specific SLI. monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-06

- [ ] **Question:** Production is degraded around Slice monitoring; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. aggregate stability can hide one tenant/language/segment regression. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Threshold; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl logs -n inference deploy/MODEL --since=30m` plus recent events/changes, then correlate the service-specific SLI. expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-08

- [ ] **Question:** Production is degraded around Data lineage; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m pytest tests/drift -q` plus recent events/changes, then correlate the service-specific SLI. identify which source/transform/model deployments explain an observed change. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Feedback loop; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` plus recent events/changes, then correlate the service-specific SLI. model decisions can alter future data and create selection or self-reinforcement bias. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-MP-10

- [ ] **Question:** Production is degraded around Response; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -s http://MODEL/metrics` plus recent events/changes, then correlate the service-specific SLI. investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-01

- [ ] **Question:** Design a production ML monitoring, drift and data quality capability where Input quality, Concept drift and Threshold are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. relationship between input and desired output changes and requires trustworthy delayed labels. expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production ML monitoring, drift and data quality capability where Covariate drift, Label delay and Data lineage are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: production input distribution differs from reference but does not alone prove quality degradation. monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. identify which source/transform/model deployments explain an observed change. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-03

- [ ] **Question:** Design a production ML monitoring, drift and data quality capability where Prediction drift, Slice monitoring and Feedback loop are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: output distribution changes and can arise from traffic, model, policy or upstream shifts. aggregate stability can hide one tenant/language/segment regression. model decisions can alter future data and create selection or self-reinforcement bias. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production ML monitoring, drift and data quality capability where Concept drift, Threshold and Response are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: relationship between input and desired output changes and requires trustworthy delayed labels. expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-05

- [ ] **Question:** Design a production ML monitoring, drift and data quality capability where Label delay, Data lineage and Input quality are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. identify which source/transform/model deployments explain an observed change. schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production ML monitoring, drift and data quality capability where Slice monitoring, Feedback loop and Covariate drift are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: aggregate stability can hide one tenant/language/segment regression. model decisions can alter future data and create selection or self-reinforcement bias. production input distribution differs from reference but does not alone prove quality degradation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-07

- [ ] **Question:** Design a production ML monitoring, drift and data quality capability where Threshold, Response and Prediction drift are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric. output distribution changes and can arise from traffic, model, policy or upstream shifts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production ML monitoring, drift and data quality capability where Data lineage, Input quality and Concept drift are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: identify which source/transform/model deployments explain an observed change. schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. relationship between input and desired output changes and requires trustworthy delayed labels. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-09

- [ ] **Question:** Design a production ML monitoring, drift and data quality capability where Feedback loop, Covariate drift and Label delay are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: model decisions can alter future data and create selection or self-reinforcement bias. production input distribution differs from reference but does not alone prove quality degradation. monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production ML monitoring, drift and data quality capability where Response, Prediction drift and Slice monitoring are first-class requirements.
> **Covered in:** [ML monitoring, drift and data quality — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric. output distribution changes and can arise from traffic, model, policy or upstream shifts. aggregate stability can hide one tenant/language/segment regression. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Input quality. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` as one read-only checkpoint, not the whole diagnosis. schema, missingness, ranges, categories and parse failures catch broken pipelines before abstract drift scores. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Covariate drift. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. production input distribution differs from reference but does not alone prove quality degradation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Prediction drift. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n inference deploy/MODEL --since=30m` as one read-only checkpoint, not the whole diagnosis. output distribution changes and can arise from traffic, model, policy or upstream shifts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Concept drift. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/drift -q` as one read-only checkpoint, not the whole diagnosis. relationship between input and desired output changes and requires trustworthy delayed labels. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Label delay. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` as one read-only checkpoint, not the whole diagnosis. monitoring architecture reconciles predictions with outcomes later using stable privacy-safe IDs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Slice monitoring. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. aggregate stability can hide one tenant/language/segment regression. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Threshold. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl logs -n inference deploy/MODEL --since=30m` as one read-only checkpoint, not the whole diagnosis. expected seasonality/sample size/uncertainty and business impact determine alerting rather than arbitrary distance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data lineage. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m pytest tests/drift -q` as one read-only checkpoint, not the whole diagnosis. identify which source/transform/model deployments explain an observed change. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Feedback loop. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/validate_batch.py --reference reference.parquet --current current.parquet` as one read-only checkpoint, not the whole diagnosis. model decisions can alter future data and create selection or self-reinforcement bias. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### ML-MONITORING-DRIFT-AND-DATA-QUALITY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Response. How do you lead it end to end?
> **Covered in:** [ML monitoring, drift and data quality — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -s http://MODEL/metrics` as one read-only checkpoint, not the whole diagnosis. investigate/evaluate/shadow/retrain/rollback under owned policy; never auto-retrain on one drift metric. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: ML/LLM deployment and progressive release](../13-deployment-progressive-release/README.md) · [Study note](README.md) · [Next: Retraining and feedback loops →](../15-retraining-feedback-loops/README.md)

<!-- reading-navigation:end -->
