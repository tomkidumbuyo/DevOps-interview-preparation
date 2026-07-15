# Foundations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-FOUNDATIONS-JN-01

- [ ] **Question:** What is Principals, and why does it matter in Foundations?

**Answer:** users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-FOUNDATIONS-JN-02

- [ ] **Question:** What is Identity policies, and why does it matter in Foundations?

**Answer:** attached policies grant or deny actions to a principal within the rest of the policy intersection. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-FOUNDATIONS-JN-03

- [ ] **Question:** What is Management account, and why does it matter in Foundations?

**Answer:** owns the organization and must be tightly protected rather than used for workloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-FOUNDATIONS-JN-04

- [ ] **Question:** What is Member accounts, and why does it matter in Foundations?

**Answer:** separate workloads, environments, teams and blast radii with independent quotas and root identities. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-FOUNDATIONS-JN-05

- [ ] **Question:** What is AssumeRole, and why does it matter in Foundations?

**Answer:** exchanges an authenticated caller for temporary role credentials subject to trust and permissions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-FOUNDATIONS-JN-06

- [ ] **Question:** What is Trust policy, and why does it matter in Foundations?

**Answer:** controls which principal and conditions may assume a role. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-FOUNDATIONS-JN-07

- [ ] **Question:** What is Landing zone, and why does it matter in Foundations?

**Answer:** standardized multi-account identity, logging, security and network foundation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-FOUNDATIONS-JN-08

- [ ] **Code:** **Question:** What does `aws controltower list-enabled-controls --target-identifier OU_ARN` help you verify for Foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: preventive, detective and proactive controls differ in enforcement timing and mechanism.

### BRANCH-FOUNDATIONS-JN-09

- [ ] **Code:** **Question:** What does `aws sts get-caller-identity` help you verify for Foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles.

### BRANCH-FOUNDATIONS-JN-10

- [ ] **Code:** **Question:** What does `aws organizations describe-organization` help you verify for Foundations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: attached policies grant or deny actions to a principal within the rest of the policy intersection.

## Junior — procedural and command questions

### BRANCH-FOUNDATIONS-JP-01

- [ ] **Code:** **Question:** A basic Principals check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-02

- [ ] **Question:** A basic Identity policies check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations describe-organization` and capture exact status/reason/request ID. attached policies grant or deny actions to a principal within the rest of the policy intersection. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-03

- [ ] **Question:** A basic Management account check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` and capture exact status/reason/request ID. owns the organization and must be tightly protected rather than used for workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-04

- [ ] **Code:** **Question:** A basic Member accounts check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws controltower list-enabled-controls --target-identifier OU_ARN` and capture exact status/reason/request ID. separate workloads, environments, teams and blast radii with independent quotas and root identities. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-05

- [ ] **Question:** A basic AssumeRole check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-06

- [ ] **Question:** A basic Trust policy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations describe-organization` and capture exact status/reason/request ID. controls which principal and conditions may assume a role. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-07

- [ ] **Code:** **Question:** A basic Landing zone check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` and capture exact status/reason/request ID. standardized multi-account identity, logging, security and network foundation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-08

- [ ] **Question:** A basic Control Tower controls check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws controltower list-enabled-controls --target-identifier OU_ARN` and capture exact status/reason/request ID. preventive, detective and proactive controls differ in enforcement timing and mechanism. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-09

- [ ] **Question:** A basic Principals check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-FOUNDATIONS-JP-10

- [ ] **Code:** **Question:** A basic Identity policies check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations describe-organization` and capture exact status/reason/request ID. attached policies grant or deny actions to a principal within the rest of the policy intersection. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-FOUNDATIONS-MN-01

- [ ] **Question:** Compare Principals with Identity policies. When would each change your design?

**Answer:** Principals: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Identity policies: attached policies grant or deny actions to a principal within the rest of the policy intersection. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-02

- [ ] **Question:** Compare Identity policies with Management account. When would each change your design?

**Answer:** Identity policies: attached policies grant or deny actions to a principal within the rest of the policy intersection. Management account: owns the organization and must be tightly protected rather than used for workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-03

- [ ] **Question:** Compare Management account with Member accounts. When would each change your design?

**Answer:** Management account: owns the organization and must be tightly protected rather than used for workloads. Member accounts: separate workloads, environments, teams and blast radii with independent quotas and root identities. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Member accounts with AssumeRole. When would each change your design?

**Answer:** Member accounts: separate workloads, environments, teams and blast radii with independent quotas and root identities. AssumeRole: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-05

- [ ] **Question:** Compare AssumeRole with Trust policy. When would each change your design?

**Answer:** AssumeRole: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Trust policy: controls which principal and conditions may assume a role. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-06

- [ ] **Question:** Compare Trust policy with Landing zone. When would each change your design?

**Answer:** Trust policy: controls which principal and conditions may assume a role. Landing zone: standardized multi-account identity, logging, security and network foundation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Landing zone with Control Tower controls. When would each change your design?

**Answer:** Landing zone: standardized multi-account identity, logging, security and network foundation. Control Tower controls: preventive, detective and proactive controls differ in enforcement timing and mechanism. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-08

- [ ] **Question:** Compare Control Tower controls with Principals. When would each change your design?

**Answer:** Control Tower controls: preventive, detective and proactive controls differ in enforcement timing and mechanism. Principals: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-09

- [ ] **Question:** Compare Principals with Identity policies. When would each change your design?

**Answer:** Principals: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Identity policies: attached policies grant or deny actions to a principal within the rest of the policy intersection. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-FOUNDATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Identity policies with Principals. When would each change your design?

**Answer:** Identity policies: attached policies grant or deny actions to a principal within the rest of the policy intersection. Principals: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-FOUNDATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Principals; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-02

- [ ] **Question:** Production is degraded around Identity policies; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations describe-organization` plus recent events/changes, then correlate the service-specific SLI. attached policies grant or deny actions to a principal within the rest of the policy intersection. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Management account; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` plus recent events/changes, then correlate the service-specific SLI. owns the organization and must be tightly protected rather than used for workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-04

- [ ] **Question:** Production is degraded around Member accounts; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws controltower list-enabled-controls --target-identifier OU_ARN` plus recent events/changes, then correlate the service-specific SLI. separate workloads, environments, teams and blast radii with independent quotas and root identities. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around AssumeRole; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-06

- [ ] **Question:** Production is degraded around Trust policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations describe-organization` plus recent events/changes, then correlate the service-specific SLI. controls which principal and conditions may assume a role. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Landing zone; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` plus recent events/changes, then correlate the service-specific SLI. standardized multi-account identity, logging, security and network foundation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-08

- [ ] **Question:** Production is degraded around Control Tower controls; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws controltower list-enabled-controls --target-identifier OU_ARN` plus recent events/changes, then correlate the service-specific SLI. preventive, detective and proactive controls differ in enforcement timing and mechanism. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Principals; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-FOUNDATIONS-MP-10

- [ ] **Question:** Production is degraded around Identity policies; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations describe-organization` plus recent events/changes, then correlate the service-specific SLI. attached policies grant or deny actions to a principal within the rest of the policy intersection. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-FOUNDATIONS-SN-01

- [ ] **Question:** Design a production Foundations capability where Principals, Member accounts and Landing zone are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. separate workloads, environments, teams and blast radii with independent quotas and root identities. standardized multi-account identity, logging, security and network foundation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Foundations capability where Identity policies, AssumeRole and Control Tower controls are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: attached policies grant or deny actions to a principal within the rest of the policy intersection. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. preventive, detective and proactive controls differ in enforcement timing and mechanism. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-03

- [ ] **Question:** Design a production Foundations capability where Management account, Trust policy and Principals are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owns the organization and must be tightly protected rather than used for workloads. controls which principal and conditions may assume a role. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Foundations capability where Member accounts, Landing zone and Identity policies are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: separate workloads, environments, teams and blast radii with independent quotas and root identities. standardized multi-account identity, logging, security and network foundation. attached policies grant or deny actions to a principal within the rest of the policy intersection. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-05

- [ ] **Question:** Design a production Foundations capability where AssumeRole, Control Tower controls and Principals are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. preventive, detective and proactive controls differ in enforcement timing and mechanism. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Foundations capability where Trust policy, Principals and Identity policies are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controls which principal and conditions may assume a role. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. attached policies grant or deny actions to a principal within the rest of the policy intersection. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-07

- [ ] **Question:** Design a production Foundations capability where Landing zone, Identity policies and Management account are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: standardized multi-account identity, logging, security and network foundation. attached policies grant or deny actions to a principal within the rest of the policy intersection. owns the organization and must be tightly protected rather than used for workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Foundations capability where Control Tower controls, Principals and Member accounts are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: preventive, detective and proactive controls differ in enforcement timing and mechanism. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. separate workloads, environments, teams and blast radii with independent quotas and root identities. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-09

- [ ] **Question:** Design a production Foundations capability where Principals, Identity policies and AssumeRole are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. attached policies grant or deny actions to a principal within the rest of the policy intersection. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-FOUNDATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Foundations capability where Identity policies, Management account and Trust policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: attached policies grant or deny actions to a principal within the rest of the policy intersection. owns the organization and must be tightly protected rather than used for workloads. controls which principal and conditions may assume a role. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-FOUNDATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Principals. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Identity policies. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations describe-organization` as one read-only checkpoint, not the whole diagnosis. attached policies grant or deny actions to a principal within the rest of the policy intersection. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Management account. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` as one read-only checkpoint, not the whole diagnosis. owns the organization and must be tightly protected rather than used for workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Member accounts. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws controltower list-enabled-controls --target-identifier OU_ARN` as one read-only checkpoint, not the whole diagnosis. separate workloads, environments, teams and blast radii with independent quotas and root identities. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AssumeRole. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Trust policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations describe-organization` as one read-only checkpoint, not the whole diagnosis. controls which principal and conditions may assume a role. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Landing zone. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` as one read-only checkpoint, not the whole diagnosis. standardized multi-account identity, logging, security and network foundation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control Tower controls. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws controltower list-enabled-controls --target-identifier OU_ARN` as one read-only checkpoint, not the whole diagnosis. preventive, detective and proactive controls differ in enforcement timing and mechanism. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Principals. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-FOUNDATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Identity policies. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations describe-organization` as one read-only checkpoint, not the whole diagnosis. attached policies grant or deny actions to a principal within the rest of the policy intersection. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
