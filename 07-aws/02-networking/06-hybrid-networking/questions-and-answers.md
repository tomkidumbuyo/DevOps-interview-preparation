# AWS hybrid networking — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AWS-HYBRID-NETWORKING-JN-01

- [ ] **Question:** What is Site-to-Site VPN, and why does it matter in AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** redundant IPsec tunnels provide encrypted connectivity over public paths. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-HYBRID-NETWORKING-JN-02

- [ ] **Question:** What is BGP, and why does it matter in AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** exchanges reachability and failover signals under ASN/prefix/timer policy. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-HYBRID-NETWORKING-JN-03

- [ ] **Question:** What is Direct Connect, and why does it matter in AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** dedicated physical connectivity needs redundant locations/devices and operational lead time. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-HYBRID-NETWORKING-JN-04

- [ ] **Question:** What is Direct Connect gateway, and why does it matter in AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** associates virtual interfaces with VPC/TGW connectivity across supported scope. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-HYBRID-NETWORKING-JN-05

- [ ] **Question:** What is Client VPN, and why does it matter in AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** managed remote-user connectivity with identity, authorization and route design. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-HYBRID-NETWORKING-JN-06

- [ ] **Question:** What is Hybrid DNS, and why does it matter in AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-HYBRID-NETWORKING-JN-07

- [ ] **Question:** What is Redundancy, and why does it matter in AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AWS-HYBRID-NETWORKING-JN-08

- [ ] **Code:** **Question:** What does `aws route53resolver list-resolver-endpoints` help you verify for AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: encapsulation and path differences can black-hole large packets while small probes pass.

### AWS-HYBRID-NETWORKING-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpn-connections` help you verify for AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: stateful firewalls/NAT can drop return paths that choose a different link.

### AWS-HYBRID-NETWORKING-JN-10

- [ ] **Code:** **Question:** What does `aws directconnect describe-connections` help you verify for AWS hybrid networking?
> **Covered in:** [AWS hybrid networking — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design.

## Junior — procedural and command questions

### AWS-HYBRID-NETWORKING-JP-01

- [ ] **Code:** **Question:** A basic Site-to-Site VPN check fails. What would you do first using the CLI?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpn-connections` and capture exact status/reason/request ID. redundant IPsec tunnels provide encrypted connectivity over public paths. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-02

- [ ] **Question:** A basic BGP check fails. What would you do first?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws directconnect describe-connections` and capture exact status/reason/request ID. exchanges reachability and failover signals under ASN/prefix/timer policy. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-03

- [ ] **Question:** A basic Direct Connect check fails. What would you do first?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-client-vpn-endpoints` and capture exact status/reason/request ID. dedicated physical connectivity needs redundant locations/devices and operational lead time. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-04

- [ ] **Code:** **Question:** A basic Direct Connect gateway check fails. What would you do first using the CLI?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53resolver list-resolver-endpoints` and capture exact status/reason/request ID. associates virtual interfaces with VPC/TGW connectivity across supported scope. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-05

- [ ] **Question:** A basic Client VPN check fails. What would you do first?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpn-connections` and capture exact status/reason/request ID. managed remote-user connectivity with identity, authorization and route design. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-06

- [ ] **Question:** A basic Hybrid DNS check fails. What would you do first?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws directconnect describe-connections` and capture exact status/reason/request ID. Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-07

- [ ] **Code:** **Question:** A basic Redundancy check fails. What would you do first using the CLI?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-client-vpn-endpoints` and capture exact status/reason/request ID. devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-08

- [ ] **Question:** A basic MTU/MSS check fails. What would you do first?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53resolver list-resolver-endpoints` and capture exact status/reason/request ID. encapsulation and path differences can black-hole large packets while small probes pass. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-09

- [ ] **Question:** A basic Asymmetric routing check fails. What would you do first?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpn-connections` and capture exact status/reason/request ID. stateful firewalls/NAT can drop return paths that choose a different link. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AWS-HYBRID-NETWORKING-JP-10

- [ ] **Code:** **Question:** A basic Monitoring/runbook check fails. What would you do first using the CLI?
> **Covered in:** [AWS hybrid networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws directconnect describe-connections` and capture exact status/reason/request ID. tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AWS-HYBRID-NETWORKING-MN-01

- [ ] **Question:** Compare Site-to-Site VPN with BGP. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Site-to-Site VPN: redundant IPsec tunnels provide encrypted connectivity over public paths. BGP: exchanges reachability and failover signals under ASN/prefix/timer policy. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-02

- [ ] **Question:** Compare BGP with Direct Connect. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** BGP: exchanges reachability and failover signals under ASN/prefix/timer policy. Direct Connect: dedicated physical connectivity needs redundant locations/devices and operational lead time. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-03

- [ ] **Question:** Compare Direct Connect with Direct Connect gateway. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Direct Connect: dedicated physical connectivity needs redundant locations/devices and operational lead time. Direct Connect gateway: associates virtual interfaces with VPC/TGW connectivity across supported scope. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-04

- [ ] **Configuration review:** **Question:** Compare Direct Connect gateway with Client VPN. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Direct Connect gateway: associates virtual interfaces with VPC/TGW connectivity across supported scope. Client VPN: managed remote-user connectivity with identity, authorization and route design. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-05

- [ ] **Question:** Compare Client VPN with Hybrid DNS. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Client VPN: managed remote-user connectivity with identity, authorization and route design. Hybrid DNS: Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-06

- [ ] **Question:** Compare Hybrid DNS with Redundancy. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Hybrid DNS: Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. Redundancy: devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-07

- [ ] **Configuration review:** **Question:** Compare Redundancy with MTU/MSS. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Redundancy: devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. MTU/MSS: encapsulation and path differences can black-hole large packets while small probes pass. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-08

- [ ] **Question:** Compare MTU/MSS with Asymmetric routing. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** MTU/MSS: encapsulation and path differences can black-hole large packets while small probes pass. Asymmetric routing: stateful firewalls/NAT can drop return paths that choose a different link. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-09

- [ ] **Question:** Compare Asymmetric routing with Monitoring/runbook. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Asymmetric routing: stateful firewalls/NAT can drop return paths that choose a different link. Monitoring/runbook: tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AWS-HYBRID-NETWORKING-MN-10

- [ ] **Configuration review:** **Question:** Compare Monitoring/runbook with Site-to-Site VPN. When would each change your design?
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Monitoring/runbook: tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design. Site-to-Site VPN: redundant IPsec tunnels provide encrypted connectivity over public paths. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AWS-HYBRID-NETWORKING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Site-to-Site VPN; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpn-connections` plus recent events/changes, then correlate the service-specific SLI. redundant IPsec tunnels provide encrypted connectivity over public paths. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-02

- [ ] **Question:** Production is degraded around BGP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws directconnect describe-connections` plus recent events/changes, then correlate the service-specific SLI. exchanges reachability and failover signals under ASN/prefix/timer policy. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Direct Connect; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-client-vpn-endpoints` plus recent events/changes, then correlate the service-specific SLI. dedicated physical connectivity needs redundant locations/devices and operational lead time. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-04

- [ ] **Question:** Production is degraded around Direct Connect gateway; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53resolver list-resolver-endpoints` plus recent events/changes, then correlate the service-specific SLI. associates virtual interfaces with VPC/TGW connectivity across supported scope. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Client VPN; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpn-connections` plus recent events/changes, then correlate the service-specific SLI. managed remote-user connectivity with identity, authorization and route design. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-06

- [ ] **Question:** Production is degraded around Hybrid DNS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws directconnect describe-connections` plus recent events/changes, then correlate the service-specific SLI. Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Redundancy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-client-vpn-endpoints` plus recent events/changes, then correlate the service-specific SLI. devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-08

- [ ] **Question:** Production is degraded around MTU/MSS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53resolver list-resolver-endpoints` plus recent events/changes, then correlate the service-specific SLI. encapsulation and path differences can black-hole large packets while small probes pass. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Asymmetric routing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpn-connections` plus recent events/changes, then correlate the service-specific SLI. stateful firewalls/NAT can drop return paths that choose a different link. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AWS-HYBRID-NETWORKING-MP-10

- [ ] **Question:** Production is degraded around Monitoring/runbook; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws directconnect describe-connections` plus recent events/changes, then correlate the service-specific SLI. tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AWS-HYBRID-NETWORKING-SN-01

- [ ] **Question:** Design a production AWS hybrid networking capability where Site-to-Site VPN, Direct Connect gateway and Redundancy are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: redundant IPsec tunnels provide encrypted connectivity over public paths. associates virtual interfaces with VPC/TGW connectivity across supported scope. devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production AWS hybrid networking capability where BGP, Client VPN and MTU/MSS are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: exchanges reachability and failover signals under ASN/prefix/timer policy. managed remote-user connectivity with identity, authorization and route design. encapsulation and path differences can black-hole large packets while small probes pass. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-03

- [ ] **Question:** Design a production AWS hybrid networking capability where Direct Connect, Hybrid DNS and Asymmetric routing are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: dedicated physical connectivity needs redundant locations/devices and operational lead time. Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. stateful firewalls/NAT can drop return paths that choose a different link. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production AWS hybrid networking capability where Direct Connect gateway, Redundancy and Monitoring/runbook are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: associates virtual interfaces with VPC/TGW connectivity across supported scope. devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-05

- [ ] **Question:** Design a production AWS hybrid networking capability where Client VPN, MTU/MSS and Site-to-Site VPN are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed remote-user connectivity with identity, authorization and route design. encapsulation and path differences can black-hole large packets while small probes pass. redundant IPsec tunnels provide encrypted connectivity over public paths. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production AWS hybrid networking capability where Hybrid DNS, Asymmetric routing and BGP are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. stateful firewalls/NAT can drop return paths that choose a different link. exchanges reachability and failover signals under ASN/prefix/timer policy. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-07

- [ ] **Question:** Design a production AWS hybrid networking capability where Redundancy, Monitoring/runbook and Direct Connect are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design. dedicated physical connectivity needs redundant locations/devices and operational lead time. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production AWS hybrid networking capability where MTU/MSS, Site-to-Site VPN and Direct Connect gateway are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encapsulation and path differences can black-hole large packets while small probes pass. redundant IPsec tunnels provide encrypted connectivity over public paths. associates virtual interfaces with VPC/TGW connectivity across supported scope. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-09

- [ ] **Question:** Design a production AWS hybrid networking capability where Asymmetric routing, BGP and Client VPN are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: stateful firewalls/NAT can drop return paths that choose a different link. exchanges reachability and failover signals under ASN/prefix/timer policy. managed remote-user connectivity with identity, authorization and route design. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AWS-HYBRID-NETWORKING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production AWS hybrid networking capability where Monitoring/runbook, Direct Connect and Hybrid DNS are first-class requirements.
> **Covered in:** [AWS hybrid networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design. dedicated physical connectivity needs redundant locations/devices and operational lead time. Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AWS-HYBRID-NETWORKING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Site-to-Site VPN. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpn-connections` as one read-only checkpoint, not the whole diagnosis. redundant IPsec tunnels provide encrypted connectivity over public paths. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving BGP. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws directconnect describe-connections` as one read-only checkpoint, not the whole diagnosis. exchanges reachability and failover signals under ASN/prefix/timer policy. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Direct Connect. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-client-vpn-endpoints` as one read-only checkpoint, not the whole diagnosis. dedicated physical connectivity needs redundant locations/devices and operational lead time. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Direct Connect gateway. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53resolver list-resolver-endpoints` as one read-only checkpoint, not the whole diagnosis. associates virtual interfaces with VPC/TGW connectivity across supported scope. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Client VPN. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpn-connections` as one read-only checkpoint, not the whole diagnosis. managed remote-user connectivity with identity, authorization and route design. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hybrid DNS. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws directconnect describe-connections` as one read-only checkpoint, not the whole diagnosis. Resolver inbound/outbound endpoints and forwarding rules bridge namespaces. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Redundancy. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-client-vpn-endpoints` as one read-only checkpoint, not the whole diagnosis. devices, tunnels, DX locations, carriers, power and routes must avoid shared failure. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving MTU/MSS. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53resolver list-resolver-endpoints` as one read-only checkpoint, not the whole diagnosis. encapsulation and path differences can black-hole large packets while small probes pass. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Asymmetric routing. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpn-connections` as one read-only checkpoint, not the whole diagnosis. stateful firewalls/NAT can drop return paths that choose a different link. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AWS-HYBRID-NETWORKING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Monitoring/runbook. How do you lead it end to end?
> **Covered in:** [AWS hybrid networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws directconnect describe-connections` as one read-only checkpoint, not the whole diagnosis. tunnel/BGP/route/DNS/synthetic metrics and tested failover prove design. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: VPC peering, Transit Gateway and Cloud WAN](../05-peering-tgw-cloudwan/README.md) · [Study note](README.md) · [Next: Amazon Route 53 →](../07-route53/README.md)

<!-- reading-navigation:end -->
