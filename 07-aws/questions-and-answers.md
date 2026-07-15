# 07 Aws — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-07-AWS-JN-01

- [ ] **Question:** What is Principals, and why does it matter in 07 Aws?

**Answer:** users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-07-AWS-JN-02

- [ ] **Question:** What is Management account, and why does it matter in 07 Aws?

**Answer:** owns the organization and must be tightly protected rather than used for workloads. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-07-AWS-JN-03

- [ ] **Question:** What is AssumeRole, and why does it matter in 07 Aws?

**Answer:** exchanges an authenticated caller for temporary role credentials subject to trust and permissions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-07-AWS-JN-04

- [ ] **Question:** What is Landing zone, and why does it matter in 07 Aws?

**Answer:** standardized multi-account identity, logging, security and network foundation. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-07-AWS-JN-05

- [ ] **Question:** What is VPC CIDR, and why does it matter in 07 Aws?

**Answer:** regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-07-AWS-JN-06

- [ ] **Question:** What is Security group state, and why does it matter in 07 Aws?

**Answer:** allowed connections automatically permit tracked return traffic. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-07-AWS-JN-07

- [ ] **Question:** What is NAT gateway, and why does it matter in 07 Aws?

**Answer:** managed AZ-scoped IPv4 translation with hourly and data-processing cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-07-AWS-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` help you verify for 07 Aws?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: route-table target for supported services such as S3/DynamoDB without endpoint ENIs.

### BRANCH-07-AWS-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpc-peering-connections` help you verify for 07 Aws?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: direct non-transitive connectivity that requires non-overlap and routes on both sides.

### BRANCH-07-AWS-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpn-connections` help you verify for 07 Aws?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: redundant IPsec tunnels provide encrypted connectivity over public paths.

## Junior — procedural and command questions

### BRANCH-07-AWS-JP-01

- [ ] **Code:** **Question:** A basic Principals check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts get-caller-identity` and capture exact status/reason/request ID. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-02

- [ ] **Question:** A basic Management account check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws organizations describe-organization` and capture exact status/reason/request ID. owns the organization and must be tightly protected rather than used for workloads. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-03

- [ ] **Question:** A basic AssumeRole check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` and capture exact status/reason/request ID. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-04

- [ ] **Code:** **Question:** A basic Landing zone check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws controltower list-enabled-controls --target-identifier OU_ARN` and capture exact status/reason/request ID. standardized multi-account identity, logging, security and network foundation. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-05

- [ ] **Question:** A basic VPC CIDR check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpcs --vpc-ids VPC_ID` and capture exact status/reason/request ID. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-06

- [ ] **Question:** A basic Security group state check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-security-groups --group-ids SG_ID` and capture exact status/reason/request ID. allowed connections automatically permit tracked return traffic. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-07

- [ ] **Code:** **Question:** A basic NAT gateway check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-nat-gateways` and capture exact status/reason/request ID. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-08

- [ ] **Question:** A basic Gateway endpoint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-09

- [ ] **Question:** A basic VPC peering check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-peering-connections` and capture exact status/reason/request ID. direct non-transitive connectivity that requires non-overlap and routes on both sides. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-07-AWS-JP-10

- [ ] **Code:** **Question:** A basic Site-to-Site VPN check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpn-connections` and capture exact status/reason/request ID. redundant IPsec tunnels provide encrypted connectivity over public paths. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-07-AWS-MN-01

- [ ] **Question:** Compare Principals with Management account. When would each change your design?

**Answer:** Principals: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Management account: owns the organization and must be tightly protected rather than used for workloads. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-02

- [ ] **Question:** Compare Management account with AssumeRole. When would each change your design?

**Answer:** Management account: owns the organization and must be tightly protected rather than used for workloads. AssumeRole: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-03

- [ ] **Question:** Compare AssumeRole with Landing zone. When would each change your design?

**Answer:** AssumeRole: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Landing zone: standardized multi-account identity, logging, security and network foundation. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-04

- [ ] **Configuration review:** **Question:** Compare Landing zone with VPC CIDR. When would each change your design?

**Answer:** Landing zone: standardized multi-account identity, logging, security and network foundation. VPC CIDR: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-05

- [ ] **Question:** Compare VPC CIDR with Security group state. When would each change your design?

**Answer:** VPC CIDR: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Security group state: allowed connections automatically permit tracked return traffic. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-06

- [ ] **Question:** Compare Security group state with NAT gateway. When would each change your design?

**Answer:** Security group state: allowed connections automatically permit tracked return traffic. NAT gateway: managed AZ-scoped IPv4 translation with hourly and data-processing cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-07

- [ ] **Configuration review:** **Question:** Compare NAT gateway with Gateway endpoint. When would each change your design?

**Answer:** NAT gateway: managed AZ-scoped IPv4 translation with hourly and data-processing cost. Gateway endpoint: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-08

- [ ] **Question:** Compare Gateway endpoint with VPC peering. When would each change your design?

**Answer:** Gateway endpoint: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. VPC peering: direct non-transitive connectivity that requires non-overlap and routes on both sides. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-09

- [ ] **Question:** Compare VPC peering with Site-to-Site VPN. When would each change your design?

**Answer:** VPC peering: direct non-transitive connectivity that requires non-overlap and routes on both sides. Site-to-Site VPN: redundant IPsec tunnels provide encrypted connectivity over public paths. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-07-AWS-MN-10

- [ ] **Configuration review:** **Question:** Compare Site-to-Site VPN with Principals. When would each change your design?

**Answer:** Site-to-Site VPN: redundant IPsec tunnels provide encrypted connectivity over public paths. Principals: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-07-AWS-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Principals; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts get-caller-identity` plus recent events/changes, then correlate the service-specific SLI. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-02

- [ ] **Question:** Production is degraded around Management account; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws organizations describe-organization` plus recent events/changes, then correlate the service-specific SLI. owns the organization and must be tightly protected rather than used for workloads. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around AssumeRole; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` plus recent events/changes, then correlate the service-specific SLI. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-04

- [ ] **Question:** Production is degraded around Landing zone; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws controltower list-enabled-controls --target-identifier OU_ARN` plus recent events/changes, then correlate the service-specific SLI. standardized multi-account identity, logging, security and network foundation. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC CIDR; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpcs --vpc-ids VPC_ID` plus recent events/changes, then correlate the service-specific SLI. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-06

- [ ] **Question:** Production is degraded around Security group state; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-security-groups --group-ids SG_ID` plus recent events/changes, then correlate the service-specific SLI. allowed connections automatically permit tracked return traffic. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around NAT gateway; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-nat-gateways` plus recent events/changes, then correlate the service-specific SLI. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-08

- [ ] **Question:** Production is degraded around Gateway endpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC peering; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-peering-connections` plus recent events/changes, then correlate the service-specific SLI. direct non-transitive connectivity that requires non-overlap and routes on both sides. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-07-AWS-MP-10

- [ ] **Question:** Production is degraded around Site-to-Site VPN; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpn-connections` plus recent events/changes, then correlate the service-specific SLI. redundant IPsec tunnels provide encrypted connectivity over public paths. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-07-AWS-SN-01

- [ ] **Question:** Design a production 07 Aws capability where Principals, Landing zone and NAT gateway are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. standardized multi-account identity, logging, security and network foundation. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production 07 Aws capability where Management account, VPC CIDR and Gateway endpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: owns the organization and must be tightly protected rather than used for workloads. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-03

- [ ] **Question:** Design a production 07 Aws capability where AssumeRole, Security group state and VPC peering are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exchanges an authenticated caller for temporary role credentials subject to trust and permissions. allowed connections automatically permit tracked return traffic. direct non-transitive connectivity that requires non-overlap and routes on both sides. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production 07 Aws capability where Landing zone, NAT gateway and Site-to-Site VPN are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: standardized multi-account identity, logging, security and network foundation. managed AZ-scoped IPv4 translation with hourly and data-processing cost. redundant IPsec tunnels provide encrypted connectivity over public paths. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-05

- [ ] **Question:** Design a production 07 Aws capability where VPC CIDR, Gateway endpoint and Principals are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production 07 Aws capability where Security group state, VPC peering and Management account are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: allowed connections automatically permit tracked return traffic. direct non-transitive connectivity that requires non-overlap and routes on both sides. owns the organization and must be tightly protected rather than used for workloads. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-07

- [ ] **Question:** Design a production 07 Aws capability where NAT gateway, Site-to-Site VPN and AssumeRole are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed AZ-scoped IPv4 translation with hourly and data-processing cost. redundant IPsec tunnels provide encrypted connectivity over public paths. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production 07 Aws capability where Gateway endpoint, Principals and Landing zone are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. standardized multi-account identity, logging, security and network foundation. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-09

- [ ] **Question:** Design a production 07 Aws capability where VPC peering, Management account and VPC CIDR are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: direct non-transitive connectivity that requires non-overlap and routes on both sides. owns the organization and must be tightly protected rather than used for workloads. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-07-AWS-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production 07 Aws capability where Site-to-Site VPN, AssumeRole and Security group state are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: redundant IPsec tunnels provide encrypted connectivity over public paths. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. allowed connections automatically permit tracked return traffic. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-07-AWS-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Principals. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts get-caller-identity` as one read-only checkpoint, not the whole diagnosis. users, roles, sessions, federated identities and AWS services can make requests under different identity lifecycles. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Management account. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws organizations describe-organization` as one read-only checkpoint, not the whole diagnosis. owns the organization and must be tightly protected rather than used for workloads. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving AssumeRole. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws sts assume-role --role-arn ROLE_ARN --role-session-name NAME` as one read-only checkpoint, not the whole diagnosis. exchanges an authenticated caller for temporary role credentials subject to trust and permissions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Landing zone. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws controltower list-enabled-controls --target-identifier OU_ARN` as one read-only checkpoint, not the whole diagnosis. standardized multi-account identity, logging, security and network foundation. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC CIDR. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpcs --vpc-ids VPC_ID` as one read-only checkpoint, not the whole diagnosis. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Security group state. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-security-groups --group-ids SG_ID` as one read-only checkpoint, not the whole diagnosis. allowed connections automatically permit tracked return traffic. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NAT gateway. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-nat-gateways` as one read-only checkpoint, not the whole diagnosis. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Gateway endpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC peering. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-peering-connections` as one read-only checkpoint, not the whole diagnosis. direct non-transitive connectivity that requires non-overlap and routes on both sides. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-07-AWS-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Site-to-Site VPN. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpn-connections` as one read-only checkpoint, not the whole diagnosis. redundant IPsec tunnels provide encrypted connectivity over public paths. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
