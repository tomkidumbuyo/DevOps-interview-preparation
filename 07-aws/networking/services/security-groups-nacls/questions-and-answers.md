# Security groups and network ACLs — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-01

- [ ] **Question:** What is Security group state, and why does it matter in Security groups and network ACLs?

**Answer:** allowed connections automatically permit tracked return traffic. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-02

- [ ] **Question:** What is Security group reference, and why does it matter in Security groups and network ACLs?

**Answer:** supported paths can allow traffic from ENIs associated with another group. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-03

- [ ] **Question:** What is Outbound rules, and why does it matter in Security groups and network ACLs?

**Answer:** restrict initiated egress and influence return assumptions only through stateful tracking. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-04

- [ ] **Question:** What is NACL ordering, and why does it matter in Security groups and network ACLs?

**Answer:** lowest numbered matching allow/deny rule wins. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-05

- [ ] **Question:** What is NACL statelessness, and why does it matter in Security groups and network ACLs?

**Answer:** return traffic and ephemeral ports require explicit rules in both directions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-06

- [ ] **Question:** What is Default groups/ACLs, and why does it matter in Security groups and network ACLs?

**Answer:** defaults may be broad and should not become undocumented production policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-07

- [ ] **Question:** What is Ephemeral ports, and why does it matter in Security groups and network ACLs?

**Answer:** client operating systems choose source ports that stateless rules must accommodate. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 describe-flow-logs` help you verify for Security groups and network ACLs?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: excessive per-tenant rules can hit limits and slow operations.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-security-groups --group-ids SG_ID` help you verify for Security groups and network ACLs?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: allow the exact source/destination/protocol/port and document owner/purpose.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-network-acls --network-acl-ids ACL_ID` help you verify for Security groups and network ACLs?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure.

## Junior — procedural and command questions

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-01

- [ ] **Code:** **Question:** A basic Security group state check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-security-groups --group-ids SG_ID` and capture exact status/reason/request ID. allowed connections automatically permit tracked return traffic. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-02

- [ ] **Question:** A basic Security group reference check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-network-acls --network-acl-ids ACL_ID` and capture exact status/reason/request ID. supported paths can allow traffic from ENIs associated with another group. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-03

- [ ] **Question:** A basic Outbound rules check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-network-interfaces --filters Name=group-id,Values=SG_ID` and capture exact status/reason/request ID. restrict initiated egress and influence return assumptions only through stateful tracking. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-04

- [ ] **Code:** **Question:** A basic NACL ordering check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-flow-logs` and capture exact status/reason/request ID. lowest numbered matching allow/deny rule wins. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-05

- [ ] **Question:** A basic NACL statelessness check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-security-groups --group-ids SG_ID` and capture exact status/reason/request ID. return traffic and ephemeral ports require explicit rules in both directions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-06

- [ ] **Question:** A basic Default groups/ACLs check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-network-acls --network-acl-ids ACL_ID` and capture exact status/reason/request ID. defaults may be broad and should not become undocumented production policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-07

- [ ] **Code:** **Question:** A basic Ephemeral ports check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-network-interfaces --filters Name=group-id,Values=SG_ID` and capture exact status/reason/request ID. client operating systems choose source ports that stateless rules must accommodate. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-08

- [ ] **Question:** A basic Rule quotas check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-flow-logs` and capture exact status/reason/request ID. excessive per-tenant rules can hit limits and slow operations. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-09

- [ ] **Question:** A basic Least-path access check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-security-groups --group-ids SG_ID` and capture exact status/reason/request ID. allow the exact source/destination/protocol/port and document owner/purpose. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### SECURITY-GROUPS-AND-NETWORK-ACLS-JP-10

- [ ] **Code:** **Question:** A basic Flow evidence check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-network-acls --network-acl-ids ACL_ID` and capture exact status/reason/request ID. rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-01

- [ ] **Question:** Compare Security group state with Security group reference. When would each change your design?

**Answer:** Security group state: allowed connections automatically permit tracked return traffic. Security group reference: supported paths can allow traffic from ENIs associated with another group. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-02

- [ ] **Question:** Compare Security group reference with Outbound rules. When would each change your design?

**Answer:** Security group reference: supported paths can allow traffic from ENIs associated with another group. Outbound rules: restrict initiated egress and influence return assumptions only through stateful tracking. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-03

- [ ] **Question:** Compare Outbound rules with NACL ordering. When would each change your design?

**Answer:** Outbound rules: restrict initiated egress and influence return assumptions only through stateful tracking. NACL ordering: lowest numbered matching allow/deny rule wins. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-04

- [ ] **Configuration review:** **Question:** Compare NACL ordering with NACL statelessness. When would each change your design?

**Answer:** NACL ordering: lowest numbered matching allow/deny rule wins. NACL statelessness: return traffic and ephemeral ports require explicit rules in both directions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-05

- [ ] **Question:** Compare NACL statelessness with Default groups/ACLs. When would each change your design?

**Answer:** NACL statelessness: return traffic and ephemeral ports require explicit rules in both directions. Default groups/ACLs: defaults may be broad and should not become undocumented production policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-06

- [ ] **Question:** Compare Default groups/ACLs with Ephemeral ports. When would each change your design?

**Answer:** Default groups/ACLs: defaults may be broad and should not become undocumented production policy. Ephemeral ports: client operating systems choose source ports that stateless rules must accommodate. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-07

- [ ] **Configuration review:** **Question:** Compare Ephemeral ports with Rule quotas. When would each change your design?

**Answer:** Ephemeral ports: client operating systems choose source ports that stateless rules must accommodate. Rule quotas: excessive per-tenant rules can hit limits and slow operations. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-08

- [ ] **Question:** Compare Rule quotas with Least-path access. When would each change your design?

**Answer:** Rule quotas: excessive per-tenant rules can hit limits and slow operations. Least-path access: allow the exact source/destination/protocol/port and document owner/purpose. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-09

- [ ] **Question:** Compare Least-path access with Flow evidence. When would each change your design?

**Answer:** Least-path access: allow the exact source/destination/protocol/port and document owner/purpose. Flow evidence: rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MN-10

- [ ] **Configuration review:** **Question:** Compare Flow evidence with Security group state. When would each change your design?

**Answer:** Flow evidence: rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure. Security group state: allowed connections automatically permit tracked return traffic. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Security group state; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-security-groups --group-ids SG_ID` plus recent events/changes, then correlate the service-specific SLI. allowed connections automatically permit tracked return traffic. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-02

- [ ] **Question:** Production is degraded around Security group reference; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-network-acls --network-acl-ids ACL_ID` plus recent events/changes, then correlate the service-specific SLI. supported paths can allow traffic from ENIs associated with another group. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Outbound rules; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-network-interfaces --filters Name=group-id,Values=SG_ID` plus recent events/changes, then correlate the service-specific SLI. restrict initiated egress and influence return assumptions only through stateful tracking. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-04

- [ ] **Question:** Production is degraded around NACL ordering; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-flow-logs` plus recent events/changes, then correlate the service-specific SLI. lowest numbered matching allow/deny rule wins. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around NACL statelessness; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-security-groups --group-ids SG_ID` plus recent events/changes, then correlate the service-specific SLI. return traffic and ephemeral ports require explicit rules in both directions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-06

- [ ] **Question:** Production is degraded around Default groups/ACLs; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-network-acls --network-acl-ids ACL_ID` plus recent events/changes, then correlate the service-specific SLI. defaults may be broad and should not become undocumented production policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Ephemeral ports; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-network-interfaces --filters Name=group-id,Values=SG_ID` plus recent events/changes, then correlate the service-specific SLI. client operating systems choose source ports that stateless rules must accommodate. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-08

- [ ] **Question:** Production is degraded around Rule quotas; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-flow-logs` plus recent events/changes, then correlate the service-specific SLI. excessive per-tenant rules can hit limits and slow operations. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Least-path access; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-security-groups --group-ids SG_ID` plus recent events/changes, then correlate the service-specific SLI. allow the exact source/destination/protocol/port and document owner/purpose. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### SECURITY-GROUPS-AND-NETWORK-ACLS-MP-10

- [ ] **Question:** Production is degraded around Flow evidence; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-network-acls --network-acl-ids ACL_ID` plus recent events/changes, then correlate the service-specific SLI. rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-01

- [ ] **Question:** Design a production Security groups and network ACLs capability where Security group state, NACL ordering and Ephemeral ports are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: allowed connections automatically permit tracked return traffic. lowest numbered matching allow/deny rule wins. client operating systems choose source ports that stateless rules must accommodate. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Security groups and network ACLs capability where Security group reference, NACL statelessness and Rule quotas are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported paths can allow traffic from ENIs associated with another group. return traffic and ephemeral ports require explicit rules in both directions. excessive per-tenant rules can hit limits and slow operations. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-03

- [ ] **Question:** Design a production Security groups and network ACLs capability where Outbound rules, Default groups/ACLs and Least-path access are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: restrict initiated egress and influence return assumptions only through stateful tracking. defaults may be broad and should not become undocumented production policy. allow the exact source/destination/protocol/port and document owner/purpose. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Security groups and network ACLs capability where NACL ordering, Ephemeral ports and Flow evidence are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: lowest numbered matching allow/deny rule wins. client operating systems choose source ports that stateless rules must accommodate. rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-05

- [ ] **Question:** Design a production Security groups and network ACLs capability where NACL statelessness, Rule quotas and Security group state are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: return traffic and ephemeral ports require explicit rules in both directions. excessive per-tenant rules can hit limits and slow operations. allowed connections automatically permit tracked return traffic. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Security groups and network ACLs capability where Default groups/ACLs, Least-path access and Security group reference are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: defaults may be broad and should not become undocumented production policy. allow the exact source/destination/protocol/port and document owner/purpose. supported paths can allow traffic from ENIs associated with another group. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-07

- [ ] **Question:** Design a production Security groups and network ACLs capability where Ephemeral ports, Flow evidence and Outbound rules are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: client operating systems choose source ports that stateless rules must accommodate. rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure. restrict initiated egress and influence return assumptions only through stateful tracking. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Security groups and network ACLs capability where Rule quotas, Security group state and NACL ordering are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: excessive per-tenant rules can hit limits and slow operations. allowed connections automatically permit tracked return traffic. lowest numbered matching allow/deny rule wins. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-09

- [ ] **Question:** Design a production Security groups and network ACLs capability where Least-path access, Security group reference and NACL statelessness are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: allow the exact source/destination/protocol/port and document owner/purpose. supported paths can allow traffic from ENIs associated with another group. return traffic and ephemeral ports require explicit rules in both directions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Security groups and network ACLs capability where Flow evidence, Outbound rules and Default groups/ACLs are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure. restrict initiated egress and influence return assumptions only through stateful tracking. defaults may be broad and should not become undocumented production policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Security group state. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-security-groups --group-ids SG_ID` as one read-only checkpoint, not the whole diagnosis. allowed connections automatically permit tracked return traffic. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Security group reference. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-network-acls --network-acl-ids ACL_ID` as one read-only checkpoint, not the whole diagnosis. supported paths can allow traffic from ENIs associated with another group. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Outbound rules. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-network-interfaces --filters Name=group-id,Values=SG_ID` as one read-only checkpoint, not the whole diagnosis. restrict initiated egress and influence return assumptions only through stateful tracking. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NACL ordering. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-flow-logs` as one read-only checkpoint, not the whole diagnosis. lowest numbered matching allow/deny rule wins. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NACL statelessness. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-security-groups --group-ids SG_ID` as one read-only checkpoint, not the whole diagnosis. return traffic and ephemeral ports require explicit rules in both directions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Default groups/ACLs. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-network-acls --network-acl-ids ACL_ID` as one read-only checkpoint, not the whole diagnosis. defaults may be broad and should not become undocumented production policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ephemeral ports. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-network-interfaces --filters Name=group-id,Values=SG_ID` as one read-only checkpoint, not the whole diagnosis. client operating systems choose source ports that stateless rules must accommodate. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Rule quotas. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-flow-logs` as one read-only checkpoint, not the whole diagnosis. excessive per-tenant rules can hit limits and slow operations. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Least-path access. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-security-groups --group-ids SG_ID` as one read-only checkpoint, not the whole diagnosis. allow the exact source/destination/protocol/port and document owner/purpose. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### SECURITY-GROUPS-AND-NETWORK-ACLS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Flow evidence. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-network-acls --network-acl-ids ACL_ID` as one read-only checkpoint, not the whole diagnosis. rejected flow logs, Reachability Analyzer and packet capture distinguish policy from listener failure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
