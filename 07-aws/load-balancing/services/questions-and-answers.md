# Load Balancing — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-LOAD-BALANCING-JN-01

- [ ] **Question:** What is Listener, and why does it matter in Load Balancing?

**Answer:** accepts a protocol/port and default action under TLS policy/certificates. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-LOAD-BALANCING-JN-02

- [ ] **Question:** What is Listener rule, and why does it matter in Load Balancing?

**Answer:** ordered conditions on host/path/header/query/method/source select actions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-LOAD-BALANCING-JN-03

- [ ] **Question:** What is Layer 4 flow, and why does it matter in Load Balancing?

**Answer:** routing is based on connection/protocol rather than HTTP path/header semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-LOAD-BALANCING-JN-04

- [ ] **Question:** What is Static zonal addresses, and why does it matter in Load Balancing?

**Answer:** one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-LOAD-BALANCING-JN-05

- [ ] **Question:** What is GENEVE, and why does it matter in Load Balancing?

**Answer:** encapsulates original packets and metadata between GWLB and appliances. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-LOAD-BALANCING-JN-06

- [ ] **Question:** What is GWLB endpoint, and why does it matter in Load Balancing?

**Answer:** PrivateLink-style route target that sends traffic to an appliance service. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-LOAD-BALANCING-JN-07

- [ ] **Question:** What is Anycast IP, and why does it matter in Load Balancing?

**Answer:** the same static addresses advertise globally and enter a nearby AWS edge. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-LOAD-BALANCING-JN-08

- [ ] **Code:** **Question:** What does `aws globalaccelerator list-accelerators --region us-west-2` help you verify for Load Balancing?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: accepts TCP/UDP port ranges and distributes to endpoint groups.

### BRANCH-LOAD-BALANCING-JN-09

- [ ] **Code:** **Question:** What does `aws elbv2 describe-load-balancers --names NAME` help you verify for Load Balancing?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: accepts a protocol/port and default action under TLS policy/certificates.

### BRANCH-LOAD-BALANCING-JN-10

- [ ] **Code:** **Question:** What does `aws elbv2 describe-load-balancers --names NAME` help you verify for Load Balancing?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: ordered conditions on host/path/header/query/method/source select actions.

## Junior — procedural and command questions

### BRANCH-LOAD-BALANCING-JP-01

- [ ] **Code:** **Question:** A basic Listener check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. accepts a protocol/port and default action under TLS policy/certificates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-02

- [ ] **Question:** A basic Listener rule check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. ordered conditions on host/path/header/query/method/source select actions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-03

- [ ] **Question:** A basic Layer 4 flow check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers` and capture exact status/reason/request ID. routing is based on connection/protocol rather than HTTP path/header semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-04

- [ ] **Code:** **Question:** A basic Static zonal addresses check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-accelerators --region us-west-2` and capture exact status/reason/request ID. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-05

- [ ] **Question:** A basic GENEVE check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. encapsulates original packets and metadata between GWLB and appliances. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-06

- [ ] **Question:** A basic GWLB endpoint check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. PrivateLink-style route target that sends traffic to an appliance service. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-07

- [ ] **Code:** **Question:** A basic Anycast IP check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers` and capture exact status/reason/request ID. the same static addresses advertise globally and enter a nearby AWS edge. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-08

- [ ] **Question:** A basic Accelerator listener check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws globalaccelerator list-accelerators --region us-west-2` and capture exact status/reason/request ID. accepts TCP/UDP port ranges and distributes to endpoint groups. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-09

- [ ] **Question:** A basic Listener check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. accepts a protocol/port and default action under TLS policy/certificates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-LOAD-BALANCING-JP-10

- [ ] **Code:** **Question:** A basic Listener rule check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. ordered conditions on host/path/header/query/method/source select actions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-LOAD-BALANCING-MN-01

- [ ] **Question:** Compare Listener with Listener rule. When would each change your design?

**Answer:** Listener: accepts a protocol/port and default action under TLS policy/certificates. Listener rule: ordered conditions on host/path/header/query/method/source select actions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-02

- [ ] **Question:** Compare Listener rule with Layer 4 flow. When would each change your design?

**Answer:** Listener rule: ordered conditions on host/path/header/query/method/source select actions. Layer 4 flow: routing is based on connection/protocol rather than HTTP path/header semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-03

- [ ] **Question:** Compare Layer 4 flow with Static zonal addresses. When would each change your design?

**Answer:** Layer 4 flow: routing is based on connection/protocol rather than HTTP path/header semantics. Static zonal addresses: one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-04

- [ ] **Configuration review:** **Question:** Compare Static zonal addresses with GENEVE. When would each change your design?

**Answer:** Static zonal addresses: one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. GENEVE: encapsulates original packets and metadata between GWLB and appliances. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-05

- [ ] **Question:** Compare GENEVE with GWLB endpoint. When would each change your design?

**Answer:** GENEVE: encapsulates original packets and metadata between GWLB and appliances. GWLB endpoint: PrivateLink-style route target that sends traffic to an appliance service. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-06

- [ ] **Question:** Compare GWLB endpoint with Anycast IP. When would each change your design?

**Answer:** GWLB endpoint: PrivateLink-style route target that sends traffic to an appliance service. Anycast IP: the same static addresses advertise globally and enter a nearby AWS edge. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-07

- [ ] **Configuration review:** **Question:** Compare Anycast IP with Accelerator listener. When would each change your design?

**Answer:** Anycast IP: the same static addresses advertise globally and enter a nearby AWS edge. Accelerator listener: accepts TCP/UDP port ranges and distributes to endpoint groups. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-08

- [ ] **Question:** Compare Accelerator listener with Listener. When would each change your design?

**Answer:** Accelerator listener: accepts TCP/UDP port ranges and distributes to endpoint groups. Listener: accepts a protocol/port and default action under TLS policy/certificates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-09

- [ ] **Question:** Compare Listener with Listener rule. When would each change your design?

**Answer:** Listener: accepts a protocol/port and default action under TLS policy/certificates. Listener rule: ordered conditions on host/path/header/query/method/source select actions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-LOAD-BALANCING-MN-10

- [ ] **Configuration review:** **Question:** Compare Listener rule with Listener. When would each change your design?

**Answer:** Listener rule: ordered conditions on host/path/header/query/method/source select actions. Listener: accepts a protocol/port and default action under TLS policy/certificates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-LOAD-BALANCING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Listener; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. accepts a protocol/port and default action under TLS policy/certificates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-02

- [ ] **Question:** Production is degraded around Listener rule; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. ordered conditions on host/path/header/query/method/source select actions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Layer 4 flow; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers` plus recent events/changes, then correlate the service-specific SLI. routing is based on connection/protocol rather than HTTP path/header semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-04

- [ ] **Question:** Production is degraded around Static zonal addresses; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-accelerators --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around GENEVE; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. encapsulates original packets and metadata between GWLB and appliances. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-06

- [ ] **Question:** Production is degraded around GWLB endpoint; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. PrivateLink-style route target that sends traffic to an appliance service. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Anycast IP; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers` plus recent events/changes, then correlate the service-specific SLI. the same static addresses advertise globally and enter a nearby AWS edge. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-08

- [ ] **Question:** Production is degraded around Accelerator listener; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws globalaccelerator list-accelerators --region us-west-2` plus recent events/changes, then correlate the service-specific SLI. accepts TCP/UDP port ranges and distributes to endpoint groups. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Listener; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. accepts a protocol/port and default action under TLS policy/certificates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-LOAD-BALANCING-MP-10

- [ ] **Question:** Production is degraded around Listener rule; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. ordered conditions on host/path/header/query/method/source select actions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-LOAD-BALANCING-SN-01

- [ ] **Question:** Design a production Load Balancing capability where Listener, Static zonal addresses and Anycast IP are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: accepts a protocol/port and default action under TLS policy/certificates. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. the same static addresses advertise globally and enter a nearby AWS edge. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Load Balancing capability where Listener rule, GENEVE and Accelerator listener are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered conditions on host/path/header/query/method/source select actions. encapsulates original packets and metadata between GWLB and appliances. accepts TCP/UDP port ranges and distributes to endpoint groups. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-03

- [ ] **Question:** Design a production Load Balancing capability where Layer 4 flow, GWLB endpoint and Listener are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: routing is based on connection/protocol rather than HTTP path/header semantics. PrivateLink-style route target that sends traffic to an appliance service. accepts a protocol/port and default action under TLS policy/certificates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Load Balancing capability where Static zonal addresses, Anycast IP and Listener rule are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. the same static addresses advertise globally and enter a nearby AWS edge. ordered conditions on host/path/header/query/method/source select actions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-05

- [ ] **Question:** Design a production Load Balancing capability where GENEVE, Accelerator listener and Listener are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encapsulates original packets and metadata between GWLB and appliances. accepts TCP/UDP port ranges and distributes to endpoint groups. accepts a protocol/port and default action under TLS policy/certificates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Load Balancing capability where GWLB endpoint, Listener and Listener rule are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: PrivateLink-style route target that sends traffic to an appliance service. accepts a protocol/port and default action under TLS policy/certificates. ordered conditions on host/path/header/query/method/source select actions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-07

- [ ] **Question:** Design a production Load Balancing capability where Anycast IP, Listener rule and Layer 4 flow are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: the same static addresses advertise globally and enter a nearby AWS edge. ordered conditions on host/path/header/query/method/source select actions. routing is based on connection/protocol rather than HTTP path/header semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Load Balancing capability where Accelerator listener, Listener and Static zonal addresses are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: accepts TCP/UDP port ranges and distributes to endpoint groups. accepts a protocol/port and default action under TLS policy/certificates. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-09

- [ ] **Question:** Design a production Load Balancing capability where Listener, Listener rule and GENEVE are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: accepts a protocol/port and default action under TLS policy/certificates. ordered conditions on host/path/header/query/method/source select actions. encapsulates original packets and metadata between GWLB and appliances. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-LOAD-BALANCING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Load Balancing capability where Listener rule, Layer 4 flow and GWLB endpoint are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered conditions on host/path/header/query/method/source select actions. routing is based on connection/protocol rather than HTTP path/header semantics. PrivateLink-style route target that sends traffic to an appliance service. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-LOAD-BALANCING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Listener. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. accepts a protocol/port and default action under TLS policy/certificates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Listener rule. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. ordered conditions on host/path/header/query/method/source select actions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Layer 4 flow. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers` as one read-only checkpoint, not the whole diagnosis. routing is based on connection/protocol rather than HTTP path/header semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Static zonal addresses. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-accelerators --region us-west-2` as one read-only checkpoint, not the whole diagnosis. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GENEVE. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. encapsulates original packets and metadata between GWLB and appliances. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GWLB endpoint. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. PrivateLink-style route target that sends traffic to an appliance service. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Anycast IP. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers` as one read-only checkpoint, not the whole diagnosis. the same static addresses advertise globally and enter a nearby AWS edge. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Accelerator listener. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws globalaccelerator list-accelerators --region us-west-2` as one read-only checkpoint, not the whole diagnosis. accepts TCP/UDP port ranges and distributes to endpoint groups. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Listener. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. accepts a protocol/port and default action under TLS policy/certificates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-LOAD-BALANCING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Listener rule. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. ordered conditions on host/path/header/query/method/source select actions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
