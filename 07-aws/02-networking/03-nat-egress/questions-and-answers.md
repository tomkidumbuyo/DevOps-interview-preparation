# NAT and egress architecture — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### NAT-AND-EGRESS-ARCHITECTURE-JN-01

- [ ] **Question:** What is NAT gateway, and why does it matter in NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** managed AZ-scoped IPv4 translation with hourly and data-processing cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NAT-AND-EGRESS-ARCHITECTURE-JN-02

- [ ] **Question:** What is NAT instance, and why does it matter in NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** customer-managed translation with patching, throughput and failover responsibility. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NAT-AND-EGRESS-ARCHITECTURE-JN-03

- [ ] **Question:** What is Centralized egress, and why does it matter in NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** shared inspection/control reduces duplication but adds routing, blast radius and processing cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NAT-AND-EGRESS-ARCHITECTURE-JN-04

- [ ] **Question:** What is Per-AZ egress, and why does it matter in NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** aligns failure domains and avoids cross-AZ dependency at higher fixed cost. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NAT-AND-EGRESS-ARCHITECTURE-JN-05

- [ ] **Question:** What is SNAT port exhaustion, and why does it matter in NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** many connections to the same destination can exhaust translation tuples. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NAT-AND-EGRESS-ARCHITECTURE-JN-06

- [ ] **Question:** What is Egress proxy, and why does it matter in NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** authenticates/filters/logs application destinations but needs client/protocol support. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NAT-AND-EGRESS-ARCHITECTURE-JN-07

- [ ] **Question:** What is IPv6 egress, and why does it matter in NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NAT-AND-EGRESS-ARCHITECTURE-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpc-endpoints` help you verify for NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: keep supported service traffic off NAT and can reduce exposure/cost.

### NAT-AND-EGRESS-ARCHITECTURE-JN-09

- [ ] **Code:** **Question:** What does `aws ec2 describe-nat-gateways` help you verify for NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: DNS-to-IP change and encrypted protocols make naive IP lists fragile.

### NAT-AND-EGRESS-ARCHITECTURE-JN-10

- [ ] **Code:** **Question:** What does `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` help you verify for NAT and egress architecture?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: bytes, errors, ports, destinations and tenant attribution reveal cost and abuse.

## Junior — procedural and command questions

### NAT-AND-EGRESS-ARCHITECTURE-JP-01

- [ ] **Code:** **Question:** A basic NAT gateway check fails. What would you do first using the CLI?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-nat-gateways` and capture exact status/reason/request ID. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-02

- [ ] **Question:** A basic NAT instance check fails. What would you do first?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` and capture exact status/reason/request ID. customer-managed translation with patching, throughput and failover responsibility. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-03

- [ ] **Question:** A basic Centralized egress check fails. What would you do first?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-route-tables` and capture exact status/reason/request ID. shared inspection/control reduces duplication but adds routing, blast radius and processing cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-04

- [ ] **Code:** **Question:** A basic Per-AZ egress check fails. What would you do first using the CLI?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints` and capture exact status/reason/request ID. aligns failure domains and avoids cross-AZ dependency at higher fixed cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-05

- [ ] **Question:** A basic SNAT port exhaustion check fails. What would you do first?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-nat-gateways` and capture exact status/reason/request ID. many connections to the same destination can exhaust translation tuples. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-06

- [ ] **Question:** A basic Egress proxy check fails. What would you do first?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` and capture exact status/reason/request ID. authenticates/filters/logs application destinations but needs client/protocol support. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-07

- [ ] **Code:** **Question:** A basic IPv6 egress check fails. What would you do first using the CLI?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-route-tables` and capture exact status/reason/request ID. uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-08

- [ ] **Question:** A basic Service endpoints check fails. What would you do first?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints` and capture exact status/reason/request ID. keep supported service traffic off NAT and can reduce exposure/cost. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-09

- [ ] **Question:** A basic Domain allowlisting check fails. What would you do first?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-nat-gateways` and capture exact status/reason/request ID. DNS-to-IP change and encrypted protocols make naive IP lists fragile. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NAT-AND-EGRESS-ARCHITECTURE-JP-10

- [ ] **Code:** **Question:** A basic Egress telemetry check fails. What would you do first using the CLI?
> **Covered in:** [NAT and egress architecture — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` and capture exact status/reason/request ID. bytes, errors, ports, destinations and tenant attribution reveal cost and abuse. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### NAT-AND-EGRESS-ARCHITECTURE-MN-01

- [ ] **Question:** Compare NAT gateway with NAT instance. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** NAT gateway: managed AZ-scoped IPv4 translation with hourly and data-processing cost. NAT instance: customer-managed translation with patching, throughput and failover responsibility. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-02

- [ ] **Question:** Compare NAT instance with Centralized egress. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** NAT instance: customer-managed translation with patching, throughput and failover responsibility. Centralized egress: shared inspection/control reduces duplication but adds routing, blast radius and processing cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-03

- [ ] **Question:** Compare Centralized egress with Per-AZ egress. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Centralized egress: shared inspection/control reduces duplication but adds routing, blast radius and processing cost. Per-AZ egress: aligns failure domains and avoids cross-AZ dependency at higher fixed cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-04

- [ ] **Configuration review:** **Question:** Compare Per-AZ egress with SNAT port exhaustion. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Per-AZ egress: aligns failure domains and avoids cross-AZ dependency at higher fixed cost. SNAT port exhaustion: many connections to the same destination can exhaust translation tuples. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-05

- [ ] **Question:** Compare SNAT port exhaustion with Egress proxy. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** SNAT port exhaustion: many connections to the same destination can exhaust translation tuples. Egress proxy: authenticates/filters/logs application destinations but needs client/protocol support. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-06

- [ ] **Question:** Compare Egress proxy with IPv6 egress. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Egress proxy: authenticates/filters/logs application destinations but needs client/protocol support. IPv6 egress: uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-07

- [ ] **Configuration review:** **Question:** Compare IPv6 egress with Service endpoints. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** IPv6 egress: uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. Service endpoints: keep supported service traffic off NAT and can reduce exposure/cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-08

- [ ] **Question:** Compare Service endpoints with Domain allowlisting. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Service endpoints: keep supported service traffic off NAT and can reduce exposure/cost. Domain allowlisting: DNS-to-IP change and encrypted protocols make naive IP lists fragile. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-09

- [ ] **Question:** Compare Domain allowlisting with Egress telemetry. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Domain allowlisting: DNS-to-IP change and encrypted protocols make naive IP lists fragile. Egress telemetry: bytes, errors, ports, destinations and tenant attribution reveal cost and abuse. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NAT-AND-EGRESS-ARCHITECTURE-MN-10

- [ ] **Configuration review:** **Question:** Compare Egress telemetry with NAT gateway. When would each change your design?
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Egress telemetry: bytes, errors, ports, destinations and tenant attribution reveal cost and abuse. NAT gateway: managed AZ-scoped IPv4 translation with hourly and data-processing cost. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### NAT-AND-EGRESS-ARCHITECTURE-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around NAT gateway; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-nat-gateways` plus recent events/changes, then correlate the service-specific SLI. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-02

- [ ] **Question:** Production is degraded around NAT instance; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` plus recent events/changes, then correlate the service-specific SLI. customer-managed translation with patching, throughput and failover responsibility. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Centralized egress; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-route-tables` plus recent events/changes, then correlate the service-specific SLI. shared inspection/control reduces duplication but adds routing, blast radius and processing cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-04

- [ ] **Question:** Production is degraded around Per-AZ egress; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints` plus recent events/changes, then correlate the service-specific SLI. aligns failure domains and avoids cross-AZ dependency at higher fixed cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around SNAT port exhaustion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-nat-gateways` plus recent events/changes, then correlate the service-specific SLI. many connections to the same destination can exhaust translation tuples. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-06

- [ ] **Question:** Production is degraded around Egress proxy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` plus recent events/changes, then correlate the service-specific SLI. authenticates/filters/logs application destinations but needs client/protocol support. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around IPv6 egress; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-route-tables` plus recent events/changes, then correlate the service-specific SLI. uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-08

- [ ] **Question:** Production is degraded around Service endpoints; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints` plus recent events/changes, then correlate the service-specific SLI. keep supported service traffic off NAT and can reduce exposure/cost. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Domain allowlisting; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-nat-gateways` plus recent events/changes, then correlate the service-specific SLI. DNS-to-IP change and encrypted protocols make naive IP lists fragile. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NAT-AND-EGRESS-ARCHITECTURE-MP-10

- [ ] **Question:** Production is degraded around Egress telemetry; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` plus recent events/changes, then correlate the service-specific SLI. bytes, errors, ports, destinations and tenant attribution reveal cost and abuse. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### NAT-AND-EGRESS-ARCHITECTURE-SN-01

- [ ] **Question:** Design a production NAT and egress architecture capability where NAT gateway, Per-AZ egress and IPv6 egress are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: managed AZ-scoped IPv4 translation with hourly and data-processing cost. aligns failure domains and avoids cross-AZ dependency at higher fixed cost. uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production NAT and egress architecture capability where NAT instance, SNAT port exhaustion and Service endpoints are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: customer-managed translation with patching, throughput and failover responsibility. many connections to the same destination can exhaust translation tuples. keep supported service traffic off NAT and can reduce exposure/cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-03

- [ ] **Question:** Design a production NAT and egress architecture capability where Centralized egress, Egress proxy and Domain allowlisting are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: shared inspection/control reduces duplication but adds routing, blast radius and processing cost. authenticates/filters/logs application destinations but needs client/protocol support. DNS-to-IP change and encrypted protocols make naive IP lists fragile. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production NAT and egress architecture capability where Per-AZ egress, IPv6 egress and Egress telemetry are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: aligns failure domains and avoids cross-AZ dependency at higher fixed cost. uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. bytes, errors, ports, destinations and tenant attribution reveal cost and abuse. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-05

- [ ] **Question:** Design a production NAT and egress architecture capability where SNAT port exhaustion, Service endpoints and NAT gateway are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: many connections to the same destination can exhaust translation tuples. keep supported service traffic off NAT and can reduce exposure/cost. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production NAT and egress architecture capability where Egress proxy, Domain allowlisting and NAT instance are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authenticates/filters/logs application destinations but needs client/protocol support. DNS-to-IP change and encrypted protocols make naive IP lists fragile. customer-managed translation with patching, throughput and failover responsibility. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-07

- [ ] **Question:** Design a production NAT and egress architecture capability where IPv6 egress, Egress telemetry and Centralized egress are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. bytes, errors, ports, destinations and tenant attribution reveal cost and abuse. shared inspection/control reduces duplication but adds routing, blast radius and processing cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production NAT and egress architecture capability where Service endpoints, NAT gateway and Per-AZ egress are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: keep supported service traffic off NAT and can reduce exposure/cost. managed AZ-scoped IPv4 translation with hourly and data-processing cost. aligns failure domains and avoids cross-AZ dependency at higher fixed cost. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-09

- [ ] **Question:** Design a production NAT and egress architecture capability where Domain allowlisting, NAT instance and SNAT port exhaustion are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: DNS-to-IP change and encrypted protocols make naive IP lists fragile. customer-managed translation with patching, throughput and failover responsibility. many connections to the same destination can exhaust translation tuples. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NAT-AND-EGRESS-ARCHITECTURE-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production NAT and egress architecture capability where Egress telemetry, Centralized egress and Egress proxy are first-class requirements.
> **Covered in:** [NAT and egress architecture — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: bytes, errors, ports, destinations and tenant attribution reveal cost and abuse. shared inspection/control reduces duplication but adds routing, blast radius and processing cost. authenticates/filters/logs application destinations but needs client/protocol support. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### NAT-AND-EGRESS-ARCHITECTURE-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NAT gateway. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-nat-gateways` as one read-only checkpoint, not the whole diagnosis. managed AZ-scoped IPv4 translation with hourly and data-processing cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NAT instance. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` as one read-only checkpoint, not the whole diagnosis. customer-managed translation with patching, throughput and failover responsibility. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Centralized egress. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-route-tables` as one read-only checkpoint, not the whole diagnosis. shared inspection/control reduces duplication but adds routing, blast radius and processing cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Per-AZ egress. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints` as one read-only checkpoint, not the whole diagnosis. aligns failure domains and avoids cross-AZ dependency at higher fixed cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving SNAT port exhaustion. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-nat-gateways` as one read-only checkpoint, not the whole diagnosis. many connections to the same destination can exhaust translation tuples. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Egress proxy. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` as one read-only checkpoint, not the whole diagnosis. authenticates/filters/logs application destinations but needs client/protocol support. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IPv6 egress. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-route-tables` as one read-only checkpoint, not the whole diagnosis. uses routable addresses and egress-only filtering rather than primary IPv4 NAT semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Service endpoints. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints` as one read-only checkpoint, not the whole diagnosis. keep supported service traffic off NAT and can reduce exposure/cost. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Domain allowlisting. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-nat-gateways` as one read-only checkpoint, not the whole diagnosis. DNS-to-IP change and encrypted protocols make naive IP lists fragile. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NAT-AND-EGRESS-ARCHITECTURE-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Egress telemetry. How do you lead it end to end?
> **Covered in:** [NAT and egress architecture — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws cloudwatch get-metric-data --metric-data-queries file://nat-metrics.json --start-time START --end-time END` as one read-only checkpoint, not the whole diagnosis. bytes, errors, ports, destinations and tenant attribution reveal cost and abuse. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Security groups and network ACLs](../02-security-groups-nacls/README.md) · [Study note](README.md) · [Next: VPC endpoints and AWS PrivateLink →](../04-endpoints-privatelink/README.md)

<!-- reading-navigation:end -->
