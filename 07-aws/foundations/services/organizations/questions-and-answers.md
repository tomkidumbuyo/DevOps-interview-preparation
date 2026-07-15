# AWS Organizations — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-ORGANIZATIONS-JN-01

- [ ] **Question:** What is Management account, and why does it matter in AWS Organizations?

**Answer:** owns the organization and must be tightly protected rather than used for workloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-ORGANIZATIONS-JN-02

- [ ] **Question:** What is Member accounts, and why does it matter in AWS Organizations?

**Answer:** separate workloads, environments, teams and blast radii with independent quotas and root identities. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-ORGANIZATIONS-JN-03

- [ ] **Question:** What is Organizational units, and why does it matter in AWS Organizations?

**Answer:** group accounts for policy inheritance and lifecycle rather than acting as runtime resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-ORGANIZATIONS-JN-04

- [ ] **Question:** What is Service Control Policies, and why does it matter in AWS Organizations?

**Answer:** define maximum permissions for member principals but grant no permission. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-ORGANIZATIONS-JN-05

- [ ] **Question:** What is Delegated administrator, and why does it matter in AWS Organizations?

**Answer:** lets a security/platform account operate supported organization-wide services. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-ORGANIZATIONS-JN-06

- [ ] **Question:** What is Consolidated billing, and why does it matter in AWS Organizations?

**Answer:** aggregates charges and commitment sharing while accounts retain usage ownership. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-ORGANIZATIONS-JN-07

- [ ] **Question:** What is Organization trails/config, and why does it matter in AWS Organizations?

**Answer:** centralize immutable audit and configuration history outside workload accounts. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-ORGANIZATIONS-JN-08

- [ ] **Code:** **Question:** What does `aws organizations list-policies-for-target --target-id ACCOUNT_ID --filter SERVICE_CONTROL_POLICY` help you verify for AWS Organizations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: creates standardized accounts with contacts, identity, networks, logs, budgets and owners.

### AWS-ORGANIZATIONS-JN-09

- [ ] **Code:** **Question:** What does `aws organizations describe-organization` help you verify for AWS Organizations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: constrain resource-side permissions for supported services within the organization.

### AWS-ORGANIZATIONS-JN-10

- [ ] **Code:** **Question:** What does `aws organizations list-roots` help you verify for AWS Organizations?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: tested emergency access must remain narrow, monitored and independent of a single federation failure.

## Junior — procedural and command questions

### AWS-ORGANIZATIONS-JP-01

- [ ] **Code:** **Question:** A basic Management account check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations describe-organization` and capture exact status/reason/request ID. owns the organization and must be tightly protected rather than used for workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-02

- [ ] **Question:** A basic Member accounts check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations list-roots` and capture exact status/reason/request ID. separate workloads, environments, teams and blast radii with independent quotas and root identities. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-03

- [ ] **Question:** A basic Organizational units check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations list-organizational-units-for-parent --parent-id ROOT_ID` and capture exact status/reason/request ID. group accounts for policy inheritance and lifecycle rather than acting as runtime resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-04

- [ ] **Code:** **Question:** A basic Service Control Policies check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations list-policies-for-target --target-id ACCOUNT_ID --filter SERVICE_CONTROL_POLICY` and capture exact status/reason/request ID. define maximum permissions for member principals but grant no permission. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-05

- [ ] **Question:** A basic Delegated administrator check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations describe-organization` and capture exact status/reason/request ID. lets a security/platform account operate supported organization-wide services. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-06

- [ ] **Question:** A basic Consolidated billing check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations list-roots` and capture exact status/reason/request ID. aggregates charges and commitment sharing while accounts retain usage ownership. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-07

- [ ] **Code:** **Question:** A basic Organization trails/config check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations list-organizational-units-for-parent --parent-id ROOT_ID` and capture exact status/reason/request ID. centralize immutable audit and configuration history outside workload accounts. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-08

- [ ] **Question:** A basic Account vending check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations list-policies-for-target --target-id ACCOUNT_ID --filter SERVICE_CONTROL_POLICY` and capture exact status/reason/request ID. creates standardized accounts with contacts, identity, networks, logs, budgets and owners. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-09

- [ ] **Question:** A basic Resource Control Policies check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations describe-organization` and capture exact status/reason/request ID. constrain resource-side permissions for supported services within the organization. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-ORGANIZATIONS-JP-10

- [ ] **Code:** **Question:** A basic Break-glass check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations list-roots` and capture exact status/reason/request ID. tested emergency access must remain narrow, monitored and independent of a single federation failure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-ORGANIZATIONS-MN-01

- [ ] **Question:** Compare Management account with Member accounts. When would each change your design?

**Answer:** Management account: owns the organization and must be tightly protected rather than used for workloads. Member accounts: separate workloads, environments, teams and blast radii with independent quotas and root identities. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-02

- [ ] **Question:** Compare Member accounts with Organizational units. When would each change your design?

**Answer:** Member accounts: separate workloads, environments, teams and blast radii with independent quotas and root identities. Organizational units: group accounts for policy inheritance and lifecycle rather than acting as runtime resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-03

- [ ] **Question:** Compare Organizational units with Service Control Policies. When would each change your design?

**Answer:** Organizational units: group accounts for policy inheritance and lifecycle rather than acting as runtime resources. Service Control Policies: define maximum permissions for member principals but grant no permission. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-04

- [ ] **Configuration review:** **Question:** Compare Service Control Policies with Delegated administrator. When would each change your design?

**Answer:** Service Control Policies: define maximum permissions for member principals but grant no permission. Delegated administrator: lets a security/platform account operate supported organization-wide services. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-05

- [ ] **Question:** Compare Delegated administrator with Consolidated billing. When would each change your design?

**Answer:** Delegated administrator: lets a security/platform account operate supported organization-wide services. Consolidated billing: aggregates charges and commitment sharing while accounts retain usage ownership. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-06

- [ ] **Question:** Compare Consolidated billing with Organization trails/config. When would each change your design?

**Answer:** Consolidated billing: aggregates charges and commitment sharing while accounts retain usage ownership. Organization trails/config: centralize immutable audit and configuration history outside workload accounts. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-07

- [ ] **Configuration review:** **Question:** Compare Organization trails/config with Account vending. When would each change your design?

**Answer:** Organization trails/config: centralize immutable audit and configuration history outside workload accounts. Account vending: creates standardized accounts with contacts, identity, networks, logs, budgets and owners. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-08

- [ ] **Question:** Compare Account vending with Resource Control Policies. When would each change your design?

**Answer:** Account vending: creates standardized accounts with contacts, identity, networks, logs, budgets and owners. Resource Control Policies: constrain resource-side permissions for supported services within the organization. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-09

- [ ] **Question:** Compare Resource Control Policies with Break-glass. When would each change your design?

**Answer:** Resource Control Policies: constrain resource-side permissions for supported services within the organization. Break-glass: tested emergency access must remain narrow, monitored and independent of a single federation failure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-ORGANIZATIONS-MN-10

- [ ] **Configuration review:** **Question:** Compare Break-glass with Management account. When would each change your design?

**Answer:** Break-glass: tested emergency access must remain narrow, monitored and independent of a single federation failure. Management account: owns the organization and must be tightly protected rather than used for workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-ORGANIZATIONS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Management account; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations describe-organization` plus recent events/changes, then correlate the service-specific SLI. owns the organization and must be tightly protected rather than used for workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-02

- [ ] **Question:** Production is degraded around Member accounts; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations list-roots` plus recent events/changes, then correlate the service-specific SLI. separate workloads, environments, teams and blast radii with independent quotas and root identities. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Organizational units; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations list-organizational-units-for-parent --parent-id ROOT_ID` plus recent events/changes, then correlate the service-specific SLI. group accounts for policy inheritance and lifecycle rather than acting as runtime resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-04

- [ ] **Question:** Production is degraded around Service Control Policies; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations list-policies-for-target --target-id ACCOUNT_ID --filter SERVICE_CONTROL_POLICY` plus recent events/changes, then correlate the service-specific SLI. define maximum permissions for member principals but grant no permission. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Delegated administrator; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations describe-organization` plus recent events/changes, then correlate the service-specific SLI. lets a security/platform account operate supported organization-wide services. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-06

- [ ] **Question:** Production is degraded around Consolidated billing; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations list-roots` plus recent events/changes, then correlate the service-specific SLI. aggregates charges and commitment sharing while accounts retain usage ownership. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Organization trails/config; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations list-organizational-units-for-parent --parent-id ROOT_ID` plus recent events/changes, then correlate the service-specific SLI. centralize immutable audit and configuration history outside workload accounts. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-08

- [ ] **Question:** Production is degraded around Account vending; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations list-policies-for-target --target-id ACCOUNT_ID --filter SERVICE_CONTROL_POLICY` plus recent events/changes, then correlate the service-specific SLI. creates standardized accounts with contacts, identity, networks, logs, budgets and owners. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Resource Control Policies; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations describe-organization` plus recent events/changes, then correlate the service-specific SLI. constrain resource-side permissions for supported services within the organization. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-ORGANIZATIONS-MP-10

- [ ] **Question:** Production is degraded around Break-glass; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations list-roots` plus recent events/changes, then correlate the service-specific SLI. tested emergency access must remain narrow, monitored and independent of a single federation failure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-ORGANIZATIONS-SN-01

- [ ] **Question:** Design a production AWS Organizations capability where Management account, Service Control Policies and Organization trails/config are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owns the organization and must be tightly protected rather than used for workloads. define maximum permissions for member principals but grant no permission. centralize immutable audit and configuration history outside workload accounts. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Organizations capability where Member accounts, Delegated administrator and Account vending are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: separate workloads, environments, teams and blast radii with independent quotas and root identities. lets a security/platform account operate supported organization-wide services. creates standardized accounts with contacts, identity, networks, logs, budgets and owners. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-03

- [ ] **Question:** Design a production AWS Organizations capability where Organizational units, Consolidated billing and Resource Control Policies are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: group accounts for policy inheritance and lifecycle rather than acting as runtime resources. aggregates charges and commitment sharing while accounts retain usage ownership. constrain resource-side permissions for supported services within the organization. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Organizations capability where Service Control Policies, Organization trails/config and Break-glass are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: define maximum permissions for member principals but grant no permission. centralize immutable audit and configuration history outside workload accounts. tested emergency access must remain narrow, monitored and independent of a single federation failure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-05

- [ ] **Question:** Design a production AWS Organizations capability where Delegated administrator, Account vending and Management account are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: lets a security/platform account operate supported organization-wide services. creates standardized accounts with contacts, identity, networks, logs, budgets and owners. owns the organization and must be tightly protected rather than used for workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Organizations capability where Consolidated billing, Resource Control Policies and Member accounts are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: aggregates charges and commitment sharing while accounts retain usage ownership. constrain resource-side permissions for supported services within the organization. separate workloads, environments, teams and blast radii with independent quotas and root identities. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-07

- [ ] **Question:** Design a production AWS Organizations capability where Organization trails/config, Break-glass and Organizational units are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: centralize immutable audit and configuration history outside workload accounts. tested emergency access must remain narrow, monitored and independent of a single federation failure. group accounts for policy inheritance and lifecycle rather than acting as runtime resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Organizations capability where Account vending, Management account and Service Control Policies are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: creates standardized accounts with contacts, identity, networks, logs, budgets and owners. owns the organization and must be tightly protected rather than used for workloads. define maximum permissions for member principals but grant no permission. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-09

- [ ] **Question:** Design a production AWS Organizations capability where Resource Control Policies, Member accounts and Delegated administrator are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: constrain resource-side permissions for supported services within the organization. separate workloads, environments, teams and blast radii with independent quotas and root identities. lets a security/platform account operate supported organization-wide services. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-ORGANIZATIONS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS Organizations capability where Break-glass, Organizational units and Consolidated billing are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tested emergency access must remain narrow, monitored and independent of a single federation failure. group accounts for policy inheritance and lifecycle rather than acting as runtime resources. aggregates charges and commitment sharing while accounts retain usage ownership. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-ORGANIZATIONS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Management account. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations describe-organization` as one read-only checkpoint, not the whole diagnosis. owns the organization and must be tightly protected rather than used for workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Member accounts. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations list-roots` as one read-only checkpoint, not the whole diagnosis. separate workloads, environments, teams and blast radii with independent quotas and root identities. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Organizational units. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations list-organizational-units-for-parent --parent-id ROOT_ID` as one read-only checkpoint, not the whole diagnosis. group accounts for policy inheritance and lifecycle rather than acting as runtime resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service Control Policies. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations list-policies-for-target --target-id ACCOUNT_ID --filter SERVICE_CONTROL_POLICY` as one read-only checkpoint, not the whole diagnosis. define maximum permissions for member principals but grant no permission. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Delegated administrator. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations describe-organization` as one read-only checkpoint, not the whole diagnosis. lets a security/platform account operate supported organization-wide services. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Consolidated billing. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations list-roots` as one read-only checkpoint, not the whole diagnosis. aggregates charges and commitment sharing while accounts retain usage ownership. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Organization trails/config. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations list-organizational-units-for-parent --parent-id ROOT_ID` as one read-only checkpoint, not the whole diagnosis. centralize immutable audit and configuration history outside workload accounts. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Account vending. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations list-policies-for-target --target-id ACCOUNT_ID --filter SERVICE_CONTROL_POLICY` as one read-only checkpoint, not the whole diagnosis. creates standardized accounts with contacts, identity, networks, logs, budgets and owners. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resource Control Policies. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations describe-organization` as one read-only checkpoint, not the whole diagnosis. constrain resource-side permissions for supported services within the organization. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-ORGANIZATIONS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Break-glass. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations list-roots` as one read-only checkpoint, not the whole diagnosis. tested emergency access must remain narrow, monitored and independent of a single federation failure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
