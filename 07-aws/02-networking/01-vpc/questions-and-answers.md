# Amazon VPC — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-VPC-JN-01

- [ ] **Question:** What is VPC CIDR, and why does it matter in Amazon VPC?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-VPC-JN-02

- [ ] **Question:** What is Subnet, and why does it matter in Amazon VPC?
> **Covered in:** [Amazon VPC — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** AZ-scoped address range whose route table and address behavior determine public/private/isolated use. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-VPC-JN-03

- [ ] **Question:** What is Route table, and why does it matter in Amazon VPC?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-VPC-JN-04

- [ ] **Question:** What is Internet gateway, and why does it matter in Amazon VPC?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** VPC edge target that supports public internet routing for appropriately addressed resources. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-VPC-JN-05

- [ ] **Question:** What is Egress-only internet gateway, and why does it matter in Amazon VPC?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** permits initiated IPv6 egress while blocking unsolicited inbound routing. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-VPC-JN-06

- [ ] **Question:** What is ENI, and why does it matter in Amazon VPC?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** carries addresses, security groups and attachment state for compute and managed-service data planes. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-VPC-JN-07

- [ ] **Question:** What is IPAM, and why does it matter in Amazon VPC?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** plans, allocates and audits address space across accounts/Regions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-VPC-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 start-network-insights-analysis --network-insights-path-id PATH_ID` help you verify for Amazon VPC?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: influence resolver/domain/NTP settings delivered to instances.

### AMAZON-VPC-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpcs --vpc-ids VPC_ID` help you verify for Amazon VPC?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: capture accepted/rejected flow metadata, not packet payload or every application event.

### AMAZON-VPC-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` help you verify for Amazon VPC?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: evaluates configured network path models and complements runtime packet evidence.

## Junior — procedural and command questions

### AMAZON-VPC-JP-01

- [ ] **Code:** **Question:** A basic VPC CIDR check fails. What would you do first using the CLI?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpcs --vpc-ids VPC_ID` and capture exact status/reason/request ID. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-02

- [ ] **Question:** A basic Subnet check fails. What would you do first?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-03

- [ ] **Question:** A basic Route table check fails. What would you do first?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-route-tables --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-04

- [ ] **Code:** **Question:** A basic Internet gateway check fails. What would you do first using the CLI?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 start-network-insights-analysis --network-insights-path-id PATH_ID` and capture exact status/reason/request ID. VPC edge target that supports public internet routing for appropriately addressed resources. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-05

- [ ] **Question:** A basic Egress-only internet gateway check fails. What would you do first?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpcs --vpc-ids VPC_ID` and capture exact status/reason/request ID. permits initiated IPv6 egress while blocking unsolicited inbound routing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-06

- [ ] **Question:** A basic ENI check fails. What would you do first?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. carries addresses, security groups and attachment state for compute and managed-service data planes. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-07

- [ ] **Code:** **Question:** A basic IPAM check fails. What would you do first using the CLI?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-route-tables --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. plans, allocates and audits address space across accounts/Regions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-08

- [ ] **Question:** A basic DHCP options check fails. What would you do first?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 start-network-insights-analysis --network-insights-path-id PATH_ID` and capture exact status/reason/request ID. influence resolver/domain/NTP settings delivered to instances. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-09

- [ ] **Question:** A basic VPC Flow Logs check fails. What would you do first?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpcs --vpc-ids VPC_ID` and capture exact status/reason/request ID. capture accepted/rejected flow metadata, not packet payload or every application event. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-VPC-JP-10

- [ ] **Code:** **Question:** A basic Reachability Analyzer check fails. What would you do first using the CLI?
> **Covered in:** [Amazon VPC — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` and capture exact status/reason/request ID. evaluates configured network path models and complements runtime packet evidence. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-VPC-MN-01

- [ ] **Question:** Compare VPC CIDR with Subnet. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** VPC CIDR: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Subnet: AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-02

- [ ] **Question:** Compare Subnet with Route table. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Subnet: AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Route table: longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-03

- [ ] **Question:** Compare Route table with Internet gateway. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Route table: longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. Internet gateway: VPC edge target that supports public internet routing for appropriately addressed resources. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-04

- [ ] **Configuration review:** **Question:** Compare Internet gateway with Egress-only internet gateway. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Internet gateway: VPC edge target that supports public internet routing for appropriately addressed resources. Egress-only internet gateway: permits initiated IPv6 egress while blocking unsolicited inbound routing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-05

- [ ] **Question:** Compare Egress-only internet gateway with ENI. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Egress-only internet gateway: permits initiated IPv6 egress while blocking unsolicited inbound routing. ENI: carries addresses, security groups and attachment state for compute and managed-service data planes. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-06

- [ ] **Question:** Compare ENI with IPAM. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ENI: carries addresses, security groups and attachment state for compute and managed-service data planes. IPAM: plans, allocates and audits address space across accounts/Regions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-07

- [ ] **Configuration review:** **Question:** Compare IPAM with DHCP options. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** IPAM: plans, allocates and audits address space across accounts/Regions. DHCP options: influence resolver/domain/NTP settings delivered to instances. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-08

- [ ] **Question:** Compare DHCP options with VPC Flow Logs. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DHCP options: influence resolver/domain/NTP settings delivered to instances. VPC Flow Logs: capture accepted/rejected flow metadata, not packet payload or every application event. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-09

- [ ] **Question:** Compare VPC Flow Logs with Reachability Analyzer. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** VPC Flow Logs: capture accepted/rejected flow metadata, not packet payload or every application event. Reachability Analyzer: evaluates configured network path models and complements runtime packet evidence. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-VPC-MN-10

- [ ] **Configuration review:** **Question:** Compare Reachability Analyzer with VPC CIDR. When would each change your design?
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Reachability Analyzer: evaluates configured network path models and complements runtime packet evidence. VPC CIDR: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-VPC-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC CIDR; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpcs --vpc-ids VPC_ID` plus recent events/changes, then correlate the service-specific SLI. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-02

- [ ] **Question:** Production is degraded around Subnet; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Route table; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-route-tables --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-04

- [ ] **Question:** Production is degraded around Internet gateway; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 start-network-insights-analysis --network-insights-path-id PATH_ID` plus recent events/changes, then correlate the service-specific SLI. VPC edge target that supports public internet routing for appropriately addressed resources. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Egress-only internet gateway; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpcs --vpc-ids VPC_ID` plus recent events/changes, then correlate the service-specific SLI. permits initiated IPv6 egress while blocking unsolicited inbound routing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-06

- [ ] **Question:** Production is degraded around ENI; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. carries addresses, security groups and attachment state for compute and managed-service data planes. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around IPAM; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-route-tables --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. plans, allocates and audits address space across accounts/Regions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-08

- [ ] **Question:** Production is degraded around DHCP options; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 start-network-insights-analysis --network-insights-path-id PATH_ID` plus recent events/changes, then correlate the service-specific SLI. influence resolver/domain/NTP settings delivered to instances. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around VPC Flow Logs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpcs --vpc-ids VPC_ID` plus recent events/changes, then correlate the service-specific SLI. capture accepted/rejected flow metadata, not packet payload or every application event. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-VPC-MP-10

- [ ] **Question:** Production is degraded around Reachability Analyzer; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` plus recent events/changes, then correlate the service-specific SLI. evaluates configured network path models and complements runtime packet evidence. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-VPC-SN-01

- [ ] **Question:** Design a production Amazon VPC capability where VPC CIDR, Internet gateway and IPAM are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. VPC edge target that supports public internet routing for appropriately addressed resources. plans, allocates and audits address space across accounts/Regions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon VPC capability where Subnet, Egress-only internet gateway and DHCP options are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AZ-scoped address range whose route table and address behavior determine public/private/isolated use. permits initiated IPv6 egress while blocking unsolicited inbound routing. influence resolver/domain/NTP settings delivered to instances. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-03

- [ ] **Question:** Design a production Amazon VPC capability where Route table, ENI and VPC Flow Logs are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. carries addresses, security groups and attachment state for compute and managed-service data planes. capture accepted/rejected flow metadata, not packet payload or every application event. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon VPC capability where Internet gateway, IPAM and Reachability Analyzer are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: VPC edge target that supports public internet routing for appropriately addressed resources. plans, allocates and audits address space across accounts/Regions. evaluates configured network path models and complements runtime packet evidence. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-05

- [ ] **Question:** Design a production Amazon VPC capability where Egress-only internet gateway, DHCP options and VPC CIDR are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: permits initiated IPv6 egress while blocking unsolicited inbound routing. influence resolver/domain/NTP settings delivered to instances. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon VPC capability where ENI, VPC Flow Logs and Subnet are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: carries addresses, security groups and attachment state for compute and managed-service data planes. capture accepted/rejected flow metadata, not packet payload or every application event. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-07

- [ ] **Question:** Design a production Amazon VPC capability where IPAM, Reachability Analyzer and Route table are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: plans, allocates and audits address space across accounts/Regions. evaluates configured network path models and complements runtime packet evidence. longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon VPC capability where DHCP options, VPC CIDR and Internet gateway are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: influence resolver/domain/NTP settings delivered to instances. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. VPC edge target that supports public internet routing for appropriately addressed resources. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-09

- [ ] **Question:** Design a production Amazon VPC capability where VPC Flow Logs, Subnet and Egress-only internet gateway are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: capture accepted/rejected flow metadata, not packet payload or every application event. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. permits initiated IPv6 egress while blocking unsolicited inbound routing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-VPC-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon VPC capability where Reachability Analyzer, Route table and ENI are first-class requirements.
> **Covered in:** [Amazon VPC — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: evaluates configured network path models and complements runtime packet evidence. longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. carries addresses, security groups and attachment state for compute and managed-service data planes. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-VPC-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC CIDR. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpcs --vpc-ids VPC_ID` as one read-only checkpoint, not the whole diagnosis. regional IPv4/IPv6 address space must avoid overlap and leave room for workloads, pods and growth. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Subnet. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. AZ-scoped address range whose route table and address behavior determine public/private/isolated use. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Route table. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-route-tables --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. longest-prefix match selects a next hop such as local, IGW, NAT, TGW, peering or endpoint. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Internet gateway. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 start-network-insights-analysis --network-insights-path-id PATH_ID` as one read-only checkpoint, not the whole diagnosis. VPC edge target that supports public internet routing for appropriately addressed resources. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Egress-only internet gateway. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpcs --vpc-ids VPC_ID` as one read-only checkpoint, not the whole diagnosis. permits initiated IPv6 egress while blocking unsolicited inbound routing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ENI. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. carries addresses, security groups and attachment state for compute and managed-service data planes. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IPAM. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-route-tables --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. plans, allocates and audits address space across accounts/Regions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DHCP options. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 start-network-insights-analysis --network-insights-path-id PATH_ID` as one read-only checkpoint, not the whole diagnosis. influence resolver/domain/NTP settings delivered to instances. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving VPC Flow Logs. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpcs --vpc-ids VPC_ID` as one read-only checkpoint, not the whole diagnosis. capture accepted/rejected flow metadata, not packet payload or every application event. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-VPC-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Reachability Analyzer. How do you lead it end to end?
> **Covered in:** [Amazon VPC — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-subnets --filters Name=vpc-id,Values=VPC_ID` as one read-only checkpoint, not the whole diagnosis. evaluates configured network path models and complements runtime packet evidence. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Networking](../README.md) · [Study note](README.md) · [Next: Security groups and network ACLs →](../02-security-groups-nacls/README.md)

<!-- reading-navigation:end -->
