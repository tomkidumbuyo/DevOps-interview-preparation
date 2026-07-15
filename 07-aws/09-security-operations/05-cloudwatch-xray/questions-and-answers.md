# Amazon CloudWatch and X-Ray — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-01

- [ ] **Question:** What is Metric/dimension, and why does it matter in Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-02

- [ ] **Question:** What is Alarm, and why does it matter in Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-03

- [ ] **Question:** What is Composite alarm, and why does it matter in Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** pages on combinations and can reduce symptom duplication. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-04

- [ ] **Question:** What is Log group/stream, and why does it matter in Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** retention, KMS, subscription and resource policy define log lifecycle. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-05

- [ ] **Question:** What is Logs Insights, and why does it matter in Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** query structured/unstructured fields over selected time/bytes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-06

- [ ] **Question:** What is Embedded Metric Format, and why does it matter in Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** logs generate custom metrics with cardinality/cost implications. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-07

- [ ] **Question:** What is Container Insights, and why does it matter in Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** curated container/cluster signals still need SLO application metrics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-08

- [ ] **Code:** **Question:** What does `aws xray get-service-graph --start-time START --end-time END` help you verify for Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: service-level telemetry/SLO features depend on supported instrumentation.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-09

- [ ] **Code:** **Question:** What does `aws cloudwatch describe-alarms --state-value ALARM` help you verify for Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: distributed trace documents service/dependency timing and errors.

### AMAZON-CLOUDWATCH-AND-X-RAY-JN-10

- [ ] **Code:** **Question:** What does `aws logs tail LOG_GROUP --since 30m` help you verify for Amazon CloudWatch and X-Ray?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: control trace/log volume and sensitive payload before export/storage.

## Junior — procedural and command questions

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-01

- [ ] **Code:** **Question:** A basic Metric/dimension check fails. What would you do first using the CLI?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch describe-alarms --state-value ALARM` and capture exact status/reason/request ID. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-02

- [ ] **Question:** A basic Alarm check fails. What would you do first?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws logs tail LOG_GROUP --since 30m` and capture exact status/reason/request ID. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-03

- [ ] **Question:** A basic Composite alarm check fails. What would you do first?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws logs start-query --log-group-name GROUP --start-time START --end-time END --query-string 'fields @timestamp,@message | limit 20'` and capture exact status/reason/request ID. pages on combinations and can reduce symptom duplication. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-04

- [ ] **Code:** **Question:** A basic Log group/stream check fails. What would you do first using the CLI?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws xray get-service-graph --start-time START --end-time END` and capture exact status/reason/request ID. retention, KMS, subscription and resource policy define log lifecycle. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-05

- [ ] **Question:** A basic Logs Insights check fails. What would you do first?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch describe-alarms --state-value ALARM` and capture exact status/reason/request ID. query structured/unstructured fields over selected time/bytes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-06

- [ ] **Question:** A basic Embedded Metric Format check fails. What would you do first?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws logs tail LOG_GROUP --since 30m` and capture exact status/reason/request ID. logs generate custom metrics with cardinality/cost implications. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-07

- [ ] **Code:** **Question:** A basic Container Insights check fails. What would you do first using the CLI?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws logs start-query --log-group-name GROUP --start-time START --end-time END --query-string 'fields @timestamp,@message | limit 20'` and capture exact status/reason/request ID. curated container/cluster signals still need SLO application metrics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-08

- [ ] **Question:** A basic Application Signals check fails. What would you do first?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws xray get-service-graph --start-time START --end-time END` and capture exact status/reason/request ID. service-level telemetry/SLO features depend on supported instrumentation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-09

- [ ] **Question:** A basic X-Ray segment/subsegment check fails. What would you do first?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch describe-alarms --state-value ALARM` and capture exact status/reason/request ID. distributed trace documents service/dependency timing and errors. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-CLOUDWATCH-AND-X-RAY-JP-10

- [ ] **Code:** **Question:** A basic Sampling/redaction check fails. What would you do first using the CLI?
> **Covered in:** [Amazon CloudWatch and X-Ray — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws logs tail LOG_GROUP --since 30m` and capture exact status/reason/request ID. control trace/log volume and sensitive payload before export/storage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-01

- [ ] **Question:** Compare Metric/dimension with Alarm. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Metric/dimension: numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Alarm: evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-02

- [ ] **Question:** Compare Alarm with Composite alarm. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Alarm: evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Composite alarm: pages on combinations and can reduce symptom duplication. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-03

- [ ] **Question:** Compare Composite alarm with Log group/stream. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Composite alarm: pages on combinations and can reduce symptom duplication. Log group/stream: retention, KMS, subscription and resource policy define log lifecycle. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-04

- [ ] **Configuration review:** **Question:** Compare Log group/stream with Logs Insights. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Log group/stream: retention, KMS, subscription and resource policy define log lifecycle. Logs Insights: query structured/unstructured fields over selected time/bytes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-05

- [ ] **Question:** Compare Logs Insights with Embedded Metric Format. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Logs Insights: query structured/unstructured fields over selected time/bytes. Embedded Metric Format: logs generate custom metrics with cardinality/cost implications. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-06

- [ ] **Question:** Compare Embedded Metric Format with Container Insights. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Embedded Metric Format: logs generate custom metrics with cardinality/cost implications. Container Insights: curated container/cluster signals still need SLO application metrics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-07

- [ ] **Configuration review:** **Question:** Compare Container Insights with Application Signals. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Container Insights: curated container/cluster signals still need SLO application metrics. Application Signals: service-level telemetry/SLO features depend on supported instrumentation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-08

- [ ] **Question:** Compare Application Signals with X-Ray segment/subsegment. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Application Signals: service-level telemetry/SLO features depend on supported instrumentation. X-Ray segment/subsegment: distributed trace documents service/dependency timing and errors. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-09

- [ ] **Question:** Compare X-Ray segment/subsegment with Sampling/redaction. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** X-Ray segment/subsegment: distributed trace documents service/dependency timing and errors. Sampling/redaction: control trace/log volume and sensitive payload before export/storage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-CLOUDWATCH-AND-X-RAY-MN-10

- [ ] **Configuration review:** **Question:** Compare Sampling/redaction with Metric/dimension. When would each change your design?
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Sampling/redaction: control trace/log volume and sensitive payload before export/storage. Metric/dimension: numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Metric/dimension; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch describe-alarms --state-value ALARM` plus recent events/changes, then correlate the service-specific SLI. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-02

- [ ] **Question:** Production is degraded around Alarm; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws logs tail LOG_GROUP --since 30m` plus recent events/changes, then correlate the service-specific SLI. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Composite alarm; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws logs start-query --log-group-name GROUP --start-time START --end-time END --query-string 'fields @timestamp,@message | limit 20'` plus recent events/changes, then correlate the service-specific SLI. pages on combinations and can reduce symptom duplication. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-04

- [ ] **Question:** Production is degraded around Log group/stream; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws xray get-service-graph --start-time START --end-time END` plus recent events/changes, then correlate the service-specific SLI. retention, KMS, subscription and resource policy define log lifecycle. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Logs Insights; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch describe-alarms --state-value ALARM` plus recent events/changes, then correlate the service-specific SLI. query structured/unstructured fields over selected time/bytes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-06

- [ ] **Question:** Production is degraded around Embedded Metric Format; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws logs tail LOG_GROUP --since 30m` plus recent events/changes, then correlate the service-specific SLI. logs generate custom metrics with cardinality/cost implications. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Container Insights; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws logs start-query --log-group-name GROUP --start-time START --end-time END --query-string 'fields @timestamp,@message | limit 20'` plus recent events/changes, then correlate the service-specific SLI. curated container/cluster signals still need SLO application metrics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-08

- [ ] **Question:** Production is degraded around Application Signals; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws xray get-service-graph --start-time START --end-time END` plus recent events/changes, then correlate the service-specific SLI. service-level telemetry/SLO features depend on supported instrumentation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around X-Ray segment/subsegment; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch describe-alarms --state-value ALARM` plus recent events/changes, then correlate the service-specific SLI. distributed trace documents service/dependency timing and errors. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-CLOUDWATCH-AND-X-RAY-MP-10

- [ ] **Question:** Production is degraded around Sampling/redaction; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws logs tail LOG_GROUP --since 30m` plus recent events/changes, then correlate the service-specific SLI. control trace/log volume and sensitive payload before export/storage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-01

- [ ] **Question:** Design a production Amazon CloudWatch and X-Ray capability where Metric/dimension, Log group/stream and Container Insights are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. retention, KMS, subscription and resource policy define log lifecycle. curated container/cluster signals still need SLO application metrics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon CloudWatch and X-Ray capability where Alarm, Logs Insights and Application Signals are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. query structured/unstructured fields over selected time/bytes. service-level telemetry/SLO features depend on supported instrumentation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-03

- [ ] **Question:** Design a production Amazon CloudWatch and X-Ray capability where Composite alarm, Embedded Metric Format and X-Ray segment/subsegment are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: pages on combinations and can reduce symptom duplication. logs generate custom metrics with cardinality/cost implications. distributed trace documents service/dependency timing and errors. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon CloudWatch and X-Ray capability where Log group/stream, Container Insights and Sampling/redaction are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: retention, KMS, subscription and resource policy define log lifecycle. curated container/cluster signals still need SLO application metrics. control trace/log volume and sensitive payload before export/storage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-05

- [ ] **Question:** Design a production Amazon CloudWatch and X-Ray capability where Logs Insights, Application Signals and Metric/dimension are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: query structured/unstructured fields over selected time/bytes. service-level telemetry/SLO features depend on supported instrumentation. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon CloudWatch and X-Ray capability where Embedded Metric Format, X-Ray segment/subsegment and Alarm are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: logs generate custom metrics with cardinality/cost implications. distributed trace documents service/dependency timing and errors. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-07

- [ ] **Question:** Design a production Amazon CloudWatch and X-Ray capability where Container Insights, Sampling/redaction and Composite alarm are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: curated container/cluster signals still need SLO application metrics. control trace/log volume and sensitive payload before export/storage. pages on combinations and can reduce symptom duplication. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon CloudWatch and X-Ray capability where Application Signals, Metric/dimension and Log group/stream are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: service-level telemetry/SLO features depend on supported instrumentation. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. retention, KMS, subscription and resource policy define log lifecycle. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-09

- [ ] **Question:** Design a production Amazon CloudWatch and X-Ray capability where X-Ray segment/subsegment, Alarm and Logs Insights are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: distributed trace documents service/dependency timing and errors. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. query structured/unstructured fields over selected time/bytes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-CLOUDWATCH-AND-X-RAY-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon CloudWatch and X-Ray capability where Sampling/redaction, Composite alarm and Embedded Metric Format are first-class requirements.
> **Covered in:** [Amazon CloudWatch and X-Ray — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: control trace/log volume and sensitive payload before export/storage. pages on combinations and can reduce symptom duplication. logs generate custom metrics with cardinality/cost implications. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metric/dimension. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch describe-alarms --state-value ALARM` as one read-only checkpoint, not the whole diagnosis. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Alarm. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws logs tail LOG_GROUP --since 30m` as one read-only checkpoint, not the whole diagnosis. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Composite alarm. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws logs start-query --log-group-name GROUP --start-time START --end-time END --query-string 'fields @timestamp,@message | limit 20'` as one read-only checkpoint, not the whole diagnosis. pages on combinations and can reduce symptom duplication. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Log group/stream. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws xray get-service-graph --start-time START --end-time END` as one read-only checkpoint, not the whole diagnosis. retention, KMS, subscription and resource policy define log lifecycle. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Logs Insights. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch describe-alarms --state-value ALARM` as one read-only checkpoint, not the whole diagnosis. query structured/unstructured fields over selected time/bytes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Embedded Metric Format. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws logs tail LOG_GROUP --since 30m` as one read-only checkpoint, not the whole diagnosis. logs generate custom metrics with cardinality/cost implications. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Container Insights. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws logs start-query --log-group-name GROUP --start-time START --end-time END --query-string 'fields @timestamp,@message | limit 20'` as one read-only checkpoint, not the whole diagnosis. curated container/cluster signals still need SLO application metrics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Application Signals. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws xray get-service-graph --start-time START --end-time END` as one read-only checkpoint, not the whole diagnosis. service-level telemetry/SLO features depend on supported instrumentation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving X-Ray segment/subsegment. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch describe-alarms --state-value ALARM` as one read-only checkpoint, not the whole diagnosis. distributed trace documents service/dependency timing and errors. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-CLOUDWATCH-AND-X-RAY-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Sampling/redaction. How do you lead it end to end?
> **Covered in:** [Amazon CloudWatch and X-Ray — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws logs tail LOG_GROUP --since 30m` as one read-only checkpoint, not the whole diagnosis. control trace/log volume and sensitive payload before export/storage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: GuardDuty, Security Hub, Inspector, Macie and Detective](../04-security-detection/README.md) · [Study note](README.md) · [Next: AWS CloudTrail and Config →](../06-cloudtrail-config/README.md)

<!-- reading-navigation:end -->
