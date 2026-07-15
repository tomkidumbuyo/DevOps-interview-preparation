# Ingress and Gateway API — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### INGRESS-AND-GATEWAY-API-JN-01

- [ ] **Question:** What is IngressClass/controller, and why does it matter in Ingress and Gateway API?

**Answer:** selects implementation and controller-specific features. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INGRESS-AND-GATEWAY-API-JN-02

- [ ] **Question:** What is Ingress rule, and why does it matter in Ingress and Gateway API?

**Answer:** host/path routes HTTP(S) to a Service backend under limited portable API. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INGRESS-AND-GATEWAY-API-JN-03

- [ ] **Question:** What is GatewayClass, and why does it matter in Ingress and Gateway API?

**Answer:** cluster-scoped implementation class controlled by infrastructure owner. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INGRESS-AND-GATEWAY-API-JN-04

- [ ] **Question:** What is Gateway/listener, and why does it matter in Ingress and Gateway API?

**Answer:** address/protocol/port/hostname/TLS attachment owned by platform/network team. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INGRESS-AND-GATEWAY-API-JN-05

- [ ] **Question:** What is HTTPRoute/GRPCRoute, and why does it matter in Ingress and Gateway API?

**Answer:** application route match/filter/backend and weighted traffic. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INGRESS-AND-GATEWAY-API-JN-06

- [ ] **Question:** What is Parent status, and why does it matter in Ingress and Gateway API?

**Answer:** Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INGRESS-AND-GATEWAY-API-JN-07

- [ ] **Question:** What is ReferenceGrant, and why does it matter in Ingress and Gateway API?

**Answer:** explicitly authorizes supported cross-namespace references. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### INGRESS-AND-GATEWAY-API-JN-08

- [ ] **Code:** **Question:** What does `curl -vk --resolve HOST:443:ADDRESS https://HOST/PATH` help you verify for Ingress and Gateway API?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: route visibility, certificate and backend encryption differ.

### INGRESS-AND-GATEWAY-API-JN-09

- [ ] **Code:** **Question:** What does `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` help you verify for Ingress and Gateway API?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: implementation/API support must align with streaming and end-to-end deadlines.

### INGRESS-AND-GATEWAY-API-JN-10

- [ ] **Code:** **Question:** What does `kubectl describe gateway NAME -n NS` help you verify for Ingress and Gateway API?

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: weights need metrics/eval/stickiness and rollback rather than assumption.

## Junior — procedural and command questions

### INGRESS-AND-GATEWAY-API-JP-01

- [ ] **Code:** **Question:** A basic IngressClass/controller check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` and capture exact status/reason/request ID. selects implementation and controller-specific features. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-02

- [ ] **Question:** A basic Ingress rule check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe gateway NAME -n NS` and capture exact status/reason/request ID. host/path routes HTTP(S) to a Service backend under limited portable API. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-03

- [ ] **Question:** A basic GatewayClass check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get httproute NAME -n NS -o jsonpath='{.status.parents}' | jq` and capture exact status/reason/request ID. cluster-scoped implementation class controlled by infrastructure owner. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-04

- [ ] **Code:** **Question:** A basic Gateway/listener check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk --resolve HOST:443:ADDRESS https://HOST/PATH` and capture exact status/reason/request ID. address/protocol/port/hostname/TLS attachment owned by platform/network team. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-05

- [ ] **Question:** A basic HTTPRoute/GRPCRoute check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` and capture exact status/reason/request ID. application route match/filter/backend and weighted traffic. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-06

- [ ] **Question:** A basic Parent status check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe gateway NAME -n NS` and capture exact status/reason/request ID. Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-07

- [ ] **Code:** **Question:** A basic ReferenceGrant check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get httproute NAME -n NS -o jsonpath='{.status.parents}' | jq` and capture exact status/reason/request ID. explicitly authorizes supported cross-namespace references. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-08

- [ ] **Question:** A basic TLS termination/passthrough check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `curl -vk --resolve HOST:443:ADDRESS https://HOST/PATH` and capture exact status/reason/request ID. route visibility, certificate and backend encryption differ. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-09

- [ ] **Question:** A basic Timeout/retry policy check fails. What would you do first?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` and capture exact status/reason/request ID. implementation/API support must align with streaming and end-to-end deadlines. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### INGRESS-AND-GATEWAY-API-JP-10

- [ ] **Code:** **Question:** A basic Traffic split check fails. What would you do first using the CLI?

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl describe gateway NAME -n NS` and capture exact status/reason/request ID. weights need metrics/eval/stickiness and rollback rather than assumption. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### INGRESS-AND-GATEWAY-API-MN-01

- [ ] **Question:** Compare IngressClass/controller with Ingress rule. When would each change your design?

**Answer:** IngressClass/controller: selects implementation and controller-specific features. Ingress rule: host/path routes HTTP(S) to a Service backend under limited portable API. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-02

- [ ] **Question:** Compare Ingress rule with GatewayClass. When would each change your design?

**Answer:** Ingress rule: host/path routes HTTP(S) to a Service backend under limited portable API. GatewayClass: cluster-scoped implementation class controlled by infrastructure owner. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-03

- [ ] **Question:** Compare GatewayClass with Gateway/listener. When would each change your design?

**Answer:** GatewayClass: cluster-scoped implementation class controlled by infrastructure owner. Gateway/listener: address/protocol/port/hostname/TLS attachment owned by platform/network team. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-04

- [ ] **Configuration review:** **Question:** Compare Gateway/listener with HTTPRoute/GRPCRoute. When would each change your design?

**Answer:** Gateway/listener: address/protocol/port/hostname/TLS attachment owned by platform/network team. HTTPRoute/GRPCRoute: application route match/filter/backend and weighted traffic. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-05

- [ ] **Question:** Compare HTTPRoute/GRPCRoute with Parent status. When would each change your design?

**Answer:** HTTPRoute/GRPCRoute: application route match/filter/backend and weighted traffic. Parent status: Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-06

- [ ] **Question:** Compare Parent status with ReferenceGrant. When would each change your design?

**Answer:** Parent status: Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. ReferenceGrant: explicitly authorizes supported cross-namespace references. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-07

- [ ] **Configuration review:** **Question:** Compare ReferenceGrant with TLS termination/passthrough. When would each change your design?

**Answer:** ReferenceGrant: explicitly authorizes supported cross-namespace references. TLS termination/passthrough: route visibility, certificate and backend encryption differ. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-08

- [ ] **Question:** Compare TLS termination/passthrough with Timeout/retry policy. When would each change your design?

**Answer:** TLS termination/passthrough: route visibility, certificate and backend encryption differ. Timeout/retry policy: implementation/API support must align with streaming and end-to-end deadlines. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-09

- [ ] **Question:** Compare Timeout/retry policy with Traffic split. When would each change your design?

**Answer:** Timeout/retry policy: implementation/API support must align with streaming and end-to-end deadlines. Traffic split: weights need metrics/eval/stickiness and rollback rather than assumption. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### INGRESS-AND-GATEWAY-API-MN-10

- [ ] **Configuration review:** **Question:** Compare Traffic split with IngressClass/controller. When would each change your design?

**Answer:** Traffic split: weights need metrics/eval/stickiness and rollback rather than assumption. IngressClass/controller: selects implementation and controller-specific features. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### INGRESS-AND-GATEWAY-API-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around IngressClass/controller; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` plus recent events/changes, then correlate the service-specific SLI. selects implementation and controller-specific features. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-02

- [ ] **Question:** Production is degraded around Ingress rule; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe gateway NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. host/path routes HTTP(S) to a Service backend under limited portable API. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around GatewayClass; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get httproute NAME -n NS -o jsonpath='{.status.parents}' | jq` plus recent events/changes, then correlate the service-specific SLI. cluster-scoped implementation class controlled by infrastructure owner. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-04

- [ ] **Question:** Production is degraded around Gateway/listener; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk --resolve HOST:443:ADDRESS https://HOST/PATH` plus recent events/changes, then correlate the service-specific SLI. address/protocol/port/hostname/TLS attachment owned by platform/network team. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around HTTPRoute/GRPCRoute; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` plus recent events/changes, then correlate the service-specific SLI. application route match/filter/backend and weighted traffic. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-06

- [ ] **Question:** Production is degraded around Parent status; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe gateway NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around ReferenceGrant; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get httproute NAME -n NS -o jsonpath='{.status.parents}' | jq` plus recent events/changes, then correlate the service-specific SLI. explicitly authorizes supported cross-namespace references. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-08

- [ ] **Question:** Production is degraded around TLS termination/passthrough; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `curl -vk --resolve HOST:443:ADDRESS https://HOST/PATH` plus recent events/changes, then correlate the service-specific SLI. route visibility, certificate and backend encryption differ. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Timeout/retry policy; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` plus recent events/changes, then correlate the service-specific SLI. implementation/API support must align with streaming and end-to-end deadlines. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### INGRESS-AND-GATEWAY-API-MP-10

- [ ] **Question:** Production is degraded around Traffic split; walk through diagnosis, mitigation and durable repair.

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl describe gateway NAME -n NS` plus recent events/changes, then correlate the service-specific SLI. weights need metrics/eval/stickiness and rollback rather than assumption. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### INGRESS-AND-GATEWAY-API-SN-01

- [ ] **Question:** Design a production Ingress and Gateway API capability where IngressClass/controller, Gateway/listener and ReferenceGrant are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selects implementation and controller-specific features. address/protocol/port/hostname/TLS attachment owned by platform/network team. explicitly authorizes supported cross-namespace references. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Ingress and Gateway API capability where Ingress rule, HTTPRoute/GRPCRoute and TLS termination/passthrough are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: host/path routes HTTP(S) to a Service backend under limited portable API. application route match/filter/backend and weighted traffic. route visibility, certificate and backend encryption differ. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-03

- [ ] **Question:** Design a production Ingress and Gateway API capability where GatewayClass, Parent status and Timeout/retry policy are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: cluster-scoped implementation class controlled by infrastructure owner. Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. implementation/API support must align with streaming and end-to-end deadlines. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Ingress and Gateway API capability where Gateway/listener, ReferenceGrant and Traffic split are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: address/protocol/port/hostname/TLS attachment owned by platform/network team. explicitly authorizes supported cross-namespace references. weights need metrics/eval/stickiness and rollback rather than assumption. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-05

- [ ] **Question:** Design a production Ingress and Gateway API capability where HTTPRoute/GRPCRoute, TLS termination/passthrough and IngressClass/controller are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: application route match/filter/backend and weighted traffic. route visibility, certificate and backend encryption differ. selects implementation and controller-specific features. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Ingress and Gateway API capability where Parent status, Timeout/retry policy and Ingress rule are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. implementation/API support must align with streaming and end-to-end deadlines. host/path routes HTTP(S) to a Service backend under limited portable API. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-07

- [ ] **Question:** Design a production Ingress and Gateway API capability where ReferenceGrant, Traffic split and GatewayClass are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: explicitly authorizes supported cross-namespace references. weights need metrics/eval/stickiness and rollback rather than assumption. cluster-scoped implementation class controlled by infrastructure owner. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Ingress and Gateway API capability where TLS termination/passthrough, IngressClass/controller and Gateway/listener are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: route visibility, certificate and backend encryption differ. selects implementation and controller-specific features. address/protocol/port/hostname/TLS attachment owned by platform/network team. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-09

- [ ] **Question:** Design a production Ingress and Gateway API capability where Timeout/retry policy, Ingress rule and HTTPRoute/GRPCRoute are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: implementation/API support must align with streaming and end-to-end deadlines. host/path routes HTTP(S) to a Service backend under limited portable API. application route match/filter/backend and weighted traffic. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### INGRESS-AND-GATEWAY-API-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Ingress and Gateway API capability where Traffic split, GatewayClass and Parent status are first-class requirements.

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: weights need metrics/eval/stickiness and rollback rather than assumption. cluster-scoped implementation class controlled by infrastructure owner. Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### INGRESS-AND-GATEWAY-API-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IngressClass/controller. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` as one read-only checkpoint, not the whole diagnosis. selects implementation and controller-specific features. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingress rule. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe gateway NAME -n NS` as one read-only checkpoint, not the whole diagnosis. host/path routes HTTP(S) to a Service backend under limited portable API. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving GatewayClass. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get httproute NAME -n NS -o jsonpath='{.status.parents}' | jq` as one read-only checkpoint, not the whole diagnosis. cluster-scoped implementation class controlled by infrastructure owner. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Gateway/listener. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk --resolve HOST:443:ADDRESS https://HOST/PATH` as one read-only checkpoint, not the whole diagnosis. address/protocol/port/hostname/TLS attachment owned by platform/network team. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving HTTPRoute/GRPCRoute. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` as one read-only checkpoint, not the whole diagnosis. application route match/filter/backend and weighted traffic. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Parent status. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe gateway NAME -n NS` as one read-only checkpoint, not the whole diagnosis. Accepted/ResolvedRefs/Programmed conditions reveal attachment/reconcile state. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ReferenceGrant. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get httproute NAME -n NS -o jsonpath='{.status.parents}' | jq` as one read-only checkpoint, not the whole diagnosis. explicitly authorizes supported cross-namespace references. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving TLS termination/passthrough. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `curl -vk --resolve HOST:443:ADDRESS https://HOST/PATH` as one read-only checkpoint, not the whole diagnosis. route visibility, certificate and backend encryption differ. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Timeout/retry policy. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` as one read-only checkpoint, not the whole diagnosis. implementation/API support must align with streaming and end-to-end deadlines. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### INGRESS-AND-GATEWAY-API-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Traffic split. How do you lead it end to end?

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl describe gateway NAME -n NS` as one read-only checkpoint, not the whole diagnosis. weights need metrics/eval/stickiness and rollback rather than assumption. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.
