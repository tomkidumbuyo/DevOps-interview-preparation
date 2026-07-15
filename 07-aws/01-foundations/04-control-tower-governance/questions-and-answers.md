# AWS Control Tower, tagging, quotas and governance — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-01

- [ ] **Question:** What is Landing zone, and why does it matter in AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** standardized multi-account identity, logging, security and network foundation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-02

- [ ] **Question:** What is Control Tower controls, and why does it matter in AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** preventive, detective and proactive controls differ in enforcement timing and mechanism. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-03

- [ ] **Question:** What is Tag taxonomy, and why does it matter in AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** owner, environment, data class, cost center and lifecycle fields support operations and allocation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-04

- [ ] **Question:** What is Tag policies, and why does it matter in AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** standardize allowed tag values but may not enforce every resource creation path alone. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-05

- [ ] **Question:** What is AWS Config, and why does it matter in AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** records supported configuration history and evaluates compliance rules. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-06

- [ ] **Question:** What is CloudTrail, and why does it matter in AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** records account/API activity and must be centralized/protected. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-07

- [ ] **Question:** What is Service quotas, and why does it matter in AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** API/resource ceilings need inventory, forecast, alert and early increase requests. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-08

- [ ] **Code:** **Question:** What does `aws resource-explorer-2 search --query-string 'tag.key:Owner'` help you verify for AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: provide cross-account resource inventory with service-specific coverage.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-09

- [ ] **Code:** **Question:** What does `aws controltower list-enabled-controls --target-identifier OU_ARN` help you verify for AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JN-10

- [ ] **Code:** **Question:** What does `aws configservice describe-compliance-by-config-rule` help you verify for AWS Control Tower, tagging, quotas and governance?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: decide source of truth and use reviewed automation rather than destructive automatic correction everywhere.

## Junior — procedural and command questions

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-01

- [ ] **Code:** **Question:** A basic Landing zone check fails. What would you do first using the CLI?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws controltower list-enabled-controls --target-identifier OU_ARN` and capture exact status/reason/request ID. standardized multi-account identity, logging, security and network foundation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-02

- [ ] **Question:** A basic Control Tower controls check fails. What would you do first?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws configservice describe-compliance-by-config-rule` and capture exact status/reason/request ID. preventive, detective and proactive controls differ in enforcement timing and mechanism. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-03

- [ ] **Question:** A basic Tag taxonomy check fails. What would you do first?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws service-quotas list-service-quotas --service-code SERVICE` and capture exact status/reason/request ID. owner, environment, data class, cost center and lifecycle fields support operations and allocation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-04

- [ ] **Code:** **Question:** A basic Tag policies check fails. What would you do first using the CLI?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws resource-explorer-2 search --query-string 'tag.key:Owner'` and capture exact status/reason/request ID. standardize allowed tag values but may not enforce every resource creation path alone. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-05

- [ ] **Question:** A basic AWS Config check fails. What would you do first?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws controltower list-enabled-controls --target-identifier OU_ARN` and capture exact status/reason/request ID. records supported configuration history and evaluates compliance rules. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-06

- [ ] **Question:** A basic CloudTrail check fails. What would you do first?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws configservice describe-compliance-by-config-rule` and capture exact status/reason/request ID. records account/API activity and must be centralized/protected. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-07

- [ ] **Code:** **Question:** A basic Service quotas check fails. What would you do first using the CLI?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws service-quotas list-service-quotas --service-code SERVICE` and capture exact status/reason/request ID. API/resource ceilings need inventory, forecast, alert and early increase requests. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-08

- [ ] **Question:** A basic AWS Resource Explorer/Config aggregators check fails. What would you do first?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws resource-explorer-2 search --query-string 'tag.key:Owner'` and capture exact status/reason/request ID. provide cross-account resource inventory with service-specific coverage. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-09

- [ ] **Question:** A basic Budget controls check fails. What would you do first?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws controltower list-enabled-controls --target-identifier OU_ARN` and capture exact status/reason/request ID. combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-JP-10

- [ ] **Code:** **Question:** A basic Drift remediation check fails. What would you do first using the CLI?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws configservice describe-compliance-by-config-rule` and capture exact status/reason/request ID. decide source of truth and use reviewed automation rather than destructive automatic correction everywhere. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-01

- [ ] **Question:** Compare Landing zone with Control Tower controls. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Landing zone: standardized multi-account identity, logging, security and network foundation. Control Tower controls: preventive, detective and proactive controls differ in enforcement timing and mechanism. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-02

- [ ] **Question:** Compare Control Tower controls with Tag taxonomy. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Control Tower controls: preventive, detective and proactive controls differ in enforcement timing and mechanism. Tag taxonomy: owner, environment, data class, cost center and lifecycle fields support operations and allocation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-03

- [ ] **Question:** Compare Tag taxonomy with Tag policies. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Tag taxonomy: owner, environment, data class, cost center and lifecycle fields support operations and allocation. Tag policies: standardize allowed tag values but may not enforce every resource creation path alone. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-04

- [ ] **Configuration review:** **Question:** Compare Tag policies with AWS Config. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Tag policies: standardize allowed tag values but may not enforce every resource creation path alone. AWS Config: records supported configuration history and evaluates compliance rules. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-05

- [ ] **Question:** Compare AWS Config with CloudTrail. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** AWS Config: records supported configuration history and evaluates compliance rules. CloudTrail: records account/API activity and must be centralized/protected. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-06

- [ ] **Question:** Compare CloudTrail with Service quotas. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CloudTrail: records account/API activity and must be centralized/protected. Service quotas: API/resource ceilings need inventory, forecast, alert and early increase requests. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-07

- [ ] **Configuration review:** **Question:** Compare Service quotas with AWS Resource Explorer/Config aggregators. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Service quotas: API/resource ceilings need inventory, forecast, alert and early increase requests. AWS Resource Explorer/Config aggregators: provide cross-account resource inventory with service-specific coverage. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-08

- [ ] **Question:** Compare AWS Resource Explorer/Config aggregators with Budget controls. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** AWS Resource Explorer/Config aggregators: provide cross-account resource inventory with service-specific coverage. Budget controls: combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-09

- [ ] **Question:** Compare Budget controls with Drift remediation. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Budget controls: combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops. Drift remediation: decide source of truth and use reviewed automation rather than destructive automatic correction everywhere. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MN-10

- [ ] **Configuration review:** **Question:** Compare Drift remediation with Landing zone. When would each change your design?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Drift remediation: decide source of truth and use reviewed automation rather than destructive automatic correction everywhere. Landing zone: standardized multi-account identity, logging, security and network foundation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Landing zone; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws controltower list-enabled-controls --target-identifier OU_ARN` plus recent events/changes, then correlate the service-specific SLI. standardized multi-account identity, logging, security and network foundation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-02

- [ ] **Question:** Production is degraded around Control Tower controls; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws configservice describe-compliance-by-config-rule` plus recent events/changes, then correlate the service-specific SLI. preventive, detective and proactive controls differ in enforcement timing and mechanism. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Tag taxonomy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws service-quotas list-service-quotas --service-code SERVICE` plus recent events/changes, then correlate the service-specific SLI. owner, environment, data class, cost center and lifecycle fields support operations and allocation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-04

- [ ] **Question:** Production is degraded around Tag policies; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws resource-explorer-2 search --query-string 'tag.key:Owner'` plus recent events/changes, then correlate the service-specific SLI. standardize allowed tag values but may not enforce every resource creation path alone. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around AWS Config; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws controltower list-enabled-controls --target-identifier OU_ARN` plus recent events/changes, then correlate the service-specific SLI. records supported configuration history and evaluates compliance rules. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-06

- [ ] **Question:** Production is degraded around CloudTrail; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws configservice describe-compliance-by-config-rule` plus recent events/changes, then correlate the service-specific SLI. records account/API activity and must be centralized/protected. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Service quotas; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws service-quotas list-service-quotas --service-code SERVICE` plus recent events/changes, then correlate the service-specific SLI. API/resource ceilings need inventory, forecast, alert and early increase requests. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-08

- [ ] **Question:** Production is degraded around AWS Resource Explorer/Config aggregators; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws resource-explorer-2 search --query-string 'tag.key:Owner'` plus recent events/changes, then correlate the service-specific SLI. provide cross-account resource inventory with service-specific coverage. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Budget controls; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws controltower list-enabled-controls --target-identifier OU_ARN` plus recent events/changes, then correlate the service-specific SLI. combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-MP-10

- [ ] **Question:** Production is degraded around Drift remediation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws configservice describe-compliance-by-config-rule` plus recent events/changes, then correlate the service-specific SLI. decide source of truth and use reviewed automation rather than destructive automatic correction everywhere. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-01

- [ ] **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where Landing zone, Tag policies and Service quotas are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: standardized multi-account identity, logging, security and network foundation. standardize allowed tag values but may not enforce every resource creation path alone. API/resource ceilings need inventory, forecast, alert and early increase requests. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where Control Tower controls, AWS Config and AWS Resource Explorer/Config aggregators are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: preventive, detective and proactive controls differ in enforcement timing and mechanism. records supported configuration history and evaluates compliance rules. provide cross-account resource inventory with service-specific coverage. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-03

- [ ] **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where Tag taxonomy, CloudTrail and Budget controls are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owner, environment, data class, cost center and lifecycle fields support operations and allocation. records account/API activity and must be centralized/protected. combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where Tag policies, Service quotas and Drift remediation are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: standardize allowed tag values but may not enforce every resource creation path alone. API/resource ceilings need inventory, forecast, alert and early increase requests. decide source of truth and use reviewed automation rather than destructive automatic correction everywhere. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-05

- [ ] **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where AWS Config, AWS Resource Explorer/Config aggregators and Landing zone are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records supported configuration history and evaluates compliance rules. provide cross-account resource inventory with service-specific coverage. standardized multi-account identity, logging, security and network foundation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where CloudTrail, Budget controls and Control Tower controls are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: records account/API activity and must be centralized/protected. combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops. preventive, detective and proactive controls differ in enforcement timing and mechanism. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-07

- [ ] **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where Service quotas, Drift remediation and Tag taxonomy are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: API/resource ceilings need inventory, forecast, alert and early increase requests. decide source of truth and use reviewed automation rather than destructive automatic correction everywhere. owner, environment, data class, cost center and lifecycle fields support operations and allocation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where AWS Resource Explorer/Config aggregators, Landing zone and Tag policies are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provide cross-account resource inventory with service-specific coverage. standardized multi-account identity, logging, security and network foundation. standardize allowed tag values but may not enforce every resource creation path alone. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-09

- [ ] **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where Budget controls, Control Tower controls and AWS Config are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops. preventive, detective and proactive controls differ in enforcement timing and mechanism. records supported configuration history and evaluates compliance rules. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Control Tower, tagging, quotas and governance capability where Drift remediation, Tag taxonomy and CloudTrail are first-class requirements.
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: decide source of truth and use reviewed automation rather than destructive automatic correction everywhere. owner, environment, data class, cost center and lifecycle fields support operations and allocation. records account/API activity and must be centralized/protected. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Landing zone. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws controltower list-enabled-controls --target-identifier OU_ARN` as one read-only checkpoint, not the whole diagnosis. standardized multi-account identity, logging, security and network foundation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control Tower controls. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws configservice describe-compliance-by-config-rule` as one read-only checkpoint, not the whole diagnosis. preventive, detective and proactive controls differ in enforcement timing and mechanism. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tag taxonomy. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws service-quotas list-service-quotas --service-code SERVICE` as one read-only checkpoint, not the whole diagnosis. owner, environment, data class, cost center and lifecycle fields support operations and allocation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Tag policies. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws resource-explorer-2 search --query-string 'tag.key:Owner'` as one read-only checkpoint, not the whole diagnosis. standardize allowed tag values but may not enforce every resource creation path alone. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AWS Config. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws controltower list-enabled-controls --target-identifier OU_ARN` as one read-only checkpoint, not the whole diagnosis. records supported configuration history and evaluates compliance rules. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CloudTrail. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws configservice describe-compliance-by-config-rule` as one read-only checkpoint, not the whole diagnosis. records account/API activity and must be centralized/protected. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service quotas. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws service-quotas list-service-quotas --service-code SERVICE` as one read-only checkpoint, not the whole diagnosis. API/resource ceilings need inventory, forecast, alert and early increase requests. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AWS Resource Explorer/Config aggregators. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws resource-explorer-2 search --query-string 'tag.key:Owner'` as one read-only checkpoint, not the whole diagnosis. provide cross-account resource inventory with service-specific coverage. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Budget controls. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws controltower list-enabled-controls --target-identifier OU_ARN` as one read-only checkpoint, not the whole diagnosis. combine alerts/anomaly detection with service/platform quotas because budgets are not universal hard stops. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-CONTROL-TOWER-TAGGING-QUOTAS-AND-GOVERNANCE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Drift remediation. How do you lead it end to end?
> **Covered in:** [AWS Control Tower, tagging, quotas and governance — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws configservice describe-compliance-by-config-rule` as one read-only checkpoint, not the whole diagnosis. decide source of truth and use reviewed automation rather than destructive automatic correction everywhere. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AWS STS, federation and IAM Identity Center](../03-sts-identity-center/README.md) · [Study note](README.md) · [Next: Networking →](../../02-networking/README.md)

<!-- reading-navigation:end -->
