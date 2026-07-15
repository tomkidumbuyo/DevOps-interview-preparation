# Gateway Load Balancer — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### GATEWAY-LOAD-BALANCER-JN-01

- [ ] **Question:** What is GENEVE, and why does it matter in Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** encapsulates original packets and metadata between GWLB and appliances. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-LOAD-BALANCER-JN-02

- [ ] **Question:** What is GWLB endpoint, and why does it matter in Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** PrivateLink-style route target that sends traffic to an appliance service. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-LOAD-BALANCER-JN-03

- [ ] **Question:** What is Appliance target group, and why does it matter in Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** health/scaling determines inspection capacity. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-LOAD-BALANCER-JN-04

- [ ] **Question:** What is Symmetric routing, and why does it matter in Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** both directions must traverse the same stateful inspection path. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-LOAD-BALANCER-JN-05

- [ ] **Question:** What is Appliance mode, and why does it matter in Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-LOAD-BALANCER-JN-06

- [ ] **Question:** What is Flow stickiness, and why does it matter in Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** keeps a flow on a target while failures/timeout determine rehash behavior. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-LOAD-BALANCER-JN-07

- [ ] **Question:** What is Fail-open/closed, and why does it matter in Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** security and availability policy must define behavior when inspection is unavailable. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### GATEWAY-LOAD-BALANCER-JN-08

- [ ] **Code:** **Question:** What does `aws ec2 describe-route-tables` help you verify for Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: new appliance readiness/state sync/licensing must precede traffic.

### GATEWAY-LOAD-BALANCER-JN-09

- [ ] **Code:** **Question:** What does `aws elbv2 describe-load-balancers` help you verify for Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Real-world exercise: easy → hard](README.md#real-world-exercise-easy-hard)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: subnet/TGW routes form explicit service chains and can create loops/asymmetry.

### GATEWAY-LOAD-BALANCER-JN-10

- [ ] **Code:** **Question:** What does `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` help you verify for Gateway Load Balancer?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss.

## Junior — procedural and command questions

### GATEWAY-LOAD-BALANCER-JP-01

- [ ] **Code:** **Question:** A basic GENEVE check fails. What would you do first using the CLI?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers` and capture exact status/reason/request ID. encapsulates original packets and metadata between GWLB and appliances. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-02

- [ ] **Question:** A basic GWLB endpoint check fails. What would you do first?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` and capture exact status/reason/request ID. PrivateLink-style route target that sends traffic to an appliance service. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-03

- [ ] **Question:** A basic Appliance target group check fails. What would you do first?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-health --target-group-arn TG_ARN` and capture exact status/reason/request ID. health/scaling determines inspection capacity. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-04

- [ ] **Code:** **Question:** A basic Symmetric routing check fails. What would you do first using the CLI?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-route-tables` and capture exact status/reason/request ID. both directions must traverse the same stateful inspection path. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-05

- [ ] **Question:** A basic Appliance mode check fails. What would you do first?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers` and capture exact status/reason/request ID. TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-06

- [ ] **Question:** A basic Flow stickiness check fails. What would you do first?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` and capture exact status/reason/request ID. keeps a flow on a target while failures/timeout determine rehash behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-07

- [ ] **Code:** **Question:** A basic Fail-open/closed check fails. What would you do first using the CLI?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-health --target-group-arn TG_ARN` and capture exact status/reason/request ID. security and availability policy must define behavior when inspection is unavailable. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-08

- [ ] **Question:** A basic Autoscaling check fails. What would you do first?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-route-tables` and capture exact status/reason/request ID. new appliance readiness/state sync/licensing must precede traffic. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-09

- [ ] **Question:** A basic Route insertion check fails. What would you do first?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers` and capture exact status/reason/request ID. subnet/TGW routes form explicit service chains and can create loops/asymmetry. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### GATEWAY-LOAD-BALANCER-JP-10

- [ ] **Code:** **Question:** A basic Observability check fails. What would you do first using the CLI?
> **Covered in:** [Gateway Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` and capture exact status/reason/request ID. endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### GATEWAY-LOAD-BALANCER-MN-01

- [ ] **Question:** Compare GENEVE with GWLB endpoint. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** GENEVE: encapsulates original packets and metadata between GWLB and appliances. GWLB endpoint: PrivateLink-style route target that sends traffic to an appliance service. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-02

- [ ] **Question:** Compare GWLB endpoint with Appliance target group. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** GWLB endpoint: PrivateLink-style route target that sends traffic to an appliance service. Appliance target group: health/scaling determines inspection capacity. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-03

- [ ] **Question:** Compare Appliance target group with Symmetric routing. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Appliance target group: health/scaling determines inspection capacity. Symmetric routing: both directions must traverse the same stateful inspection path. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-04

- [ ] **Configuration review:** **Question:** Compare Symmetric routing with Appliance mode. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Symmetric routing: both directions must traverse the same stateful inspection path. Appliance mode: TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-05

- [ ] **Question:** Compare Appliance mode with Flow stickiness. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Appliance mode: TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. Flow stickiness: keeps a flow on a target while failures/timeout determine rehash behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-06

- [ ] **Question:** Compare Flow stickiness with Fail-open/closed. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Flow stickiness: keeps a flow on a target while failures/timeout determine rehash behavior. Fail-open/closed: security and availability policy must define behavior when inspection is unavailable. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-07

- [ ] **Configuration review:** **Question:** Compare Fail-open/closed with Autoscaling. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Fail-open/closed: security and availability policy must define behavior when inspection is unavailable. Autoscaling: new appliance readiness/state sync/licensing must precede traffic. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-08

- [ ] **Question:** Compare Autoscaling with Route insertion. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Autoscaling: new appliance readiness/state sync/licensing must precede traffic. Route insertion: subnet/TGW routes form explicit service chains and can create loops/asymmetry. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-09

- [ ] **Question:** Compare Route insertion with Observability. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Route insertion: subnet/TGW routes form explicit service chains and can create loops/asymmetry. Observability: endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### GATEWAY-LOAD-BALANCER-MN-10

- [ ] **Configuration review:** **Question:** Compare Observability with GENEVE. When would each change your design?
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Observability: endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss. GENEVE: encapsulates original packets and metadata between GWLB and appliances. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### GATEWAY-LOAD-BALANCER-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around GENEVE; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers` plus recent events/changes, then correlate the service-specific SLI. encapsulates original packets and metadata between GWLB and appliances. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-02

- [ ] **Question:** Production is degraded around GWLB endpoint; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` plus recent events/changes, then correlate the service-specific SLI. PrivateLink-style route target that sends traffic to an appliance service. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Appliance target group; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-health --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. health/scaling determines inspection capacity. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-04

- [ ] **Question:** Production is degraded around Symmetric routing; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-route-tables` plus recent events/changes, then correlate the service-specific SLI. both directions must traverse the same stateful inspection path. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Appliance mode; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers` plus recent events/changes, then correlate the service-specific SLI. TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-06

- [ ] **Question:** Production is degraded around Flow stickiness; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` plus recent events/changes, then correlate the service-specific SLI. keeps a flow on a target while failures/timeout determine rehash behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around Fail-open/closed; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-health --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. security and availability policy must define behavior when inspection is unavailable. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-08

- [ ] **Question:** Production is degraded around Autoscaling; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-route-tables` plus recent events/changes, then correlate the service-specific SLI. new appliance readiness/state sync/licensing must precede traffic. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Route insertion; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers` plus recent events/changes, then correlate the service-specific SLI. subnet/TGW routes form explicit service chains and can create loops/asymmetry. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### GATEWAY-LOAD-BALANCER-MP-10

- [ ] **Question:** Production is degraded around Observability; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Gateway Load Balancer — Observability](README.md#observability)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` plus recent events/changes, then correlate the service-specific SLI. endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### GATEWAY-LOAD-BALANCER-SN-01

- [ ] **Question:** Design a production Gateway Load Balancer capability where GENEVE, Symmetric routing and Fail-open/closed are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: encapsulates original packets and metadata between GWLB and appliances. both directions must traverse the same stateful inspection path. security and availability policy must define behavior when inspection is unavailable. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway Load Balancer capability where GWLB endpoint, Appliance mode and Autoscaling are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: PrivateLink-style route target that sends traffic to an appliance service. TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. new appliance readiness/state sync/licensing must precede traffic. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-03

- [ ] **Question:** Design a production Gateway Load Balancer capability where Appliance target group, Flow stickiness and Route insertion are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: health/scaling determines inspection capacity. keeps a flow on a target while failures/timeout determine rehash behavior. subnet/TGW routes form explicit service chains and can create loops/asymmetry. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway Load Balancer capability where Symmetric routing, Fail-open/closed and Observability are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: both directions must traverse the same stateful inspection path. security and availability policy must define behavior when inspection is unavailable. endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-05

- [ ] **Question:** Design a production Gateway Load Balancer capability where Appliance mode, Autoscaling and GENEVE are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. new appliance readiness/state sync/licensing must precede traffic. encapsulates original packets and metadata between GWLB and appliances. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway Load Balancer capability where Flow stickiness, Route insertion and GWLB endpoint are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: keeps a flow on a target while failures/timeout determine rehash behavior. subnet/TGW routes form explicit service chains and can create loops/asymmetry. PrivateLink-style route target that sends traffic to an appliance service. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-07

- [ ] **Question:** Design a production Gateway Load Balancer capability where Fail-open/closed, Observability and Appliance target group are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: security and availability policy must define behavior when inspection is unavailable. endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss. health/scaling determines inspection capacity. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway Load Balancer capability where Autoscaling, GENEVE and Symmetric routing are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: new appliance readiness/state sync/licensing must precede traffic. encapsulates original packets and metadata between GWLB and appliances. both directions must traverse the same stateful inspection path. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-09

- [ ] **Question:** Design a production Gateway Load Balancer capability where Route insertion, GWLB endpoint and Appliance mode are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: subnet/TGW routes form explicit service chains and can create loops/asymmetry. PrivateLink-style route target that sends traffic to an appliance service. TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### GATEWAY-LOAD-BALANCER-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Gateway Load Balancer capability where Observability, Appliance target group and Flow stickiness are first-class requirements.
> **Covered in:** [Gateway Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss. health/scaling determines inspection capacity. keeps a flow on a target while failures/timeout determine rehash behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### GATEWAY-LOAD-BALANCER-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GENEVE. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers` as one read-only checkpoint, not the whole diagnosis. encapsulates original packets and metadata between GWLB and appliances. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GWLB endpoint. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` as one read-only checkpoint, not the whole diagnosis. PrivateLink-style route target that sends traffic to an appliance service. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Appliance target group. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-health --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. health/scaling determines inspection capacity. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Symmetric routing. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-route-tables` as one read-only checkpoint, not the whole diagnosis. both directions must traverse the same stateful inspection path. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Appliance mode. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers` as one read-only checkpoint, not the whole diagnosis. TGW setting helps preserve AZ/flow symmetry through appliance VPC patterns. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Flow stickiness. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` as one read-only checkpoint, not the whole diagnosis. keeps a flow on a target while failures/timeout determine rehash behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Fail-open/closed. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-health --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. security and availability policy must define behavior when inspection is unavailable. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Autoscaling. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-route-tables` as one read-only checkpoint, not the whole diagnosis. new appliance readiness/state sync/licensing must precede traffic. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Route insertion. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers` as one read-only checkpoint, not the whole diagnosis. subnet/TGW routes form explicit service chains and can create loops/asymmetry. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### GATEWAY-LOAD-BALANCER-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Observability. How do you lead it end to end?
> **Covered in:** [Gateway Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws ec2 describe-vpc-endpoints --filters Name=service-name,Values=SERVICE` as one read-only checkpoint, not the whole diagnosis. endpoint/GWLB/appliance/flow logs and synthetic paths locate packet loss. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Network Load Balancer](../02-nlb/README.md) · [Study note](README.md) · [Next: AWS Global Accelerator →](../04-global-accelerator/README.md)

<!-- reading-navigation:end -->
