# Application Load Balancer — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### APPLICATION-LOAD-BALANCER-JN-01

- [ ] **Question:** What is Listener, and why does it matter in Application Load Balancer?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** accepts a protocol/port and default action under TLS policy/certificates. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### APPLICATION-LOAD-BALANCER-JN-02

- [ ] **Question:** What is Listener rule, and why does it matter in Application Load Balancer?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ordered conditions on host/path/header/query/method/source select actions. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### APPLICATION-LOAD-BALANCER-JN-03

- [ ] **Question:** What is Target group, and why does it matter in Application Load Balancer?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** defines target type/protocol/port/health and deregistration behavior. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### APPLICATION-LOAD-BALANCER-JN-04

- [ ] **Question:** What is Health check, and why does it matter in Application Load Balancer?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** controls endpoint admission and should represent readiness without excessive dependency coupling. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### APPLICATION-LOAD-BALANCER-JN-05

- [ ] **Question:** What is Weighted target groups, and why does it matter in Application Load Balancer?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** split traffic for canary/blue-green while stickiness can distort percentages. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### APPLICATION-LOAD-BALANCER-JN-06

- [ ] **Question:** What is Authentication action, and why does it matter in Application Load Balancer?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** integrates supported OIDC/Cognito flows but application authorization remains necessary. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### APPLICATION-LOAD-BALANCER-JN-07

- [ ] **Question:** What is gRPC/WebSocket, and why does it matter in Application Load Balancer?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** long-lived/streaming protocols require timeout, draining and client retry alignment. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### APPLICATION-LOAD-BALANCER-JN-08

- [ ] **Code:** **Question:** What does `aws elbv2 describe-target-health --target-group-arn TG_ARN` help you verify for Application Load Balancer?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: filters L7 traffic and needs tuned rules/false-positive observability.

### APPLICATION-LOAD-BALANCER-JN-09

- [ ] **Code:** **Question:** What does `aws elbv2 describe-load-balancers --names NAME` help you verify for Application Load Balancer?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces.

### APPLICATION-LOAD-BALANCER-JN-10

- [ ] **Code:** **Question:** What does `aws elbv2 describe-listeners --load-balancer-arn ARN` help you verify for Application Load Balancer?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: generated 5xx and target 5xx point to different failure layers.

## Junior — procedural and command questions

### APPLICATION-LOAD-BALANCER-JP-01

- [ ] **Code:** **Question:** A basic Listener check fails. What would you do first using the CLI?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. accepts a protocol/port and default action under TLS policy/certificates. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-02

- [ ] **Question:** A basic Listener rule check fails. What would you do first?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-listeners --load-balancer-arn ARN` and capture exact status/reason/request ID. ordered conditions on host/path/header/query/method/source select actions. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-03

- [ ] **Question:** A basic Target group check fails. What would you do first?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-rules --listener-arn ARN` and capture exact status/reason/request ID. defines target type/protocol/port/health and deregistration behavior. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-04

- [ ] **Code:** **Question:** A basic Health check check fails. What would you do first using the CLI?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-health --target-group-arn TG_ARN` and capture exact status/reason/request ID. controls endpoint admission and should represent readiness without excessive dependency coupling. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-05

- [ ] **Question:** A basic Weighted target groups check fails. What would you do first?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. split traffic for canary/blue-green while stickiness can distort percentages. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-06

- [ ] **Question:** A basic Authentication action check fails. What would you do first?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-listeners --load-balancer-arn ARN` and capture exact status/reason/request ID. integrates supported OIDC/Cognito flows but application authorization remains necessary. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-07

- [ ] **Code:** **Question:** A basic gRPC/WebSocket check fails. What would you do first using the CLI?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-rules --listener-arn ARN` and capture exact status/reason/request ID. long-lived/streaming protocols require timeout, draining and client retry alignment. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-08

- [ ] **Question:** A basic WAF integration check fails. What would you do first?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-target-health --target-group-arn TG_ARN` and capture exact status/reason/request ID. filters L7 traffic and needs tuned rules/false-positive observability. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-09

- [ ] **Question:** A basic Access logs check fails. What would you do first?
> **Covered in:** [Application Load Balancer — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-load-balancers --names NAME` and capture exact status/reason/request ID. distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### APPLICATION-LOAD-BALANCER-JP-10

- [ ] **Code:** **Question:** A basic ELB vs target errors check fails. What would you do first using the CLI?
> **Covered in:** [Application Load Balancer — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `aws elbv2 describe-listeners --load-balancer-arn ARN` and capture exact status/reason/request ID. generated 5xx and target 5xx point to different failure layers. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### APPLICATION-LOAD-BALANCER-MN-01

- [ ] **Question:** Compare Listener with Listener rule. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Listener: accepts a protocol/port and default action under TLS policy/certificates. Listener rule: ordered conditions on host/path/header/query/method/source select actions. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-02

- [ ] **Question:** Compare Listener rule with Target group. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Listener rule: ordered conditions on host/path/header/query/method/source select actions. Target group: defines target type/protocol/port/health and deregistration behavior. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-03

- [ ] **Question:** Compare Target group with Health check. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Target group: defines target type/protocol/port/health and deregistration behavior. Health check: controls endpoint admission and should represent readiness without excessive dependency coupling. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-04

- [ ] **Configuration review:** **Question:** Compare Health check with Weighted target groups. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Health check: controls endpoint admission and should represent readiness without excessive dependency coupling. Weighted target groups: split traffic for canary/blue-green while stickiness can distort percentages. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-05

- [ ] **Question:** Compare Weighted target groups with Authentication action. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Weighted target groups: split traffic for canary/blue-green while stickiness can distort percentages. Authentication action: integrates supported OIDC/Cognito flows but application authorization remains necessary. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-06

- [ ] **Question:** Compare Authentication action with gRPC/WebSocket. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Authentication action: integrates supported OIDC/Cognito flows but application authorization remains necessary. gRPC/WebSocket: long-lived/streaming protocols require timeout, draining and client retry alignment. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-07

- [ ] **Configuration review:** **Question:** Compare gRPC/WebSocket with WAF integration. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** gRPC/WebSocket: long-lived/streaming protocols require timeout, draining and client retry alignment. WAF integration: filters L7 traffic and needs tuned rules/false-positive observability. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-08

- [ ] **Question:** Compare WAF integration with Access logs. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** WAF integration: filters L7 traffic and needs tuned rules/false-positive observability. Access logs: distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-09

- [ ] **Question:** Compare Access logs with ELB vs target errors. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Access logs: distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces. ELB vs target errors: generated 5xx and target 5xx point to different failure layers. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### APPLICATION-LOAD-BALANCER-MN-10

- [ ] **Configuration review:** **Question:** Compare ELB vs target errors with Listener. When would each change your design?
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ELB vs target errors: generated 5xx and target 5xx point to different failure layers. Listener: accepts a protocol/port and default action under TLS policy/certificates. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### APPLICATION-LOAD-BALANCER-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around Listener; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. accepts a protocol/port and default action under TLS policy/certificates. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-02

- [ ] **Question:** Production is degraded around Listener rule; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-listeners --load-balancer-arn ARN` plus recent events/changes, then correlate the service-specific SLI. ordered conditions on host/path/header/query/method/source select actions. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Target group; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-rules --listener-arn ARN` plus recent events/changes, then correlate the service-specific SLI. defines target type/protocol/port/health and deregistration behavior. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-04

- [ ] **Question:** Production is degraded around Health check; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-health --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. controls endpoint admission and should represent readiness without excessive dependency coupling. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Weighted target groups; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. split traffic for canary/blue-green while stickiness can distort percentages. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-06

- [ ] **Question:** Production is degraded around Authentication action; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-listeners --load-balancer-arn ARN` plus recent events/changes, then correlate the service-specific SLI. integrates supported OIDC/Cognito flows but application authorization remains necessary. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around gRPC/WebSocket; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-rules --listener-arn ARN` plus recent events/changes, then correlate the service-specific SLI. long-lived/streaming protocols require timeout, draining and client retry alignment. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-08

- [ ] **Question:** Production is degraded around WAF integration; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-target-health --target-group-arn TG_ARN` plus recent events/changes, then correlate the service-specific SLI. filters L7 traffic and needs tuned rules/false-positive observability. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Access logs; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-load-balancers --names NAME` plus recent events/changes, then correlate the service-specific SLI. distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### APPLICATION-LOAD-BALANCER-MP-10

- [ ] **Question:** Production is degraded around ELB vs target errors; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `aws elbv2 describe-listeners --load-balancer-arn ARN` plus recent events/changes, then correlate the service-specific SLI. generated 5xx and target 5xx point to different failure layers. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### APPLICATION-LOAD-BALANCER-SN-01

- [ ] **Question:** Design a production Application Load Balancer capability where Listener, Health check and gRPC/WebSocket are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: accepts a protocol/port and default action under TLS policy/certificates. controls endpoint admission and should represent readiness without excessive dependency coupling. long-lived/streaming protocols require timeout, draining and client retry alignment. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Application Load Balancer capability where Listener rule, Weighted target groups and WAF integration are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: ordered conditions on host/path/header/query/method/source select actions. split traffic for canary/blue-green while stickiness can distort percentages. filters L7 traffic and needs tuned rules/false-positive observability. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-03

- [ ] **Question:** Design a production Application Load Balancer capability where Target group, Authentication action and Access logs are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: defines target type/protocol/port/health and deregistration behavior. integrates supported OIDC/Cognito flows but application authorization remains necessary. distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Application Load Balancer capability where Health check, gRPC/WebSocket and ELB vs target errors are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: controls endpoint admission and should represent readiness without excessive dependency coupling. long-lived/streaming protocols require timeout, draining and client retry alignment. generated 5xx and target 5xx point to different failure layers. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-05

- [ ] **Question:** Design a production Application Load Balancer capability where Weighted target groups, WAF integration and Listener are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: split traffic for canary/blue-green while stickiness can distort percentages. filters L7 traffic and needs tuned rules/false-positive observability. accepts a protocol/port and default action under TLS policy/certificates. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Application Load Balancer capability where Authentication action, Access logs and Listener rule are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: integrates supported OIDC/Cognito flows but application authorization remains necessary. distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces. ordered conditions on host/path/header/query/method/source select actions. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-07

- [ ] **Question:** Design a production Application Load Balancer capability where gRPC/WebSocket, ELB vs target errors and Target group are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: long-lived/streaming protocols require timeout, draining and client retry alignment. generated 5xx and target 5xx point to different failure layers. defines target type/protocol/port/health and deregistration behavior. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Application Load Balancer capability where WAF integration, Listener and Health check are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: filters L7 traffic and needs tuned rules/false-positive observability. accepts a protocol/port and default action under TLS policy/certificates. controls endpoint admission and should represent readiness without excessive dependency coupling. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-09

- [ ] **Question:** Design a production Application Load Balancer capability where Access logs, Listener rule and Weighted target groups are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces. ordered conditions on host/path/header/query/method/source select actions. split traffic for canary/blue-green while stickiness can distort percentages. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### APPLICATION-LOAD-BALANCER-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Application Load Balancer capability where ELB vs target errors, Target group and Authentication action are first-class requirements.
> **Covered in:** [Application Load Balancer — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: generated 5xx and target 5xx point to different failure layers. defines target type/protocol/port/health and deregistration behavior. integrates supported OIDC/Cognito flows but application authorization remains necessary. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### APPLICATION-LOAD-BALANCER-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Listener. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. accepts a protocol/port and default action under TLS policy/certificates. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Listener rule. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-listeners --load-balancer-arn ARN` as one read-only checkpoint, not the whole diagnosis. ordered conditions on host/path/header/query/method/source select actions. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Target group. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-rules --listener-arn ARN` as one read-only checkpoint, not the whole diagnosis. defines target type/protocol/port/health and deregistration behavior. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Health check. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-health --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. controls endpoint admission and should represent readiness without excessive dependency coupling. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Weighted target groups. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. split traffic for canary/blue-green while stickiness can distort percentages. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Authentication action. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-listeners --load-balancer-arn ARN` as one read-only checkpoint, not the whole diagnosis. integrates supported OIDC/Cognito flows but application authorization remains necessary. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving gRPC/WebSocket. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-rules --listener-arn ARN` as one read-only checkpoint, not the whole diagnosis. long-lived/streaming protocols require timeout, draining and client retry alignment. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving WAF integration. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-target-health --target-group-arn TG_ARN` as one read-only checkpoint, not the whole diagnosis. filters L7 traffic and needs tuned rules/false-positive observability. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Access logs. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-load-balancers --names NAME` as one read-only checkpoint, not the whole diagnosis. distinguish chosen rule/target timing/status and complement CloudWatch metrics/traces. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### APPLICATION-LOAD-BALANCER-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ELB vs target errors. How do you lead it end to end?
> **Covered in:** [Application Load Balancer — Detailed learning notes](README.md#detailed-learning-notes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `aws elbv2 describe-listeners --load-balancer-arn ARN` as one read-only checkpoint, not the whole diagnosis. generated 5xx and target 5xx point to different failure layers. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Load Balancing](../README.md) · [Study note](README.md) · [Next: Network Load Balancer →](../02-nlb/README.md)

<!-- reading-navigation:end -->
