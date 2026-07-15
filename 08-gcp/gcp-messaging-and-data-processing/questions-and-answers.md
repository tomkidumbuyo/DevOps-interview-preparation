# GCP messaging and data processing — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-01

- [ ] **Question:** What is Pub/Sub, and why does it matter in GCP messaging and data processing?

**Answer:** is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-02

- [ ] **Question:** What is Dataflow, and why does it matter in GCP messaging and data processing?

**Answer:** is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-03

- [ ] **Question:** What is Dataproc, and why does it matter in GCP messaging and data processing?

**Answer:** is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-04

- [ ] **Question:** What is Cloud Composer, and why does it matter in GCP messaging and data processing?

**Answer:** is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-05

- [ ] **Question:** What is Eventarc, and why does it matter in GCP messaging and data processing?

**Answer:** is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-06

- [ ] **Question:** What is Workflows, and why does it matter in GCP messaging and data processing?

**Answer:** is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-07

- [ ] **Question:** What is Kafka integration, and why does it matter in GCP messaging and data processing?

**Answer:** is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-08

- [ ] **Code:** **Question:** What does `gcloud logging read 'severity>=ERROR' --limit=20` help you verify for GCP messaging and data processing?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-09

- [ ] **Code:** **Question:** What does `gcloud auth list` help you verify for GCP messaging and data processing?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JN-10

- [ ] **Code:** **Question:** What does `gcloud config list` help you verify for GCP messaging and data processing?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off.

## Junior — procedural and command questions

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-01

- [ ] **Code:** **Question:** A basic Pub/Sub check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-02

- [ ] **Question:** A basic Dataflow check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-03

- [ ] **Question:** A basic Dataproc check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-04

- [ ] **Code:** **Question:** A basic Cloud Composer check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-05

- [ ] **Question:** A basic Eventarc check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-06

- [ ] **Question:** A basic Workflows check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-07

- [ ] **Code:** **Question:** A basic Kafka integration check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud projects describe PROJECT` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-08

- [ ] **Question:** A basic Dead-letter handling check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud logging read 'severity>=ERROR' --limit=20` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-09

- [ ] **Question:** A basic Streaming and batch pipelines check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud auth list` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-JP-10

- [ ] **Code:** **Question:** A basic Pub/Sub check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `gcloud config list` and capture exact status/reason/request ID. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-01

- [ ] **Question:** Compare Pub/Sub with Dataflow. When would each change your design?

**Answer:** Pub/Sub: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dataflow: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-02

- [ ] **Question:** Compare Dataflow with Dataproc. When would each change your design?

**Answer:** Dataflow: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dataproc: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-03

- [ ] **Question:** Compare Dataproc with Cloud Composer. When would each change your design?

**Answer:** Dataproc: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Cloud Composer: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-04

- [ ] **Configuration review:** **Question:** Compare Cloud Composer with Eventarc. When would each change your design?

**Answer:** Cloud Composer: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Eventarc: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-05

- [ ] **Question:** Compare Eventarc with Workflows. When would each change your design?

**Answer:** Eventarc: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Workflows: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-06

- [ ] **Question:** Compare Workflows with Kafka integration. When would each change your design?

**Answer:** Workflows: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Kafka integration: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-07

- [ ] **Configuration review:** **Question:** Compare Kafka integration with Dead-letter handling. When would each change your design?

**Answer:** Kafka integration: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Dead-letter handling: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-08

- [ ] **Question:** Compare Dead-letter handling with Streaming and batch pipelines. When would each change your design?

**Answer:** Dead-letter handling: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Streaming and batch pipelines: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-09

- [ ] **Question:** Compare Streaming and batch pipelines with Pub/Sub. When would each change your design?

**Answer:** Streaming and batch pipelines: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Pub/Sub: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MN-10

- [ ] **Configuration review:** **Question:** Compare Pub/Sub with Pub/Sub. When would each change your design?

**Answer:** Pub/Sub: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Pub/Sub: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pub/Sub; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-02

- [ ] **Question:** Production is degraded around Dataflow; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Dataproc; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-04

- [ ] **Question:** Production is degraded around Cloud Composer; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Eventarc; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-06

- [ ] **Question:** Production is degraded around Workflows; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Kafka integration; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud projects describe PROJECT` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-08

- [ ] **Question:** Production is degraded around Dead-letter handling; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud logging read 'severity>=ERROR' --limit=20` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Streaming and batch pipelines; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud auth list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-MP-10

- [ ] **Question:** Production is degraded around Pub/Sub; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `gcloud config list` plus recent events/changes, then correlate the service-specific SLI. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-01

- [ ] **Question:** Design a production GCP messaging and data processing capability where Pub/Sub, Cloud Composer and Kafka integration are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production GCP messaging and data processing capability where Dataflow, Eventarc and Dead-letter handling are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-03

- [ ] **Question:** Design a production GCP messaging and data processing capability where Dataproc, Workflows and Streaming and batch pipelines are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production GCP messaging and data processing capability where Cloud Composer, Kafka integration and Pub/Sub are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-05

- [ ] **Question:** Design a production GCP messaging and data processing capability where Eventarc, Dead-letter handling and Pub/Sub are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production GCP messaging and data processing capability where Workflows, Streaming and batch pipelines and Dataflow are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-07

- [ ] **Question:** Design a production GCP messaging and data processing capability where Kafka integration, Pub/Sub and Dataproc are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production GCP messaging and data processing capability where Dead-letter handling, Pub/Sub and Cloud Composer are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-09

- [ ] **Question:** Design a production GCP messaging and data processing capability where Streaming and batch pipelines, Dataflow and Eventarc are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production GCP messaging and data processing capability where Pub/Sub, Dataproc and Workflows are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pub/Sub. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dataflow. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dataproc. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cloud Composer. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Eventarc. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Workflows. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Kafka integration. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud projects describe PROJECT` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Dead-letter handling. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud logging read 'severity>=ERROR' --limit=20` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Streaming and batch pipelines. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud auth list` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-GCP-MESSAGING-AND-DATA-PROCESSING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pub/Sub. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `gcloud config list` as one read-only checkpoint, not the whole diagnosis. is part of GCP messaging and data processing; learn its precise definition, mechanism and lifecycle, nearest alternatives, configuration interface, failure/limit, security boundary, observable evidence and production trade-off. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
