# Network Load Balancer — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### NETWORK-LOAD-BALANCER-JN-01

- [ ] **Question:** What is Layer 4 flow, and why does it matter in Network Load Balancer?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** routing is based on connection/protocol rather than HTTP path/header semantics. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NETWORK-LOAD-BALANCER-JN-02

- [ ] **Question:** What is Static zonal addresses, and why does it matter in Network Load Balancer?
> **Covered in:** [Network Load Balancer — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NETWORK-LOAD-BALANCER-JN-03

- [ ] **Question:** What is Source IP preservation, and why does it matter in Network Load Balancer?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** depends on target type/protocol/settings and affects security/logging/return path. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NETWORK-LOAD-BALANCER-JN-04

- [ ] **Question:** What is TLS listener, and why does it matter in Network Load Balancer?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** terminates TLS with certificates/policy while a TCP listener can pass TLS through. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NETWORK-LOAD-BALANCER-JN-05

- [ ] **Question:** What is UDP, and why does it matter in Network Load Balancer?
> **Covered in:** [Network Load Balancer — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** health/connection assumptions differ because transport is connectionless. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NETWORK-LOAD-BALANCER-JN-06

- [ ] **Question:** What is IP targets, and why does it matter in Network Load Balancer?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** route to VPC/on-prem IPs under documented reachability and registration constraints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NETWORK-LOAD-BALANCER-JN-07

- [ ] **Question:** What is ALB target, and why does it matter in Network Load Balancer?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### NETWORK-LOAD-BALANCER-JN-08

- [ ] **Code:** **Question:** What does `openssl s_client -connect HOST:443 -servername NAME` help you verify for Network Load Balancer?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: endpoint services commonly use NLB as producer data plane.

### NETWORK-LOAD-BALANCER-JN-09

- [ ] **Code:** **Question:** What does `aws elbv2 describe-load-balancers --names NAME` help you verify for Network Load Balancer?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: client/LB/target timeouts, draining and resets govern rollout behavior.

### NETWORK-LOAD-BALANCER-JN-10

- [ ] **Code:** **Question:** What does `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` help you verify for Network Load Balancer?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: capacity in each enabled zone and DNS fail-away influence resilience.

## Junior — procedural and command questions

### NETWORK-LOAD-BALANCER-JP-01

- [ ] **Code:** **Question:** A basic Layer 4 flow check fails. What would you do first using the CLI?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. routing is based on connection/protocol rather than HTTP path/header semantics. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-02

- [ ] **Question:** A basic Static zonal addresses check fails. What would you do first?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` and capture exact status/reason/request ID. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-03

- [ ] **Question:** A basic Source IP preservation check fails. What would you do first?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-health --target-group-arn TG_ARN` and capture exact status/reason/request ID. depends on target type/protocol/settings and affects security/logging/return path. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-04

- [ ] **Code:** **Question:** A basic TLS listener check fails. What would you do first using the CLI?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `openssl s_client -connect HOST:443 -servername NAME` and capture exact status/reason/request ID. terminates TLS with certificates/policy while a TCP listener can pass TLS through. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-05

- [ ] **Question:** A basic UDP check fails. What would you do first?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. health/connection assumptions differ because transport is connectionless. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-06

- [ ] **Question:** A basic IP targets check fails. What would you do first?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` and capture exact status/reason/request ID. route to VPC/on-prem IPs under documented reachability and registration constraints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-07

- [ ] **Code:** **Question:** A basic ALB target check fails. What would you do first using the CLI?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-health --target-group-arn TG_ARN` and capture exact status/reason/request ID. combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-08

- [ ] **Question:** A basic PrivateLink check fails. What would you do first?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `openssl s_client -connect HOST:443 -servername NAME` and capture exact status/reason/request ID. endpoint services commonly use NLB as producer data plane. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-09

- [ ] **Question:** A basic Long-lived connections check fails. What would you do first?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. client/LB/target timeouts, draining and resets govern rollout behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### NETWORK-LOAD-BALANCER-JP-10

- [ ] **Code:** **Question:** A basic Zonal health/cross-zone check fails. What would you do first using the CLI?
> **Covered in:** [Network Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` and capture exact status/reason/request ID. capacity in each enabled zone and DNS fail-away influence resilience. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### NETWORK-LOAD-BALANCER-MN-01

- [ ] **Question:** Compare Layer 4 flow with Static zonal addresses. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Layer 4 flow: routing is based on connection/protocol rather than HTTP path/header semantics. Static zonal addresses: one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-02

- [ ] **Question:** Compare Static zonal addresses with Source IP preservation. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Static zonal addresses: one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Source IP preservation: depends on target type/protocol/settings and affects security/logging/return path. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-03

- [ ] **Question:** Compare Source IP preservation with TLS listener. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Source IP preservation: depends on target type/protocol/settings and affects security/logging/return path. TLS listener: terminates TLS with certificates/policy while a TCP listener can pass TLS through. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-04

- [ ] **Configuration review:** **Question:** Compare TLS listener with UDP. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** TLS listener: terminates TLS with certificates/policy while a TCP listener can pass TLS through. UDP: health/connection assumptions differ because transport is connectionless. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-05

- [ ] **Question:** Compare UDP with IP targets. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** UDP: health/connection assumptions differ because transport is connectionless. IP targets: route to VPC/on-prem IPs under documented reachability and registration constraints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-06

- [ ] **Question:** Compare IP targets with ALB target. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** IP targets: route to VPC/on-prem IPs under documented reachability and registration constraints. ALB target: combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-07

- [ ] **Configuration review:** **Question:** Compare ALB target with PrivateLink. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ALB target: combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. PrivateLink: endpoint services commonly use NLB as producer data plane. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-08

- [ ] **Question:** Compare PrivateLink with Long-lived connections. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** PrivateLink: endpoint services commonly use NLB as producer data plane. Long-lived connections: client/LB/target timeouts, draining and resets govern rollout behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-09

- [ ] **Question:** Compare Long-lived connections with Zonal health/cross-zone. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Long-lived connections: client/LB/target timeouts, draining and resets govern rollout behavior. Zonal health/cross-zone: capacity in each enabled zone and DNS fail-away influence resilience. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### NETWORK-LOAD-BALANCER-MN-10

- [ ] **Configuration review:** **Question:** Compare Zonal health/cross-zone with Layer 4 flow. When would each change your design?
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Zonal health/cross-zone: capacity in each enabled zone and DNS fail-away influence resilience. Layer 4 flow: routing is based on connection/protocol rather than HTTP path/header semantics. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### NETWORK-LOAD-BALANCER-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Layer 4 flow; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. routing is based on connection/protocol rather than HTTP path/header semantics. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-02

- [ ] **Question:** Production is degraded around Static zonal addresses; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Source IP preservation; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-health --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. depends on target type/protocol/settings and affects security/logging/return path. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-04

- [ ] **Question:** Production is degraded around TLS listener; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `openssl s_client -connect HOST:443 -servername NAME` plus recent events/changes, then correlate the service-specific SLI. terminates TLS with certificates/policy while a TCP listener can pass TLS through. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around UDP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. health/connection assumptions differ because transport is connectionless. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-06

- [ ] **Question:** Production is degraded around IP targets; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. route to VPC/on-prem IPs under documented reachability and registration constraints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around ALB target; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-health --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-08

- [ ] **Question:** Production is degraded around PrivateLink; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `openssl s_client -connect HOST:443 -servername NAME` plus recent events/changes, then correlate the service-specific SLI. endpoint services commonly use NLB as producer data plane. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Long-lived connections; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. client/LB/target timeouts, draining and resets govern rollout behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### NETWORK-LOAD-BALANCER-MP-10

- [ ] **Question:** Production is degraded around Zonal health/cross-zone; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. capacity in each enabled zone and DNS fail-away influence resilience. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### NETWORK-LOAD-BALANCER-SN-01

- [ ] **Question:** Design a production Network Load Balancer capability where Layer 4 flow, TLS listener and ALB target are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: routing is based on connection/protocol rather than HTTP path/header semantics. terminates TLS with certificates/policy while a TCP listener can pass TLS through. combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Network Load Balancer capability where Static zonal addresses, UDP and PrivateLink are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. health/connection assumptions differ because transport is connectionless. endpoint services commonly use NLB as producer data plane. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-03

- [ ] **Question:** Design a production Network Load Balancer capability where Source IP preservation, IP targets and Long-lived connections are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: depends on target type/protocol/settings and affects security/logging/return path. route to VPC/on-prem IPs under documented reachability and registration constraints. client/LB/target timeouts, draining and resets govern rollout behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Network Load Balancer capability where TLS listener, ALB target and Zonal health/cross-zone are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: terminates TLS with certificates/policy while a TCP listener can pass TLS through. combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. capacity in each enabled zone and DNS fail-away influence resilience. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-05

- [ ] **Question:** Design a production Network Load Balancer capability where UDP, PrivateLink and Layer 4 flow are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: health/connection assumptions differ because transport is connectionless. endpoint services commonly use NLB as producer data plane. routing is based on connection/protocol rather than HTTP path/header semantics. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Network Load Balancer capability where IP targets, Long-lived connections and Static zonal addresses are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: route to VPC/on-prem IPs under documented reachability and registration constraints. client/LB/target timeouts, draining and resets govern rollout behavior. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-07

- [ ] **Question:** Design a production Network Load Balancer capability where ALB target, Zonal health/cross-zone and Source IP preservation are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. capacity in each enabled zone and DNS fail-away influence resilience. depends on target type/protocol/settings and affects security/logging/return path. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Network Load Balancer capability where PrivateLink, Layer 4 flow and TLS listener are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: endpoint services commonly use NLB as producer data plane. routing is based on connection/protocol rather than HTTP path/header semantics. terminates TLS with certificates/policy while a TCP listener can pass TLS through. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-09

- [ ] **Question:** Design a production Network Load Balancer capability where Long-lived connections, Static zonal addresses and UDP are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: client/LB/target timeouts, draining and resets govern rollout behavior. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. health/connection assumptions differ because transport is connectionless. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### NETWORK-LOAD-BALANCER-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Network Load Balancer capability where Zonal health/cross-zone, Source IP preservation and IP targets are first-class requirements.
> **Covered in:** [Network Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: capacity in each enabled zone and DNS fail-away influence resilience. depends on target type/protocol/settings and affects security/logging/return path. route to VPC/on-prem IPs under documented reachability and registration constraints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### NETWORK-LOAD-BALANCER-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Layer 4 flow. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. routing is based on connection/protocol rather than HTTP path/header semantics. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Static zonal addresses. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. one address per enabled zone can satisfy allowlists and anycast/global patterns via other services. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Source IP preservation. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-health --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. depends on target type/protocol/settings and affects security/logging/return path. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TLS listener. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `openssl s_client -connect HOST:443 -servername NAME` as one read-only checkpoint, not the whole diagnosis. terminates TLS with certificates/policy while a TCP listener can pass TLS through. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving UDP. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. health/connection assumptions differ because transport is connectionless. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IP targets. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. route to VPC/on-prem IPs under documented reachability and registration constraints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ALB target. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-health --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. combines NLB static/private/TCP endpoint features with downstream ALB L7 routing. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving PrivateLink. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `openssl s_client -connect HOST:443 -servername NAME` as one read-only checkpoint, not the whole diagnosis. endpoint services commonly use NLB as producer data plane. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Long-lived connections. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. client/LB/target timeouts, draining and resets govern rollout behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### NETWORK-LOAD-BALANCER-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Zonal health/cross-zone. How do you lead it end to end?
> **Covered in:** [Network Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-group-attributes --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. capacity in each enabled zone and DNS fail-away influence resilience. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Application Load Balancer](../01-alb/README.md) · [Study note](README.md) · [Next: Gateway Load Balancer →](../03-gwlb/README.md)

<!-- reading-navigation:end -->
