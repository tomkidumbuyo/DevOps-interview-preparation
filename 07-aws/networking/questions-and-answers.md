# Networking — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-NETWORKING-JN-01

- [ ] **Question:** What is VPC CIDR, and why does it matter in Networking?

**Answer:** regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-02

- [ ] **Question:** What is Subnet, and why does it matter in Networking?

**Answer:** AZ-scoped address range whose route table and address behavior determine public/private/isolated use. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-03

- [ ] **Question:** What is Security group state, and why does it matter in Networking?

**Answer:** allowed connections automatically permit tracked return traffic. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-04

- [ ] **Question:** What is Security group reference, and why does it matter in Networking?

**Answer:** supported paths can allow traffic from ENIs associated with another group. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-05

- [ ] **Question:** What is NAT gateway, and why does it matter in Networking?

**Answer:** managed AZ-scoped IPv4 translation with hourly and data-processing cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-06

- [ ] **Question:** What is NAT instance, and why does it matter in Networking?

**Answer:** customer-managed translation with patching, throughput and failover responsibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-07

- [ ] **Question:** What is Gateway endpoint, and why does it matter in Networking?

**Answer:** route-table target for supported services such as S3/DynamoDB without endpoint ENIs. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpcs --vpc-ids VPC_ID` help you verify for Networking?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: PrivateLink ENIs in subnets with security groups and per-hour/data cost.

### BRANCH-NETWORKING-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-security-groups --group-ids SG_ID` help you verify for Networking?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: direct non-transitive connectivity that requires non-overlap and routes on both sides.

### BRANCH-NETWORKING-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-nat-gateways` help you verify for Networking?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: connect VPC, VPN, Direct Connect gateway or peering into a routed hub.

## Junior — procedural and command questions

### BRANCH-NETWORKING-JP-01

- [ ] **Code:** **Question:** A basic VPC CIDR check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpcs --vpc-ids VPC_ID` and capture exact status/reason/request ID. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-02

- [ ] **Question:** A basic Subnet check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-security-groups --group-ids SG_ID` and capture exact status/reason/request ID. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-03

- [ ] **Question:** A basic Security group state check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-nat-gateways` and capture exact status/reason/request ID. allowed connections automatically permit tracked return traffic. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-04

- [ ] **Code:** **Question:** A basic Security group reference check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. supported paths can allow traffic from ENIs associated with another group. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-05

- [ ] **Question:** A basic NAT gateway check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-peering-connections` and capture exact status/reason/request ID. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-06

- [ ] **Question:** A basic NAT instance check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpn-connections` and capture exact status/reason/request ID. customer-managed translation with patching, throughput and failover responsibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-07

- [ ] **Code:** **Question:** A basic Gateway endpoint check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53 list-hosted-zones` and capture exact status/reason/request ID. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-08

- [ ] **Question:** A basic Interface endpoint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpcs --vpc-ids VPC_ID` and capture exact status/reason/request ID. PrivateLink ENIs in subnets with security groups and per-hour/data cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-09

- [ ] **Question:** A basic VPC peering check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-security-groups --group-ids SG_ID` and capture exact status/reason/request ID. direct non-transitive connectivity that requires non-overlap and routes on both sides. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-10

- [ ] **Code:** **Question:** A basic Transit Gateway attachments check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-nat-gateways` and capture exact status/reason/request ID. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-NETWORKING-MN-01

- [ ] **Question:** Compare VPC CIDR with Subnet. When would each change your design?

**Answer:** VPC CIDR: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Subnet: AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-02

- [ ] **Question:** Compare Subnet with Security group state. When would each change your design?

**Answer:** Subnet: AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Security group state: allowed connections automatically permit tracked return traffic. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-03

- [ ] **Question:** Compare Security group state with Security group reference. When would each change your design?

**Answer:** Security group state: allowed connections automatically permit tracked return traffic. Security group reference: supported paths can allow traffic from ENIs associated with another group. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-04

- [ ] **Configuration review:** **Question:** Compare Security group reference with NAT gateway. When would each change your design?

**Answer:** Security group reference: supported paths can allow traffic from ENIs associated with another group. NAT gateway: managed AZ-scoped IPv4 translation with hourly and data-processing cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-05

- [ ] **Question:** Compare NAT gateway with NAT instance. When would each change your design?

**Answer:** NAT gateway: managed AZ-scoped IPv4 translation with hourly and data-processing cost. NAT instance: customer-managed translation with patching, throughput and failover responsibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-06

- [ ] **Question:** Compare NAT instance with Gateway endpoint. When would each change your design?

**Answer:** NAT instance: customer-managed translation with patching, throughput and failover responsibility. Gateway endpoint: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-07

- [ ] **Configuration review:** **Question:** Compare Gateway endpoint with Interface endpoint. When would each change your design?

**Answer:** Gateway endpoint: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Interface endpoint: PrivateLink ENIs in subnets with security groups and per-hour/data cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-08

- [ ] **Question:** Compare Interface endpoint with VPC peering. When would each change your design?

**Answer:** Interface endpoint: PrivateLink ENIs in subnets with security groups and per-hour/data cost. VPC peering: direct non-transitive connectivity that requires non-overlap and routes on both sides. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-09

- [ ] **Question:** Compare VPC peering with Transit Gateway attachments. When would each change your design?

**Answer:** VPC peering: direct non-transitive connectivity that requires non-overlap and routes on both sides. Transit Gateway attachments: connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-10

- [ ] **Configuration review:** **Question:** Compare Transit Gateway attachments with VPC CIDR. When would each change your design?

**Answer:** Transit Gateway attachments: connect VPC, VPN, Direct Connect gateway or peering into a routed hub. VPC CIDR: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-NETWORKING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC CIDR; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpcs --vpc-ids VPC_ID` plus recent events/changes, then correlate the service-specific SLI. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-02

- [ ] **Question:** Production is degraded around Subnet; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-security-groups --group-ids SG_ID` plus recent events/changes, then correlate the service-specific SLI. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Security group state; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-nat-gateways` plus recent events/changes, then correlate the service-specific SLI. allowed connections automatically permit tracked return traffic. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-04

- [ ] **Question:** Production is degraded around Security group reference; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. supported paths can allow traffic from ENIs associated with another group. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around NAT gateway; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-peering-connections` plus recent events/changes, then correlate the service-specific SLI. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-06

- [ ] **Question:** Production is degraded around NAT instance; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpn-connections` plus recent events/changes, then correlate the service-specific SLI. customer-managed translation with patching, throughput and failover responsibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Gateway endpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53 list-hosted-zones` plus recent events/changes, then correlate the service-specific SLI. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-08

- [ ] **Question:** Production is degraded around Interface endpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpcs --vpc-ids VPC_ID` plus recent events/changes, then correlate the service-specific SLI. PrivateLink ENIs in subnets with security groups and per-hour/data cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC peering; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-security-groups --group-ids SG_ID` plus recent events/changes, then correlate the service-specific SLI. direct non-transitive connectivity that requires non-overlap and routes on both sides. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-10

- [ ] **Question:** Production is degraded around Transit Gateway attachments; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-nat-gateways` plus recent events/changes, then correlate the service-specific SLI. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-NETWORKING-SN-01

- [ ] **Question:** Design a production Networking capability where VPC CIDR, Security group reference and Gateway endpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. supported paths can allow traffic from ENIs associated with another group. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Subnet, NAT gateway and Interface endpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AZ-scoped address range whose route table and address behavior determine public/private/isolated use. managed AZ-scoped IPv4 translation with hourly and data-processing cost. PrivateLink ENIs in subnets with security groups and per-hour/data cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-03

- [ ] **Question:** Design a production Networking capability where Security group state, NAT instance and VPC peering are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: allowed connections automatically permit tracked return traffic. customer-managed translation with patching, throughput and failover responsibility. direct non-transitive connectivity that requires non-overlap and routes on both sides. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Security group reference, Gateway endpoint and Transit Gateway attachments are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: supported paths can allow traffic from ENIs associated with another group. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-05

- [ ] **Question:** Design a production Networking capability where NAT gateway, Interface endpoint and VPC CIDR are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed AZ-scoped IPv4 translation with hourly and data-processing cost. PrivateLink ENIs in subnets with security groups and per-hour/data cost. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where NAT instance, VPC peering and Subnet are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: customer-managed translation with patching, throughput and failover responsibility. direct non-transitive connectivity that requires non-overlap and routes on both sides. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-07

- [ ] **Question:** Design a production Networking capability where Gateway endpoint, Transit Gateway attachments and Security group state are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: route-table target for supported services such as S3/DynamoDB without endpoint ENIs. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. allowed connections automatically permit tracked return traffic. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Interface endpoint, VPC CIDR and Security group reference are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: PrivateLink ENIs in subnets with security groups and per-hour/data cost. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. supported paths can allow traffic from ENIs associated with another group. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-09

- [ ] **Question:** Design a production Networking capability where VPC peering, Subnet and NAT gateway are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: direct non-transitive connectivity that requires non-overlap and routes on both sides. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Transit Gateway attachments, Security group state and NAT instance are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: connect VPC, VPN, Direct Connect gateway or peering into a routed hub. allowed connections automatically permit tracked return traffic. customer-managed translation with patching, throughput and failover responsibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-NETWORKING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC CIDR. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpcs --vpc-ids VPC_ID` as one read-only checkpoint, not the whole diagnosis. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Subnet. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-security-groups --group-ids SG_ID` as one read-only checkpoint, not the whole diagnosis. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Security group state. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-nat-gateways` as one read-only checkpoint, not the whole diagnosis. allowed connections automatically permit tracked return traffic. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Security group reference. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. supported paths can allow traffic from ENIs associated with another group. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NAT gateway. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-peering-connections` as one read-only checkpoint, not the whole diagnosis. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NAT instance. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpn-connections` as one read-only checkpoint, not the whole diagnosis. customer-managed translation with patching, throughput and failover responsibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Gateway endpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53 list-hosted-zones` as one read-only checkpoint, not the whole diagnosis. route-table target for supported services such as S3/DynamoDB without endpoint ENIs. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Interface endpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpcs --vpc-ids VPC_ID` as one read-only checkpoint, not the whole diagnosis. PrivateLink ENIs in subnets with security groups and per-hour/data cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC peering. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-security-groups --group-ids SG_ID` as one read-only checkpoint, not the whole diagnosis. direct non-transitive connectivity that requires non-overlap and routes on both sides. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Transit Gateway attachments. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-nat-gateways` as one read-only checkpoint, not the whole diagnosis. connect VPC, VPN, Direct Connect gateway or peering into a routed hub. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
