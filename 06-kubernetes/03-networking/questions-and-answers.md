# Networking — interview questions and answers

> Study first: [README.md](README.md) · Minimum: 20 answered questions per level, split into normal and procedural. Code/CLI prompts are marked **Code**.

## Junior — normal conceptual and code questions

### BRANCH-NETWORKING-JN-01

- [ ] **Question:** What is ClusterIP, and why does it matter in Networking?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** virtual internal IP implemented by the cluster service data plane. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-02

- [ ] **Question:** What is NodePort, and why does it matter in Networking?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** reserves a port on nodes and routes to Service endpoints. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-03

- [ ] **Question:** What is Kubernetes network model, and why does it matter in Networking?
> **Covered in:** [Networking — Easy mode: purpose and mental model](README.md#easy-mode-purpose-and-mental-model)

**Answer:** Pods have cluster-routable IP identity and communicate without required NAT inside the model. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-04

- [ ] **Question:** What is CNI plugin, and why does it matter in Networking?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** configures Pod interface, address, route and cleanup when runtime creates sandbox. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-05

- [ ] **Question:** What is Pod selection, and why does it matter in Networking?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** policy applies only to Pods matched in its namespace. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-06

- [ ] **Question:** What is Isolation direction, and why does it matter in Networking?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** selecting a Pod for ingress/egress isolates that direction to allowed union. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-07

- [ ] **Question:** What is IngressClass/controller, and why does it matter in Networking?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** selects implementation and controller-specific features. In an interview, connect it to the request/resource lifecycle, name one limit or failure, and explain how you would observe it. Do not stop at the vendor definition.

### BRANCH-NETWORKING-JN-08

- [ ] **Code:** **Question:** What does `kubectl get networkpolicy -A -o yaml` help you verify for Networking?
> **Covered in:** [Networking — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: host/path routes HTTP(S) to a Service backend under limited portable API.

### BRANCH-NETWORKING-JN-09

- [ ] **Code:** **Question:** What does `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` help you verify for Networking?
> **Covered in:** [Networking — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries.

### BRANCH-NETWORKING-JN-10

- [ ] **Code:** **Question:** What does `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` help you verify for Networking?
> **Covered in:** [Networking — Command lab](README.md#command-lab)

**Answer:** It is a read-oriented check in this leaf's command path. Run it only after confirming identity, account/context, Region/namespace and resource. Interpret it against the desired configuration and healthy baseline; then correlate events, metrics, logs and audit rather than changing state from one output. The relevant mechanism is: distributes service discovery, certificates and policy to proxies.

## Junior — procedural and command questions

### BRANCH-NETWORKING-JP-01

- [ ] **Code:** **Question:** A basic ClusterIP check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get svc,endpoints,endpointslice -A -o wide` and capture exact status/reason/request ID. virtual internal IP implemented by the cluster service data plane. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-02

- [ ] **Question:** A basic NodePort check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ds -n kube-system` and capture exact status/reason/request ID. reserves a port on nodes and routes to Service endpoints. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-03

- [ ] **Question:** A basic Kubernetes network model check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get networkpolicy -A -o yaml` and capture exact status/reason/request ID. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-04

- [ ] **Code:** **Question:** A basic CNI plugin check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` and capture exact status/reason/request ID. configures Pod interface, address, route and cleanup when runtime creates sandbox. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-05

- [ ] **Question:** A basic Pod selection check fails. What would you do first?
> **Covered in:** [CNI, kube-proxy and eBPF data planes — Command lab](02-cni-kubeproxy-ebpf/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` and capture exact status/reason/request ID. policy applies only to Pods matched in its namespace. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-06

- [ ] **Question:** A basic Isolation direction check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get svc,endpoints,endpointslice -A -o wide` and capture exact status/reason/request ID. selecting a Pod for ingress/egress isolates that direction to allowed union. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-07

- [ ] **Code:** **Question:** A basic IngressClass/controller check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ds -n kube-system` and capture exact status/reason/request ID. selects implementation and controller-specific features. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-08

- [ ] **Question:** A basic Ingress rule check fails. What would you do first?
> **Covered in:** [Networking — Command lab](README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get networkpolicy -A -o yaml` and capture exact status/reason/request ID. host/path routes HTTP(S) to a Service backend under limited portable API. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-09

- [ ] **Question:** A basic Data-plane proxy check fails. What would you do first?
> **Covered in:** [Service mesh — Command lab](05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` and capture exact status/reason/request ID. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

### BRANCH-NETWORKING-JP-10

- [ ] **Code:** **Question:** A basic Control plane check fails. What would you do first using the CLI?
> **Covered in:** [Service mesh — Command lab](05-service-mesh/README.md#command-lab)

**Answer:** Confirm the user-visible symptom, time and blast radius; verify your read-only identity/context; then run `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` and capture exact status/reason/request ID. distributes service discovery, certificates and policy to proxies. Compare desired with observed state, inspect the immediately adjacent dependency, and change only one reversible variable. Verify from the original client, then record the source fix and prevention.

## Mid-level — normal, comparison and configuration questions

### BRANCH-NETWORKING-MN-01

- [ ] **Question:** Compare ClusterIP with NodePort. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** ClusterIP: virtual internal IP implemented by the cluster service data plane. NodePort: reserves a port on nodes and routes to Service endpoints. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-02

- [ ] **Question:** Compare NodePort with Kubernetes network model. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** NodePort: reserves a port on nodes and routes to Service endpoints. Kubernetes network model: Pods have cluster-routable IP identity and communicate without required NAT inside the model. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-03

- [ ] **Question:** Compare Kubernetes network model with CNI plugin. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Kubernetes network model: Pods have cluster-routable IP identity and communicate without required NAT inside the model. CNI plugin: configures Pod interface, address, route and cleanup when runtime creates sandbox. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-04

- [ ] **Configuration review:** **Question:** Compare CNI plugin with Pod selection. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** CNI plugin: configures Pod interface, address, route and cleanup when runtime creates sandbox. Pod selection: policy applies only to Pods matched in its namespace. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-05

- [ ] **Question:** Compare Pod selection with Isolation direction. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Pod selection: policy applies only to Pods matched in its namespace. Isolation direction: selecting a Pod for ingress/egress isolates that direction to allowed union. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-06

- [ ] **Question:** Compare Isolation direction with IngressClass/controller. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Isolation direction: selecting a Pod for ingress/egress isolates that direction to allowed union. IngressClass/controller: selects implementation and controller-specific features. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-07

- [ ] **Configuration review:** **Question:** Compare IngressClass/controller with Ingress rule. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** IngressClass/controller: selects implementation and controller-specific features. Ingress rule: host/path routes HTTP(S) to a Service backend under limited portable API. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-08

- [ ] **Question:** Compare Ingress rule with Data-plane proxy. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Ingress rule: host/path routes HTTP(S) to a Service backend under limited portable API. Data-plane proxy: sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-09

- [ ] **Question:** Compare Data-plane proxy with Control plane. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Data-plane proxy: sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Control plane: distributes service discovery, certificates and policy to proxies. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

### BRANCH-NETWORKING-MN-10

- [ ] **Configuration review:** **Question:** Compare Control plane with ClusterIP. When would each change your design?
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Control plane: distributes service discovery, certificates and policy to proxies. ClusterIP: virtual internal IP implemented by the cluster service data plane. Select by protocol/access pattern, isolation/trust, failure domain and recovery, performance/scale, operational ownership and total cost. State which evidence or SLO would make you revisit the choice; they may be complementary rather than substitutes.

## Mid-level — procedural, CLI and troubleshooting questions

### BRANCH-NETWORKING-MP-01

- [ ] **CLI/debugging:** **Question:** Production is degraded around ClusterIP; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get svc,endpoints,endpointslice -A -o wide` plus recent events/changes, then correlate the service-specific SLI. virtual internal IP implemented by the cluster service data plane. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-02

- [ ] **Question:** Production is degraded around NodePort; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ds -n kube-system` plus recent events/changes, then correlate the service-specific SLI. reserves a port on nodes and routes to Service endpoints. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-03

- [ ] **CLI/debugging:** **Question:** Production is degraded around Kubernetes network model; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get networkpolicy -A -o yaml` plus recent events/changes, then correlate the service-specific SLI. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-04

- [ ] **Question:** Production is degraded around CNI plugin; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` plus recent events/changes, then correlate the service-specific SLI. configures Pod interface, address, route and cleanup when runtime creates sandbox. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-05

- [ ] **CLI/debugging:** **Question:** Production is degraded around Pod selection; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` plus recent events/changes, then correlate the service-specific SLI. policy applies only to Pods matched in its namespace. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-06

- [ ] **Question:** Production is degraded around Isolation direction; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get svc,endpoints,endpointslice -A -o wide` plus recent events/changes, then correlate the service-specific SLI. selecting a Pod for ingress/egress isolates that direction to allowed union. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-07

- [ ] **CLI/debugging:** **Question:** Production is degraded around IngressClass/controller; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ds -n kube-system` plus recent events/changes, then correlate the service-specific SLI. selects implementation and controller-specific features. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-08

- [ ] **Question:** Production is degraded around Ingress rule; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get networkpolicy -A -o yaml` plus recent events/changes, then correlate the service-specific SLI. host/path routes HTTP(S) to a Service backend under limited portable API. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-09

- [ ] **CLI/debugging:** **Question:** Production is degraded around Data-plane proxy; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` plus recent events/changes, then correlate the service-specific SLI. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

### BRANCH-NETWORKING-MP-10

- [ ] **Question:** Production is degraded around Control plane; walk through diagnosis, mitigation and durable repair.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Declare impact/owner and freeze risky changes. Segment identity/policy, DNS/network/TLS, control-plane reconciliation, data path, dependency and quota/capacity. Start with `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` plus recent events/changes, then correlate the service-specific SLI. distributes service discovery, certificates and policy to proxies. Stop retry amplification, shed or fail over only to an approved compatible path, and preserve evidence. Verify user outcome/data correctness, repair IaC/Git, add a regression test/alert and rehearse the runbook.

## Senior — architecture, trade-off and code-design questions

### BRANCH-NETWORKING-SN-01

- [ ] **Question:** Design a production Networking capability where ClusterIP, CNI plugin and IngressClass/controller are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: virtual internal IP implemented by the cluster service data plane. configures Pod interface, address, route and cleanup when runtime creates sandbox. selects implementation and controller-specific features. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-02

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where NodePort, Pod selection and Ingress rule are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: reserves a port on nodes and routes to Service endpoints. policy applies only to Pods matched in its namespace. host/path routes HTTP(S) to a Service backend under limited portable API. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-03

- [ ] **Question:** Design a production Networking capability where Kubernetes network model, Isolation direction and Data-plane proxy are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: Pods have cluster-routable IP identity and communicate without required NAT inside the model. selecting a Pod for ingress/egress isolates that direction to allowed union. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-04

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where CNI plugin, IngressClass/controller and Control plane are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: configures Pod interface, address, route and cleanup when runtime creates sandbox. selects implementation and controller-specific features. distributes service discovery, certificates and policy to proxies. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-05

- [ ] **Question:** Design a production Networking capability where Pod selection, Ingress rule and ClusterIP are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: policy applies only to Pods matched in its namespace. host/path routes HTTP(S) to a Service backend under limited portable API. virtual internal IP implemented by the cluster service data plane. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-06

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Isolation direction, Data-plane proxy and NodePort are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selecting a Pod for ingress/egress isolates that direction to allowed union. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. reserves a port on nodes and routes to Service endpoints. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-07

- [ ] **Question:** Design a production Networking capability where IngressClass/controller, Control plane and Kubernetes network model are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: selects implementation and controller-specific features. distributes service discovery, certificates and policy to proxies. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-08

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Ingress rule, ClusterIP and CNI plugin are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: host/path routes HTTP(S) to a Service backend under limited portable API. virtual internal IP implemented by the cluster service data plane. configures Pod interface, address, route and cleanup when runtime creates sandbox. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-09

- [ ] **Question:** Design a production Networking capability where Data-plane proxy, NodePort and Pod selection are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. reserves a port on nodes and routes to Service endpoints. policy applies only to Pods matched in its namespace. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

### BRANCH-NETWORKING-SN-10

- [ ] **Architecture/configuration:** **Question:** Design a production Networking capability where Control plane, Kubernetes network model and Isolation direction are first-class requirements.
> **Covered in:** [Networking — Architecture and lifecycle](README.md#architecture-and-lifecycle)

**Answer:** Clarify tenants, workload/scale, latency/quality SLO, data class/residency, RPO/RTO, deployment modes, team and budget. Relevant facts: distributes service discovery, certificates and policy to proxies. Pods have cluster-routable IP identity and communicate without required NAT inside the model. selecting a Pod for ingress/egress isolates that direction to allowed union. Separate control/data planes and failure domains; define identity/trust and encryption/key lifecycle; quantify capacity/headroom/cold path; use immutable delivery/canary/rollback; instrument SLO, saturation, audit and unit cost. Compare managed/shared/dedicated options and include migration, DR test and exit triggers.

## Senior — procedural incident, migration and ownership questions

### BRANCH-NETWORKING-SP-01

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving ClusterIP. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get svc,endpoints,endpointslice -A -o wide` as one read-only checkpoint, not the whole diagnosis. virtual internal IP implemented by the cluster service data plane. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-02

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving NodePort. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ds -n kube-system` as one read-only checkpoint, not the whole diagnosis. reserves a port on nodes and routes to Service endpoints. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-03

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Kubernetes network model. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get networkpolicy -A -o yaml` as one read-only checkpoint, not the whole diagnosis. Pods have cluster-routable IP identity and communicate without required NAT inside the model. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-04

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving CNI plugin. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` as one read-only checkpoint, not the whole diagnosis. configures Pod interface, address, route and cleanup when runtime creates sandbox. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-05

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Pod selection. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` as one read-only checkpoint, not the whole diagnosis. policy applies only to Pods matched in its namespace. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-06

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Isolation direction. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get svc,endpoints,endpointslice -A -o wide` as one read-only checkpoint, not the whole diagnosis. selecting a Pod for ingress/egress isolates that direction to allowed union. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-07

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving IngressClass/controller. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ds -n kube-system` as one read-only checkpoint, not the whole diagnosis. selects implementation and controller-specific features. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-08

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Ingress rule. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get networkpolicy -A -o yaml` as one read-only checkpoint, not the whole diagnosis. host/path routes HTTP(S) to a Service backend under limited portable API. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-09

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Data-plane proxy. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get ingressclass,ingress,gatewayclass,gateway,httproute,grpcroute -A` as one read-only checkpoint, not the whole diagnosis. sidecar/ambient/node proxy intercepts workload traffic under mode-specific boundaries. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

### BRANCH-NETWORKING-SP-10

- [ ] **Incident/migration:** **Question:** You own a high-severity failure or migration involving Control plane. How do you lead it end to end?
> **Covered in:** [Networking — Availability and failure modes](README.md#availability-and-failure-modes)

**Answer:** Establish incident/change command, impact, decision rights, communications cadence and abort criteria. Preserve evidence and use `kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].name}{"\n"}{end}' | rg 'proxy'` as one read-only checkpoint, not the whole diagnosis. distributes service discovery, certificates and policy to proxies. Choose reversible containment, protect tenant/data boundaries, and keep rollback artifacts/state. Recover in waves and validate SLO, correctness/quality, security and billing. Publish timeline/trade-off/ADR or postmortem, assign preventive actions with owners, and verify them in a game day or migration rehearsal.

## Self-grading

A complete spoken answer names the mechanism, scope/assumptions, one concrete command or configuration field, a failure mode, security/recovery, an SLI and a cost/trade-off. For procedural answers, explicitly separate immediate reversible mitigation from durable source-of-truth repair.

<!-- reading-navigation:start -->
---

**Reading path:** [← Back: Probes and container lifecycle](../02-workloads/05-probes-lifecycle/README.md) · [Study note](README.md) · [Next: Services, EndpointSlices and CoreDNS →](01-services-endpoints-dns/README.md)

<!-- reading-navigation:end -->
