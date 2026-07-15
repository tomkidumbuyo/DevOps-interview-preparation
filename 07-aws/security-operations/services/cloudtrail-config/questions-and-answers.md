# AWS CloudTrail and Config — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-CLOUDTRAIL-AND-CONFIG-JN-01

- [ ] **Question:** What is Management event, and why does it matter in AWS CloudTrail and Config?

**Answer:** control-plane API activity such as creating/changing resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-02

- [ ] **Question:** What is Data event, and why does it matter in AWS CloudTrail and Config?

**Answer:** high-volume resource data-plane activity enabled selectively at additional cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-03

- [ ] **Question:** What is Organization trail, and why does it matter in AWS CloudTrail and Config?

**Answer:** covers current/new member accounts under centralized governance. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-04

- [ ] **Question:** What is Log file validation, and why does it matter in AWS CloudTrail and Config?

**Answer:** digest chain helps verify delivered CloudTrail file integrity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-05

- [ ] **Question:** What is CloudTrail Lake, and why does it matter in AWS CloudTrail and Config?

**Answer:** managed event store/query with event data stores and retention/cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-06

- [ ] **Question:** What is Config recorder, and why does it matter in AWS CloudTrail and Config?

**Answer:** records supported resource configuration and relationship changes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-07

- [ ] **Question:** What is Config rule, and why does it matter in AWS CloudTrail and Config?

**Answer:** evaluates desired compliance periodically or on change. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-08

- [ ] **Code:** **Question:** What does `aws configservice get-resource-config-history --resource-type TYPE --resource-id ID` help you verify for AWS CloudTrail and Config?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: centralizes configuration/compliance across accounts/Regions.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-09

- [ ] **Code:** **Question:** What does `aws cloudtrail describe-trails` help you verify for AWS CloudTrail and Config?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: SSM automation can correct findings but needs blast-radius and exception handling.

### AWS-CLOUDTRAIL-AND-CONFIG-JN-10

- [ ] **Code:** **Question:** What does `aws cloudtrail get-trail-status --name TRAIL` help you verify for AWS CloudTrail and Config?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: independent log account, restrictive bucket/KMS, retention/object lock prevent tampering.

## Junior — procedural and command questions

### AWS-CLOUDTRAIL-AND-CONFIG-JP-01

- [ ] **Code:** **Question:** A basic Management event check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail describe-trails` and capture exact status/reason/request ID. control-plane API activity such as creating/changing resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-02

- [ ] **Question:** A basic Data event check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail get-trail-status --name TRAIL` and capture exact status/reason/request ID. high-volume resource data-plane activity enabled selectively at additional cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-03

- [ ] **Question:** A basic Organization trail check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=EVENT` and capture exact status/reason/request ID. covers current/new member accounts under centralized governance. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-04

- [ ] **Code:** **Question:** A basic Log file validation check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws configservice get-resource-config-history --resource-type TYPE --resource-id ID` and capture exact status/reason/request ID. digest chain helps verify delivered CloudTrail file integrity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-05

- [ ] **Question:** A basic CloudTrail Lake check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail describe-trails` and capture exact status/reason/request ID. managed event store/query with event data stores and retention/cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-06

- [ ] **Question:** A basic Config recorder check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail get-trail-status --name TRAIL` and capture exact status/reason/request ID. records supported resource configuration and relationship changes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-07

- [ ] **Code:** **Question:** A basic Config rule check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=EVENT` and capture exact status/reason/request ID. evaluates desired compliance periodically or on change. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-08

- [ ] **Question:** A basic Aggregator check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws configservice get-resource-config-history --resource-type TYPE --resource-id ID` and capture exact status/reason/request ID. centralizes configuration/compliance across accounts/Regions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-09

- [ ] **Question:** A basic Remediation check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail describe-trails` and capture exact status/reason/request ID. SSM automation can correct findings but needs blast-radius and exception handling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CLOUDTRAIL-AND-CONFIG-JP-10

- [ ] **Code:** **Question:** A basic Delivery protection check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudtrail get-trail-status --name TRAIL` and capture exact status/reason/request ID. independent log account, restrictive bucket/KMS, retention/object lock prevent tampering. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-CLOUDTRAIL-AND-CONFIG-MN-01

- [ ] **Question:** Compare Management event with Data event. When would each change your design?

**Answer:** Management event: control-plane API activity such as creating/changing resources. Data event: high-volume resource data-plane activity enabled selectively at additional cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-02

- [ ] **Question:** Compare Data event with Organization trail. When would each change your design?

**Answer:** Data event: high-volume resource data-plane activity enabled selectively at additional cost. Organization trail: covers current/new member accounts under centralized governance. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-03

- [ ] **Question:** Compare Organization trail with Log file validation. When would each change your design?

**Answer:** Organization trail: covers current/new member accounts under centralized governance. Log file validation: digest chain helps verify delivered CloudTrail file integrity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-04

- [ ] **Configuration review:** **Question:** Compare Log file validation with CloudTrail Lake. When would each change your design?

**Answer:** Log file validation: digest chain helps verify delivered CloudTrail file integrity. CloudTrail Lake: managed event store/query with event data stores and retention/cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-05

- [ ] **Question:** Compare CloudTrail Lake with Config recorder. When would each change your design?

**Answer:** CloudTrail Lake: managed event store/query with event data stores and retention/cost. Config recorder: records supported resource configuration and relationship changes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-06

- [ ] **Question:** Compare Config recorder with Config rule. When would each change your design?

**Answer:** Config recorder: records supported resource configuration and relationship changes. Config rule: evaluates desired compliance periodically or on change. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-07

- [ ] **Configuration review:** **Question:** Compare Config rule with Aggregator. When would each change your design?

**Answer:** Config rule: evaluates desired compliance periodically or on change. Aggregator: centralizes configuration/compliance across accounts/Regions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-08

- [ ] **Question:** Compare Aggregator with Remediation. When would each change your design?

**Answer:** Aggregator: centralizes configuration/compliance across accounts/Regions. Remediation: SSM automation can correct findings but needs blast-radius and exception handling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-09

- [ ] **Question:** Compare Remediation with Delivery protection. When would each change your design?

**Answer:** Remediation: SSM automation can correct findings but needs blast-radius and exception handling. Delivery protection: independent log account, restrictive bucket/KMS, retention/object lock prevent tampering. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CLOUDTRAIL-AND-CONFIG-MN-10

- [ ] **Configuration review:** **Question:** Compare Delivery protection with Management event. When would each change your design?

**Answer:** Delivery protection: independent log account, restrictive bucket/KMS, retention/object lock prevent tampering. Management event: control-plane API activity such as creating/changing resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-CLOUDTRAIL-AND-CONFIG-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Management event; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail describe-trails` plus recent events/changes, then correlate the service-specific SLI. control-plane API activity such as creating/changing resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-02

- [ ] **Question:** Production is degraded around Data event; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail get-trail-status --name TRAIL` plus recent events/changes, then correlate the service-specific SLI. high-volume resource data-plane activity enabled selectively at additional cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Organization trail; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=EVENT` plus recent events/changes, then correlate the service-specific SLI. covers current/new member accounts under centralized governance. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-04

- [ ] **Question:** Production is degraded around Log file validation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws configservice get-resource-config-history --resource-type TYPE --resource-id ID` plus recent events/changes, then correlate the service-specific SLI. digest chain helps verify delivered CloudTrail file integrity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around CloudTrail Lake; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail describe-trails` plus recent events/changes, then correlate the service-specific SLI. managed event store/query with event data stores and retention/cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-06

- [ ] **Question:** Production is degraded around Config recorder; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail get-trail-status --name TRAIL` plus recent events/changes, then correlate the service-specific SLI. records supported resource configuration and relationship changes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Config rule; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=EVENT` plus recent events/changes, then correlate the service-specific SLI. evaluates desired compliance periodically or on change. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-08

- [ ] **Question:** Production is degraded around Aggregator; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws configservice get-resource-config-history --resource-type TYPE --resource-id ID` plus recent events/changes, then correlate the service-specific SLI. centralizes configuration/compliance across accounts/Regions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Remediation; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail describe-trails` plus recent events/changes, then correlate the service-specific SLI. SSM automation can correct findings but needs blast-radius and exception handling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CLOUDTRAIL-AND-CONFIG-MP-10

- [ ] **Question:** Production is degraded around Delivery protection; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudtrail get-trail-status --name TRAIL` plus recent events/changes, then correlate the service-specific SLI. independent log account, restrictive bucket/KMS, retention/object lock prevent tampering. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-CLOUDTRAIL-AND-CONFIG-SN-01

- [ ] **Question:** Design a production AWS CloudTrail and Config capability where Management event, Log file validation and Config rule are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: control-plane API activity such as creating/changing resources. digest chain helps verify delivered CloudTrail file integrity. evaluates desired compliance periodically or on change. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudTrail and Config capability where Data event, CloudTrail Lake and Aggregator are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: high-volume resource data-plane activity enabled selectively at additional cost. managed event store/query with event data stores and retention/cost. centralizes configuration/compliance across accounts/Regions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-03

- [ ] **Question:** Design a production AWS CloudTrail and Config capability where Organization trail, Config recorder and Remediation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: covers current/new member accounts under centralized governance. records supported resource configuration and relationship changes. SSM automation can correct findings but needs blast-radius and exception handling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudTrail and Config capability where Log file validation, Config rule and Delivery protection are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: digest chain helps verify delivered CloudTrail file integrity. evaluates desired compliance periodically or on change. independent log account, restrictive bucket/KMS, retention/object lock prevent tampering. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-05

- [ ] **Question:** Design a production AWS CloudTrail and Config capability where CloudTrail Lake, Aggregator and Management event are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed event store/query with event data stores and retention/cost. centralizes configuration/compliance across accounts/Regions. control-plane API activity such as creating/changing resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudTrail and Config capability where Config recorder, Remediation and Data event are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records supported resource configuration and relationship changes. SSM automation can correct findings but needs blast-radius and exception handling. high-volume resource data-plane activity enabled selectively at additional cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-07

- [ ] **Question:** Design a production AWS CloudTrail and Config capability where Config rule, Delivery protection and Organization trail are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: evaluates desired compliance periodically or on change. independent log account, restrictive bucket/KMS, retention/object lock prevent tampering. covers current/new member accounts under centralized governance. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudTrail and Config capability where Aggregator, Management event and Log file validation are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: centralizes configuration/compliance across accounts/Regions. control-plane API activity such as creating/changing resources. digest chain helps verify delivered CloudTrail file integrity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-09

- [ ] **Question:** Design a production AWS CloudTrail and Config capability where Remediation, Data event and CloudTrail Lake are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: SSM automation can correct findings but needs blast-radius and exception handling. high-volume resource data-plane activity enabled selectively at additional cost. managed event store/query with event data stores and retention/cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CLOUDTRAIL-AND-CONFIG-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS CloudTrail and Config capability where Delivery protection, Organization trail and Config recorder are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: independent log account, restrictive bucket/KMS, retention/object lock prevent tampering. covers current/new member accounts under centralized governance. records supported resource configuration and relationship changes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-CLOUDTRAIL-AND-CONFIG-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Management event. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail describe-trails` as one read-only checkpoint, not the whole diagnosis. control-plane API activity such as creating/changing resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data event. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail get-trail-status --name TRAIL` as one read-only checkpoint, not the whole diagnosis. high-volume resource data-plane activity enabled selectively at additional cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Organization trail. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=EVENT` as one read-only checkpoint, not the whole diagnosis. covers current/new member accounts under centralized governance. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Log file validation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws configservice get-resource-config-history --resource-type TYPE --resource-id ID` as one read-only checkpoint, not the whole diagnosis. digest chain helps verify delivered CloudTrail file integrity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CloudTrail Lake. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail describe-trails` as one read-only checkpoint, not the whole diagnosis. managed event store/query with event data stores and retention/cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Config recorder. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail get-trail-status --name TRAIL` as one read-only checkpoint, not the whole diagnosis. records supported resource configuration and relationship changes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Config rule. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=EVENT` as one read-only checkpoint, not the whole diagnosis. evaluates desired compliance periodically or on change. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Aggregator. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws configservice get-resource-config-history --resource-type TYPE --resource-id ID` as one read-only checkpoint, not the whole diagnosis. centralizes configuration/compliance across accounts/Regions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Remediation. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail describe-trails` as one read-only checkpoint, not the whole diagnosis. SSM automation can correct findings but needs blast-radius and exception handling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CLOUDTRAIL-AND-CONFIG-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Delivery protection. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudtrail get-trail-status --name TRAIL` as one read-only checkpoint, not the whole diagnosis. independent log account, restrictive bucket/KMS, retention/object lock prevent tampering. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
