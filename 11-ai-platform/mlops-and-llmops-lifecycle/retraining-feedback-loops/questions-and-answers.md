# Retraining and feedback loops — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### RETRAINING-AND-FEEDBACK-LOOPS-JN-01

- [ ] **Question:** What is Trigger, and why does it matter in Retraining and feedback loops?

**Answer:** schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-02

- [ ] **Question:** What is Feedback collection, and why does it matter in Retraining and feedback loops?

**Answer:** stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-03

- [ ] **Question:** What is Label quality, and why does it matter in Retraining and feedback loops?

**Answer:** reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-04

- [ ] **Question:** What is Sampling bias, and why does it matter in Retraining and feedback loops?

**Answer:** observed feedback reflects product exposure and user response rather than the target population automatically. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-05

- [ ] **Question:** What is Poisoning, and why does it matter in Retraining and feedback loops?

**Answer:** anomalous contributors/content and influence controls protect training/evaluation sets. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-06

- [ ] **Question:** What is Replay set, and why does it matter in Retraining and feedback loops?

**Answer:** retain representative historical/edge cases so adaptation does not catastrophically forget. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-07

- [ ] **Question:** What is Pipeline version, and why does it matter in Retraining and feedback loops?

**Answer:** retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-08

- [ ] **Code:** **Question:** What does `python -m evals.run --manifest candidate.yaml --dataset regression.jsonl` help you verify for Retraining and feedback loops?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: GPU, provider and pipeline quotas prevent feedback automation from starving serving.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-09

- [ ] **Code:** **Question:** What does `python scripts/build_feedback_dataset.py --dry-run` help you verify for Retraining and feedback loops?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: candidate must beat champion within owned quality/safety/performance/cost gates.

### RETRAINING-AND-FEEDBACK-LOOPS-JN-10

- [ ] **Code:** **Question:** What does `dvc repro retrain` help you verify for Retraining and feedback loops?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: high-risk changes retain approval, exception and rollback rather than automatic drift-to-production.

## Junior — procedural and command questions

### RETRAINING-AND-FEEDBACK-LOOPS-JP-01

- [ ] **Code:** **Question:** A basic Trigger check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/build_feedback_dataset.py --dry-run` and capture exact status/reason/request ID. schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-02

- [ ] **Question:** A basic Feedback collection check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc repro retrain` and capture exact status/reason/request ID. stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-03

- [ ] **Question:** A basic Label quality check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow runs list --experiment-id EXPERIMENT_ID` and capture exact status/reason/request ID. reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-04

- [ ] **Code:** **Question:** A basic Sampling bias check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest candidate.yaml --dataset regression.jsonl` and capture exact status/reason/request ID. observed feedback reflects product exposure and user response rather than the target population automatically. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-05

- [ ] **Question:** A basic Poisoning check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/build_feedback_dataset.py --dry-run` and capture exact status/reason/request ID. anomalous contributors/content and influence controls protect training/evaluation sets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-06

- [ ] **Question:** A basic Replay set check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc repro retrain` and capture exact status/reason/request ID. retain representative historical/edge cases so adaptation does not catastrophically forget. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-07

- [ ] **Code:** **Question:** A basic Pipeline version check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `mlflow runs list --experiment-id EXPERIMENT_ID` and capture exact status/reason/request ID. retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-08

- [ ] **Question:** A basic Budget/admission check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python -m evals.run --manifest candidate.yaml --dataset regression.jsonl` and capture exact status/reason/request ID. GPU, provider and pipeline quotas prevent feedback automation from starving serving. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-09

- [ ] **Question:** A basic Validation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `python scripts/build_feedback_dataset.py --dry-run` and capture exact status/reason/request ID. candidate must beat champion within owned quality/safety/performance/cost gates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### RETRAINING-AND-FEEDBACK-LOOPS-JP-10

- [ ] **Code:** **Question:** A basic Human promotion check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dvc repro retrain` and capture exact status/reason/request ID. high-risk changes retain approval, exception and rollback rather than automatic drift-to-production. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### RETRAINING-AND-FEEDBACK-LOOPS-MN-01

- [ ] **Question:** Compare Trigger with Feedback collection. When would each change your design?

**Answer:** Trigger: schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. Feedback collection: stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-02

- [ ] **Question:** Compare Feedback collection with Label quality. When would each change your design?

**Answer:** Feedback collection: stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. Label quality: reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-03

- [ ] **Question:** Compare Label quality with Sampling bias. When would each change your design?

**Answer:** Label quality: reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. Sampling bias: observed feedback reflects product exposure and user response rather than the target population automatically. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-04

- [ ] **Configuration review:** **Question:** Compare Sampling bias with Poisoning. When would each change your design?

**Answer:** Sampling bias: observed feedback reflects product exposure and user response rather than the target population automatically. Poisoning: anomalous contributors/content and influence controls protect training/evaluation sets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-05

- [ ] **Question:** Compare Poisoning with Replay set. When would each change your design?

**Answer:** Poisoning: anomalous contributors/content and influence controls protect training/evaluation sets. Replay set: retain representative historical/edge cases so adaptation does not catastrophically forget. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-06

- [ ] **Question:** Compare Replay set with Pipeline version. When would each change your design?

**Answer:** Replay set: retain representative historical/edge cases so adaptation does not catastrophically forget. Pipeline version: retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-07

- [ ] **Configuration review:** **Question:** Compare Pipeline version with Budget/admission. When would each change your design?

**Answer:** Pipeline version: retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. Budget/admission: GPU, provider and pipeline quotas prevent feedback automation from starving serving. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-08

- [ ] **Question:** Compare Budget/admission with Validation. When would each change your design?

**Answer:** Budget/admission: GPU, provider and pipeline quotas prevent feedback automation from starving serving. Validation: candidate must beat champion within owned quality/safety/performance/cost gates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-09

- [ ] **Question:** Compare Validation with Human promotion. When would each change your design?

**Answer:** Validation: candidate must beat champion within owned quality/safety/performance/cost gates. Human promotion: high-risk changes retain approval, exception and rollback rather than automatic drift-to-production. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### RETRAINING-AND-FEEDBACK-LOOPS-MN-10

- [ ] **Configuration review:** **Question:** Compare Human promotion with Trigger. When would each change your design?

**Answer:** Human promotion: high-risk changes retain approval, exception and rollback rather than automatic drift-to-production. Trigger: schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### RETRAINING-AND-FEEDBACK-LOOPS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Trigger; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/build_feedback_dataset.py --dry-run` plus recent events/changes, then correlate the service-specific SLI. schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-02

- [ ] **Question:** Production is degraded around Feedback collection; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc repro retrain` plus recent events/changes, then correlate the service-specific SLI. stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Label quality; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow runs list --experiment-id EXPERIMENT_ID` plus recent events/changes, then correlate the service-specific SLI. reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-04

- [ ] **Question:** Production is degraded around Sampling bias; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest candidate.yaml --dataset regression.jsonl` plus recent events/changes, then correlate the service-specific SLI. observed feedback reflects product exposure and user response rather than the target population automatically. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Poisoning; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/build_feedback_dataset.py --dry-run` plus recent events/changes, then correlate the service-specific SLI. anomalous contributors/content and influence controls protect training/evaluation sets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-06

- [ ] **Question:** Production is degraded around Replay set; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc repro retrain` plus recent events/changes, then correlate the service-specific SLI. retain representative historical/edge cases so adaptation does not catastrophically forget. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pipeline version; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `mlflow runs list --experiment-id EXPERIMENT_ID` plus recent events/changes, then correlate the service-specific SLI. retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-08

- [ ] **Question:** Production is degraded around Budget/admission; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python -m evals.run --manifest candidate.yaml --dataset regression.jsonl` plus recent events/changes, then correlate the service-specific SLI. GPU, provider and pipeline quotas prevent feedback automation from starving serving. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Validation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `python scripts/build_feedback_dataset.py --dry-run` plus recent events/changes, then correlate the service-specific SLI. candidate must beat champion within owned quality/safety/performance/cost gates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### RETRAINING-AND-FEEDBACK-LOOPS-MP-10

- [ ] **Question:** Production is degraded around Human promotion; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dvc repro retrain` plus recent events/changes, then correlate the service-specific SLI. high-risk changes retain approval, exception and rollback rather than automatic drift-to-production. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### RETRAINING-AND-FEEDBACK-LOOPS-SN-01

- [ ] **Question:** Design a production Retraining and feedback loops capability where Trigger, Sampling bias and Pipeline version are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. observed feedback reflects product exposure and user response rather than the target population automatically. retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Retraining and feedback loops capability where Feedback collection, Poisoning and Budget/admission are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. anomalous contributors/content and influence controls protect training/evaluation sets. GPU, provider and pipeline quotas prevent feedback automation from starving serving. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-03

- [ ] **Question:** Design a production Retraining and feedback loops capability where Label quality, Replay set and Validation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. retain representative historical/edge cases so adaptation does not catastrophically forget. candidate must beat champion within owned quality/safety/performance/cost gates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Retraining and feedback loops capability where Sampling bias, Pipeline version and Human promotion are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: observed feedback reflects product exposure and user response rather than the target population automatically. retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. high-risk changes retain approval, exception and rollback rather than automatic drift-to-production. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-05

- [ ] **Question:** Design a production Retraining and feedback loops capability where Poisoning, Budget/admission and Trigger are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: anomalous contributors/content and influence controls protect training/evaluation sets. GPU, provider and pipeline quotas prevent feedback automation from starving serving. schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Retraining and feedback loops capability where Replay set, Validation and Feedback collection are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retain representative historical/edge cases so adaptation does not catastrophically forget. candidate must beat champion within owned quality/safety/performance/cost gates. stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-07

- [ ] **Question:** Design a production Retraining and feedback loops capability where Pipeline version, Human promotion and Label quality are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. high-risk changes retain approval, exception and rollback rather than automatic drift-to-production. reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Retraining and feedback loops capability where Budget/admission, Trigger and Sampling bias are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: GPU, provider and pipeline quotas prevent feedback automation from starving serving. schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. observed feedback reflects product exposure and user response rather than the target population automatically. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-09

- [ ] **Question:** Design a production Retraining and feedback loops capability where Validation, Feedback collection and Poisoning are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: candidate must beat champion within owned quality/safety/performance/cost gates. stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. anomalous contributors/content and influence controls protect training/evaluation sets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### RETRAINING-AND-FEEDBACK-LOOPS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Retraining and feedback loops capability where Human promotion, Label quality and Replay set are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-risk changes retain approval, exception and rollback rather than automatic drift-to-production. reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. retain representative historical/edge cases so adaptation does not catastrophically forget. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### RETRAINING-AND-FEEDBACK-LOOPS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Trigger. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/build_feedback_dataset.py --dry-run` as one read-only checkpoint, not the whole diagnosis. schedule, data volume, drift, quality incident or business change proposes retraining under debounce/budget controls. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Feedback collection. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc repro retrain` as one read-only checkpoint, not the whole diagnosis. stable prediction/outcome IDs, consent, provenance and label definition determine trustworthy supervision. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Label quality. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow runs list --experiment-id EXPERIMENT_ID` as one read-only checkpoint, not the whole diagnosis. reviewer agreement, adjudication, sampling and leakage tests are part of training evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sampling bias. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest candidate.yaml --dataset regression.jsonl` as one read-only checkpoint, not the whole diagnosis. observed feedback reflects product exposure and user response rather than the target population automatically. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Poisoning. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/build_feedback_dataset.py --dry-run` as one read-only checkpoint, not the whole diagnosis. anomalous contributors/content and influence controls protect training/evaluation sets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Replay set. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc repro retrain` as one read-only checkpoint, not the whole diagnosis. retain representative historical/edge cases so adaptation does not catastrophically forget. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pipeline version. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `mlflow runs list --experiment-id EXPERIMENT_ID` as one read-only checkpoint, not the whole diagnosis. retraining uses immutable data/code/config/environment and produces a new candidate, never silent in-place mutation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Budget/admission. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python -m evals.run --manifest candidate.yaml --dataset regression.jsonl` as one read-only checkpoint, not the whole diagnosis. GPU, provider and pipeline quotas prevent feedback automation from starving serving. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Validation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `python scripts/build_feedback_dataset.py --dry-run` as one read-only checkpoint, not the whole diagnosis. candidate must beat champion within owned quality/safety/performance/cost gates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### RETRAINING-AND-FEEDBACK-LOOPS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Human promotion. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dvc repro retrain` as one read-only checkpoint, not the whole diagnosis. high-risk changes retain approval, exception and rollback rather than automatic drift-to-production. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
