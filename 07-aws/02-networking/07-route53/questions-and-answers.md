# Amazon Route 53 — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### AMAZON-ROUTE-53-JN-01

- [ ] **Question:** What is Hosted zone, and why does it matter in Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** authoritative public or VPC-associated private namespace. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ROUTE-53-JN-02

- [ ] **Question:** What is Alias record, and why does it matter in Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** AWS-specific record that targets supported resources without a CNAME at the zone apex. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ROUTE-53-JN-03

- [ ] **Question:** What is Weighted routing, and why does it matter in Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** probabilistically distributes DNS answers and is affected by resolver/client caching. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ROUTE-53-JN-04

- [ ] **Question:** What is Latency routing, and why does it matter in Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** chooses Region from measured AWS network latency rather than application load. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ROUTE-53-JN-05

- [ ] **Question:** What is Failover routing, and why does it matter in Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** health-check state selects primary/secondary answers but recovery still depends on data/service readiness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ROUTE-53-JN-06

- [ ] **Question:** What is TTL, and why does it matter in Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** balances cache/query load against change/failover responsiveness. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ROUTE-53-JN-07

- [ ] **Question:** What is Resolver endpoints, and why does it matter in Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### AMAZON-ROUTE-53-JN-08

- [ ] **Code:** **Question:** What does `aws route53 get-health-check-status --health-check-id ID` help you verify for Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: public/private views can intentionally answer differently and complicate diagnosis.

### AMAZON-ROUTE-53-JN-09

- [ ] **Code:** **Question:** What does `aws route53resolver list-resolver-rules` help you verify for Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: authenticates signed DNS data; it does not encrypt queries.

### AMAZON-ROUTE-53-JN-10

- [ ] **Code:** **Question:** What does `dig +trace NAME` help you verify for Amazon Route 53?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design.

## Junior — procedural and command questions

### AMAZON-ROUTE-53-JP-01

- [ ] **Code:** **Question:** A basic Hosted zone check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53 list-hosted-zones` and capture exact status/reason/request ID. authoritative public or VPC-associated private namespace. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-02

- [ ] **Question:** A basic Alias record check fails. What would you do first?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID` and capture exact status/reason/request ID. AWS-specific record that targets supported resources without a CNAME at the zone apex. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-03

- [ ] **Question:** A basic Weighted routing check fails. What would you do first?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53 get-health-check-status --health-check-id ID` and capture exact status/reason/request ID. probabilistically distributes DNS answers and is affected by resolver/client caching. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-04

- [ ] **Code:** **Question:** A basic Latency routing check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53resolver list-resolver-rules` and capture exact status/reason/request ID. chooses Region from measured AWS network latency rather than application load. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-05

- [ ] **Question:** A basic Failover routing check fails. What would you do first?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. health-check state selects primary/secondary answers but recovery still depends on data/service readiness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-06

- [ ] **Question:** A basic TTL check fails. What would you do first?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53 list-hosted-zones` and capture exact status/reason/request ID. balances cache/query load against change/failover responsiveness. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-07

- [ ] **Code:** **Question:** A basic Resolver endpoints check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID` and capture exact status/reason/request ID. inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-08

- [ ] **Question:** A basic Split-horizon DNS check fails. What would you do first?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53 get-health-check-status --health-check-id ID` and capture exact status/reason/request ID. public/private views can intentionally answer differently and complicate diagnosis. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-09

- [ ] **Question:** A basic DNSSEC check fails. What would you do first?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws route53resolver list-resolver-rules` and capture exact status/reason/request ID. authenticates signed DNS data; it does not encrypt queries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### AMAZON-ROUTE-53-JP-10

- [ ] **Code:** **Question:** A basic Health checks check fails. What would you do first using the CLI?
> **Covered in:** [Amazon Route 53 — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `dig +trace NAME` and capture exact status/reason/request ID. endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### AMAZON-ROUTE-53-MN-01

- [ ] **Question:** Compare Hosted zone with Alias record. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Hosted zone: authoritative public or VPC-associated private namespace. Alias record: AWS-specific record that targets supported resources without a CNAME at the zone apex. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-02

- [ ] **Question:** Compare Alias record with Weighted routing. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Alias record: AWS-specific record that targets supported resources without a CNAME at the zone apex. Weighted routing: probabilistically distributes DNS answers and is affected by resolver/client caching. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-03

- [ ] **Question:** Compare Weighted routing with Latency routing. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Weighted routing: probabilistically distributes DNS answers and is affected by resolver/client caching. Latency routing: chooses Region from measured AWS network latency rather than application load. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-04

- [ ] **Configuration review:** **Question:** Compare Latency routing with Failover routing. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Latency routing: chooses Region from measured AWS network latency rather than application load. Failover routing: health-check state selects primary/secondary answers but recovery still depends on data/service readiness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-05

- [ ] **Question:** Compare Failover routing with TTL. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Failover routing: health-check state selects primary/secondary answers but recovery still depends on data/service readiness. TTL: balances cache/query load against change/failover responsiveness. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-06

- [ ] **Question:** Compare TTL with Resolver endpoints. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** TTL: balances cache/query load against change/failover responsiveness. Resolver endpoints: inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-07

- [ ] **Configuration review:** **Question:** Compare Resolver endpoints with Split-horizon DNS. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Resolver endpoints: inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. Split-horizon DNS: public/private views can intentionally answer differently and complicate diagnosis. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-08

- [ ] **Question:** Compare Split-horizon DNS with DNSSEC. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Split-horizon DNS: public/private views can intentionally answer differently and complicate diagnosis. DNSSEC: authenticates signed DNS data; it does not encrypt queries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-09

- [ ] **Question:** Compare DNSSEC with Health checks. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** DNSSEC: authenticates signed DNS data; it does not encrypt queries. Health checks: endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### AMAZON-ROUTE-53-MN-10

- [ ] **Configuration review:** **Question:** Compare Health checks with Hosted zone. When would each change your design?
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Health checks: endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. Hosted zone: authoritative public or VPC-associated private namespace. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### AMAZON-ROUTE-53-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Hosted zone; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53 list-hosted-zones` plus recent events/changes, then correlate the service-specific SLI. authoritative public or VPC-associated private namespace. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-02

- [ ] **Question:** Production is degraded around Alias record; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID` plus recent events/changes, then correlate the service-specific SLI. AWS-specific record that targets supported resources without a CNAME at the zone apex. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Weighted routing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53 get-health-check-status --health-check-id ID` plus recent events/changes, then correlate the service-specific SLI. probabilistically distributes DNS answers and is affected by resolver/client caching. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-04

- [ ] **Question:** Production is degraded around Latency routing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53resolver list-resolver-rules` plus recent events/changes, then correlate the service-specific SLI. chooses Region from measured AWS network latency rather than application load. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Failover routing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. health-check state selects primary/secondary answers but recovery still depends on data/service readiness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-06

- [ ] **Question:** Production is degraded around TTL; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53 list-hosted-zones` plus recent events/changes, then correlate the service-specific SLI. balances cache/query load against change/failover responsiveness. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Resolver endpoints; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID` plus recent events/changes, then correlate the service-specific SLI. inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-08

- [ ] **Question:** Production is degraded around Split-horizon DNS; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53 get-health-check-status --health-check-id ID` plus recent events/changes, then correlate the service-specific SLI. public/private views can intentionally answer differently and complicate diagnosis. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around DNSSEC; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws route53resolver list-resolver-rules` plus recent events/changes, then correlate the service-specific SLI. authenticates signed DNS data; it does not encrypt queries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### AMAZON-ROUTE-53-MP-10

- [ ] **Question:** Production is degraded around Health checks; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `dig +trace NAME` plus recent events/changes, then correlate the service-specific SLI. endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### AMAZON-ROUTE-53-SN-01

- [ ] **Question:** Design a production Amazon Route 53 capability where Hosted zone, Latency routing and Resolver endpoints are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authoritative public or VPC-associated private namespace. chooses Region from measured AWS network latency rather than application load. inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Route 53 capability where Alias record, Failover routing and Split-horizon DNS are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: AWS-specific record that targets supported resources without a CNAME at the zone apex. health-check state selects primary/secondary answers but recovery still depends on data/service readiness. public/private views can intentionally answer differently and complicate diagnosis. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-03

- [ ] **Question:** Design a production Amazon Route 53 capability where Weighted routing, TTL and DNSSEC are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: probabilistically distributes DNS answers and is affected by resolver/client caching. balances cache/query load against change/failover responsiveness. authenticates signed DNS data; it does not encrypt queries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Route 53 capability where Latency routing, Resolver endpoints and Health checks are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: chooses Region from measured AWS network latency rather than application load. inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-05

- [ ] **Question:** Design a production Amazon Route 53 capability where Failover routing, Split-horizon DNS and Hosted zone are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: health-check state selects primary/secondary answers but recovery still depends on data/service readiness. public/private views can intentionally answer differently and complicate diagnosis. authoritative public or VPC-associated private namespace. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Route 53 capability where TTL, DNSSEC and Alias record are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: balances cache/query load against change/failover responsiveness. authenticates signed DNS data; it does not encrypt queries. AWS-specific record that targets supported resources without a CNAME at the zone apex. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-07

- [ ] **Question:** Design a production Amazon Route 53 capability where Resolver endpoints, Health checks and Weighted routing are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. probabilistically distributes DNS answers and is affected by resolver/client caching. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Route 53 capability where Split-horizon DNS, Hosted zone and Latency routing are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: public/private views can intentionally answer differently and complicate diagnosis. authoritative public or VPC-associated private namespace. chooses Region from measured AWS network latency rather than application load. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-09

- [ ] **Question:** Design a production Amazon Route 53 capability where DNSSEC, Alias record and Failover routing are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: authenticates signed DNS data; it does not encrypt queries. AWS-specific record that targets supported resources without a CNAME at the zone apex. health-check state selects primary/secondary answers but recovery still depends on data/service readiness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### AMAZON-ROUTE-53-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Amazon Route 53 capability where Health checks, Weighted routing and TTL are first-class requirements.
> **Covered in:** [Amazon Route 53 — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. probabilistically distributes DNS answers and is affected by resolver/client caching. balances cache/query load against change/failover responsiveness. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### AMAZON-ROUTE-53-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Hosted zone. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53 list-hosted-zones` as one read-only checkpoint, not the whole diagnosis. authoritative public or VPC-associated private namespace. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Alias record. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID` as one read-only checkpoint, not the whole diagnosis. AWS-specific record that targets supported resources without a CNAME at the zone apex. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Weighted routing. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53 get-health-check-status --health-check-id ID` as one read-only checkpoint, not the whole diagnosis. probabilistically distributes DNS answers and is affected by resolver/client caching. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Latency routing. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53resolver list-resolver-rules` as one read-only checkpoint, not the whole diagnosis. chooses Region from measured AWS network latency rather than application load. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Failover routing. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. health-check state selects primary/secondary answers but recovery still depends on data/service readiness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TTL. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53 list-hosted-zones` as one read-only checkpoint, not the whole diagnosis. balances cache/query load against change/failover responsiveness. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Resolver endpoints. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53 list-resource-record-sets --hosted-zone-id ZONE_ID` as one read-only checkpoint, not the whole diagnosis. inbound/outbound interfaces bridge VPC and external DNS with forwarding rules. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Split-horizon DNS. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53 get-health-check-status --health-check-id ID` as one read-only checkpoint, not the whole diagnosis. public/private views can intentionally answer differently and complicate diagnosis. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving DNSSEC. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws route53resolver list-resolver-rules` as one read-only checkpoint, not the whole diagnosis. authenticates signed DNS data; it does not encrypt queries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### AMAZON-ROUTE-53-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Health checks. How do you lead it end to end?
> **Covered in:** [Amazon Route 53 — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `dig +trace NAME` as one read-only checkpoint, not the whole diagnosis. endpoint/calculated/CloudWatch checks need quorum, firewall and false-positive design. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: AWS hybrid networking](../06-hybrid-networking/README.md) · [Study note](README.md) · [Next: Compute →](../../03-compute/README.md)

<!-- reading-navigation:end -->
