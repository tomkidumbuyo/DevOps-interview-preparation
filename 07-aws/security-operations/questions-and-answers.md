# Security Operations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-SECURITY-OPERATIONS-JN-01

- [ ] **Question:** What is KMS key, and why does it matter in Security Operations?

**Answer:** logical key with policy, metadata and protected key material used by integrated services. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-OPERATIONS-JN-02

- [ ] **Question:** What is Envelope encryption, and why does it matter in Security Operations?

**Answer:** KMS protects data keys while applications/services encrypt bulk data locally. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-OPERATIONS-JN-03

- [ ] **Question:** What is Secret version/stage, and why does it matter in Security Operations?

**Answer:** labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-OPERATIONS-JN-04

- [ ] **Question:** What is Rotation Lambda, and why does it matter in Security Operations?

**Answer:** creates/sets/tests/finishes a new credential under idempotent staged workflow. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-OPERATIONS-JN-05

- [ ] **Question:** What is ACM certificate, and why does it matter in Security Operations?

**Answer:** managed public/private/imported certificate with supported service integration. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-OPERATIONS-JN-06

- [ ] **Question:** What is DNS validation, and why does it matter in Security Operations?

**Answer:** persistent validation record enables managed renewal when service conditions hold. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-OPERATIONS-JN-07

- [ ] **Question:** What is GuardDuty, and why does it matter in Security Operations?

**Answer:** analyzes supported logs/signals to emit contextual threat findings. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-SECURITY-OPERATIONS-JN-08

- [ ] **Code:** **Question:** What does `aws kms describe-key --key-id KEY` help you verify for Security Operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: aggregates/normalizes findings and control standards across accounts/Regions.

### BRANCH-SECURITY-OPERATIONS-JN-09

- [ ] **Code:** **Question:** What does `aws secretsmanager describe-secret --secret-id SECRET` help you verify for Security Operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost.

### BRANCH-SECURITY-OPERATIONS-JN-10

- [ ] **Code:** **Question:** What does `aws acm list-certificates` help you verify for Security Operations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state.

## Junior — procedural and command questions

### BRANCH-SECURITY-OPERATIONS-JP-01

- [ ] **Code:** **Question:** A basic KMS key check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms describe-key --key-id KEY` and capture exact status/reason/request ID. logical key with policy, metadata and protected key material used by integrated services. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-02

- [ ] **Question:** A basic Envelope encryption check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager describe-secret --secret-id SECRET` and capture exact status/reason/request ID. KMS protects data keys while applications/services encrypt bulk data locally. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-03

- [ ] **Question:** A basic Secret version/stage check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws acm list-certificates` and capture exact status/reason/request ID. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-04

- [ ] **Code:** **Question:** A basic Rotation Lambda check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws guardduty list-detectors` and capture exact status/reason/request ID. creates/sets/tests/finishes a new credential under idempotent staged workflow. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-05

- [ ] **Question:** A basic ACM certificate check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch describe-alarms --state-value ALARM` and capture exact status/reason/request ID. managed public/private/imported certificate with supported service integration. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-06

- [ ] **Question:** A basic DNS validation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail describe-trails` and capture exact status/reason/request ID. persistent validation record enables managed renewal when service conditions hold. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-07

- [ ] **Code:** **Question:** A basic GuardDuty check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ssm describe-instance-information` and capture exact status/reason/request ID. analyzes supported logs/signals to emit contextual threat findings. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-08

- [ ] **Question:** A basic Security Hub check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws kms describe-key --key-id KEY` and capture exact status/reason/request ID. aggregates/normalizes findings and control standards across accounts/Regions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-09

- [ ] **Question:** A basic Metric/dimension check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws secretsmanager describe-secret --secret-id SECRET` and capture exact status/reason/request ID. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-SECURITY-OPERATIONS-JP-10

- [ ] **Code:** **Question:** A basic Alarm check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws acm list-certificates` and capture exact status/reason/request ID. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-SECURITY-OPERATIONS-MN-01

- [ ] **Question:** Compare KMS key with Envelope encryption. When would each change your design?

**Answer:** KMS key: logical key with policy, metadata and protected key material used by integrated services. Envelope encryption: KMS protects data keys while applications/services encrypt bulk data locally. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-02

- [ ] **Question:** Compare Envelope encryption with Secret version/stage. When would each change your design?

**Answer:** Envelope encryption: KMS protects data keys while applications/services encrypt bulk data locally. Secret version/stage: labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-03

- [ ] **Question:** Compare Secret version/stage with Rotation Lambda. When would each change your design?

**Answer:** Secret version/stage: labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Rotation Lambda: creates/sets/tests/finishes a new credential under idempotent staged workflow. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Rotation Lambda with ACM certificate. When would each change your design?

**Answer:** Rotation Lambda: creates/sets/tests/finishes a new credential under idempotent staged workflow. ACM certificate: managed public/private/imported certificate with supported service integration. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-05

- [ ] **Question:** Compare ACM certificate with DNS validation. When would each change your design?

**Answer:** ACM certificate: managed public/private/imported certificate with supported service integration. DNS validation: persistent validation record enables managed renewal when service conditions hold. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-06

- [ ] **Question:** Compare DNS validation with GuardDuty. When would each change your design?

**Answer:** DNS validation: persistent validation record enables managed renewal when service conditions hold. GuardDuty: analyzes supported logs/signals to emit contextual threat findings. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare GuardDuty with Security Hub. When would each change your design?

**Answer:** GuardDuty: analyzes supported logs/signals to emit contextual threat findings. Security Hub: aggregates/normalizes findings and control standards across accounts/Regions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-08

- [ ] **Question:** Compare Security Hub with Metric/dimension. When would each change your design?

**Answer:** Security Hub: aggregates/normalizes findings and control standards across accounts/Regions. Metric/dimension: numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-09

- [ ] **Question:** Compare Metric/dimension with Alarm. When would each change your design?

**Answer:** Metric/dimension: numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Alarm: evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-SECURITY-OPERATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Alarm with KMS key. When would each change your design?

**Answer:** Alarm: evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. KMS key: logical key with policy, metadata and protected key material used by integrated services. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-SECURITY-OPERATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around KMS key; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms describe-key --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. logical key with policy, metadata and protected key material used by integrated services. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-02

- [ ] **Question:** Production is degraded around Envelope encryption; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager describe-secret --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. KMS protects data keys while applications/services encrypt bulk data locally. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Secret version/stage; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws acm list-certificates` plus recent events/changes, then correlate the service-specific SLI. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-04

- [ ] **Question:** Production is degraded around Rotation Lambda; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws guardduty list-detectors` plus recent events/changes, then correlate the service-specific SLI. creates/sets/tests/finishes a new credential under idempotent staged workflow. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around ACM certificate; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch describe-alarms --state-value ALARM` plus recent events/changes, then correlate the service-specific SLI. managed public/private/imported certificate with supported service integration. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-06

- [ ] **Question:** Production is degraded around DNS validation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail describe-trails` plus recent events/changes, then correlate the service-specific SLI. persistent validation record enables managed renewal when service conditions hold. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around GuardDuty; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ssm describe-instance-information` plus recent events/changes, then correlate the service-specific SLI. analyzes supported logs/signals to emit contextual threat findings. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-08

- [ ] **Question:** Production is degraded around Security Hub; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws kms describe-key --key-id KEY` plus recent events/changes, then correlate the service-specific SLI. aggregates/normalizes findings and control standards across accounts/Regions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Metric/dimension; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws secretsmanager describe-secret --secret-id SECRET` plus recent events/changes, then correlate the service-specific SLI. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-SECURITY-OPERATIONS-MP-10

- [ ] **Question:** Production is degraded around Alarm; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws acm list-certificates` plus recent events/changes, then correlate the service-specific SLI. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-SECURITY-OPERATIONS-SN-01

- [ ] **Question:** Design a production Security Operations capability where KMS key, Rotation Lambda and GuardDuty are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: logical key with policy, metadata and protected key material used by integrated services. creates/sets/tests/finishes a new credential under idempotent staged workflow. analyzes supported logs/signals to emit contextual threat findings. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Security Operations capability where Envelope encryption, ACM certificate and Security Hub are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: KMS protects data keys while applications/services encrypt bulk data locally. managed public/private/imported certificate with supported service integration. aggregates/normalizes findings and control standards across accounts/Regions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-03

- [ ] **Question:** Design a production Security Operations capability where Secret version/stage, DNS validation and Metric/dimension are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. persistent validation record enables managed renewal when service conditions hold. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Security Operations capability where Rotation Lambda, GuardDuty and Alarm are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: creates/sets/tests/finishes a new credential under idempotent staged workflow. analyzes supported logs/signals to emit contextual threat findings. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-05

- [ ] **Question:** Design a production Security Operations capability where ACM certificate, Security Hub and KMS key are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed public/private/imported certificate with supported service integration. aggregates/normalizes findings and control standards across accounts/Regions. logical key with policy, metadata and protected key material used by integrated services. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Security Operations capability where DNS validation, Metric/dimension and Envelope encryption are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: persistent validation record enables managed renewal when service conditions hold. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. KMS protects data keys while applications/services encrypt bulk data locally. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-07

- [ ] **Question:** Design a production Security Operations capability where GuardDuty, Alarm and Secret version/stage are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: analyzes supported logs/signals to emit contextual threat findings. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Security Operations capability where Security Hub, KMS key and Rotation Lambda are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: aggregates/normalizes findings and control standards across accounts/Regions. logical key with policy, metadata and protected key material used by integrated services. creates/sets/tests/finishes a new credential under idempotent staged workflow. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-09

- [ ] **Question:** Design a production Security Operations capability where Metric/dimension, Envelope encryption and ACM certificate are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. KMS protects data keys while applications/services encrypt bulk data locally. managed public/private/imported certificate with supported service integration. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-SECURITY-OPERATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Security Operations capability where Alarm, Secret version/stage and DNS validation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. persistent validation record enables managed renewal when service conditions hold. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-SECURITY-OPERATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving KMS key. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms describe-key --key-id KEY` as one read-only checkpoint, not the whole diagnosis. logical key with policy, metadata and protected key material used by integrated services. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Envelope encryption. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager describe-secret --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. KMS protects data keys while applications/services encrypt bulk data locally. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Secret version/stage. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws acm list-certificates` as one read-only checkpoint, not the whole diagnosis. labels such as AWSCURRENT/AWSPENDING coordinate rotation and rollback. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rotation Lambda. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws guardduty list-detectors` as one read-only checkpoint, not the whole diagnosis. creates/sets/tests/finishes a new credential under idempotent staged workflow. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ACM certificate. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch describe-alarms --state-value ALARM` as one read-only checkpoint, not the whole diagnosis. managed public/private/imported certificate with supported service integration. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNS validation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail describe-trails` as one read-only checkpoint, not the whole diagnosis. persistent validation record enables managed renewal when service conditions hold. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GuardDuty. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ssm describe-instance-information` as one read-only checkpoint, not the whole diagnosis. analyzes supported logs/signals to emit contextual threat findings. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Security Hub. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws kms describe-key --key-id KEY` as one read-only checkpoint, not the whole diagnosis. aggregates/normalizes findings and control standards across accounts/Regions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Metric/dimension. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws secretsmanager describe-secret --secret-id SECRET` as one read-only checkpoint, not the whole diagnosis. numeric time series and bounded dimensions enable aggregation but high cardinality multiplies cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-SECURITY-OPERATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Alarm. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws acm list-certificates` as one read-only checkpoint, not the whole diagnosis. evaluates metric/statistic/period/datapoints/missing-data into OK/ALARM/insufficient state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
