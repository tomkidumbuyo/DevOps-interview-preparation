# AWS Backup — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-BACKUP-JN-01

- [ ] **Question:** What is Backup plan, and why does it matter in AWS Backup?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** schedule, window, lifecycle and copy rules define intended RPO/retention. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-BACKUP-JN-02

- [ ] **Question:** What is Resource selection, and why does it matter in AWS Backup?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** tags/ARNs/roles determine coverage and need inventory validation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-BACKUP-JN-03

- [ ] **Question:** What is Backup vault, and why does it matter in AWS Backup?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** access/KMS/lock policies isolate recovery points from workloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-BACKUP-JN-04

- [ ] **Question:** What is Vault Lock, and why does it matter in AWS Backup?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** governance/compliance modes constrain deletion and require careful retention/legal operation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-BACKUP-JN-05

- [ ] **Question:** What is Cross-account copy, and why does it matter in AWS Backup?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** reduces workload-account compromise blast radius under organization/KMS policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-BACKUP-JN-06

- [ ] **Question:** What is Cross-Region copy, and why does it matter in AWS Backup?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** addresses regional disaster while adding transfer/residency considerations. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-BACKUP-JN-07

- [ ] **Question:** What is Recovery point, and why does it matter in AWS Backup?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** provider-specific restore metadata and consistency determine usefulness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-BACKUP-JN-08

- [ ] **Code:** **Question:** What does `aws backup list-recovery-points-by-backup-vault --backup-vault-name VAULT` help you verify for AWS Backup?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: scheduled restore plus application validation measures actual recovery.

### AWS-BACKUP-JN-09

- [ ] **Code:** **Question:** What does `aws backup list-restore-testing-plans` help you verify for AWS Backup?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: produces control evidence but needs accurate framework/scope.

### AWS-BACKUP-JN-10

- [ ] **Code:** **Question:** What does `aws backup list-restore-jobs` help you verify for AWS Backup?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: job success, lag, copy and timed restore results must meet business targets.

## Junior — procedural and command questions

### AWS-BACKUP-JP-01

- [ ] **Code:** **Question:** A basic Backup plan check fails. What would you do first using the CLI?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-backup-plans` and capture exact status/reason/request ID. schedule, window, lifecycle and copy rules define intended RPO/retention. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-02

- [ ] **Question:** A basic Resource selection check fails. What would you do first?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-backup-jobs` and capture exact status/reason/request ID. tags/ARNs/roles determine coverage and need inventory validation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-03

- [ ] **Question:** A basic Backup vault check fails. What would you do first?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-recovery-points-by-backup-vault --backup-vault-name VAULT` and capture exact status/reason/request ID. access/KMS/lock policies isolate recovery points from workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-04

- [ ] **Code:** **Question:** A basic Vault Lock check fails. What would you do first using the CLI?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-restore-testing-plans` and capture exact status/reason/request ID. governance/compliance modes constrain deletion and require careful retention/legal operation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-05

- [ ] **Question:** A basic Cross-account copy check fails. What would you do first?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-restore-jobs` and capture exact status/reason/request ID. reduces workload-account compromise blast radius under organization/KMS policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-06

- [ ] **Question:** A basic Cross-Region copy check fails. What would you do first?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-backup-plans` and capture exact status/reason/request ID. addresses regional disaster while adding transfer/residency considerations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-07

- [ ] **Code:** **Question:** A basic Recovery point check fails. What would you do first using the CLI?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-backup-jobs` and capture exact status/reason/request ID. provider-specific restore metadata and consistency determine usefulness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-08

- [ ] **Question:** A basic Restore testing check fails. What would you do first?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-recovery-points-by-backup-vault --backup-vault-name VAULT` and capture exact status/reason/request ID. scheduled restore plus application validation measures actual recovery. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-09

- [ ] **Question:** A basic Backup Audit Manager check fails. What would you do first?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-restore-testing-plans` and capture exact status/reason/request ID. produces control evidence but needs accurate framework/scope. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-BACKUP-JP-10

- [ ] **Code:** **Question:** A basic RPO/RTO evidence check fails. What would you do first using the CLI?
> **Covered in:** [AWS Backup — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws backup list-restore-jobs` and capture exact status/reason/request ID. job success, lag, copy and timed restore results must meet business targets. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-BACKUP-MN-01

- [ ] **Question:** Compare Backup plan with Resource selection. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Backup plan: schedule, window, lifecycle and copy rules define intended RPO/retention. Resource selection: tags/ARNs/roles determine coverage and need inventory validation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-02

- [ ] **Question:** Compare Resource selection with Backup vault. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Resource selection: tags/ARNs/roles determine coverage and need inventory validation. Backup vault: access/KMS/lock policies isolate recovery points from workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-03

- [ ] **Question:** Compare Backup vault with Vault Lock. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Backup vault: access/KMS/lock policies isolate recovery points from workloads. Vault Lock: governance/compliance modes constrain deletion and require careful retention/legal operation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-04

- [ ] **Configuration review:** **Question:** Compare Vault Lock with Cross-account copy. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Vault Lock: governance/compliance modes constrain deletion and require careful retention/legal operation. Cross-account copy: reduces workload-account compromise blast radius under organization/KMS policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-05

- [ ] **Question:** Compare Cross-account copy with Cross-Region copy. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cross-account copy: reduces workload-account compromise blast radius under organization/KMS policy. Cross-Region copy: addresses regional disaster while adding transfer/residency considerations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-06

- [ ] **Question:** Compare Cross-Region copy with Recovery point. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Cross-Region copy: addresses regional disaster while adding transfer/residency considerations. Recovery point: provider-specific restore metadata and consistency determine usefulness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-07

- [ ] **Configuration review:** **Question:** Compare Recovery point with Restore testing. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Recovery point: provider-specific restore metadata and consistency determine usefulness. Restore testing: scheduled restore plus application validation measures actual recovery. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-08

- [ ] **Question:** Compare Restore testing with Backup Audit Manager. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Restore testing: scheduled restore plus application validation measures actual recovery. Backup Audit Manager: produces control evidence but needs accurate framework/scope. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-09

- [ ] **Question:** Compare Backup Audit Manager with RPO/RTO evidence. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Backup Audit Manager: produces control evidence but needs accurate framework/scope. RPO/RTO evidence: job success, lag, copy and timed restore results must meet business targets. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-BACKUP-MN-10

- [ ] **Configuration review:** **Question:** Compare RPO/RTO evidence with Backup plan. When would each change your design?
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** RPO/RTO evidence: job success, lag, copy and timed restore results must meet business targets. Backup plan: schedule, window, lifecycle and copy rules define intended RPO/retention. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-BACKUP-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backup plan; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-backup-plans` plus recent events/changes, then correlate the service-specific SLI. schedule, window, lifecycle and copy rules define intended RPO/retention. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-02

- [ ] **Question:** Production is degraded around Resource selection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-backup-jobs` plus recent events/changes, then correlate the service-specific SLI. tags/ARNs/roles determine coverage and need inventory validation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backup vault; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-recovery-points-by-backup-vault --backup-vault-name VAULT` plus recent events/changes, then correlate the service-specific SLI. access/KMS/lock policies isolate recovery points from workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-04

- [ ] **Question:** Production is degraded around Vault Lock; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-restore-testing-plans` plus recent events/changes, then correlate the service-specific SLI. governance/compliance modes constrain deletion and require careful retention/legal operation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Cross-account copy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-restore-jobs` plus recent events/changes, then correlate the service-specific SLI. reduces workload-account compromise blast radius under organization/KMS policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-06

- [ ] **Question:** Production is degraded around Cross-Region copy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-backup-plans` plus recent events/changes, then correlate the service-specific SLI. addresses regional disaster while adding transfer/residency considerations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Recovery point; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-backup-jobs` plus recent events/changes, then correlate the service-specific SLI. provider-specific restore metadata and consistency determine usefulness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-08

- [ ] **Question:** Production is degraded around Restore testing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-recovery-points-by-backup-vault --backup-vault-name VAULT` plus recent events/changes, then correlate the service-specific SLI. scheduled restore plus application validation measures actual recovery. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Backup Audit Manager; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-restore-testing-plans` plus recent events/changes, then correlate the service-specific SLI. produces control evidence but needs accurate framework/scope. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-BACKUP-MP-10

- [ ] **Question:** Production is degraded around RPO/RTO evidence; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws backup list-restore-jobs` plus recent events/changes, then correlate the service-specific SLI. job success, lag, copy and timed restore results must meet business targets. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-BACKUP-SN-01

- [ ] **Question:** Design a production AWS Backup capability where Backup plan, Vault Lock and Recovery point are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: schedule, window, lifecycle and copy rules define intended RPO/retention. governance/compliance modes constrain deletion and require careful retention/legal operation. provider-specific restore metadata and consistency determine usefulness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Backup capability where Resource selection, Cross-account copy and Restore testing are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tags/ARNs/roles determine coverage and need inventory validation. reduces workload-account compromise blast radius under organization/KMS policy. scheduled restore plus application validation measures actual recovery. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-03

- [ ] **Question:** Design a production AWS Backup capability where Backup vault, Cross-Region copy and Backup Audit Manager are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: access/KMS/lock policies isolate recovery points from workloads. addresses regional disaster while adding transfer/residency considerations. produces control evidence but needs accurate framework/scope. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Backup capability where Vault Lock, Recovery point and RPO/RTO evidence are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: governance/compliance modes constrain deletion and require careful retention/legal operation. provider-specific restore metadata and consistency determine usefulness. job success, lag, copy and timed restore results must meet business targets. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-05

- [ ] **Question:** Design a production AWS Backup capability where Cross-account copy, Restore testing and Backup plan are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reduces workload-account compromise blast radius under organization/KMS policy. scheduled restore plus application validation measures actual recovery. schedule, window, lifecycle and copy rules define intended RPO/retention. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Backup capability where Cross-Region copy, Backup Audit Manager and Resource selection are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: addresses regional disaster while adding transfer/residency considerations. produces control evidence but needs accurate framework/scope. tags/ARNs/roles determine coverage and need inventory validation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-07

- [ ] **Question:** Design a production AWS Backup capability where Recovery point, RPO/RTO evidence and Backup vault are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: provider-specific restore metadata and consistency determine usefulness. job success, lag, copy and timed restore results must meet business targets. access/KMS/lock policies isolate recovery points from workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Backup capability where Restore testing, Backup plan and Vault Lock are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: scheduled restore plus application validation measures actual recovery. schedule, window, lifecycle and copy rules define intended RPO/retention. governance/compliance modes constrain deletion and require careful retention/legal operation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-09

- [ ] **Question:** Design a production AWS Backup capability where Backup Audit Manager, Resource selection and Cross-account copy are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: produces control evidence but needs accurate framework/scope. tags/ARNs/roles determine coverage and need inventory validation. reduces workload-account compromise blast radius under organization/KMS policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-BACKUP-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Backup capability where RPO/RTO evidence, Backup vault and Cross-Region copy are first-class requirements.
> **Covered in:** [AWS Backup — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: job success, lag, copy and timed restore results must meet business targets. access/KMS/lock policies isolate recovery points from workloads. addresses regional disaster while adding transfer/residency considerations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-BACKUP-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backup plan. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-backup-plans` as one read-only checkpoint, not the whole diagnosis. schedule, window, lifecycle and copy rules define intended RPO/retention. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource selection. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-backup-jobs` as one read-only checkpoint, not the whole diagnosis. tags/ARNs/roles determine coverage and need inventory validation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backup vault. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-recovery-points-by-backup-vault --backup-vault-name VAULT` as one read-only checkpoint, not the whole diagnosis. access/KMS/lock policies isolate recovery points from workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Vault Lock. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-restore-testing-plans` as one read-only checkpoint, not the whole diagnosis. governance/compliance modes constrain deletion and require careful retention/legal operation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cross-account copy. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-restore-jobs` as one read-only checkpoint, not the whole diagnosis. reduces workload-account compromise blast radius under organization/KMS policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Cross-Region copy. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-backup-plans` as one read-only checkpoint, not the whole diagnosis. addresses regional disaster while adding transfer/residency considerations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Recovery point. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-backup-jobs` as one read-only checkpoint, not the whole diagnosis. provider-specific restore metadata and consistency determine usefulness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Restore testing. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-recovery-points-by-backup-vault --backup-vault-name VAULT` as one read-only checkpoint, not the whole diagnosis. scheduled restore plus application validation measures actual recovery. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Backup Audit Manager. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-restore-testing-plans` as one read-only checkpoint, not the whole diagnosis. produces control evidence but needs accurate framework/scope. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-BACKUP-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving RPO/RTO evidence. How do you lead it end to end?
> **Covered in:** [AWS Backup — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws backup list-restore-jobs` as one read-only checkpoint, not the whole diagnosis. job success, lag, copy and timed restore results must meet business targets. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Amazon FSx](../04-fsx/README.md) · [Study note](README.md) · [Next: Containers →](../../06-containers/README.md)

<!-- reading-navigation:end -->
